# Enterprise Architect Skill — Modularization Design

**Date**: 2026-04-28  
**Status**: Approved  
**Goal**: Modularize the monolithic `enterprise-architect.md` skill into a two-tier structure with shared references and an ADD (Architecture Design Document) orchestration mode, without disrupting existing outcomes.

---

## Context

The current `enterprise-architect.md` skill is a single file handling 11 distinct capabilities. All behavioral guidelines, output formats, and quality standards are inlined. This makes the skill hard to maintain (changing a standard requires editing the whole file) and impossible to invoke capability-by-capability cleanly.

The user's primary outcome is producing a full **Architecture Design Document (ADD)**. The redesign must support both:
- Standalone invocation of any single capability
- A sequenced ADD mode that assembles a complete document

---

## File Structure

```
~/.claude/commands/
└── enterprise-architect.md                  ← orchestrator + ADD mode

~/.claude/commands/enterprise-architect/
├── references/
│   ├── behavioral-guidelines.md             ← scope discipline, clarification, rigor, risk, vendor neutrality
│   ├── quality-standards.md                 ← Mermaid validity, language precision, traceability
│   └── output-formats.md                    ← all format templates (ADR, review, gap analysis, SAD)
│
├── c4-diagrams.md
├── adr.md
├── solution-architecture.md
├── architecture-review.md
├── api-documentation.md
├── data-architecture.md
├── integration-architecture.md
├── deployment-architecture.md
├── technical-debt.md
├── target-architecture.md
└── gap-analysis.md
```

---

## Orchestrator Design (`enterprise-architect.md`)

The orchestrator is a thin routing file. It does four things:

1. **Interactive menu**: When invoked with no argument, display a numbered menu of all 12 capabilities. User types a number or describes their need. The orchestrator routes to the correct sub-skill.

2. **Standalone mode**: When invoked with a specific capability (e.g., `/enterprise-architect adr`), skip the menu and load the matching sub-skill directly.

3. **ADD mode**: When invoked with `/enterprise-architect add` or when the user selects option 1 from the menu, run the ADD sequence below.

4. **Memory**: On every invocation, check `docs/architecture/.add-session.md` in the working project (if it exists) and load relevant context before proceeding.

### Interactive Menu

```
Welcome to Enterprise Architect. What would you like to do?

 1. Build a full Architecture Design Document (ADD)
 2. Create a C4 Diagram
 3. Write an Architecture Decision Record (ADR)
 4. Perform a Gap Analysis
 5. Review an existing architecture
 6. Document APIs
 7. Design data architecture
 8. Design integration architecture
 9. Create a deployment diagram
10. Identify technical debt
11. Propose a target architecture
12. Create a solution architecture document

Type a number or describe what you need.
```

### Context-Giving Flow (Hybrid — Option C)

When the user selects a capability, the orchestrator:

1. **Shows a context brief** — a short "here's what I'll need" summary specific to that capability. Example for ADR:
   > "To write an ADR I'll need: the decision being made, the options considered, the drivers (cost, risk, speed, compliance), and who the deciders are. Share what you have and I'll ask about anything missing."

2. **User provides what they have** — freeform, paste docs, describe the situation, whatever they have.

3. **Orchestrator asks gap-filling questions one at a time** — only for information not already provided. Stops asking once it has enough to produce the artifact.

4. **Produces the output** using the sub-skill + shared references.

Each sub-skill defines its own context brief (what it needs) and its gap-filling questions (what to ask if context is missing). This keeps the orchestrator thin — it just runs the flow, the sub-skill defines the content.

### ADD Mode Sequence

| Step | Sub-skill | Purpose |
|------|-----------|---------|
| 1 | `gap-analysis` | Establish current vs target state — scopes everything that follows |
| 2 | `solution-architecture` | Overall solution design and principles |
| 3 | `c4-diagrams` | Visual architecture (context + container minimum) |
| 4 | `integration-architecture` | Integration layer design |
| 5 | `data-architecture` | Data models, flows, storage strategy |
| 6 | `deployment-architecture` | Infrastructure and cloud topology |
| 7 | `adr` | Capture decisions made during the above steps |
| 8 | `architecture-review` | Final risk and anti-pattern check across the full ADD |

After each step, the orchestrator updates `docs/architecture/.add-session.md` with the section status and any decisions or open questions surfaced.

---

## Sub-skill Design

Each sub-skill file follows this structure:

```markdown
---
name: enterprise-architect/<capability>
description: <one-line trigger description>
---

<!-- Loads automatically via orchestrator -->

## Purpose
<one paragraph — what this capability produces and when to use it>

## Inputs Required
<what the user must provide before this skill can proceed>

## Process
<how to execute this capability — questions to ask, steps to follow>

## Output
<exact output format — references references/output-formats.md for the template>
```

Sub-skills do **not** repeat behavioral guidelines or quality standards — those live exclusively in `references/` and are loaded by the orchestrator on every invocation.

---

## Shared References Design

### `references/behavioral-guidelines.md`
Contains the 7 behavioral rules from the current skill:
- Scope discipline
- Clarification first (all questions in one response)
- Structured Markdown output
- Mermaid diagrams
- Architectural rigor and framework references
- Risk awareness and taxonomy
- Vendor neutrality

### `references/quality-standards.md`
Contains:
- Mermaid syntax validity requirements
- Language precision standards
- Traceability requirements (recommendations traceable to requirements)
- Terminology consistency
- Assumption flagging

### `references/output-formats.md`
Contains all format templates:
- ADR format
- Architecture Review format
- Gap Analysis format
- Solution Architecture Document format
- (Add new formats here without touching sub-skills)

---

## Session State Design

Two-layer persistence:

### Layer 1 — Project session file
`docs/architecture/.add-session.md` in the working project.

Tracks:
- Which ADD sections are complete / in-progress / pending
- Key decisions made (with ADR references)
- Open questions not yet resolved
- Technology stack confirmed for this project

Created on first ADD mode invocation, updated after each step. Checked on every orchestrator invocation.

### Layer 2 — Auto-memory
`/Users/GUNDLLX/.claude/projects/-Users-GUNDLLX-.../memory/`

Stores cross-session preferences:
- Preferred diagram styles
- Technology stack defaults
- ADD workflow preferences learned from past sessions

---

## Migration Plan

1. Extract `references/behavioral-guidelines.md`, `references/quality-standards.md`, `references/output-formats.md` from current skill
2. Create 11 sub-skill files — each focused, referencing shared content
3. Rewrite `enterprise-architect.md` as thin orchestrator with ADD mode
4. Fix hardcoded memory path (`/Users/kenwilson/` → `/Users/GUNDLLX/`)
5. Install to `~/.claude/commands/enterprise-architect/`
6. Smoke-test: standalone invocation of `adr`, then full ADD mode end-to-end

---

## What Does Not Change

- All 11 capability outputs remain identical
- Output format templates are preserved exactly
- Behavioral guidelines are preserved exactly — just moved to a shared file
- The skill trigger description and examples in the frontmatter are preserved
