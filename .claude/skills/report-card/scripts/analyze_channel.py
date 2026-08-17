#!/usr/bin/env python3
"""
Analyzes a YouTube Studio "Content" table CSV export (Advanced mode, last 28 days)
and produces the quantitative building blocks for the channel report card.

Usage:
    python3 analyze_channel.py <path-to-csv> [--as-of YYYY-MM-DD]

Outputs a single JSON blob to stdout with these keys:
    meta                - date range info, totals, row counts
    cleaned_videos       - full list of every real video row (dicts), for Claude
                            to use when doing the creative sections (video ideas,
                            title format classification)
    videos_to_recover    - candidates for section 1
    top_converters       - candidates for section 3
    length_buckets       - data for section 4's chart
    evergreen_topics     - candidates for section 5

Design notes (read this if you're modifying the script):

- YouTube Studio's CSV export mixes real videos in with Shorts, Community posts,
  and "video replies". Community posts / replies always have a BLANK
  "Impressions click-through rate (%)" field (real videos and real Shorts always
  have a number there, even if 0). That's the most reliable filter available in
  this export format, so we use it instead of a duration cutoff, since real
  Shorts can be just as short as a reply clip.

- The CSV's Views/Impressions/Subscribers columns reflect the last-28-days
  window, not lifetime totals, even for old videos. So "best video" and
  "evergreen" logic below is about how a video is performing THIS WINDOW,
  which is exactly what makes something "evergreen" (an old video still
  pulling fresh traffic) meaningfully different from "recently published and
  doing well because it's new."

- "As of" date defaults to today. Pass --as-of when analyzing an export that's
  being looked at well after the fact, so recency windows (90 days / 18 months)
  stay meaningful.
"""

import argparse
import csv
import json
import sys
from datetime import datetime
from pathlib import Path


def parse_date(raw):
    return datetime.strptime(raw.strip(), "%d-%b-%y")


def load_rows(csv_path):
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows


def is_real_video(row):
    # Total row has no video title
    if not row.get("Video title", "").strip():
        return False
    ctr_raw = row.get("Impressions click-through rate (%)", "")
    if ctr_raw is None or ctr_raw.strip() == "":
        return False
    return True


def to_float(val, default=0.0):
    try:
        return float(val)
    except (TypeError, ValueError):
        return default


def to_int(val, default=0):
    try:
        return int(float(val))
    except (TypeError, ValueError):
        return default


def clean_video(row):
    return {
        "id": row.get("Content", "").strip(),
        "title": row.get("Video title", "").strip(),
        "publish_date": row.get("Video publish time", "").strip(),
        "duration_seconds": to_int(row.get("Duration")),
        "views": to_int(row.get("Views")),
        "watch_time_hours": to_float(row.get("Watch time (hours)")),
        "subscribers_gained": to_int(row.get("Subscribers")),
        "impressions": to_int(row.get("Impressions")),
        "ctr_percent": to_float(row.get("Impressions click-through rate (%)")),
    }


def days_between(a, b):
    return abs((a - b).days)


