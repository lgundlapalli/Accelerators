# DDD Workshop Skill

A virtual Domain-Driven Design facilitator that guides you from domain discovery through strategic and tactical design to concrete artifacts.

## Skill Files

### SKILL.md — Main Orchestrator

The entry point and routing logic for the entire DDD workshop.

**Input:** A user prompt describing what they want to model — could be a greenfield domain description, a brownfield codebase, or a request for a specific DDD technique.

**Output:** Routes to the appropriate phase (Discovery, Strategic, Tactical, Artifacts) and coordinates the full interactive flow. Does not produce artifacts directly — delegates to the reference files for detailed guidance at each phase.

**Responsibilities:**
- Detects which entry point fits the user's request (event storming, storytelling, strategic, or tactical)
- Adapts explanation depth to the user's DDD fluency
- Handles greenfield vs. brownfield detection
- Manages transitions between phases
- Coordinates artifact generation at the end

---

### references/event-storming.md — Event Storming Facilitation

A step-by-step guide for running a virtual Event Storming session (based on Alberto Brandolini's technique).

**Input:** A domain or problem space the user wants to explore. Works best when the domain is unfamiliar or complex and needs collaborative discovery.

**Output:**
- A timeline of domain events (past tense: OrderPlaced, PaymentReceived)
- Commands that trigger each event (PlaceOrder, ProcessPayment)
- Actors who issue the commands (Customer, Admin, External System)
- Policies — reactive business rules connecting events to commands
- Read models — what information actors need to make decisions
- Hotspots — areas of confusion or complexity

**Derived artifacts:** Proposed aggregate boundaries (from event clusters), proposed bounded contexts (from language/actor/temporal shifts), and domain services (from cross-aggregate policies).

---

### references/domain-storytelling.md — Domain Storytelling Facilitation

A guide for narrative-based domain discovery (based on Stefan Hofer and Henning Schwentner's technique).

**Input:** The user tells stories about how work gets done in their domain — concrete scenarios with specific actors doing specific things.

**Output:**
- Structured story tables: numbered activities with Actor, Activity, and Work Object columns
- Extracted actors (roles and systems)
- Extracted work objects (classified as candidate entities or value objects)
- Extracted activities (mapped to candidate commands and domain events)
- Proposed bounded context boundaries (from language shifts, actor boundaries, scope gaps)

**Derived artifacts:** Feeds into Strategic Design (context boundaries) and Tactical Design (entities, VOs, commands, events extracted from stories).

---

### references/strategic-patterns.md — Strategic Design Patterns

Reference material for the "big picture" phase of DDD: decomposing the system into bounded contexts and understanding their relationships.

**Input:** A domain with enough complexity to warrant multiple bounded contexts — either discovered through Event Storming / Domain Storytelling, or brought by the user directly.

**Output:**
- Subdomain classification (Core, Supporting, Generic) with rationale
- Bounded context definitions with names and responsibilities
- Context map diagram (Mermaid) showing relationships between contexts
- Relationship type per context pair (Shared Kernel, Customer-Supplier, Conformist, Anti-Corruption Layer, Open Host Service, Published Language, Separate Ways, Partnership)
- Ubiquitous language glossary per context, with polysemous terms flagged

**Key decision it helps make:** Where to invest deep modeling effort (core domain) vs. where to keep it simple (generic) or buy off-the-shelf.

---

### references/tactical-patterns.md — Tactical Design Patterns

Reference material for the building blocks inside a single bounded context.

**Input:** A bounded context with identified entities and domain concepts — either from the strategic phase or brought directly by the user.

**Output:**
- Entity definitions with identity, attributes, types, and behavior methods
- Value object definitions with immutability, validation, and domain logic
- Aggregate designs with root entity, members, consistency boundaries, and invariants
- Domain events with name, trigger, payload, and consumers
- Domain services for cross-aggregate operations
- Repository interfaces with domain-language query methods
- Application service patterns for use case orchestration
- Invariant documentation table (rule, aggregate, condition, violation behavior)

**Key decision it helps make:** What goes inside an aggregate vs. outside, what's an entity vs. a value object, and where domain logic lives.

---

### references/output-templates.md — Artifact Templates

Templates and scaffolding patterns for generating concrete deliverables.

**Input:** A completed (or in-progress) domain model from the tactical design phase, plus the user's preferred output format and programming language.

**Output (user chooses one or more):**
- **Design document** — Markdown spec with glossary, context map, aggregate designs, event catalog, business rules
- **Code scaffold** — Project directory structure with entity classes, value objects, domain events, repository interfaces, and application services in the user's preferred language (TypeScript, Python, Java, C#, Go, Kotlin)
- **Diagrams** — Context maps (graph), aggregate boundaries (class diagram), event flows (sequence diagram) in Mermaid or PlantUML
- **JSON Schema** — Formal schema definitions for entities and events

**File output location:** `domain-model/` in the working directory, organized by bounded context for multi-context systems.
