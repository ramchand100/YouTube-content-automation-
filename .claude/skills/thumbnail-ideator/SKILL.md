---
name: thumbnail-ideator
description: Generates 4-5 YouTube thumbnail concept ideas for a given video topic/title, grounded in thumbnail psychology (curiosity gaps, storytelling, focal points) and 12 proven viral thumbnail formats. Use this skill whenever the user asks for thumbnail ideas, thumbnail concepts, thumbnail suggestions, "what should my thumbnail be", or wants help brainstorming a clickable thumbnail for a video — even if they just paste a title/topic and say "thumbnail ideas for this." Always describe each idea in words (visual composition, elements, text) rather than generating an actual image.
---

# Thumbnail Ideator

Generates thumbnail concepts for a YouTube video. Input: a video topic or title. Output: 4-5 distinct, described-in-words thumbnail ideas that are genuinely clickable — not just "cool looking."

## Core Philosophy (read this before generating ideas)

A thumbnail is not decoration — it's a story-telling device. The single biggest mistake is a thumbnail that just repeats the title or shows a generic image with no story. **A clickable thumbnail always creates a story or an open question in the viewer's mind, which only watching the video can resolve.**

Before generating ideas, internalize these principles:

1. **Title + thumbnail = one curiosity gap, told together.** They should never say the same thing in different words. If the title already explains something, the thumbnail should add a *new* piece of information, a contradiction, or an emotional beat — never a repeat. This is non-negotiable.
2. **One main character / focal point.** No matter how many elements are in the frame, viewer attention must land on one clear "hero" element first. Everything else (arrows, small text, secondary faces) exists only to support that main element, not compete with it.
3. **Text is a story-teller, not a label.** Thumbnail text should never restate the title. It should add context, tension, or a twist. Keep it to 2-4 words max — fewer words means bigger, more scannable text.
4. **Simplicity beats clutter.** More elements = divided attention = unprofessional look. Only include elements that are essential to telling the story.
5. **Contrast drives attention — and color carries meaning.** Especially complementary color pairs (red/green, purple/yellow, blue/orange) or plain black/white against saturated color. Beyond pure contrast, pick colors for what they signal: red reads as danger/lies/warning/urgency, green reads as growth/money/go-ahead, gold/yellow reads as premium/reward, blue reads as trust/calm. Match the highlight color to the specific word or emotion in that idea, even if it means deviating from a creator's usual highlight color for one concept — the concept's impact comes first (see Brand Constraints below for how to balance this against a stated brand palette).
6. **It has to work small.** Since most views come from feeds where the thumbnail is tiny, the concept must be readable/understandable at a glance — don't propose ideas that only work at full size.

## Brand Constraints (check for these before generating ideas)

This skill gets used by different creators, so don't assume any fixed palette or font.

1. First, check the user's project instructions / custom instructions / anything else in context for their stated thumbnail color palette and font (e.g. "black background, green/white text" or similar). If present, use it as the base (background + primary text color).
2. **But prioritize color psychology over a rigid palette for highlight/accent colors.** A creator's stated highlight color (e.g. "use green to highlight the important word") is a default, not a rule that overrides what the concept needs. If a specific word or idea calls for a different color — red for danger/lies/scam/warning, green for growth/money/positive, gold for premium/reward — use that color instead for that word, even if it's not the creator's usual highlight. The background and primary/body text color should still stay consistent with their brand; it's specifically the accent/highlight color that should flex per-concept.
3. If nothing is specified, don't invent a generic default — instead, pick whatever palette, font, and style genuinely serves each individual idea best. State the suggested colors/font briefly within each idea.
4. Check whether the channel is faceless or facecam (this is often mentioned alongside channel info in project instructions). If faceless, avoid ideas that require the creator's own face/photo — use illustrated characters, UI mockups, objects, data visuals, whiteboard-style diagrams, etc. instead. If facecam is explicitly stated, face-forward ideas (Surrounded Hero, Candid Shot, Transformation, etc.) are fully in play, and you can suggest using the creator's own face/photo as the hero element.
5. Check the project instructions for any mention of a channel avatar, mascot, or recurring character. This is rare, but if one is mentioned, treat it as a usable "hero" element in relevant ideas, the same way a facecam creator's face would be used.
6. Text length: keep to 2-4 words regardless of channel, unless the format specifically calls for something else (e.g. Prime Text can occasionally run a touch longer if every word earns its place).

## Niche-Specific Notes

