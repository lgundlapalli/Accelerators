---
name: enterprise-architect/solution-architecture
description: Produce a comprehensive Solution Architecture Document covering functional, non-functional, and cross-cutting concerns.
---

## Purpose
Produces a full Solution Architecture Document (SAD) that defines the technical approach to solving a business problem, covering functional design, NFRs, integration points, security, and deployment. Use this when building a new system or making a significant architectural change that requires a formal design record.

## Context Brief
> To complete this I'll need: business problem, key functional requirements, non-functional requirements (scale/availability/security), technology constraints, integration points
> Share what you have and I'll ask about anything missing.

## Gap Questions
Ask these one at a time, only if not already provided by the user:
1. What business problem does this solve?
2. What are the top 3-5 functional requirements?
3. What are the NFRs (scale, availability, security, compliance)?
4. What technology stack is in use or preferred?
5. What are the key integration points with other systems?

## Process
1. Establish business context and goals — why this solution is being built.
2. Define scope and constraints — what is in and out of scope.
3. State architecture principles guiding decisions.
4. Produce a solution overview with a high-level diagram.
5. Detail component, integration, data, security, and deployment architecture.
6. Document how each NFR is met by the design.
7. Log key architectural decisions made during the design.

## Output
Produce output following the format in `references/output-formats.md` → [Solution Architecture Document Format].
Apply all rules in `references/behavioral-guidelines.md` and `references/quality-standards.md`.
Use `references/add-template.md` as the document template.
Save to `docs/architecture/solution-architecture-[date].md`.
