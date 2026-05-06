# Abbott GenAI Blueprint & Capability Model
**Enterprise AI Landscape — 220 Use Cases Across 15 Divisions**
*Version 1.0 — May 2026*

---

## Executive Summary

Abbott is executing a broad-based GenAI transformation across 12 business divisions, encompassing 220 catalogued use cases that span from clinical research to commercial marketing. As of 1Q26, **40 use cases are in production**, 43 are in active development (WIP), and 29 are pending ESC approval. The portfolio reflects a deliberate **Buy-first strategy** (133 Buy vs. 86 Build), anchored on enterprise platforms such as Azure AI Foundry, Microsoft M365 Copilot, Salesforce Einstein, and Adobe Experience Cloud.

The capability landscape has been consolidated from 15 raw capability categories into **six strategic domains**, providing a coherent blueprint for investment, governance, and platform standardization. The largest divisions by use case volume — BTS (32), ADC (31), and Corporate (27) — are driving enterprise-wide tooling, while commercial divisions like EPD and GMEA are leading production deployment in field engagement.

**Key metrics at a glance:**
| Metric | Value |
|---|---|
| Total use cases catalogued | 220 |
| Divisions represented | 12 |
| In production | 40 (18%) |
| WIP / Active development | 43 (20%) |
| Buy vs. Build ratio | 133:86 (61% Buy) |
| Top business function | Marketing/Sales (22) |

---

## Six Capability Domains

Abbott's 15 raw GenAI capability categories have been logically grouped into six strategic domains:

---

### Domain 1: Content & Creative Studio

**Definition:** Generation, drafting, and transformation of written, visual, and multimedia content for internal and external audiences — spanning marketing copy, medical communications, training materials, and brand assets.

**Sub-capabilities:**
- Creative Content Draft
- Writing Drafts & Data Entry
- Personalize Content
- Translation

**Example use cases:**
- Personalized HCP marketing content (ADC)
- Medical affairs document generation (Corp)
- Field rep communication drafts (EPD)
- Multi-language regulatory translations (RMDx)

**Divisions using it:** ADC, Corp, EPD, GMEA, RMDx, CHR, MD

**In-production tools:** Writer Newsroom (GMEA), Adobe Firefly/Express (RMDx), AutogenAI (AN)

**Maturity:** **Scaling** — Multiple tools in production; standardization opportunity exists around enterprise content platforms.

---

### Domain 2: Insights & Analytics Acceleration

**Definition:** AI-powered search, synthesis, and generation of insights from structured and unstructured data — including literature review, market intelligence, clinical data, and business reporting.

**Sub-capabilities:**
- Search, Screen & Insights
- Reporting & Observability
- Forecast

**Example use cases:**
- Marketing Insights Accelerator (GMEA)
- Clinical trial literature screening (AN)
- Sales performance analytics (EPD, ADC)
- Adverse event signal detection (RMDx)

**Divisions using it:** GMEA, AN, RMDx, BTS, ADC, Corp

**In-production tools:** Marketing Insights Accelerator (GMEA), RADIA Research (AN), Databricks (RMDx)

**Maturity:** **Producing** — Most mature domain with production deployments in research, commercial, and operations.

---

### Domain 3: Productivity & Automation

**Definition:** Enterprise-wide productivity enhancement through AI-integrated tools — including meeting summarization, document management, workflow automation, and process intelligence embedded in everyday work tools.

**Sub-capabilities:**
- Enterprise Productivity Tools
- Writing Drafts & Data Entry

**Example use cases:**
- M365 Copilot enterprise rollout (BTS)
- HR process automation (CHR)
- Procurement document analysis (Corp)
- Audit workflow automation (Corp)

**Divisions using it:** BTS, Corp, CHR, AN, MD, EPD

**In-production tools:** Microsoft M365 Copilot (BTS), Cursor/Windsurf/Atlassian AI (BTS), Five9 GSD (BTS)

**Maturity:** **Scaling** — M365 Copilot deployment underway; broad opportunity for process automation standardization.

---

### Domain 4: Customer & Field Engagement

**Definition:** AI-powered tools that augment customer-facing roles — field sales, customer service, patient engagement, and healthcare provider (HCP) interactions — with intelligent assistants, next-best-action, and personalized recommendations.

**Sub-capabilities:**
- Assistants
- Personalize Content
- Search, Screen & Insights (applied to CRM)

**Example use cases:**
- SmartRep Call Planning (EPD)
- Neuron7 field service AI (CoreDx)
- Five9 AI-assisted customer service (BTS)
- HCP virtual assistant (ADC)

**Divisions using it:** EPD, ADC, CoreDx, BTS, GMEA

**In-production tools:** SmartRep Call Planning (EPD), Neuron7 (CoreDx), Five9 GSD (BTS)

**Maturity:** **Producing** — Strong production presence in commercial; expanding to additional markets and segments.

---

### Domain 5: Engineering & Development Acceleration

**Definition:** AI tools that augment software engineering, quality assurance, and product development workflows — including code generation, testing, architecture assistance, and DevSecOps integration.

**Sub-capabilities:**
- Code Creation with Platform
- Code Creation IDE & Test Authoring

**Example use cases:**
- Cursor/Windsurf AI-assisted coding (BTS)
- Atlassian AI for project management (BTS)
- Azure AI Sandbox for rapid prototyping (MD)
- Automated test generation (BTS)

