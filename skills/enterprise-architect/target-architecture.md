---
name: enterprise-architect/target-architecture
description: Design a future-state target architecture aligned to business goals with a migration approach.
---

## Purpose
Produces a target architecture document that defines the desired future state, the principles and goals driving it, and a migration path from the current state. Use this when setting a multi-year technical direction, responding to a business transformation, or establishing an architectural north star.

## Context Brief
> To complete this I'll need: current state summary, business goals driving the change, constraints, time horizon (1yr/3yr/5yr)
> Share what you have and I'll ask about anything missing.

## Gap Questions
Ask these one at a time, only if not already provided by the user:
1. What does today's architecture look like?
2. What business goals are driving this target architecture?
3. What constraints must be respected (technology, budget, compliance, team skills)?
4. What is the time horizon? (1yr / 3yr / 5yr)
5. Are there any non-negotiable architectural principles or patterns to apply?

## Process
1. Document the current state briefly — key capabilities, limitations, and pain points.
2. Define target state principles and goals — what success looks like at the horizon.
3. Design the target architecture with diagrams showing the future structure.
4. Identify the migration path from current to target — phases, sequencing, and decision points.
5. Flag risks and dependencies in the migration that could derail or delay progress.

## Output
Produce target architecture diagrams in Mermaid, a principles table, and a migration path.
Apply all rules in `references/behavioral-guidelines.md` and `references/quality-standards.md`.
Save to `docs/architecture/target-architecture-[date].md`.
