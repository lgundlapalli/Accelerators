---
name: enterprise-architect
description: "Enterprise architecture skill with interactive menu. Supports 12 capabilities including full Architecture Design Document (ADD) generation. Invoke with no arguments to see the menu, or directly: /enterprise-architect adr, /enterprise-architect add, /enterprise-architect c4-diagrams, etc."
model: sonnet
memory: user
---

## On Every Invocation

1. Load `enterprise-architect/references/behavioral-guidelines.md` and `enterprise-architect/references/quality-standards.md` — apply these rules to all outputs.
2. Check for `docs/architecture/.add-session.md` in the working project. If found, note the in-progress ADD session.
3. If invoked with a direct argument (e.g., `/enterprise-architect adr`), skip the menu and route directly to the matching sub-skill.
4. Otherwise, display the interactive menu below.

## Interactive Menu

Present this menu exactly:

---

**Enterprise Architect** — What would you like to do?

```
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
```

Type a number, or describe what you need.

---

If an in-progress ADD session was found in step 2, prepend this note above the menu:
> **Note:** You have an in-progress ADD session. Select 1 to resume it.

## Routing Table

| Selection | Sub-skill |
|-----------|-----------|
| 1 or "ADD" or "full document" | `enterprise-architect/add-mode` |
| 2 or "C4" or "diagram" | `enterprise-architect/c4-diagrams` |
| 3 or "ADR" or "decision record" | `enterprise-architect/adr` |
| 4 or "gap" or "gap analysis" | `enterprise-architect/gap-analysis` |
| 5 or "review" or "risk" | `enterprise-architect/architecture-review` |
| 6 or "API" or "interface" | `enterprise-architect/api-documentation` |
| 7 or "data" or "database" | `enterprise-architect/data-architecture` |
| 8 or "integration" | `enterprise-architect/integration-architecture` |
| 9 or "deployment" or "infrastructure" | `enterprise-architect/deployment-architecture` |
| 10 or "debt" or "technical debt" | `enterprise-architect/technical-debt` |
| 11 or "target" or "future state" | `enterprise-architect/target-architecture` |
| 12 or "solution" or "SAD" | `enterprise-architect/solution-architecture` |

If the user describes their need in natural language instead of a number, map it to the closest sub-skill and confirm before proceeding:
> "It sounds like you need [capability name] — is that right?"

## Context-Giving Flow

After routing to a sub-skill:
1. Show the sub-skill's **Context Brief** — the "here's what I'll need" summary
2. User provides what they have (freeform — paste docs, describe the situation, share diagrams)
3. Ask **Gap Questions** from the sub-skill one at a time — only for information not already provided
4. Once sufficient context is gathered, execute the sub-skill's Process and produce the Output

## Memory

Save cross-session preferences to the user's auto-memory at `/Users/GUNDLLX/.claude/projects/`:
- Technology stack defaults confirmed for a project
- Preferred diagram styles
- ADD workflow notes and decisions
- Any standing architectural principles the user has established
