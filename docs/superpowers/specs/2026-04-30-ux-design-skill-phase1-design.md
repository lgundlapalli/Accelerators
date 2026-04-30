# UX Design Skill — Phase 1 Design Spec

**Date**: 2026-04-30
**Status**: Approved
**Phase**: 1 of 3
**Goal**: Build a modular UX design skill that takes a confirmed idea (from vision/scope) and produces the right UX artifacts adaptively — user stories, flows, personas, user journeys, and interaction patterns.

---

## Context

This skill serves a broad audience — both technical and non-technical users at Abbott — who need to translate a confirmed product idea into UX design artifacts. Input can be a vision/scope document or a verbal description. The skill assesses complexity and decides what to produce, confirms with the user before generating, and accumulates context across sub-skills so later artifacts build on earlier ones.

Phase 1 covers core artifacts and Mermaid-based flows.
Phase 2 (separate spec) adds HTML prototype output.
Phase 3 (separate spec) adds PPTX deck output via the existing pptx-generator skill.

---

## File Structure

```
~/.claude/commands/
└── ux-design.md                          ← thin orchestrator

~/.claude/commands/ux-design/
├── references/
│   ├── ux-principles.md                  ← UX best practices, accessibility, voice/tone
│   ├── artifact-decision-guide.md        ← complexity rules driving artifact selection
│   └── output-formats.md                 ← templates for all artifact types
│
├── personas.md
├── user-journeys.md
├── user-stories.md
├── flows.md
└── interaction-patterns.md
```

Source files live in `learn-claude/skills/ux-design/` and are synced to `~/.claude/commands/` using the existing `skills/shared-scripts/sync_skill.sh`.

---

## Orchestrator Design (`ux-design.md`)

### Invocation Menu

```
UX Design — Let's turn your idea into a design.

How would you like to provide your input?
  1. Paste or describe your confirmed idea
  2. Point me to a vision/scope document (file path or paste content)

After I understand the idea, I'll assess what artifacts to produce and confirm with you before starting.
```

### Input Processing

- If the user provides a file path, read the file and extract: problem statement, target users, key features, constraints.
- If the user pastes content or describes verbally, extract the same fields through a brief clarifying question if anything is missing.
- Summarize the extracted input back to the user in 3–5 bullet points and ask: "Does this capture the idea correctly?"

### Complexity Assessment

Apply rules from `references/artifact-decision-guide.md`:

| Signal | Artifacts Produced |
|---|---|
| Simple feature, single user type | User stories + Flows |
| Multi-user or multi-step workflow | + Personas + User journeys |
| New product, platform, or system | Full package + Interaction patterns |
| Explicit user request | Whatever they specified |

### Confirmation Before Generating

After assessment, present:
> "Based on your input, this looks like a [simple feature / multi-step workflow / new platform]. I'll produce: [list of artifacts]. Does that sound right, or do you want to adjust?"

Wait for confirmation before running any sub-skill.

### Sub-skill Execution Sequence

Run in this order to accumulate context:
1. `personas` (if applicable)
2. `user-journeys` (if applicable)
3. `user-stories` (always)
4. `flows` (always)
5. `interaction-patterns` (if applicable)

Pass accumulated context forward:
- Personas → actor names used in user stories and flows
- User journeys → step names used as flow nodes
- User stories → acceptance criteria referenced in interaction patterns

### Session Output Summary

After all sub-skills complete, present:
```
UX Design complete. Artifacts produced:

- Personas: docs/ux/personas-[date].md
- User Journeys: docs/ux/user-journeys-[date].md
- User Stories: docs/ux/user-stories-[date].md
- Flows: docs/ux/flows-[date].md
- Interaction Patterns: docs/ux/interaction-patterns-[date].md
```

---

## Sub-skill Design

All sub-skills follow this structure:
```markdown
---
name: ux-design/<capability>
description: <one-line trigger>
---

## Purpose
## Inputs (passed from orchestrator — do not re-ask)
## Process
## Output
```

### `personas.md`
- **Purpose**: Generate 2–4 user personas capturing goals, pain points, context, and behavior patterns
- **Inputs**: Extracted user types from vision/scope, problem statement
- **Process**: For each user type, define name, role, goals (3), pain points (3), context (how/when/where they use the product), and a one-line quote
- **Output format**: Persona card table per persona. Save to `docs/ux/personas-[date].md`

