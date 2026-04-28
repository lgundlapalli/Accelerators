---
name: enterprise-architect/technical-debt
description: Catalog, assess, and prioritize existing technical debt with remediation recommendations.
---

## Purpose
Produces a technical debt catalog and prioritized remediation roadmap for a system or codebase. Use this to create visibility into accumulated debt, build a business case for remediation, and sequence paydown work alongside feature delivery.

## Context Brief
> To complete this I'll need: system or codebase description, known problem areas, business criticality, tolerance for disruption
> Share what you have and I'll ask about anything missing.

## Gap Questions
Ask these one at a time, only if not already provided by the user:
1. What system or area are we assessing?
2. What are the known pain points or problem areas?
3. What is the business criticality — what is the cost if this fails?
4. What is the team's tolerance for disruption during remediation?
5. Is there a timeline or budget constraint for debt remediation?

## Process
1. Catalog each debt item with a description and location in the system.
2. Classify each item by type: architectural, code, test, documentation, or infrastructure.
3. Score each item by likelihood of impact and cost to fix.
4. Prioritize using a 2x2 of impact vs. effort — address high-impact/low-effort items first.
5. Produce a phased remediation roadmap with sequencing rationale tied to business risk reduction.

## Output
Produce a technical debt catalog table with priority scores and a phased remediation roadmap.
Apply all rules in `references/behavioral-guidelines.md` and `references/quality-standards.md`.
Save to `docs/architecture/technical-debt-[date].md`.
