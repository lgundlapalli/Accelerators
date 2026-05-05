# UX Design Skill — Phase 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a modular UX design skill (`/ux-design`) that takes a confirmed idea or vision/scope document and adaptively produces UX artifacts — personas, user journeys, user stories, Mermaid flows, and interaction patterns.

**Architecture:** Thin orchestrator (`ux-design.md`) routes to 5 capability sub-skills in `ux-design/`. Shared UX principles, artifact decision rules, and output format templates live in `ux-design/references/`. The orchestrator assesses input complexity, confirms artifact selection with the user, and sequences sub-skills while accumulating context. All output saved to `docs/ux/`.

**Tech Stack:** Markdown skill files, Mermaid diagrams, existing `sync_skill.sh` for installation to `~/.claude/commands/`

---

## File Structure

**Create:**
- `skills/ux-design/references/ux-principles.md`
- `skills/ux-design/references/artifact-decision-guide.md`
- `skills/ux-design/references/output-formats.md`
- `skills/ux-design/personas.md`
- `skills/ux-design/user-journeys.md`
- `skills/ux-design/user-stories.md`
- `skills/ux-design/flows.md`
- `skills/ux-design/interaction-patterns.md`
- `skills/ux-design.md` ← orchestrator

**Sync to:**
- `~/.claude/commands/ux-design.md`
- `~/.claude/commands/ux-design/` (all sub-skills and references)

---

## Task 1: Create Shared Reference Files

**Files:**
- Create: `skills/ux-design/references/ux-principles.md`
- Create: `skills/ux-design/references/artifact-decision-guide.md`
- Create: `skills/ux-design/references/output-formats.md`

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p /Users/GUNDLLX/learn-claude/skills/ux-design/references
```

Expected: no output, directory exists.

- [ ] **Step 2: Write ux-principles.md**

Create `/Users/GUNDLLX/learn-claude/skills/ux-design/references/ux-principles.md`:

```markdown
# UX Principles

Apply these principles to all UX design artifacts produced by this skill.

## 1. Progressive Disclosure
Show only what the user needs at each step. Defer secondary actions and advanced options until they are relevant. Never front-load complexity.

## 2. Error Prevention Over Error Recovery
Design to prevent errors before they happen. Use constraints, defaults, confirmations, and inline validation. When errors do occur, explain clearly what went wrong and how to fix it.

## 3. Consistency
Use the same patterns for the same interactions throughout the product. If a button saves on one screen, it saves on all screens. If a red color means error in one place, it means error everywhere.

## 4. Accessibility (WCAG 2.1 AA minimum)
- All form fields must have visible labels
- Color contrast ratio ≥ 4.5:1 for normal text, ≥ 3:1 for large text
- All interactive elements must be keyboard-navigable
- Error messages must not rely on color alone
- Images must have alt text

## 5. Mobile-First
Design for the smallest viewport first. Enhance for larger screens. Touch targets must be ≥ 44×44px. Avoid hover-only interactions.

## 6. Feedback
Every user action must produce a visible response. Immediate feedback for instant actions (button press, toggle). Progress indicators for actions taking > 1 second. Completion confirmation for multi-step flows.

## 7. Minimal Cognitive Load
Chunk information into groups of 5–7 items maximum. Use whitespace to separate distinct sections. Prefer recognition over recall — show options rather than requiring users to remember them.
```

- [ ] **Step 3: Write artifact-decision-guide.md**

Create `/Users/GUNDLLX/learn-claude/skills/ux-design/references/artifact-decision-guide.md`:

```markdown
# Artifact Decision Guide

Use this guide to assess input complexity and select the right artifacts to produce.

## Complexity Signals

### Simple Feature (User Stories + Flows only)
Signals present in input:
- Single user type mentioned (user, customer, admin — only one)
- Single screen or single interaction described
- No mention of steps, stages, workflow, or process
- Feature adds to an existing product (not a new product)

### Multi-User / Multi-Step Workflow (+ Personas + User Journeys)
Signals present in input:
- Two or more user types mentioned (e.g., "users and admins", "customers and suppliers")
- Words like: steps, stages, workflow, process, journey, flow, sequence
- Multi-screen interactions described
- Onboarding, setup, or configuration flows mentioned

