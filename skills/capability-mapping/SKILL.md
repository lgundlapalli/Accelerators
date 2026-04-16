---
name: capability-mapping
description: "Map business capabilities to technical enablers and architecture components. Use standalone when you need to categorize capabilities, identify technology patterns, and produce a traceability table — without running a full notional architecture. Also used as a reference within /notional-architecture."
---

# Capability Mapping

## What
Takes a list of **business capabilities** and maps each one to a technical enabler, a named component, and an architecture layer. Produces a traceability table showing how business needs connect to technology decisions.

## When
- You have a list of capabilities (from a PRD, user stories, or brainstorm) and want to know what technology patterns support them
- You want a quick capability-to-component mapping without running the full `/notional-architecture` 10-input process
- You're reviewing an architecture and want to verify every capability has a corresponding component

## Where
- **Input**: A list of capabilities (typed, pasted, or extracted from .docx/.pptx/.pdf)
- **Output**: A markdown mapping table (Capability → Category → Enabler → Component → Layer)
- **Parent skill**: Also runs automatically as part of `/notional-architecture` (Step 1-2 of the processing phase)

---

You are a solution architect helping the user map business capabilities to technical enablers and architecture components.

## Standalone Mode

When invoked directly (not from `/notional-architecture`), collect inputs interactively:

### Step 1: Collect Capabilities

Ask the user:
> **What business capabilities do you need to map?**
> List what the system needs to do — or provide a document (.docx, .pptx, .pdf) and I'll extract them.

Accept input as:
- A bullet list of capabilities
- A document file (use Document Ingestion — `python3 ~/.claude/scripts/extract_doc.py` or `python3 ~/.claude/scripts/extract_pptx.py`)
- A description of the system ("we need a customer portal that does X, Y, Z")
- A PRD, user story, or requirements doc

### Step 2: Ask for Context (optional but recommended)

> **Any constraints I should know?**
> - Cloud provider preference (AWS, Azure, GCP, multi-cloud)?
> - Regulatory requirements (HIPAA, GDPR, PCI-DSS, SOC2)?
> - Existing technology landscape (what's already in place)?
> - Scale expectations (users, transactions, data volume)?

If the user skips this, proceed with cloud-agnostic recommendations.

### Step 3: Categorize, Map, and Output

1. Categorize each capability (use the Capability Categories reference below)
2. Map to technical enablers (use the Enabler Catalog patterns)
3. Derive named components
4. Assign to architecture layers
5. Produce the output table

### Output

Produce a markdown table:

| # | Business Capability | Category | Technical Enabler | Component | Layer |
|---|---|---|---|---|---|
| 1 | [capability] | [category] | [enabler] | [component] | [layer] |

If the user wants, also produce:
- A grouped view by layer
- Technology options for each enabler (from the enabler catalog)
- A gap analysis (capabilities that don't map cleanly)

---

## Capability Categories

### Experience Capabilities
User-facing interactions and touchpoints. These map to the Experience Layer.

| Capability Pattern | Examples |
|---|---|
| Self-service portals | Customer portal, patient portal, partner portal |
| Mobile experience | Native app, PWA, responsive web |
| Notifications & alerts | Email, SMS, push, in-app notifications |
| Content management | CMS, digital asset management |
| Search & discovery | Product search, knowledge base, catalog browsing |
| Personalization | Recommendations, tailored content, user preferences |
| Accessibility | WCAG compliance, multi-language, screen reader support |

### Process Capabilities
Business logic, workflows, and orchestration. These map to the Application Services Layer.

| Capability Pattern | Examples |
|---|---|
| Workflow orchestration | Order processing, approval chains, onboarding flows |
| Business rules engine | Eligibility checks, pricing rules, policy enforcement |
| Case management | Support tickets, claims processing, dispute resolution |
| Scheduling | Appointment booking, job scheduling, batch processing |
| Document generation | Invoices, reports, certificates, letters |
| State management | Order status tracking, lifecycle management |

### Data Capabilities
Storage, analytics, and data management. These map to the Data Layer.

| Capability Pattern | Examples |
|---|---|
| Transactional data | OLTP databases, record systems |
| Analytics & reporting | BI dashboards, ad-hoc queries, KPI tracking |
| Data integration | ETL/ELT, data pipelines, master data management |
| Data warehouse | Historical analytics, data lake, dimensional modeling |
| Caching | Session cache, content cache, API response cache |
| Search indexing | Full-text search, faceted search, autocomplete |

### Integration Capabilities
Connectivity between systems, external APIs, and messaging. These map to the Integration Layer.

| Capability Pattern | Examples |
|---|---|
| API management | API gateway, rate limiting, versioning, developer portal |
| Event-driven messaging | Pub/sub, event streaming, message queues |
| System integration | ESB, iPaaS, point-to-point connectors |
| File transfer | SFTP, bulk data exchange, EDI |
| External API consumption | Third-party services, partner APIs, SaaS connectors |
| Real-time sync | Webhooks, change data capture, bidirectional sync |

### Platform Capabilities
Cross-cutting infrastructure and operational concerns. These map to the Infrastructure Layer and Security & Governance cross-cut.

| Capability Pattern | Examples |
|---|---|
| Identity & access | IAM, SSO, MFA, RBAC, OAuth2/OIDC |
| Security | Encryption, WAF, DDoS protection, vulnerability scanning |
| Compliance & governance | Audit logging, data classification, policy enforcement |
| Observability | Logging, metrics, tracing, alerting, dashboards |
| CI/CD | Build pipelines, automated testing, deployment automation |
| Container orchestration | Kubernetes, service mesh, auto-scaling |
| Networking | CDN, load balancing, DNS, VPN, private links |
| Disaster recovery | Backup, failover, multi-region replication |

## Mapping Process

### Step 1: List all business capabilities from user input

Extract every capability mentioned — not just explicit ones. Capabilities hide in:
- Pain points ("we can't do X" = missing capability)
- Journeys (each step implies a capability)
- Success drivers ("must support X" = required capability)

### Step 2: Categorize each capability

Assign each to one of the 5 categories above. Some capabilities span categories — list the primary category and note the secondary.

### Step 3: Map to technical enablers

For each capability, identify the technology pattern. Consider:
- The user's regional context (cloud provider preferences, data sovereignty)
- Current state pain points (what to avoid repeating)
- Scale requirements (derived from outcomes and success drivers)

### Step 4: Derive components

Group related enablers into named components. A component is a logical building block that appears in the architecture diagram.

Example:
- Capabilities: "User Registration", "Profile Management", "Authentication"
- Enabler: IAM Platform
- Component: **Identity & Access Management** (placed in Security & Governance cross-cut)

### Step 5: Place components into layers

Assign each component to its primary architecture layer. Some components touch multiple layers — place them in the primary layer and note cross-layer dependencies.

### Step 6: Draw connections

Map how components interact:
- Experience → Application Services (API calls)
- Application Services → Data (read/write)
- Application Services ↔ Integration (external systems)
- Integration → External Systems (outbound)
- Security & Governance → All layers (cross-cutting)
