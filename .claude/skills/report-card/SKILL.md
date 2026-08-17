---
name: report-card
description: "Generates a visual, dark-mode \"report card\" from a YouTube Studio Content-table CSV export (Advanced mode, last 28 days). Use this whenever the user uploads a YouTube analytics/channel CSV and asks for a report, analysis, breakdown, or \"how is my channel doing\" type request — even if they don't use the word \"report card\" explicitly. Trigger on phrases like \"analyze my channel\", \"here's my last 28 days csv\", \"what's working on my channel\", or any CSV with columns like Video title, Views, Impressions, Impressions click-through rate. Covers 6 fixed sections: videos to recover, video ideas for more views, top subscriber converters, best performing video length, evergreen topics, and title format classifier. Always produce the full 6-section HTML report card, don't just answer with a text summary."
---

# Channel Report Card

Turns a YouTube Studio "Advanced" CSV export into a 6-section visual report card. Three of the sections are pure arithmetic (handled by a bundled script) and three require actual judgment about the channel's content (handled by you, reading the cleaned data the script hands back). Both halves matter — don't skip the reasoning half just because the script did the counting.

## Step 1: Locate and run the analysis script

The CSV the user uploads is YouTube Studio's raw "Content" table export. It's messy in predictable ways: it has a `Total` summary row, and it mixes in Community posts and video replies alongside real videos (these show up with a blank CTR field, since only real videos/Shorts get impression data). `scripts/analyze_channel.py` handles all of this cleanup plus the objective math.

Run it:

```bash
python3 scripts/analyze_channel.py <path-to-uploaded-csv>
```

If the user mentions the export is old or you have reason to think "today" isn't the right reference date (e.g. they say "this is from a few months ago"), pass `--as-of YYYY-MM-DD` so the 90-day and 18-month windows stay meaningful.

This prints one JSON object with:
- `meta` — totals, average CTR, how many junk rows got filtered, which recovery window ended up being used
- `cleaned_videos` — every real video with title, publish date, duration, views, impressions, CTR, subscribers gained, days since publish. This is your raw material for Steps 2 and 3 below.
- `videos_to_recover` — already-ranked candidates for Section 1
- `top_converters` — already-ranked candidates for Section 3
- `length_buckets` — bucketed averages for Section 4
- `evergreen_topics` — already-ranked candidates for Section 5

Sections 1, 3, 4, and 5 are ready to drop straight into the report. Sections 2 and 6 need you to actually look at the titles and think.

## Step 2: Video ideas for more views (needs your judgment)

Look at `cleaned_videos` sorted by views, but don't just recommend "more of the top video." A video published recently gets an algorithmic novelty boost regardless of topic quality, so raw view count alone is misleading for videos that are only a few weeks old. Weight your read toward videos that are both high-viewed AND either older (survived past the initial push) or have a high CTR/high views-per-subscriber alongside the views, since that combination signals the topic itself is working, not just the freshness bump.

From the patterns you find (recurring topics, formats, angles that are outperforming), propose 5 fresh video ideas. Get the scope right before you get the title right:

- **Find the topic at the right altitude.** A recurring cluster in the data (e.g. several mobile-editing videos, several packaging videos) tells you the *broad subject* is durable — it does not mean the next video should zoom into one narrow sub-piece of it. "5 editing transitions" is narrower than what made the cluster work; the videos that actually performed were about the broader skill (editing on mobile, professional-feeling edits), not one technique inside it. Stay at the altitude the data actually supports.
- **Every idea needs mass-appeal, not just insider appeal.** This channel's own CCN framework (Core/Casual/New viewers) is the test to apply here: a good idea should pull in viewers who've never seen the channel before, not just the die-hard subscribers who already know the jargon. "Why your CTR is low" only works on someone who already knows what CTR means — reframe it in terms of the outcome any viewer recognizes (not getting clicks, videos flopping) rather than the niche mechanism.
- **The title itself has to do the clicking, not just the topic.** A solid topic with a flat title won't perform — pull in the same power-word categories this channel already uses in its own packaging (curiosity: "the real reason", "what nobody tells you"; stakes/fear: "killing your growth", "the mistake that's costing you"; authority: proven numbers or credibility). Don't hand back a title that reads like a description of the video; hand back one that creates a curiosity gap or names a stake, the way the channel's actual top performers do.

If you have web search available and the topic warrants checking what's currently trending in the YouTube-growth / content-creation space, use it — but the core signal should come from what's actually working on this channel.

## Step 3: Title format classifier (needs your judgment)

Read through every title in `cleaned_videos` and sort them into 4-5 psychological formats based on what's actually driving the click, not a rigid keyword list. Common formats that tend to show up in this niche (a track record already exists in this project — see the power-word categories in the title/description/tags material) include:

