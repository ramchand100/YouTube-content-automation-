# Footage and Copyright Guidelines

## Core principle

**Public availability is not copyright permission.**

A video appearing on YouTube, a news website, or in search results does not mean it
can be reused. Reuse requires explicit licence permission for commercial use.

---

## Approved free sources (CC0 — confirm per clip)

| Source | URL | Notes |
|--------|-----|-------|
| Pexels | pexels.com | Confirm licence on each individual clip |
| Pixabay | pixabay.com | Confirm licence on each individual clip |
| Videvo (CC0 only) | videvo.net | Filter explicitly to CC0; some Videvo clips are not CC0 |

Even for these sources, check the specific clip's licence page before using it.
Platform policies can change. A clip that was CC0 in one upload may have been re-uploaded
with different terms by a different contributor.

---

## Approved licensed sources (require active account or purchase)

| Source | URL | Notes |
|--------|-----|-------|
| Pond5 | pond5.com | Purchase per clip; save licence certificate |
| Shutterstock | shutterstock.com | Requires active subscription or clip purchase |
| Artgrid | artgrid.io | Subscription-based; confirm commercial tier |
| Envato Elements | elements.envato.com | Subscription-based; confirm video licence |

Save the licence certificate or purchase confirmation for every clip used.

---

## Self-captured footage

Any footage the channel shoots itself is cleared by default. Document the shooting
location, date, and purpose in the footage rights register.

---

## Official government footage

Pakistan government press conferences, National Assembly sessions, and SECP/SBP
official releases may be usable, but this is not automatic.

- Confirm whether the specific clip carries an explicit reuse licence.
- Do not assume government footage is public domain.
- If in doubt, use a fallback (Remotion graphic or text card).

---

## Never use without clearance

The following categories require explicit rights clearance before use. Do not assume
permission without a documented licence:

- Pakistan TV network clips: Geo, ARY, Hum, Dawn News, GNN, Dunya, Samaa
- Airline promotional footage: PIA, Emirates, Qatar Airways, Turkish Airlines, etc.
- Company promotional videos (Engro, Interloop, National Foods, etc.)
- News broadcast clips from any outlet (BBC, CNN, Al Jazeera, etc.)
- Sports footage of any kind
- Music (all music; use only content-ID-safe tracks with an explicit licence)

---

## Fallback hierarchy

When footage cannot be cleared, apply in this order:

1. **Remotion motion graphic** — preferred; on-brand, data-driven, no rights risk.
2. **Text card** — episode palette, key stat or quote, clean and clear.
3. **Self-captured equivalent footage** — feasible for generic Pakistan street/city shots.

Update the storyboard's footage cue to reflect the fallback used. Record the
decision in the footage rights register.

---

## Footage rights register

Every footage cue in every storyboard must have a corresponding row in:
`research/source-registers/NN_slug_sources.csv`

Required columns (extend the standard source register with):
`clip_id | description | timestamp | source | licence_type | licence_url | commercial_ok | cleared | fallback | notes`

No episode may enter production with any `cleared: pending` entries.

---

## Music

Use only tracks with an explicit licence that permits:
- Commercial use (YouTube monetisation)
- Use in modified / edited form (the track is placed under voiceover)

Approved sources for music:
- YouTube Audio Library (filter to "free to use" commercial tracks)
- Artlist (with active subscription)
- Epidemic Sound (with active subscription)
- Pixabay Music (CC0 confirmed per track)

Do not use:
- Copyrighted tracks "credited in the description" — this is not a valid licence.
- AI-generated music services unless they provide a documented commercial licence.

---

## Attribution

Some CC licences (e.g. CC BY, CC BY-SA) require attribution. If a clip requires
attribution, include the credit in the video description and note it in the footage
rights register. CC0 clips do not require attribution, but it is good practice.

---

## .gitignore

Raw video and audio files are not committed to this repository. The `.gitignore`
includes:
```
/media/
*.mp4
*.mov
*.wav
*.aif
*.aiff
```

Store raw footage on an external drive or cloud storage, not in the repo.