- **Cooking/food videos:** avoid over-engineered formats like Transformation or Comparison — split-frame before/afters tend to look gimmicky for food content and can even undercut appetite appeal. Simple, high-quality Candid Shot or Prime Text ideas (a great close-up of the dish, minimal or no text) usually outperform complicated compositions in this niche. Only reach for Transformation/Comparison here if the video is specifically about a fix/upgrade (e.g. "fixing a failed recipe") where the before/after is the actual point.
- **Vlogs:** give preference to Candid Shot and variants of it (different angles — face-first, moment-first, hands/object-first, etc.) over heavily designed formats. Vlogs sell an authentic "come along with me" feeling, and an overly graphic thumbnail works against that. It's fine to include 1-2 more designed ideas (Prime Text, Surrounded Hero) alongside the Candid variants for range, but Candid-style should be the backbone of the set.

## The 12 Proven Formats (use as inspiration, not a checklist)

Pull from these when relevant, but don't force a fit — an original concept that nails the curiosity-gap principle beats a shoehorned format.

1. **3-Panel Collage** — canvas split into 3 vertical panels, each a different angle/example of the topic, tied together with central text. Good for topics with 3 distinct facets or steps.
2. **UI Interface** — mocks up a familiar app/platform UI (notification, DM, post, YouTube Studio screenshot) to borrow that interface's built-in credibility.
3. **Prime Text** — text is the star; a simple background image plus a punchy phrase that only makes sense combined with the title (not on its own).
4. **Surrounded Hero** — one central visual anchor (character/object) with smaller supporting elements arranged around it, maintaining clear size hierarchy.
5. **Candid Shot** — a simple, "un-designed" real moment/screenshot. Works as a pattern interrupt against overly-designed feeds; feels authentic and unstaged.
6. **Cinematic Text** — fancy/elegant font, muted or non-flashy colors, poster-like feel. Signals premium/aesthetic content; fits reflective, aesthetic, or documentary-style videos better than bold educational ones.
7. **Whiteboard Diagram** — a hand-drawn-feeling framework or diagram, intentionally a little messy/complex so it hints at depth without fully explaining itself.
8. **Ultra Minimal** — plain background, over 50% empty space, tiny/minimal text. Signals confidence and stands out against cluttered feeds. When the concept calls for an icon, prefer something instantly recognizable (e.g. the YouTube logo, a platform icon) over a generic/abstract icon (e.g. a plain arrow) — recognizability lands faster at a glance.
9. **Maximal / Multi-Focal** — canvas is packed, multiple focal points. Best for listicle/roundup/"best of" style videos where viewers should expect many options.
10. **Transformation** — split before/after, left = relatable/common starting point, right = desirable or shocking result. The bigger the contrast, the stronger the pull.
11. **Comparison** — two things, people, or situations placed side by side to be directly compared.
12. **Detective Board** — central subject with related cutouts/text/icons connected by red thread on a corkboard. Great for exposes, case studies, or "connecting the dots" style topics.

## Process

When the user gives you a topic or title:

1. If no title exists yet, work off the topic. If a title exists, read it closely — the thumbnail must add something the title doesn't already say.
2. **If the topic references something you're not confidently familiar with** (a specific episode, a recent event, a person, a product, a trend, etc.), use web search before generating ideas. Find out what actually happened / what's notable / what the specific hook or controversy is — generic ideas based on a vague guess will be weaker than ideas grounded in the real specifics. This matters most for reaction content, news, current events, and niche-specific references.
3. Generate **4-5 ideas**, aiming for genuine variety — don't give 5 versions of the same format. Mix in at least 2-3 different formats from the list above, plus at least one idea that doesn't map cleanly to any of the 12 (an original concept built purely from the story/curiosity principle).
4. For each idea, describe in words:
   - **Concept name** (short label, can reference the format if used, e.g. "Prime Text" or just a custom name)
   - **Visual composition**: what's in the frame, where it's placed, what's the focal point
   - **Text**: the exact 2-4 word text to use (if any) and where it sits
   - **Why it creates curiosity**: one line on the story/question it plants in the viewer's mind
5. Apply the Brand Constraints check above — use the creator's stated palette/font if known, otherwise suggest what's best per idea.
6. If you genuinely can't come up with a strong concept for a topic, say so rather than forcing a weak idea — quality over hitting a quota.

## Output Format

Present as a numbered list, one idea per entry, using these fields:
   - **Concept name**
   - **Visual composition**
   - **Text**
   - **Colors/font** (only include this field if you're suggesting something beyond what the creator already told you — skip it if their brand palette already applies and there's nothing extra to note)
   - **Why it works**

Keep each idea tight — a few lines, not a paragraph. After the list, you can briefly ask the user if the title is more search-based or browse-based if that would change which idea fits best, but don't block on this — give the ideas first.
