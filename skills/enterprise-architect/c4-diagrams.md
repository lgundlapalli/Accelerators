---
name: enterprise-architect/c4-diagrams
description: Create C4 architecture diagrams (Context, Container, Component, Code) using Mermaid syntax.
---

## Purpose
Produces C4 model diagrams in Mermaid syntax at the requested level of abstraction — Context, Container, Component, or Code. Use this to communicate architecture clearly to different audiences, from executives (Context) to developers (Component/Code).

## Context Brief
> To complete this I'll need: system name, key users/actors, external systems it integrates with, internal components if known, diagram level needed
> Share what you have and I'll ask about anything missing.

## Gap Questions
Ask these one at a time, only if not already provided by the user:
1. What is the system name and what does it do?
2. Who are the key users or actors?
3. What external systems does it integrate with?
4. Which C4 level is needed? (Context / Container / Component / Code)
5. Are there any internal components you want to highlight?

## Process
1. Clarify which C4 level(s) are needed and confirm scope.
2. For Context: show the system, users, and external systems only — no internal detail.
3. For Container: show internal containers (web app, API, database, etc.) and their interactions with each other and external systems.
4. For Component: drill into one container and show its internal components and responsibilities.
5. Ensure all Mermaid syntax is valid before outputting — test bracket nesting, node IDs, and relationship syntax.

## Output
Produce Mermaid diagrams with explanatory text for each level produced.
Apply all rules in `references/behavioral-guidelines.md` and `references/quality-standards.md`.
Save to `docs/architecture/diagrams/`.
