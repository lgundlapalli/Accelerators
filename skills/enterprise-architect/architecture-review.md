---
name: enterprise-architect/architecture-review
description: Review an existing architecture to identify risks, anti-patterns, single points of failure, scalability issues, and security concerns.
---

## Purpose
Produces a structured architecture review report that surfaces critical risks, anti-patterns, scalability limits, and security gaps in an existing system design. Use this during pre-production reviews, post-incident analysis, or periodic architectural health checks.

## Context Brief
> To complete this I'll need: existing architecture description or docs, known pain points, scale requirements, business criticality
> Share what you have and I'll ask about anything missing.

## Gap Questions
Ask these one at a time, only if not already provided by the user:
1. Share the architecture — paste docs, diagrams, or describe the components.
2. What are the known pain points or concerns?
3. What scale does it need to support (users, transactions, data volume)?
4. What is the business criticality — what breaks if this goes down?
5. Are there any specific areas of concern you want prioritized?

## Process
1. Summarize the architecture in your own words to confirm understanding before proceeding.
2. Identify critical risks: single points of failure, data loss scenarios, unrecoverable failures.
3. Identify high risks: scalability limits, security gaps, tight coupling, missing observability.
4. Identify medium and low risks and general observations.
5. Catalog technical debt items with location and impact.
6. Produce ranked recommendations with suggested owners and concrete next steps.

## Output
Produce output following the format in `references/output-formats.md` → [Architecture Review Format].
Apply all rules in `references/behavioral-guidelines.md` and `references/quality-standards.md`.
Save to `docs/architecture/review-[date].md`.
