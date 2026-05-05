# Marketing Future — Capability Gap Analysis
**Project:** EPD Marketer of the Future (AI-Empowered, Human-Led)
**Date:** 2026-05-05
**Source Documents:** The Marketer of the Future EPD 15.04.26.pdf, pharma-genai-tool-map[97].pdf
**Status:** Current state tools pending validation with EPD teams

---

## How to Read This Document

| Status | Meaning |
|---|---|
| **Investigation for Validation** | Current tool unknown — needs discovery with EPD stakeholders |
| **Gap** | Capability does not exist today; must be built or bought |
| **Partial** | Capability exists but is limited, manual, or not scaled |
| **Exists** | Capability confirmed in current state |

---

## Agent 1: ALICE — Creative Excellence
*AI-Led Intelligent Creative Engine*

| # | Capability | Definition | Current State | Current Tool | Future Tool (Recommended) | Gap Type |
|---|---|---|---|---|---|---|
| 1 | Creative Generation | Generate brand-safe images, video, modular assets at scale | Investigation for Validation | ? | Adobe Firefly / GenStudio | TBD post-validation |
| 2 | Brief Intelligence | Auto-optimize creative briefs; score concepts against benchmarks | Investigation for Validation | ? | Persado | TBD post-validation |
| 3 | Copy & Claim Generation | Pharma-compliant copy variants with brand voice guardrails | Investigation for Validation | ? | Writer.com | TBD post-validation |
| 4 | Creative Ops & Workflow | Brief intake → asset production with automated routing | Investigation for Validation | ? | Adobe Workfront | TBD post-validation |

**Known Pain Points (from EPD document):**
- Manual, inconsistent creative briefs
- Agency-dependent (high cost, 3–5 day brief cycle)
- 4–6 revision cycles per brief
- Limited localization capability

---

## Agent 2: BRANDS — Brand Strategy
*Brand Strategy Planning System*

| # | Capability | Definition | Current State | Current Tool | Future Tool (Recommended) | Gap Type |
|---|---|---|---|---|---|---|
| 5 | Market Intelligence | Synthesize research, competitive intel, HCP/patient sentiment | Investigation for Validation | ? | Deepsights | TBD post-validation |
| 6 | Social Listening | Real-time brand perception monitoring across HCP/patient communities | Investigation for Validation | ? | Brandwatch / Synthesio | TBD post-validation |
| 7 | Commercial Strategy Modeling | Scenario modeling, portfolio planning, market archetype analysis | Investigation for Validation | ? | McKinsey Lilli / ZS ZAIDYN | TBD post-validation |
| 8 | Synthetic Research / Digital Twins | Synthetic HCP & patient personas for rapid message testing | Investigation for Validation | ? | Synthetic Audiences / Digital Twins | TBD post-validation |

**Known Pain Points (from EPD document):**
- Static insights from fragmented data
- Resource-intensive 2–3 month workshops
- Annual brand plans with limited adaptability
- Intuition-based judgments, not data-driven

---

## Agent 3: CRAFTS — Content Excellence
*Content Lifecycle Management*

| # | Capability | Definition | Current State | Current Tool | Future Tool (Recommended) | Gap Type |
|---|---|---|---|---|---|---|
| 9 | MLR Review & Compliance | AI-assisted pre-review, claim checking, citation linking | Investigation for Validation | ? | Veeva Vault PromoMats + AI Agents | TBD post-validation |
| 10 | Compliance Detection | Auto-detect non-compliant claims, flag risk in global content audits | Investigation for Validation | ? | Indegene AI Compliance Engine | TBD post-validation |
| 11 | Modular Content Creation | Claim-safe modular content blocks for multi-channel rendering | Investigation for Validation | ? | Writer.com / Adobe AEM + Firefly | TBD post-validation |
| 12 | Content Testing & Optimization | A/B and multivariate testing for HCP-facing digital content | Investigation for Validation | ? | Optimizely / VWO AI | TBD post-validation |

**Known Pain Points (from EPD document):**
- Slow MLR reviews — manual coordination bottlenecks
- Linear campaign rollouts
- One-size-fits-all campaigns
- Asset-based (not customer journey) execution

---