### New Product / Platform / System (Full Package + Interaction Patterns)
Signals present in input:
- Words like: platform, system, product, app, portal, tool, solution
- Multiple feature areas described
- New user experience being created from scratch
- Integration with multiple external systems mentioned

### Explicit User Override
If the user explicitly says which artifacts they want, ignore complexity signals and produce exactly what was requested.

## Decision Table

| Complexity Level | Personas | User Journeys | User Stories | Flows | Interaction Patterns |
|---|---|---|---|---|---|
| Simple feature | — | — | ✓ | ✓ | — |
| Multi-user/step | ✓ | ✓ | ✓ | ✓ | — |
| New platform | ✓ | ✓ | ✓ | ✓ | ✓ |
| User override | as requested | as requested | as requested | as requested | as requested |

## When In Doubt
Default to the next complexity level up. It's easier to skip an artifact than to discover mid-design that a key artifact is missing.
```

- [ ] **Step 4: Write output-formats.md**

Create `/Users/GUNDLLX/learn-claude/skills/ux-design/references/output-formats.md`:

```markdown
# Output Formats

## Persona Card Format

```markdown
## Persona: [Name]

| Field | Detail |
|---|---|
| **Role** | [Job title or user type] |
| **Age range** | [e.g., 25–40] |
| **Context** | [How, when, where they use the product] |
| **Goals** | 1. [Goal 1] 2. [Goal 2] 3. [Goal 3] |
| **Pain Points** | 1. [Pain 1] 2. [Pain 2] 3. [Pain 3] |
| **Tech comfort** | [Low / Medium / High] |
| **Quote** | "[One sentence that captures their perspective]" |
```

---

## User Journey Map Format

```markdown
## Journey: [Persona Name] — [Journey Name]

**Trigger**: [What causes the user to start this journey]
**Goal**: [What they're trying to accomplish]

| Step | Action | Touchpoint | Emotion | Pain Point | Opportunity |
|---|---|---|---|---|---|
| 1 | [What user does] | [Screen/channel] | 😐/😊/😤 | [Friction] | [Design improvement] |
| 2 | ... | ... | ... | ... | ... |

**Journey outcome**: [What success looks like for the user]
```

---

## User Story Format

```markdown
## [Feature Area]

### Story [N]: [Short title]
**As a** [persona name],
**I want** [action],
**So that** [outcome].

**Acceptance Criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

**Notes**: [Any edge cases, constraints, or split flags]
```

---

## Interaction Pattern Entry Format

```markdown
## Pattern: [Pattern Name]

| Field | Detail |
|---|---|
| **When to use** | [Specific scenarios where this pattern applies] |
| **Key behavior** | [What happens when the user interacts] |
| **Accessibility** | [Specific accessibility requirements for this pattern] |
| **Edge cases** | [Empty state, error state, loading state behavior] |
| **Examples in this product** | [Which screens/features use this pattern] |
```
```

- [ ] **Step 5: Commit**

```bash
cd /Users/GUNDLLX/learn-claude
git add skills/ux-design/references/
git commit -m "feat: add ux-design shared reference files"
```

Expected: 3 files committed.

---

## Task 2: Create Sub-skill Files

**Files:**
- Create: `skills/ux-design/personas.md`
- Create: `skills/ux-design/user-journeys.md`
- Create: `skills/ux-design/user-stories.md`
- Create: `skills/ux-design/flows.md`
- Create: `skills/ux-design/interaction-patterns.md`

- [ ] **Step 1: Write personas.md**

Create `/Users/GUNDLLX/learn-claude/skills/ux-design/personas.md`:

```markdown
---
name: ux-design/personas
description: Generate user personas from a confirmed idea or vision/scope input. Each persona captures goals, pain points, context, tech comfort, and a representative quote.
---

## Purpose
Produces 2–4 user personas that represent the distinct user types identified in the input. Use when the idea involves multiple user types or a multi-step workflow.

## Inputs (passed from orchestrator — do not re-ask)
- User types identified from vision/scope
- Problem statement
- Key features list

