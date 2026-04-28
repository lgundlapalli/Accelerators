---
name: enterprise-architect/adr
description: Write a formal Architecture Decision Record documenting a specific architectural decision, its context, alternatives, and consequences.
---

## Purpose
Produces a structured Architecture Decision Record (ADR) that captures the context, decision, consequences, and alternatives for a significant architectural choice. Use this when a decision needs to be formally documented for future reference, team alignment, or audit purposes.

## Context Brief
> To complete this I'll need: the decision being made, options considered, key drivers (cost/risk/speed/compliance), deciders
> Share what you have and I'll ask about anything missing.

## Gap Questions
Ask these one at a time, only if not already provided by the user:
1. What is the specific decision being recorded?
2. What alternatives were considered?
3. What are the key drivers or constraints (cost, risk, speed, compliance)?
4. Who are the deciders and stakeholders?
5. What are the known risks or negative consequences of the chosen option?

## Process
1. Confirm the decision statement is precise and unambiguous.
2. Document context — the forces, events, and requirements that led to this decision.
3. State the decision in one clear sentence.
4. List positive consequences, negative consequences, and risks separately.
5. Document each alternative with a concise rationale for why it was rejected.
6. Assign an ADR number — check `docs/architecture/adr/` if present to determine the next sequence number.

## Output
Produce output following the format in `references/output-formats.md` → [ADR Format].
Apply all rules in `references/behavioral-guidelines.md` and `references/quality-standards.md`.
Save to `docs/architecture/adr/ADR-[NUMBER]-[slug].md`.