def build_length_buckets(videos):
    buckets = [
        ("Under 5 min", 0, 300),
        ("5-10 min", 300, 600),
        ("10-15 min", 600, 900),
        ("15-20 min", 900, 1200),
        ("20+ min", 1200, float("inf")),
    ]
    result = []
    for label, lo, hi in buckets:
        in_bucket = [v for v in videos if lo <= v["duration_seconds"] < hi]
        if not in_bucket:
            result.append({"label": label, "video_count": 0, "avg_views": 0})
            continue
        avg_views = sum(v["views"] for v in in_bucket) / len(in_bucket)
        result.append({
            "label": label,
            "video_count": len(in_bucket),
            "avg_views": round(avg_views),
        })
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path")
    parser.add_argument("--as-of", default=None, help="YYYY-MM-DD, defaults to today")
    args = parser.parse_args()

    as_of = datetime.strptime(args.as_of, "%Y-%m-%d") if args.as_of else datetime.now()

    raw_rows = load_rows(args.csv_path)
    real_rows = [r for r in raw_rows if is_real_video(r)]
    videos = [clean_video(r) for r in real_rows]

    for v in videos:
        try:
            pub_dt = parse_date(v["publish_date"])
            v["_publish_dt"] = pub_dt
            v["days_since_publish"] = days_between(as_of, pub_dt)
        except ValueError:
            v["_publish_dt"] = None
            v["days_since_publish"] = None

    videos_with_dates = [v for v in videos if v["_publish_dt"] is not None]

    # ---- Section 1: Videos to Recover ----
    # A video is a "recovery" candidate if it's getting shown a lot (high
    # impressions) but people aren't clicking (below-average CTR) -- that's a
    # packaging problem, not a content problem, and it's fixable by swapping
    # the title/thumbnail. We score by how much impression volume is being
    # wasted: impressions * (avg_ctr - ctr), so a video with huge reach and a
    # middling CTR gap outranks a small video with a huge CTR gap.
    #
    # We start with a 90-day window since "recently published" is what makes a
    # packaging fix worth doing (older videos aren't getting fresh impressions
    # to recover). If that window doesn't surface at least 3 real candidates,
    # we widen to 180 days rather than force out mediocre picks -- better to
    # show fewer, more meaningful candidates than pad the list.
    ctr_values = [v["ctr_percent"] for v in videos if v["impressions"] > 0]
    avg_ctr = sum(ctr_values) / len(ctr_values) if ctr_values else 0

    def recovery_candidates(window_days):
        pool = [v for v in videos_with_dates if v["days_since_publish"] <= window_days and v["impressions"] > 0]
        scored = []
        for v in pool:
            gap = avg_ctr - v["ctr_percent"]
            if gap > 0:
                scored.append({**v, "opportunity_score": round(v["impressions"] * gap)})
        scored.sort(key=lambda v: v["opportunity_score"], reverse=True)
        return scored

    videos_to_recover = recovery_candidates(90)
    recovery_window_used = 90
    if len(videos_to_recover) < 3:
        wider = recovery_candidates(180)
        if len(wider) > len(videos_to_recover):
            videos_to_recover = wider
            recovery_window_used = 180
    videos_to_recover = videos_to_recover[:5]

    # ---- Section 3: Top Converters ----
    # Views needed per subscriber gained. Lower is better. Exclude 0-subscriber videos.
    convertible = [v for v in videos if v["subscribers_gained"] > 0]
    for v in convertible:
        v["views_per_subscriber"] = round(v["views"] / v["subscribers_gained"], 1)
    convertible.sort(key=lambda v: v["views_per_subscriber"])
    top_converters = convertible[:5]

    # ---- Section 4: Best Performing Video Length ----
    length_buckets = build_length_buckets(videos)

    # ---- Section 5: Evergreen Topics ----
    # Published 18+ months ago but still pulling meaningful views/impressions
    # in this window.
    evergreen_candidates = [
        v for v in videos_with_dates
        if v["days_since_publish"] >= 548  # ~18 months
    ]
    evergreen_candidates.sort(key=lambda v: v["views"], reverse=True)
    evergreen_topics = evergreen_candidates[:5]

    def strip_internal(v):
        return {k: val for k, val in v.items() if not k.startswith("_")}

    output = {
        "meta": {
            "as_of_date": as_of.strftime("%Y-%m-%d"),
            "total_real_videos": len(videos),
            "average_ctr_percent": round(avg_ctr, 2),
            "rows_excluded_as_non_video": len(raw_rows) - len(real_rows) - 1,  # minus Total row
            "recovery_window_days_used": recovery_window_used,
        },
        "cleaned_videos": [strip_internal(v) for v in videos_with_dates],
        "videos_to_recover": [strip_internal(v) for v in videos_to_recover],
        "top_converters": [strip_internal(v) for v in top_converters],
        "length_buckets": length_buckets,
        "evergreen_topics": [strip_internal(v) for v in evergreen_topics],
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