## Process
1. Identify distinct user types from the inputs (look for roles, actors, user segments)
2. For each user type, create one persona using the Persona Card Format
3. Give each persona a realistic name, not a generic label ("Sarah, Operations Manager" not "Admin User")
4. Goals must be specific to the product context, not generic (not "get things done faster")
5. Pain points must connect to problems the product is solving
6. Limit to 4 personas maximum — merge similar types rather than creating redundant ones
7. After producing personas, list the persona names — these become the actor names used in user stories and flows

## Output
Use the Persona Card Format from `references/output-formats.md`.
Apply all rules in `references/ux-principles.md`.
Save to `docs/ux/personas-[YYYY-MM-DD].md`.
Return the list of persona names to the orchestrator for use in subsequent sub-skills.
```

- [ ] **Step 2: Write user-journeys.md**

Create `/Users/GUNDLLX/learn-claude/skills/ux-design/user-journeys.md`:

```markdown
---
name: ux-design/user-journeys
description: Map end-to-end user journeys for each persona — from trigger through task completion, capturing touchpoints, emotions, pain points, and opportunities.
---

## Purpose
Produces one journey map per persona covering the primary task they need to complete. Use when the idea involves multi-step workflows or when understanding the full user experience is critical.

## Inputs (passed from orchestrator — do not re-ask)
- Persona names and summaries from the personas sub-skill
- Key features and workflow steps from vision/scope
- Problem statement

## Process
1. For each persona, identify their primary journey (the most important task they need to accomplish)
2. Define the trigger — what causes them to start this journey
3. Break the journey into 5–8 steps (fewer if simpler, more only if genuinely needed)
4. For each step: name the action, identify the touchpoint (which screen or channel), assign an emotion (😊 positive / 😐 neutral / 😤 frustrated), identify any friction, and note a design opportunity
5. State the journey outcome — what success looks like
6. Flag any steps where the user is likely to drop off or get confused — these become priority design areas
7. After producing journey maps, list the step names per persona — these become node names in flow diagrams

## Output
Use the User Journey Map Format from `references/output-formats.md`.
Apply all rules in `references/ux-principles.md`.
Save to `docs/ux/user-journeys-[YYYY-MM-DD].md`.
Return journey step names per persona to the orchestrator for use in the flows sub-skill.
```

- [ ] **Step 3: Write user-stories.md**

Create `/Users/GUNDLLX/learn-claude/skills/ux-design/user-stories.md`:

```markdown
---
name: ux-design/user-stories
description: Generate user stories with acceptance criteria for all key features, grouped by feature area and written from the perspective of confirmed personas.
---

## Purpose
Produces a complete set of user stories covering all key features identified in the vision/scope. Always produced regardless of complexity level.

## Inputs (passed from orchestrator — do not re-ask)
- Persona names from personas sub-skill (or generic "user" if personas were not produced)
- Feature list from vision/scope
- Problem statement

## Process
1. Group features into logical feature areas (e.g., "Authentication", "Dashboard", "Settings")
2. For each feature, write 1–3 user stories using the format: "As a [persona], I want [specific action], so that [concrete outcome]"
3. Rules for good stories:
   - Use actual persona names, not "user" (e.g., "As Sarah" not "As a user")
   - The action must be specific and testable, not vague ("submit the expense report" not "manage expenses")
   - The outcome must describe a benefit, not a feature ("so that I can track spending" not "so that the form is submitted")
4. Add 2–4 acceptance criteria per story as checkboxes
5. Flag any story that is too large to implement in a single sprint with a "⚠️ Split recommended" note
6. After all stories, produce a summary count: [N] stories across [M] feature areas

## Output
Use the User Story Format from `references/output-formats.md`.
Apply all rules in `references/ux-principles.md`.
Save to `docs/ux/user-stories-[YYYY-MM-DD].md`.
```

- [ ] **Step 4: Write flows.md**

Create `/Users/GUNDLLX/learn-claude/skills/ux-design/flows.md`:

```markdown
---
name: ux-design/flows
description: Produce full flow coverage in Mermaid — navigation flows, screen interaction flows, and error state flows. Always produced regardless of complexity level.
---

