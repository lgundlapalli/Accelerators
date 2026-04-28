---
name: enterprise-architect/add-mode
description: Orchestrates the full Architecture Design Document sequence, progressing through all 8 steps and tracking state in docs/architecture/.add-session.md
---

## Purpose
Produces a complete Architecture Design Document by sequencing 8 sub-skills in logical order. Tracks progress in a session file so work can be paused and resumed across sessions.

## ADD Sequence

| Step | Sub-skill | Output | Abbott Template |
|------|-----------|--------|-----------------|
| 1 | gap-analysis | Current vs target state, migration path | — |
| 2 | solution-architecture | Full solution design | add-template.md |
| 3 | c4-diagrams | Context + container diagrams minimum | — |
| 4 | integration-architecture | Integration layer design | interface-design-template.md |
| 5 | data-architecture | Data models, flows, storage | database-design-template.md |
| 6 | deployment-architecture | Infrastructure topology | — |
| 7 | adr | Decisions made during steps 1–6 | — |
| 8 | architecture-review | Risk check across full ADD | — |

## Session State File

On first invocation, create `docs/architecture/.add-session.md` in the working project with this content:

```
# ADD Session State
**Started**: [today's date]
**Project**: [project name — ask user if not obvious]

## Progress
- [ ] Step 1: Gap Analysis
- [ ] Step 2: Solution Architecture
- [ ] Step 3: C4 Diagrams
- [ ] Step 4: Integration Architecture
- [ ] Step 5: Data Architecture
- [ ] Step 6: Deployment Architecture
- [ ] Step 7: ADRs
- [ ] Step 8: Architecture Review

## Decisions Log
(populated as decisions are made during the session)

## Open Questions
(populated as questions arise that need follow-up)

## Technology Stack
(populated as the stack is confirmed during the session)
```

On each subsequent invocation, read this file and resume from the first unchecked step.

## Process

1. **Check for existing session**: Look for `docs/architecture/.add-session.md`. If found, read it and show current progress. Ask: "Resume from Step [N] or start over?"

2. **Collect project context** (if starting fresh): Ask the user for the project name, business problem being solved, and any existing docs or diagrams to incorporate.

3. **For each step in sequence**:
   - Load the corresponding sub-skill
   - Present its Context Brief to the user
   - Ask Gap Questions one at a time for any missing information
   - Produce the artifact using the sub-skill's Process and Output instructions
   - Save the artifact to the sub-skill's specified path
   - Mark the step complete in `.add-session.md`
   - Log any decisions made to the Decisions Log section
   - Log any unresolved questions to the Open Questions section

4. **After Step 6 (Deployment Architecture)**:
   - Review the Decisions Log
   - Consolidate all significant decisions into ADR format (Step 7)
   - A decision is "significant" if it: chose one technology over alternatives, established a pattern that others must follow, or accepted a known trade-off

5. **After Step 8 (Architecture Review)**:
   - Present a summary of the complete ADD with links to all artifacts produced
   - List any open questions that need resolution
   - Ask if the user wants to create a final consolidated ADD document using `references/add-template.md`

## Context Accumulation

As the session progresses, carry forward context discovered in earlier steps:
- Technology stack confirmed in Step 1 → inform technology choices in Steps 2–6
- Integration points discovered in Step 2 → drive depth of Step 4
- Data entities established in Step 5 → referenced in Step 8 review
- All decisions logged in Steps 1–6 → become ADRs in Step 7

Apply all rules in `references/behavioral-guidelines.md` and `references/quality-standards.md`.