### `user-journeys.md`
- **Purpose**: Map end-to-end journeys for each persona — from first awareness through task completion
- **Inputs**: Personas produced in step 1, key features from vision/scope
- **Process**: For each persona, define: trigger, steps (numbered), touchpoints, emotions at each step, pain points, and opportunities
- **Output format**: Journey map table per persona. Save to `docs/ux/user-journeys-[date].md`

### `user-stories.md`
- **Purpose**: Generate user stories with acceptance criteria for all key features
- **Inputs**: Personas, feature list from vision/scope
- **Process**: (1) Group stories by feature area (2) Write each as "As a [persona], I want [action] so that [outcome]" (3) Add 2–4 acceptance criteria per story (4) Flag any story that is too large and should be split
- **Output format**: Stories grouped by feature, with acceptance criteria. Save to `docs/ux/user-stories-[date].md`

### `flows.md`
- **Purpose**: Produce full flow coverage — navigation flows, screen interaction flows, and error state flows in Mermaid
- **Inputs**: User journeys, user stories, feature list
- **Process**:
  1. **Navigation flows**: Top-level flow showing how users move between screens/sections
  2. **Screen interaction flows**: Per key screen — happy path, alternate paths, validation states
  3. **Error state flows**: What happens when things go wrong (empty states, errors, timeouts)
  - Use Mermaid `flowchart TD` for navigation, `stateDiagram-v2` for interaction/error states
  - Ensure all Mermaid is syntactically valid
- **Output format**: One Mermaid block per flow with explanatory text. Save to `docs/ux/flows-[date].md`

### `interaction-patterns.md`
- **Purpose**: Identify and document reusable UX patterns needed by the product
- **Inputs**: User stories, flows, feature list
- **Process**: (1) Identify recurring interaction types (forms, modals, navigation, data tables, empty states, loading states) (2) For each pattern document: when to use it, key behavior, accessibility notes, edge cases
- **Output format**: Pattern catalog table with behavior descriptions. Save to `docs/ux/interaction-patterns-[date].md`

---

## Shared References Design

### `references/ux-principles.md`
Core UX principles applied to all artifacts:
- Progressive disclosure — show only what's needed at each step
- Error prevention over error recovery
- Consistency — same patterns for same interactions
- Accessibility — WCAG 2.1 AA minimum; label all form fields; sufficient color contrast
- Mobile-first — design for smallest viewport first
- Feedback — every user action gets a visible response

### `references/artifact-decision-guide.md`
Contains the complexity assessment rules table (see Orchestrator Design above) plus:
- How to detect user type count from input (look for "users", "roles", "personas", "customers", "admins")
- How to detect workflow complexity (look for "steps", "stages", "process", "workflow", "journey")
- How to detect platform scope (look for "platform", "system", "product", "app", "portal")

### `references/output-formats.md`
Templates for:
- Persona card (name, role, goals, pain points, context, quote)
- Journey map (persona, trigger, steps, touchpoints, emotions, pain points, opportunities)
- User story (As a / I want / So that + acceptance criteria)
- Interaction pattern entry (name, when to use, behavior, accessibility, edge cases)

---

## Phase Boundaries

### Phase 1 (this spec)
- Orchestrator + 5 sub-skills + 3 reference files
- All output in Markdown + Mermaid

### Phase 2 (separate spec)
- Add `ux-design/html-prototype.md` sub-skill
- Reads Phase 1 artifacts and generates a navigable HTML prototype
- No changes to Phase 1 files

### Phase 3 (separate spec)
- Add `ux-design/pptx-output.md` sub-skill
- Reads Phase 1 artifacts and calls existing `pptx-generator` skill
- Outputs a UX presentation deck in Abbott BTS-DTS brand
- No changes to Phase 1 files

---

## What Does Not Change
- All existing skills (`enterprise-architect`, `presentation`, etc.) are untouched
- Sync script `skills/shared-scripts/sync_skill.sh` is reused as-is
- Output format follows the same `docs/` convention used across the project