## Purpose
Produces three types of flows in Mermaid syntax: (1) top-level navigation showing how users move between screens, (2) screen-level interaction flows showing happy path, alternates, and validation states, (3) error state flows showing empty states, errors, and timeouts.

## Inputs (passed from orchestrator — do not re-ask)
- Persona names and journey step names from earlier sub-skills
- Feature list and key screens from vision/scope
- User stories (for identifying key interactions per screen)

## Process

### Navigation Flows
1. List all screens/pages in the product
2. Map how users navigate between them (entry points, forward paths, back paths, exit points)
3. Use `flowchart TD` in Mermaid
4. One navigation flow per primary user type if they have different navigation structures

### Screen Interaction Flows
1. Identify the 3–5 most complex or important screens
2. For each screen, map: initial state → user action → system response → next state
3. Include alternate paths (e.g., user cancels, user edits before submitting)
4. Include validation states (e.g., form field invalid, required field missing)
5. Use `flowchart TD` with decision nodes (diamond shapes) for branches

### Error State Flows
1. For each key screen, map what happens when things go wrong:
   - Empty state: no data to display
   - Error state: system error or failed action
   - Timeout state: slow network or processing
   - Permissions state: user doesn't have access
2. Use `stateDiagram-v2` in Mermaid for state transitions

### Mermaid Validity Rules
- Every node must have a unique ID
- Node labels with spaces must be quoted: `A["Screen Name"]`
- Decision nodes use `{Question?}` syntax
- Test every diagram by tracing all paths — no dead ends unless intentional (terminal states)
- Wrap all Mermaid in ```mermaid fenced code blocks

## Output
One Mermaid block per flow with a one-paragraph explanation above each diagram.
Apply all rules in `references/ux-principles.md`.
Save to `docs/ux/flows-[YYYY-MM-DD].md`.
```

- [ ] **Step 5: Write interaction-patterns.md**

Create `/Users/GUNDLLX/learn-claude/skills/ux-design/interaction-patterns.md`:

```markdown
---
name: ux-design/interaction-patterns
description: Identify and document reusable UX interaction patterns needed by the product — forms, modals, navigation, data tables, empty states, loading states.
---

## Purpose
Produces a pattern catalog of reusable interaction patterns identified from the user stories and flows. Use for complex or platform-level products to ensure consistent implementation across the product.

## Inputs (passed from orchestrator — do not re-ask)
- User stories produced earlier
- Flow diagrams produced earlier
- Feature list from vision/scope

## Process
1. Scan user stories and flows for recurring interaction types:
   - Form submission (with validation)
   - Modal dialogs (confirmation, alert, input)
   - Navigation patterns (tabs, sidebar, breadcrumbs, back)
   - Data tables (sorting, filtering, pagination, row actions)
   - Empty states (no data, first use, search no results)
   - Loading states (skeleton screens, spinners, progress bars)
   - Notifications (success toast, error banner, inline message)
2. For each pattern identified, document it using the Interaction Pattern Entry Format
3. Under "Examples in this product", reference the specific screens or user stories where this pattern appears
4. Flag any patterns where accessibility requires special attention (e.g., modal focus trapping, form error announcements for screen readers)
5. Limit to patterns actually needed by this product — do not document patterns for interactions that don't exist in the flows

## Output
Use the Interaction Pattern Entry Format from `references/output-formats.md`.
Apply all rules in `references/ux-principles.md`.
Save to `docs/ux/interaction-patterns-[YYYY-MM-DD].md`.
```

- [ ] **Step 6: Commit all sub-skills**

```bash
cd /Users/GUNDLLX/learn-claude
git add skills/ux-design/personas.md \
        skills/ux-design/user-journeys.md \
        skills/ux-design/user-stories.md \
        skills/ux-design/flows.md \
        skills/ux-design/interaction-patterns.md
git commit -m "feat: add ux-design sub-skill files"
```

Expected: 5 files committed.

---

## Task 3: Create Orchestrator

**Files:**
- Create: `skills/ux-design.md`

- [ ] **Step 1: Write ux-design.md**

Create `/Users/GUNDLLX/learn-claude/skills/ux-design.md`:

