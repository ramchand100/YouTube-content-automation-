# YouTube Content Automation

A toolkit of Claude Skills plus a project-instructions persona for running a
YouTube channel end to end: ideation, intro hooks, Shorts hooks, thumbnails, and
channel analytics. Originally packaged for a claude.ai Project and set up here so
the skills are auto-discoverable by Claude Code.

## What's here

```
CLAUDE.md                       Project instructions — your "YouTube team member" persona
.claude/skills/                 The 4 skills (auto-loaded by Claude Code)
  intro-hook-writer/
  shorts-hook-generator/
  thumbnail-ideator/
  report-card/
    scripts/analyze_channel.py  Bundled analytics script used by report-card
docs/                           Original source assets, kept for reference
  Prompt for Team Member.pdf
  READ ME FIRST.png
```

## Setup

1. **Fill in `CLAUDE.md`.** Open it and replace the blank fields (channel name,
   niche, subscriber count, language, audience profile, etc.) with your own
   channel data. Edit the pre-filled `BRAND VOICE`, workflow, and packaging/
   editing sections if they don't match how you work. The skills lean on this
   context to produce on-brand output, so the more complete it is, the better the
   results.

2. **(claude.ai Projects only) Enable Memory.** If you also use this toolkit
   inside a claude.ai Project, go to **Settings > Capabilities > Memory** and turn
   on both toggles — *Search and reference chats* and *Generate memory from chat
   history* — so Claude can recall your channel context across chats. This step is
   not needed for Claude Code, which reads `CLAUDE.md` directly.

## The skills

| Skill | What it does | Triggers when you… |
|---|---|---|
| **intro-hook-writer** | Drafts a 30-40s (~125 word) long-form video intro using a 5-step viral-intro framework. | give a topic/title and ask for an intro, hook, or opening. |
| **shorts-hook-generator** | Produces 10 Shorts intro hooks, one per fixed format, as a 2-column table. | give a Shorts topic and ask for hook ideas/options. |
| **thumbnail-ideator** | Generates 4-5 described-in-words thumbnail concepts grounded in curiosity-gap psychology and 12 proven formats. | ask for thumbnail ideas/concepts for a video. |
| **report-card** | Turns a YouTube Studio "Advanced" 28-day CSV export into a 6-section dark-mode HTML report card. | upload a channel analytics CSV and ask how the channel is doing. |

## Note on `report-card` in Claude Code

The `report-card` skill was authored for claude.ai Projects, so it refers to a
couple of claude.ai-specific tools (`create_file` / `present_files`) and to the
Memory feature. In Claude Code the equivalent is writing the HTML file with the
`Write` tool and sharing it (`SendUserFile` or `Artifact`). The skill's
instructions still execute correctly here — only those tool names differ. The
skill files are kept verbatim as authored.
