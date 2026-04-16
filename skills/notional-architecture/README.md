# Notional Architecture Skill

Produces a high-level conceptual notional architecture from strategic business inputs. Maps business capabilities to technical enablers and components, organized into a 6-layer architecture model with security and governance as cross-cutting concerns.

## Skill Files

### SKILL.md — Main Orchestrator

The entry point and interactive flow for the notional architecture design process.

**Input:** 10 structured strategic inputs collected one at a time:
1. Vision
2. Mission
3. Current State Pain Points
4. Journeys
5. Value Proposition
6. Outcomes Expected
7. Success Drivers
8. Regional Contexts
9. Business Capabilities
10. Journey Experience Matrix

**Output:** Routes through input collection → capability categorization → enabler mapping → component derivation → layered architecture diagram. User chooses output format (Mermaid, Miro, or both).

---

### references/capability-mapping.md — Capability Mapping Process

Step-by-step guide for categorizing business capabilities and mapping them to architecture layers.

**Input:** Raw business capabilities extracted from all 10 user inputs.

**Output:** Categorized capabilities (Experience, Process, Data, Integration, Platform) mapped to technical enablers, then grouped into named components placed into architecture layers.

---

### references/enabler-catalog.md — Technical Enabler Catalog

Reference catalog of common business capability → technical enabler → technology option mappings.

**Input:** A categorized business capability (e.g., "API Management" in the Integration category).

**Output:** Recommended technical enabler pattern and concrete technology options (e.g., API Gateway → Kong, AWS API Gateway, Apigee). Includes regional context overlays for data residency, multi-region, and regulatory requirements.

---

### references/output-formats.md — Output Format Templates

Templates for producing the notional architecture in Mermaid, Miro, or both formats.

**Input:** Completed capability-to-enabler-to-component mapping with layer assignments.

**Output:**
- **Mermaid template** — Layered architecture diagram with subgraphs per layer, components, and connections
- **Miro template** — Step-by-step instructions for pushing the architecture to a Miro board using MCP (frames, shapes, connectors, color scheme)
- **Design document template** — Full Markdown spec with strategic context, mapping tables, component descriptions, and journey traceability