- **Curiosity-driven** — withholds information ("The REAL reason...", "What nobody tells you about...")
- **Authority/tutorial-driven** — positions the creator as the expert delivering a clear how-to ("How to...", "The Ultimate Guide to...")
- **Fear/warning-driven** — implies a mistake or loss if ignored ("Stop doing this...", "X Mistakes that...")
- **Desire/outcome-driven** — names the result the viewer wants ("Get 1K Subscribers in...", "10X Your Views")
- **Listicle** — a counted list ("8 Faceless Channel Ideas", "6 Signs Your Channel...")

Use your own judgment on the actual set — if the data clearly clusters differently, adjust the categories rather than forcing a fit. For each format, compute the average views across all titles in that bucket, and note the video count per bucket (a format with 2 videos averaging high views is a weaker signal than one with 15).

## Step 4: Build the report card

Generate a single self-contained HTML file and save it so it can be shared as an artifact (this renders inline for the user). Use `create_file` to write it, then `present_files` to share it.

### Whose name goes in the header

This skill gets run by many different creators, so never hardcode a channel name. Figure out what to display, in this order, and don't ask the user to clarify — just make the best call and move on:
1. If the CSV export itself contains a channel name/handle column, use that.
2. If the person's channel name or handle is available from project instructions, memory, or earlier in the conversation, use that.
3. Otherwise, fall back to whatever name the person goes by on their account (their preferred name/display name) rather than a generic placeholder like "Your Channel."

### Design system — follow this for the visual style

```
Background:      #0a0a0a (near-black)
Card surface:     #151515, 1px solid #262626 border, 16px radius
Primary accent:   #4ADE80 (green) — use for headers, key numbers, positive signals
Secondary accent: #F5F5F5 (white) — body text, secondary emphasis
Problem/warning:  #FB7185 (soft red) — only in Section 1, to flag underperformance
Muted text:       #9CA3AF — descriptions, captions, labels
Display font:     'Archivo Black', sans-serif (or similar condensed bold sans) for headers and big numbers — loaded from Google Fonts CDN
Body font:        'Inter', sans-serif for everything else
```

This palette is the default and works well as a generic dark "creator report" look. If the person has a known brand palette or font from memory/context (e.g. they've mentioned their thumbnail colors before), prefer that instead — otherwise use the default above.

### Structure

1. **Header band** — channel name, "Last 28 Days" label, and 4 hero stats in a row (Total Views, Avg CTR, Subscribers Gained, Videos Analyzed) pulled from `meta` and a sum over `cleaned_videos`. Big green numbers, small muted labels underneath — this is the one place bold numbers-as-hero make sense, since the brief itself is a data report.

2. **Six section cards**, each with an icon, a title, the one-line description text specified below (use it verbatim, it's the user's own framing), and the content:

   - 📉 **Videos to Recover** — "These videos have the potential to do better if their packaging is improved." List each: title, impressions, CTR (in red if below the channel average shown in `meta`), and a one-line note on what a stronger title/thumbnail might unlock.
   - 💡 **Video Ideas for More Views** — no boilerplate description needed; list your 5 ideas from Step 2, each with a one-sentence rationale tied to a real pattern in the data.
   - 🔄 **Top Converters** — "These videos were the strongest in converting viewers to subscribers." List each: title, views, subscribers gained, and the views-per-subscriber ratio.
   - ⏱️ **Best Performing Video Length** — a horizontal bar chart (plain HTML/CSS bars, width proportional to avg views, is enough — no charting library needed) across the 5 duration buckets, with video count and avg views labeled per bar.
   - 🌲 **Evergreen Topics** — "These topics continue to generate traction even after months." List each: title, how long ago it was published (in months, not raw days), and views in this window.
   - 🏷️ **Title Format Classifier** — a small table or bar comparison of your format buckets from Step 3, sorted by average views descending, so the winning format is immediately visible.

3. Keep it to one scroll, no unnecessary animation — this is a report the user will screenshot or refer back to, not a landing page. A little hover state on cards is fine; skip anything flashier.

### Why this shape

The header stats exist so the report has an at-a-glance summary before the detail sections — useful since the user reads these every 2 weeks and wants the headline first. The red-flagging in Section 1 only (not elsewhere) keeps the report from feeling alarmist; every other section is framed as a positive signal to act on, matching a coaching tone rather than a scolding one.

## After generating

Briefly point out anything that stood out while you were building it (a section that revealed a clearly actionable insight, or a section that turned up thin/inconclusive because the data doesn't support many candidates) — don't just hand over the file silently. If a section came back sparse (e.g. only 1-2 videos to recover), say so rather than padding it.
