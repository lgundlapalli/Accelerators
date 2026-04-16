# Presentation Skill — Definitions

## SKILL.md — Presentation Builder (Main Orchestrator)

**Purpose**: Interactive presentation builder that generates structured `.md` presentation files with embedded executive communication frameworks.

**Entry Modes**:
- **Mode 1 — Build from Scratch**: Topic + audience + outcome + time slot → full presentation
- **Mode 2 — Refactor Draft**: Existing slides → audit against 7 principles → restructure with before/after per slide → refactored `.md`
- **Mode 3 — Review Only**: Existing slides → principle scorecard + top 5 fixes + 3 example rewrites (no full rewrite)

**Inputs (Mode 1)**:
1. Topic / project / initiative description
2. Target audience (engineers, executives, mixed, board, customers)
3. Desired outcome (approval, alignment, education, funding, decision)
4. Time slot duration (5, 15, 30, 60 min)
5. Existing content to incorporate (docs, diagrams, data, prior decks) — optional

**Inputs (Mode 2/3)**:
1. Existing draft (pasted, file path, or described)
2. Target audience (if not obvious from draft)
3. Desired outcome (if not obvious from draft)
4. What to preserve (elements the user wants kept as-is)

**Outputs**:
- Single `.md` file with slide-separated presentation
- Speaker notes per slide
- Appendix with anticipated Q&A (5 hardest questions + crisp answers)
- Backup/appendix slides for deep-dive topics
- Principle scorecard (Mode 2 and 3)
- Before/after per slide (Mode 2)

**Adaptive Types**: Architecture Deck (A), Stakeholder Pitch (B), General Presentation (C), Executive Briefing (D), Auto-detect (E)

---

## references/brand-template.md

**Purpose**: Abbott BTS-DTS brand template extracted from the AI-First Strategy & Operating Model deck. Applied to ALL presentations automatically.

**Inputs**: N/A — loaded automatically at session start

**Outputs**: Enforces across all generated/refactored presentations:
- Color palette (deep navy `#000050`, lavender `#DDDDF8`, white, near-black) with Mermaid theme variables
- 12 slide layout patterns (title, exec summary 3-column grid, numbered agenda, side-by-side definitions, vision+objectives, big number impact grid, People/Process/Technology shifts, hub-spoke ownership, role/responsibility table, phased roadmap, section divider, detail table)
- Typography rules, confidentiality footer, source citation format
- Terminology map (POD, AI-First, guardrails, capacity uplift, blueprint, etc.)
- Deck structure: Title → Exec Summary → Agenda → Content → Appendix Divider → Appendix
- Voice: confident, outcome-anchored, metric-driven, Human + AI framing

---

## references/architecture-deck.md

**Purpose**: Template and guidance for presenting technical architectures to mixed audiences.

**Inputs**: Architecture artifacts (diagrams, design docs, capability maps)

**Outputs**: 12-slide structure covering business context, architecture overview (Mermaid), design decisions, before/after comparison, risk matrix, roadmap, and the ask. Includes audience calibration matrix (C-Suite → Architects) and Mermaid diagram guidelines.

---

## references/stakeholder-pitch.md

**Purpose**: Template for persuading decision-makers to approve, fund, or prioritize an initiative.

**Inputs**: Business case, financial model, competitive analysis, implementation plan

**Outputs**: 11-slide structure following the Why Care → What We Propose → Why It Works → What To Do framework. Includes persuasion techniques (anchoring, loss aversion, social proof, commitment consistency) and options comparison table.

---

## references/general-presentation.md

**Purpose**: Template for team alignment, knowledge sharing, project kickoffs, and training.

**Inputs**: Topic content, audience context, desired learning outcomes

**Outputs**: N-slide structure using the Inform-Align-Act framework. Includes 5 content slide patterns (Comparison, Framework, Evidence, Demo, Decision), engagement techniques for remote vs. in-person, and visual design guidance for Mermaid/tables/code.

---

## references/executive-briefing.md

**Purpose**: Ultra-concise briefing format for C-suite / VP-level audiences (15 min or less).

**Inputs**: Status metrics, risk/blocker details, decision context

**Outputs**: 5-slide BLUF (Bottom Line Up Front) structure with traffic-light dashboard, key metrics, and prepared answers for the 5 hardest executive questions. Includes escalation-specific guidance and time budgeting (present less, discuss more).