## Agent 4: SPARK — Customer Engagement
*Intelligent Customer Engagement*

| # | Capability | Definition | Current State | Current Tool | Future Tool (Recommended) | Gap Type |
|---|---|---|---|---|---|---|
| 13 | Next-Best-Action (NBA) | AI-driven field suggestions; HCP pre-call intelligence & rep coaching | Investigation for Validation | ? | Aktana / PharmaForceIQ | TBD post-validation |
| 14 | CRM & HCP Journey Orchestration | HCP segmentation, behavioral analytics, omnichannel campaign delivery | Investigation for Validation | ? | Veeva Vault CRM AI Agents | TBD post-validation |
| 15 | Patient Engagement | Conversational AI for HCP/patient queries on dosing, side effects, access | Investigation for Validation | ? | Conversa Health | TBD post-validation |
| 16 | Omnichannel Personalization | Real-time content personalization across email, web, and field channels | Investigation for Validation | ? | Adobe Sensei / Marketing Cloud | TBD post-validation |

**Known Pain Points (from EPD document):**
- Mass reach — one-size-fits-all content
- Broad segments, unable to scale personalization
- Reactive mode — static annual planning
- Disconnected data and tool silos

---

## Agent 5: ACCESS — Market Access
*AI-Powered Market Access Agent*

| # | Capability | Definition | Current State | Current Tool | Future Tool (Recommended) | Gap Type |
|---|---|---|---|---|---|---|
| 17 | Competitive Intelligence | Monitor competitor launches, payer decisions, access signals in real time | Investigation for Validation | ? | IQVIA Market Edge AI | TBD post-validation |
| 18 | HTA & Value Dossier | Build and simulate economic value dossiers, ICER models, HTA narratives | Investigation for Validation | ? | Payer Sciences / ZS ZAIDYN Access | TBD post-validation |
| 19 | Patient Support Programs | Automate copay, prior auth, and patient assistance program operations | Investigation for Validation | ? | ConnectiveRx AI Platform | TBD post-validation |
| 20 | Regulatory & Access Compliance | Scan content for access-related risk, OPDP compliance, global claim audit trails | Investigation for Validation | ? | RegASK / Veripharm | TBD post-validation |

**Known Pain Points (from EPD document):**
- Compliance viewed as a gatekeeper, not an enabler
- Post-campaign analysis with limited actionability
- Siloed data, quantitative-only measurement
- Lagging indicators (sales/recall) rather than real-time signals

---

## Validation Workplan

Before building the target architecture, the following discovery activities are required:

| Priority | Activity | Owner | Target Date |
|---|---|---|---|
| P1 | Inventory current MarTech tools across EPD regions | EPD Marketing Ops | TBD |
| P1 | Identify existing Veeva, Salesforce, or Adobe licenses | IT / Procurement | TBD |
| P1 | Map current MLR process and tooling | Medical / Regulatory | TBD |
| P2 | Assess CRM maturity (Veeva vs Salesforce vs other) | Commercial IT | TBD |
| P2 | Review existing analytics and data platforms | Data & Analytics | TBD |
| P3 | Identify regional variation in tool usage (markets differ) | Regional Marketing Leads | TBD |

---

## Summary: Systemic Gaps (from EPD Document)

Regardless of current tool validation, the EPD document identifies **5 confirmed systemic gaps**:

| Gap | Description | Agents Affected |
|---|---|---|
| **Fragmentation** | Data, tools, and teams operate in silos | BRANDS, SPARK, ACCESS |
| **Reactive Mode** | Static annual planning, unable to pivot quickly | BRANDS, SPARK |
| **Bottlenecks** | Manual production and review cycles | ALICE, CRAFTS |
| **Mass Reach** | Cannot scale personalized content variations | ALICE, CRAFTS, SPARK |
| **Compliance Gating** | MLR viewed as blocker, not integrated enabler | CRAFTS, ACCESS |

---

## Next Steps

1. **Complete validation workplan** — fill in current state tool inventory
2. **Build capability map diagrams** — current state vs future state (side by side)
3. **Build integration architecture** — how the 5 agents connect and share data
4. **Build target architecture** — full future state with recommended tool stack
