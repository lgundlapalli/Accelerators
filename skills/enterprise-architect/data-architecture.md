---
name: enterprise-architect/data-architecture
description: Design data models, data flows, storage strategy, and governance considerations.
---

## Purpose
Produces a data architecture document covering entity models, data flows, storage strategy, and governance requirements. Use this when designing a new data platform, onboarding a major new data domain, or addressing compliance and data management gaps.

## Context Brief
> To complete this I'll need: key data entities, data volume/velocity, storage technology constraints, compliance requirements (HIPAA/GDPR/SOX)
> Share what you have and I'll ask about anything missing.

## Gap Questions
Ask these one at a time, only if not already provided by the user:
1. What are the core data entities and their relationships?
2. What are the data volume and velocity requirements?
3. Are there any compliance or regulatory constraints (HIPAA, GDPR, SOX)?
4. What storage technologies are already in use or preferred?
5. Are there data residency requirements?

## Process
1. Identify and model the core entities — name, key attributes, and purpose.
2. Define relationships and cardinality between entities.
3. Design the storage strategy — OLTP vs. OLAP, caching, archival tiers.
4. Document data flows — how data moves between systems, including ingestion, transformation, and consumption.
5. Address governance: data ownership, lineage, retention policies, and access control.

## Output
Produce an entity-relationship diagram in Mermaid, a data flow diagram, and a storage strategy table.
Apply all rules in `references/behavioral-guidelines.md` and `references/quality-standards.md`.
Use `references/database-design-template.md` as the document template.
Save to `docs/architecture/data-architecture-[date].md`.
