---
title: Usense Branding Assets & Workflow
aliases:
  - branding
  - Usense brand
  - logo
  - md2pdf workflow
tags:
  - topic/branding
  - type/reference
  - status/complete
date: 2026-04-26
status: complete
type: reference
author: Usense Healthcare
---

# Usense Branding

Branding assets and the canonical PDF-generation workflow for Usense-branded deliverables across all projects (not just `datascience`). Use this when producing PDFs, slides, report headers, or any externally-facing document with the Usense identity.

## Assets

| Asset | Path | Notes |
|-------|------|-------|
| Logo | `C:/Users/rwa/.claude/assets/usenseLogo.png` | Use this file directly — do not ask the user to supply one |
| Brand palette | navy + amber | Implemented inside `md2pdf` |

## Markdown → PDF

For markdown-to-PDF rendering, **invoke the `/md2pdf` skill** rather than re-implementing the branding. It generates Usense-branded PDFs from markdown with a banner (logo + title) and the navy/amber palette pre-applied.

> [!IMPORTANT]
> Do not roll your own pandoc/xelatex pipeline for Usense deliverables. The `md2pdf` skill already handles the banner, palette, fonts, and page geometry. Re-implementing this drifts from the brand and wastes work.

- **Skill location**: [`md2pdf`](file:///C:/Users/rwa/.claude/skills/md2pdf/)
- **Invocation**: `/md2pdf <src.md> <tgt.pdf> [subtitle] [a4|letter]`

## Sources

| Source | Notes |
|--------|-------|
| `~/.claude/skills/md2pdf/SKILL.md` | Skill definition and parameters |
| `~/.claude/assets/usenseLogo.png` | Logo file |

## Gaps
- No documented Usense slide template equivalent to `md2pdf`. PowerPoint and Beamer decks are produced ad-hoc via [[scientific-slides]] without enforced branding.
- Brand palette is not formally specified anywhere outside the `md2pdf` source — exact hex values would help if other tools need to match.