**Divisions using it:** BTS, MD, RMDx

**In-production tools:** Cursor/Windsurf/Atlassian AI (BTS), Azure AI Sandbox (MD)

**Maturity:** **Scaling** — Developer tooling deployed; opportunity to expand to all engineering teams and establish coding standards.

---

### Domain 6: Learning, Compliance & Governance

**Definition:** AI applications that support employee learning and development, regulatory compliance, risk management, legal review, and organizational knowledge management.

**Sub-capabilities:**
- Learning, Training & Coaching
- Image Identification/Analysis (for quality/regulatory)

**Example use cases:**
- Personalized learning paths (CHR)
- Regulatory document review (Corp, RMDx)
- Legal contract analysis (Corp)
- Manufacturing defect image analysis (MD, AN)

**Divisions using it:** CHR, Corp, RMDx, MD, AN, Cyber

**In-production tools:** (Multiple vendor-specific tools in pilot/WIP)

**Maturity:** **Exploring** — Nascent stage; high governance sensitivity requires careful CoE oversight before scaling.

---

## Blueprint Principles

### 1. Buy-First Platform Strategy
With 61% of use cases sourced as Buy solutions, Abbott's strategy is to leverage best-in-class enterprise AI platforms before building custom solutions. Key platform investments:
- **Microsoft Azure AI Foundry** — foundational infrastructure and model access
- **Anthropic Claude** — reasoning-heavy and long-context enterprise tasks
- **Salesforce Einstein** — CRM-native AI for commercial teams
- **Adobe Experience Cloud** — content creation and personalization
- **Veeva Vault AI** — regulated content management for Life Sciences
- **Microsoft M365 Copilot** — enterprise productivity across all business functions

### 2. Center of Excellence (CoE) Governance Model
A GenAI CoE embedded within BTS-DTS provides:
- Use case intake and ESC review (29 pending as of 1Q26)
- Platform standards and approved tooling catalog
- Security, privacy, and compliance guardrails
- Division-specific enablement and training
- Cross-division knowledge sharing and reuse tracking

### 3. Shared Platform Architecture
Three-tier model:
- **Tier 1 — Business Domains:** 6 capability domains mapped to business outcomes
- **Tier 2 — GenAI Capabilities:** Reusable capability layer (sub-capabilities shared across divisions)
- **Tier 3 — Shared Platform:** Managed enterprise platforms with centralized access, billing, and governance

### 4. Build Criteria
Custom build (86 use cases) is appropriate when:
- Capability requires proprietary data not accessible via SaaS APIs
- Division-specific regulatory constraints preclude off-shelf solutions
- Competitive differentiation requires unique model behavior
- Platform capability gaps exist for critical use cases

---

## Maturity Assessment by Domain

| Domain | Maturity | In Production | WIP | Key Risk |
|---|---|---|---|---|
| Content & Creative Studio | Scaling | 8 | 12 | Platform fragmentation |
| Insights & Analytics Acceleration | Producing | 14 | 9 | Data governance |
| Productivity & Automation | Scaling | 10 | 11 | Change management |
| Customer & Field Engagement | Producing | 12 | 6 | Compliance/regulatory |
| Engineering & Development | Scaling | 6 | 8 | Talent/skill gaps |
| Learning, Compliance & Governance | Exploring | 2 | 5 | Sensitivity/risk aversion |

---

## Division Breakdown

| Division | Use Cases | Top Domain | In Production |
|---|---|---|---|
| BTS | 32 | Productivity & Automation | 8 |
| ADC | 31 | Content & Creative Studio | 6 |
| Corp | 27 | Insights & Analytics | 5 |
| AN | 22 | Insights & Analytics | 5 |
| RMDx | 22 | Content & Creative Studio | 4 |
| MD | 22 | Engineering & Development | 3 |
| EPD | 19 | Customer & Field Engagement | 4 |
| CHR | 14 | Learning & Governance | 2 |
| GMEA | 9 | Customer & Field Engagement | 3 |
| CoreDx | 9 | Customer & Field Engagement | 3 |
| Lingo | 5 | Productivity & Automation | 1 |
| Cyber | 5 | Learning & Governance | 1 |

---

## Recommendations & Next Steps

1. **Consolidate content platforms** — Rationalize Writer, Adobe Firefly, and AutogenAI under a unified Content & Creative Studio platform contract with centralized governance.
2. **Accelerate ESC approvals** — 29 use cases pending ESC represent ~$Xm in deferred value; establish 30-day SLA for review cadence.
3. **Expand SmartRep model** — SmartRep Call Planning's success in EPD should be templated and offered to ADC and GMEA commercial teams.
4. **Formalize Build criteria** — Define clear guardrails for when to Build vs. Buy to prevent shadow AI and unapproved custom models.
5. **Launch Domain Champions program** — Assign a CoE domain champion for each of the 6 capability domains to drive reuse and cross-division knowledge transfer.
6. **Address Exploring domains** — Learning, Compliance & Governance domain requires dedicated investment plan and pilot use case in CHR to advance maturity.

---

*Source: Abbott GenAI Historical Catalog of Use Cases — 1Q26 snapshot | 220 use cases across 12 divisions*
*Generated: 2026-05-06*
