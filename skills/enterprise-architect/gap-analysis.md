---
name: enterprise-architect/gap-analysis
description: Perform a structured gap analysis comparing current state architecture to a defined target state, with a prioritized migration path.
---

## Purpose
Produces a structured gap analysis that maps the delta between current and target architecture across capability areas, and proposes a phased migration roadmap. Use this when planning a transformation, platform migration, or modernization initiative.

## Context Brief
> To complete this I'll need: current architecture description or docs, target state vision or requirements, constraints (timeline/budget/compliance/tech lock-in)
> Share what you have and I'll ask about anything missing.

## Gap Questions
Ask these one at a time, only if not already provided by the user:
1. How would you describe the current architecture?
2. What does the target state look like?
3. What are the hard constraints (timeline, budget, compliance, technology lock-in)?
4. What is the migration timeline?
5. Which gaps are highest priority from a business perspective?

## Process
1. Summarize the current state in 3-5 bullets covering key capabilities and limitations.
2. Summarize the target state in 3-5 bullets covering what the future architecture achieves.
3. For each capability area, assess current vs. target and identify the gap.
4. Prioritize gaps High/Medium/Low by business impact and migration effort.
5. Propose a phased migration roadmap with logical sequencing that respects dependencies and constraints.

## Output
Produce output following the format in `references/output-formats.md` → [Gap Analysis Format].
Apply all rules in `references/behavioral-guidelines.md` and `references/quality-standards.md`.
Save to `docs/architecture/gap-analysis-[date].md`.