```markdown
---
name: ux-design
description: "UX design skill that takes a confirmed idea or vision/scope document and produces UX artifacts adaptively — personas, user journeys, user stories, Mermaid flows, and interaction patterns. Invoked after a product idea has been validated at vision/scope level."
model: sonnet
---

## On Every Invocation

Load `ux-design/references/ux-principles.md` — apply these rules to all outputs.

## Invocation Menu

Present this menu exactly:

---
**UX Design** — Let's turn your confirmed idea into a design.

How would you like to provide your input?
  1. Describe or paste your confirmed idea
  2. Point me to a vision/scope document (file path or paste content)

---

## Input Processing

After the user provides input, extract these fields:
- **Problem statement**: what problem is being solved
- **Target users**: who uses this product (list all user types mentioned)
- **Key features**: what the product does (bullet list)
- **Constraints**: technical, business, or timeline constraints mentioned

Summarize back to the user:
> "Here's what I understood from your input:
> - Problem: [problem statement]
> - Users: [list of user types]
> - Features: [feature list]
> - Constraints: [constraints or 'none mentioned']
>
> Does this capture the idea correctly? (yes / correct these points)"

Wait for confirmation before proceeding.

## Complexity Assessment

After input is confirmed, apply the rules in `ux-design/references/artifact-decision-guide.md` to determine which artifacts to produce.

Present to the user:
> "Based on your input, this looks like a [simple feature / multi-user workflow / new platform].
> I'll produce: [list of artifacts].
> Does that sound right, or do you want to adjust?"

Wait for confirmation before generating any artifacts.

## Sub-skill Execution Sequence

Run sub-skills in this order, passing context forward at each step:

1. **personas** (if selected) — pass: user types, problem statement, feature list
   - After completion, extract: persona names → pass to steps 2, 3, 4
2. **user-journeys** (if selected) — pass: personas, feature list, problem statement
   - After completion, extract: journey step names per persona → pass to step 4
3. **user-stories** (always) — pass: persona names (or "user" if no personas), feature list
4. **flows** (always) — pass: persona names, journey step names, feature list, key screens from user stories
5. **interaction-patterns** (if selected) — pass: user stories, flows, feature list

## Session Output Summary

After all sub-skills complete, present:

---
**UX Design complete.** Artifacts produced:

[List only the artifacts that were produced, with their file paths]
- Personas: `docs/ux/personas-[date].md`
- User Journeys: `docs/ux/user-journeys-[date].md`
- User Stories: `docs/ux/user-stories-[date].md`
- Flows: `docs/ux/flows-[date].md`
- Interaction Patterns: `docs/ux/interaction-patterns-[date].md`

**Next steps available:**
- `/ux-design html-prototype` — generate an HTML prototype from these artifacts *(Phase 2)*
- `/ux-design pptx` — generate a presentation deck *(Phase 3)*
---
```

- [ ] **Step 2: Commit**

```bash
cd /Users/GUNDLLX/learn-claude
git add skills/ux-design.md
git commit -m "feat: add ux-design orchestrator skill"
```

---

## Task 4: Sync and Verify

**Files:**
- Run: `skills/shared-scripts/sync_skill.sh ux-design`

- [ ] **Step 1: Run sync script**

```bash
/Users/GUNDLLX/learn-claude/skills/shared-scripts/sync_skill.sh ux-design
```

Expected:
```
Synced: ux-design
```

- [ ] **Step 2: Verify files installed**

```bash
echo "=== Orchestrator ===" && head -3 ~/.claude/commands/ux-design.md
echo "=== Sub-skills ===" && ls ~/.claude/commands/ux-design/*.md
echo "=== References ===" && ls ~/.claude/commands/ux-design/references/*.md
```

Expected:
- Orchestrator header with `name: ux-design`
- 5 sub-skill files listed
- 3 reference files listed

- [ ] **Step 3: Verify skill appears in Claude Code**

Start a new Claude Code session. Run `/ux-design`. Expected: invocation menu appears with options 1 and 2.

- [ ] **Step 4: Commit sync verification note**

```bash
cd /Users/GUNDLLX/learn-claude
git add .
git commit -m "feat: ux-design skill Phase 1 complete — synced to ~/.claude/commands"
```
