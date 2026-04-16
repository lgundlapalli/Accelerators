# Brand Template — Abbott BTS-DTS

This template is extracted from the AI-First Strategy & Operating Model deck and must be applied to ALL presentations generated or refactored by this skill.

## Brand Identity

- **Organization**: Abbott — BTS / DTS Architecture
- **Logo placement**: Bottom-left (Abbott "a" mark) and bottom-right (ABBOTT wordmark) on title slides only
- **Confidentiality footer**: `Proprietary and confidential — do not distribute` on every slide except title and appendix divider

## Color Palette

| Role | Color | Hex (approx) | Usage |
|------|-------|-------------|-------|
| Primary | Deep Navy | `#000050` | Title slide background, section dividers, slide titles, numbered labels |
| Secondary | Light Lavender | `#DDDDF8` | Content boxes, comparison panels, highlight regions |
| Accent | White | `#FFFFFF` | Text on navy backgrounds |
| Text | Near Black | `#1A1A1A` | Body text on white backgrounds |
| Highlight | Medium Blue | `#3333AA` | Bold headers within content (e.g., "Value + Cost Savings") |
| Alert/Callout | Navy Bold | `#000080` | Big number callouts ("4-12x", ">20%") |

### Mermaid Diagram Colors
When generating Mermaid diagrams, apply these styles:
```
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#DDDDF8', 'primaryTextColor': '#000050', 'primaryBorderColor': '#000080', 'lineColor': '#000080', 'secondaryColor': '#F0F0FF', 'tertiaryColor': '#FFFFFF' }}}%%
```

## Typography Rules (Markdown Approximation)

| Element | Style | Markdown |
|---------|-------|----------|
| Title Slide Title | Large, light-weight | `# Title Text` |
| Title Slide Subtitle | Italic, smaller | `*Subtitle text*` |
| Slide Title | Navy, large | `## Slide Title` |
| Section Header | Bold, medium | `**Section Header**` |
| Body Text | Regular weight, concise | Normal text |
| Big Number Callout | Extra large, navy bold | `# 4-12x` (use H1 within slide for callout numbers) |
| Callout Label | Bold below number | `**Output Multiplier**` |
| Source Citation | Small italic at bottom | `*Source: McKinsey Global Institute (2023)*` |

## Slide Layout Patterns

### Pattern 1: Title Slide (Navy Background)
```markdown
---
<!-- NAVY BACKGROUND -->
# [Main Title]
# [Title Line 2 if needed]

*[Subtitle — proposal context or audience]*

[Abbott Logo Left]                                    [ABBOTT Wordmark Right]
---
```

### Pattern 2: Executive Summary (3-Column Grid)
Lead with a one-sentence thesis, then 3 columns with bold header + big metric + explanation. Always include:
- Column 1: Value/Impact proposition
- Column 2: Speed/Efficiency proposition  
- Column 3: The Ask + Expected Outcome

```markdown
---
## Executive Summary

[One-sentence thesis connecting recommendation to business priority]

| **[Value Header]** | **[Speed Header]** | **[Ask]** |
|---|---|---|
| **[Big Metric]** | **[Big Metric]** | **[Action Statement]** |
| [2-3 line explanation] | [2-3 line explanation] | [2-3 line explanation] |
| **[Secondary Header]** | **[Secondary Header]** | **[Expected Outcome Header]** |
| [2-3 line explanation] | [2-3 line explanation] | [2-3 line explanation] |

*Source: [citation]*
---
```

### Pattern 3: Agenda (Numbered Sections)
Numbered items with horizontal dividers. Use two-digit numbers (01, 02, 03...).
```markdown
---
## Agenda

| | |
|---|---|
| **01** | [Section Name] |
| **02** | [Section Name] |
| **03** | [Section Name] |
| **04** | [Section Name] |
| **05** | [Section Name] |

Proprietary and confidential — do not distribute
---
```

### Pattern 4: Definitions / Comparison (Side-by-Side Panels)
Two concepts in lavender boxes side by side with bullet points. Include a directional note at bottom.
```markdown
---
## [Concept Title]

| **[Concept A]** | **[Concept B]** |
|---|---|
| [Bullet 1] | [Bullet 1] |
| [Bullet 2] | [Bullet 2] |
| [Bullet 3] | [Bullet 3] |

*[Directional guidance: e.g., "Begin with A before B transformation"]*
---
```

### Pattern 5: Vision + Objectives
Subtitle as framing statement, then Vision as a single paragraph, then Objectives as bullet list (max 5).
```markdown
---
## [Title]: Vision, Objectives

[One-line framing statement connecting to strategic priority]

**Vision**
[Single paragraph — 1-2 sentences max]

**Objectives**
- [Objective 1]
- [Objective 2]
- [Objective 3]
- [Objective 4]
- [Objective 5]
---
```

