---
name: enterprise-architect/integration-architecture
description: Design integration patterns, middleware selection, event bus topology, and API gateway architecture.
---

## Purpose
Produces an integration architecture document that maps integration points, selects appropriate patterns, and designs middleware or event bus topology. Use this when connecting multiple systems, designing an event-driven platform, or selecting integration middleware.

## Context Brief
> To complete this I'll need: systems being integrated, integration style (sync/async/event), data volumes, reliability and ordering requirements
> Share what you have and I'll ask about anything missing.

## Gap Questions
Ask these one at a time, only if not already provided by the user:
1. What systems need to integrate?
2. Sync, async, or event-driven?
3. What are the data volumes per integration?
4. What are the reliability and ordering requirements?
5. Is there existing middleware or an API gateway already in place?

## Process
1. Map all integration points between systems as a matrix or list.
2. Select the appropriate pattern for each integration (request/reply, pub/sub, event sourcing, saga).
3. Design middleware or event bus topology if async patterns are used.
4. Address error handling, retry strategies, and dead-letter queue patterns.
5. Document security at integration boundaries — authentication, authorization, and encryption in transit.

## Output
Produce an integration topology diagram in Mermaid and a pattern decision table.
Apply all rules in `references/behavioral-guidelines.md` and `references/quality-standards.md`.
Use `references/interface-design-template.md` as the document template.
Save to `docs/architecture/integration-architecture-[date].md`.
