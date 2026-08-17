---
name: shorts-hook-generator
description: Generate 10 formatted intro hook ideas for a YouTube Shorts video, one for each of 10 fixed hook formats (Contrarian, Fear-Based, Authority, Time-Sensitive, Curiosity, Outcome-Based, Listicle, Scroll Interrupt, Regret-Based, Length-Based). Use this skill whenever the user gives a Shorts topic/title and asks for hook ideas, hook options, intro hooks, or "hooks for this short" — even if they don't name all 10 formats explicitly. Also trigger on phrases like "give me hooks for this topic", "hook ideas for my short on X", or when the user pastes a topic/title right after referencing this skill. Always present the output as a clean 2-column markdown table (hook format name, hook line) — never a bullet list.
---

# Shorts Intro Hook Generator

Generates exactly 10 intro hook lines for a given YouTube Shorts topic/title — one hook per fixed format below. Each hook is the first line (or first ~3 seconds) a viewer would hear/read on the short.

## Input
The user provides a topic or working title for a Shorts video. If they give something vague ("hooks for my shorts idea"), ask them for the actual topic/title before proceeding — don't guess a topic.

## The 10 Hook Formats (fixed order, always use all 10)

1. **The Contrarian Hook** — Say something that contradicts a popular belief the viewer holds about the topic itself (the broad topic, not a random sub-detail). Never invent or assume a specific narrow sub-claim (e.g. a particular tactic, setting, or detail) that the video may not actually cover — stay at the level of the topic's general premise so the hook can't overpromise something the video doesn't deliver.
2. **Fear-Based Hook** — Create FOMO / loss-aversion around the topic. Stick close to the standard patterns rather than substituting in invented specifics: "if you ignore this, you'll never...", "watch this if you don't want to...", "don't miss this if...". Prefer plain, safe verbs like "ignore" over dramatic synonyms (e.g. say "if you ignore this" — not "if this gets buried" or similar embellishments).
3. **Authority Hook** — Establish credibility so the viewer trusts the advice is experience-based, using the creator's own general experience/results — never frame it as a case study or analysis of one specific channel/video/person unless the video's actual premise is exactly that. Patterns: "I [did X] for [time period], here's what I found", "I've [done X extensively], here's what actually works".
4. **Time-Sensitive Hook** — Anchor the hook to the current year so the info feels fresh. Pattern: "This is how to [do X] in [year]."
5. **Curiosity Hook** — Open with "did you know" / "have you ever wondered" framed around the topic's general premise. Same rule as the Contrarian Hook: never assume a specific narrow sub-detail (e.g. a particular feature, setting, or mechanic) that the video may not actually cover — keep it broadly relevant to any video on this topic.
6. **Outcome-Based Hook** — Use the exact pattern "If you want [outcome], this is for you" — replace [outcome] with what the viewer actually gets from watching.
7. **Listicle Hook** — Always start with "here are" followed by a fixed number relevant to the topic. Pattern: "here are [N] [things/ways/reasons/etc] [about the topic]" — e.g. "here are 3 things the algorithm checks before recommending your video".
8. **Scroll Interrupt Hook** — Use the exact literal pattern "if you are a [target audience], stop scrolling" — replace [target audience] with whoever the video is actually for, inferred from the topic. Always keep the full phrase "if you are a ___, stop scrolling" — don't shorten or reword it.
9. **Regret-Based Hook** — Use the pattern "I wish I knew this [xyz] before" or a close variant like "I wish someone had told me about this [xyz] before" — replace [xyz] with something that fits the topic naturally (e.g. "I wish I knew this algorithm secret before", "I wish I knew these minecraft mods before"). Small variations in phrasing are fine as long as the core "I wish I knew/someone had told me... before" regret framing is preserved.
10. **Length-Based Hook** — Use the exact pattern "This is [abc] in just x seconds" — replace [abc] with a short phrase describing the topic (e.g. "This is how the algorithm works in just x seconds", "This is the dark reality of bollywood in just x seconds", "This is YouTube's new monetization update explained in just x seconds"). Always leave the literal letter "x" in place for the seconds — never fill it in with a guessed number. Right after this hook (inside the same table cell, on a new line, in smaller/italic-style text if the output format allows, e.g. using markdown like `*replace x with your video length*`) add a short reminder that the user needs to replace "x" with their actual video's length.

## Rules for writing the hooks

- Adapt every hook specifically to the given topic — never leave a format generic or copy the example patterns verbatim. The bracketed placeholders above are structural guides, not filler to leave unfilled.
- Never assume or invent a specific sub-detail, tactic, or narrow claim that isn't guaranteed to be part of the video just because it plausibly relates to the topic (e.g. for a video on "how the algorithm works", don't assume it specifically covers upload schedule, tags, or any other single sub-topic unless the user's topic/title says so). Hooks should stay true to the topic as given, not a guessed-at specific angle within it.
- Keep each hook to one short, punchy sentence — this is a Shorts intro line, not a paragraph. Aim for something that could realistically be said out loud in 3 seconds.
- Match the channel's brand voice: conversational, to the point, no filler, never overhyped or exaggerated, avoid em dashes.
- If a format genuinely doesn't fit a topic well, still make a best-effort adaptation rather than skipping it — but you may note briefly (outside the table) if one format is a stretch for this particular topic.
- Titles/hooks are in English (per this channel's metadata language convention) unless the user is clearly writing the underlying script in Hinglish and asks for the hook in that style.

## Output format

Present the result as a clean 2-column markdown table in the response (not a bullet list):

| Hook Format | Hook |
|---|---|
| Contrarian | ... |
| Fear-Based | ... |
| Authority | ... |
| Time-Sensitive | ... |
| Curiosity | ... |
| Outcome-Based | ... |
| Listicle | ... |
| Scroll Interrupt | ... |
| Regret-Based | ... |
| Length-Based | ... (with the "replace x with your video length" note in the same cell) |

Keep it minimal — no extra columns, no explanations inside the table. Before the table, add one short line naming the topic being hooked. After the table, don't over-explain — a one-line offer to refine any specific hook is enough.