### Pattern 6: Big Number Impact Grid
Large metrics in a row with labels and explanations underneath. Maximum 4 columns.
```markdown
---
## [Impact Title]

[One-sentence thesis]

| | | | |
|---|---|---|---|
| **[Big Number 1]** | **[Big Number 2]** | **[Big Number 3]** | **[Big Number 4]** |
| **[Label]** | **[Label]** | **[Label]** | **[Label]** |
| [Explanation] | [Explanation] | [Explanation] | [Explanation] |
| **[Secondary Label]** | **[Secondary Label]** | **[Secondary Label]** | **[Secondary Label]** |
| [Explanation] | [Explanation] | [Explanation] | [Explanation] |

*Sources: [citations]*
---
```

### Pattern 7: Three-Column Shift / Transformation
Used for People / Process / Technology or similar triads. Bold "From X to Y" headers with explanations.
```markdown
---
## [Shift Title]

[Cultural framing statement in bold]

| **[Column A]** | **[Column B]** | **[Column C]** |
|---|---|---|
| **[From → To statement]** | **[From → To statement]** | **[From → To statement]** |
| [Explanation] | [Explanation] | [Explanation] |
| **[From → To statement]** | **[From → To statement]** | **[From → To statement]** |
| [Explanation] | [Explanation] | [Explanation] |

**Transition Plan** — [Column A action] | [Column B action] | [Column C action]
---
```

### Pattern 8: Hub-and-Spoke / Ownership Split
Two-column layout with matching categories (People, Process, Technology) on each side.
```markdown
---
## [Ownership Title]

| **[Entity A] Owns** | **[Entity B] Owns** |
|---|---|
| **People** | **People** |
| [Bullet list] | [Bullet list] |
| **Process** | **Process** |
| [Bullet list] | [Bullet list] |
| **Technology** | **Technology** |
| [Bullet list] | [Bullet list] |
---
```

### Pattern 9: Role / Responsibility Table
Used for POD drill-downs, RACI-style content. Bold role names in left column, clear Human vs AI split.
```markdown
---
## [Role Title]

[Framing statement: who owns what]

| **Role** | **Human-Led** | **AI-Led** |
|---|---|---|
| **[Role 1]** | [Responsibilities] | [Capabilities] |
| **[Role 2]** | [Responsibilities] | [Capabilities] |
| ... | ... | ... |
---
```

### Pattern 10: Phased Roadmap (Horizontal Phases)
Three phases in columns: Prove → Embed → Scale (or similar progression). Each phase has a timing label, action statement, and decision/success signal.
```markdown
---
## [Roadmap Title]

[One-sentence framing: what the phases achieve]

| **Phase 1 — [Name]** | **Phase 2 — [Name]** | **Phase 3 — [Name]** |
|---|---|---|
| *[Timing]* | *[Timing]* | *[Timing]* |
| **[Action headline]** | **[Action headline]** | **[Action headline]** |
| [Details] | [Details] | [Details] |
| **[Decision/Signal]** | **[Success Signal]** | **[Long-term Value]** |
| [Details] | [Details] | [Details] |
---
```

### Pattern 11: Section Divider (Navy Background)
Full navy background with single word/phrase. Used for Appendix and major section breaks.
```markdown
---
<!-- NAVY BACKGROUND -->
# [Section Name]
---
```

### Pattern 12: Details / Data Table (Appendix)
Dense table with multiple columns for reference data. Used in appendix slides.

## Standard Slide Elements

### Header
- Slide title in navy, top-left
- Subtitle or framing statement directly below title (regular weight)

### Footer (every content slide)
- Left: *Proprietary and confidential — do not distribute*
- Right: Page number

### Source Citations
- Bottom of slide, small italic
- Format: `*Source: [Organization], "[Report Title]" (Year)*`
- Multiple sources separated by semicolons

## Content Voice & Tone

- **Confident and direct**: "positions BTS-DTS to deliver" not "could potentially help"
- **Outcome-anchored**: Lead every section with the business impact
- **Human + AI framing**: Always position AI as augmenting humans, never replacing
- **Governance-aware**: Reference Responsible AI, compliance, and human-in-the-loop in every major section
- **Metric-driven**: Include specific numbers (4-10x, >20%, ~5 FTE) wherever possible
- **Source-backed**: Cite McKinsey, Gartner, MIT CISR, or equivalent for claims

## Terminology Preferences

| Use | Instead Of |
|-----|-----------|
| POD | Team / Squad |
| AI-First | AI-Enabled / AI-Powered |
| Human-in-the-loop | Manual oversight |
| Guardrails | Restrictions / Limitations |
| Intent-first | Requirements-driven |
| Capacity uplift | Headcount reduction |
| Operating model | Process change |
| Responsible AI | Ethical AI |
| Spoke | Business unit team |
| Hub | Center of Excellence |
| Multiplier | Productivity gain |
| Blueprint | Template / Playbook |

## Deck Structure Convention

1. **Title slide** — Navy background, main title + subtitle + logos
2. **Executive Summary** — 3-column grid with thesis
3. **Agenda** — Numbered sections (01-05 typical)
4. **Content slides** — Following patterns above
5. **Appendix divider** — Navy background, "Appendix"
6. **Appendix slides** — Detail tables, pilot candidates, supporting data
