# GlucoSense Connected Glucose Management Platform — PRD

**Path:** A — Standard (no prototype)
**Version:** 1.0
**Date:** 2026-04-14
**Status:** Draft — pending regulatory and clinical review

---

## Section 1: Opportunity Framing

### Core Problem

Patients with diabetes using FreeStyle Libre CGM sensors cannot see the real-time impact of specific food choices on their glucose levels, which causes 60-80% food logging abandonment within 30 days and leaves clinicians without dietary data to inform care decisions between appointments.

> `[TBD — owner: Product Research]` Validate 60-80% abandonment rate with internal FreeStyle Libre engagement data. Industry benchmarks (MySugr, mySugr/Roche 2024 retention reports) suggest 65-75% drop-off for manual food logging in CGM companion apps.

### Hypothesis

If we build real-time food-glucose correlation with sub-30-second food logging (photo recognition + barcode + favorites), then 30-day food logging retention will increase from `[TBD — baseline required]` to 60%+ because immediate visual feedback showing "this meal caused this spike" creates a reward loop that sustains engagement and drives dietary behavior change.

### Strategy Fit

**FreeStyle Libre Ecosystem Expansion** — GlucoSense extends the Libre CGM hardware into a connected platform play, shifting Abbott from "sensor company" to "glucose management platform." Directly supports:
- Abbott Diabetes Care growth strategy: increase recurring digital revenue per sensor user
- ADC connected ecosystem OKR: grow monthly active connected users by `[TBD — owner: ADC Strategy]`%
- Competitive differentiation vs. Dexcom Clarity and Medtronic CareLink, neither of which offers food-glucose correlation as a first-class feature

### Solution Approach

**What we're building:**
A multi-actor connected platform where CGM glucose data streams in real time to web and mobile apps. Patients log food in under 30 seconds using AI-assisted recognition (photo, barcode, favorites). A SaMD-classified Correlation Engine time-aligns glucose readings with food entries and surfaces patterns. Clinicians, caregivers, and dietitians each get role-specific dashboards to monitor and collaborate on care.

**Why this approach:**
- Builds on existing FreeStyle Libre BLE sensor hardware — no new hardware required
- Food-glucose correlation is the #1 unmet need in CGM companion apps (existing apps show raw glucose curves but don't explain *why* spikes happen)
- Multi-actor model (patient + clinician + caregiver + dietitian) creates network effects — clinician adoption drives patient retention
- SaMD isolation of the Correlation Engine allows iterative regulatory submissions without blocking the rest of the platform

**Key components:**
1. **Smart Food Logger** — AI-assisted food entry (photo recognition, barcode scanning, favorites, quick-log) targeting <30s per entry
2. **Correlation Engine (SaMD)** — Time-aligned glucose + food pattern detection, isolated for FDA 510(k) / EU MDR regulatory traceability
3. **Multi-Actor Portal System** — Patient, Clinician, Caregiver, Dietitian, and Admin portals with role-based access
4. **Alert Engine** — Configurable glucose thresholds with multi-channel notifications (push, SMS, email) and escalation chains
5. **EHR Integration Hub** — FHIR R4 adapter for bidirectional hospital EHR data exchange

**Alternatives considered:**
1. **Glucose-only app (no food logging)** — Rejected because it replicates LibreLink without differentiation. The correlation feature is the entire value proposition; without it, there's no reason for patients to switch from the existing app.
2. **Manual correlation (patient interprets their own data)** — Rejected because it requires nutritional literacy most patients don't have, and produces inconsistent insights that clinicians can't trust for care decisions.
3. **Third-party food logging integration (partner with MyFitnessPal/Cronometer)** — Rejected because it introduces a dependency on external data formats, creates latency in the correlation pipeline (batch sync vs. real-time), and loses control over the food logging UX that directly drives the <30s target.

### Evidence

**User Research:**
`[TBD — owner: Product Research / ADC User Research]` — No primary research data provided. Required before PRD approval:
- N=`[TBD]` patient interviews on food logging friction with current CGM apps
- Clinician survey on between-visit data gaps (target: N=50+ endocrinologists)
- Validate <30s food logging threshold as the engagement inflection point

**Competitive Snapshot:**
- **Dexcom Clarity**: Shows glucose trends and patterns but has zero food logging or correlation capability. Clinician-facing reports are PDF-based, not interactive. *Gap: no food integration. Differentiator: they own the G7 sensor ecosystem.*
- **LibreLink (Abbott's own)**: Shows glucose readings and basic trend arrows. No food logging. Limited clinician sharing via LibreView. *Gap: no correlation or multi-actor collaboration. Differentiator: already has the Libre sensor user base — GlucoSense can inherit it.*
- **MySugr (Roche)**: Has food logging (manual text entry) but no AI-assisted input and no automated correlation to glucose. Logging abandonment is high due to manual friction. *Gap: no smart logging or automated correlation. Differentiator: Roche distribution and coaching feature.*
- **Our gap:** No existing Abbott app correlates food to glucose. **Our differentiator:** AI-assisted food logging (<30s) + automated correlation engine + multi-actor collaboration — none of the top 3 competitors offer all three.

---

## Section 2: Boundaries

### In Scope

- **Platform:** iOS, Android (mobile), Web (portals)
- **Actors:** Patient, Clinician, Caregiver/Family Member, Dietitian/Nutritionist, Admin
- **Sensor:** FreeStyle Libre 2 and Libre 3 via BLE
- **Markets (Phase 1):** US (HIPAA, FDA SaMD pathway), EU (GDPR, EU MDR)
- **Food logging:** Photo recognition, barcode scanning, favorites/recent, manual text entry, regional food databases
- **Correlation:** Time-aligned glucose + food pattern detection (SaMD-classified)
- **Alerts:** Configurable glucose thresholds, multi-channel notification (push, SMS, email), escalation chains
- **Integration:** EHR via FHIR R4, data export (PDF, CSV, FHIR)
- **Languages (Phase 1):** English, Spanish, German, French
- **Compliance:** HIPAA, GDPR, FDA 510(k) for Correlation Engine, EU MDR, IEC 62304 software lifecycle

### Non-Goals

- **Insulin dosing recommendations** — GlucoSense shows correlations and patterns, it does not recommend insulin doses. This is a common feature request but crosses into a different SaMD classification (Class III vs. Class II) and would add 18-24 months to regulatory timeline.
- **Pharmaceutical or supplement suggestions** — The platform does not recommend medications, supplements, or treatments. Clinicians make treatment decisions using GlucoSense data as one input.
- **Non-Libre CGM sensor support** — Phase 1 is FreeStyle Libre only. Dexcom G7 or Medtronic Guardian integration is a future consideration but adds BLE protocol complexity and partnership negotiations.
- **Meal planning or diet prescriptions** — GlucoSense shows what happened (correlation), not what to eat next (prescription). Dietitians use the data to inform their own recommendations.

### Dependencies

| Dependency | Owner | Status |
|---|---|---|
| FreeStyle Libre BLE SDK access and documentation | ADC Sensor Engineering | `[TBD — owner: ADC Engineering to confirm SDK availability]` |
| Regional food & nutrition database (US, EU markets) | ADC Data Partnerships | Not started |
| FDA 510(k) pre-submission for Correlation Engine (SaMD Class II) | Regulatory Affairs | Not started |
| EU MDR technical documentation for Correlation Engine | Regulatory Affairs (EU) | Not started |
| HIPAA BAA with cloud provider (AWS/Azure) for PHI hosting | BTS Cloud Infrastructure | `[TBD — may already exist for other Abbott projects]` |
| FHIR R4 endpoint availability from target EHR systems (Epic, Cerner) | ADC Interoperability | Not started |
| IEC 62304 compliant CI/CD pipeline for SaMD traceability | BTS DevOps | Not started |
| ML training data for food image recognition (regional food photos) | ADC Data Science | Not started |
| Regulatory / Compliance Review | Legal / Regulatory Affairs / Privacy | Not started |

### AI Feature Readiness

*Data Sources:*
- Food image recognition: requires labeled training dataset of 50K+ food images across US and EU regional cuisines. Dataset does not exist — must be sourced or licensed. Owner: `[TBD — ADC Data Science]`, timeline: `[TBD]`
- Barcode-to-nutrition mapping: requires UPC/EAN database license (OpenFoodFacts or Nutritionix). Owner: `[TBD — ADC Data Partnerships]`, timeline: `[TBD]`
- Glucose time-series data: available from existing FreeStyle Libre sensor readings via BLE SDK. Format: 1-minute or 5-minute intervals depending on Libre model.

*System Integrations:*
- FreeStyle Libre BLE SDK: required for real-time glucose data ingestion. SDK availability to be confirmed by ADC Sensor Engineering.
- EHR FHIR R4 endpoints: required for clinician workflow integration. Epic and Cerner sandbox access needed for development.

*Infrastructure:*
- Multi-region cloud deployment (US, EU) with data residency enforcement. Requires PHI-capable infrastructure with BAA. Owner: `[TBD — BTS Cloud Infrastructure]`, timeline: `[TBD]`
- SaMD-isolated compute environment for Correlation Engine with full audit trail and version pinning per IEC 62304.

### Tradeoffs Accepted

- **Phase 1 is Libre-only** — excludes Dexcom and Medtronic users (~40% of CGM market), but avoids multi-protocol BLE complexity and gets to market faster with Abbott's own hardware.
- **Correlation Engine starts rule-based, not ML** — initial correlation uses time-window alignment and glycemic index lookup rather than personalized ML models. Less accurate for individual variation, but faster to validate for SaMD submission. ML personalization is Phase 2.
- **No offline food logging in Phase 1** — food entries require network connectivity to hit the food database API. Users in low-connectivity environments will have degraded experience. Offline-first architecture adds 3+ months.

---

## Section 3: Success Measurement

### Primary Metric

**30-day food logging retention rate** — % of patients who log food at least 3x/week at day 30 post-activation.

Target: 60% retention at day 30 vs. `[TBD — baseline required before PRD approval]`.

> Industry benchmark: MySugr reports ~30% 30-day food logging retention for manual entry. Our hypothesis is that AI-assisted logging (<30s) doubles this. If no internal baseline exists, use 30% as proxy baseline. Target: 60% = 2x improvement.

### Guardrail Metrics

| Metric | Baseline | Acceptable Floor |
|---|---|---|
| Glucose data transmission reliability (% readings successfully received) | `[TBD — Libre BLE SDK benchmark]` | 98% |
| Food logging time per entry (median seconds) | N/A (new feature) | < 45 seconds (target: < 30s) |
| Correlation Engine accuracy (% of food-glucose correlations rated "helpful" by patients) | N/A (new feature) | 70% positive rating |
| App crash rate (crashes per 1000 sessions) | N/A (new app) | < 5 per 1000 sessions |
| Clinician portal monthly active rate (% of onboarded clinicians using portal 1x/month) | N/A (new feature) | 40% monthly active |
| PHI data incident count | 0 | 0 — any PHI incident is a P0 |

### Kill Criteria

Roll back the Correlation Engine if:
- Correlation accuracy (patient-rated "helpful") drops below 50% over any 7-day window, OR
- A PHI data exposure incident occurs (immediate kill, no threshold), OR
- Glucose data transmission reliability drops below 95% for >24 hours (indicates BLE pipeline failure), OR
- App crash rate exceeds 15 per 1000 sessions for >48 hours

Kill switch owner: `[TBD — Engineering Lead]`
Mechanism: Feature flags per component (Correlation Engine, Smart Food Logger, Alert Engine can be independently disabled)
Speed: < 5 minutes via configuration change

### Graduate When

Move from limited pilot to full rollout when:
- 30-day food logging retention >= 55% (slightly below target to allow for expansion effects)
- Correlation accuracy >= 70% patient-rated "helpful"
- Zero PHI incidents during pilot
- Clinician portal monthly active >= 35%
- FDA 510(k) clearance received for Correlation Engine (US market)
- EU MDR conformity assessment complete (EU market)

---

## Section 4: Rollout Plan

### Timeline

- **Q3 2026:** US limited pilot — 500 patients, 20 endocrinology practices (FDA pre-submission in parallel)
- **Q4 2026:** US expanded pilot — 5,000 patients, 100 practices (pending FDA 510(k) clearance for Correlation Engine)
- **Q1 2027:** US full rollout + EU limited pilot (pending EU MDR conformity)
- **Q2 2027:** EU expanded rollout, APAC market assessment begins

### Phasing Strategy

- **Stage 1 (US Pilot):** 500 FreeStyle Libre 3 patients at 20 partner endocrinology practices. English only. All 5 actor roles active. Correlation Engine in "display only" mode (shows correlations but does not make dietary suggestions) pending FDA clearance.
- **Stage 2 (US Expansion):** 5,000 patients, 100 practices. Add Spanish language support. Correlation Engine fully active post-FDA 510(k). Add EHR integration with Epic (top 3 pilot sites).
- **Stage 3 (Full US + EU Pilot):** US general availability via App Store/Play Store for all FreeStyle Libre 2/3 users. EU pilot: 1,000 patients, 30 practices in Germany and UK. German, French, English.
- **Stage 4 (Global):** EU general availability. APAC market entry assessment for Japan and Australia.

### Gates for Expansion

Stage 1 → Stage 2:
- Primary metric (30-day retention) >= 55%
- Zero PHI incidents
- BLE data reliability >= 98%
- No P0/P1 incidents open for >48 hours
- FDA 510(k) submission accepted (not necessarily cleared — Stage 2 can proceed with "display only" correlation)

Stage 2 → Stage 3:
- FDA 510(k) clearance received for Correlation Engine
- Primary metric holds at >= 55% at 5,000 patient scale
- Clinician portal monthly active >= 35%
- EHR integration validated at 3+ Epic sites
- EU MDR technical file submission complete

### Kill Switch

- **Mechanism:** Feature flags per component — Correlation Engine, Smart Food Logger, Alert Engine, EHR Integration each independently toggleable
- **Owner:** `[TBD — Engineering Lead]` can trigger; `[TBD — VP ADC Digital]` approves for full platform kill
- **Speed:** < 5 minutes for individual component; < 15 minutes for full platform disable

---

## Section 5: Risk Management

### Top Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| FDA 510(k) review takes longer than projected (12-18 months vs. planned 9 months), delaying Correlation Engine activation | High | High | Submit pre-submission package in Q2 2026. Launch Phase 1 with "display only" correlation (informational, not SaMD-classified). Engage FDA early via Pre-Sub meeting. |
| BLE data transmission gaps between Libre sensor and mobile app cause missing glucose readings, breaking correlation accuracy | Medium | High | Implement gap detection and interpolation in Data Validation Engine. Alert patient when >15 min gap detected. Design correlation algorithm to handle sparse data gracefully. |
| Food image recognition accuracy insufficient for regional cuisines (non-US food items) | Medium | Medium | Launch photo recognition as US-only in Phase 1 using licensed US food image dataset. EU Phase 1 uses barcode + manual + favorites only. Collect EU food images during pilot for Phase 2 ML training. |
| Clinician adoption stalls — clinicians don't check portal between appointments | Medium | High | Embed GlucoSense alerts into existing EHR workflows (Epic In-Basket, Cerner Message Center) so clinicians don't need a separate portal login. Provide weekly email digest as fallback. |
| PHI data breach during multi-region deployment | Low | Critical | Encrypt all PHI at rest (AES-256) and in transit (TLS 1.3). Data stays in-region. Immutable audit trail on all PHI access. Penetration testing before each rollout stage. Zero-tolerance kill criterion. |

### Detection

| Signal | Threshold | Monitoring |
|---|---|---|
| BLE transmission gap rate | > 2% of readings missing per patient per day | Real-time dashboard in Observability Stack; automated alert to on-call engineering |
| Correlation accuracy drop | Patient "helpful" rating < 60% (7-day rolling) | In-app feedback widget; weekly analytics review by Product |
| Food logging abandonment spike | 7-day active logging rate drops > 10 percentage points week-over-week | Engagement analytics dashboard; automated Slack alert to Product |
| PHI access anomaly | Any access pattern flagged by DLP or outside RBAC scope | Audit Service real-time monitoring; automated page to Security on-call |

### Fallback & Kill Switch

- **Fallback:** If Correlation Engine is disabled, patients see raw glucose chart + food log timeline without correlation overlays. App remains functional as a glucose viewer + food diary. Clinician portal shows glucose trends without dietary insights.
- **Kill switch:** `[TBD — Engineering Lead]` triggers via feature flag dashboard. Individual components (Correlation, Food Logger, Alerts) can be killed independently. Full platform kill requires `[TBD — VP ADC Digital]` approval.

---

## Section 6: Ownership + Action

### Primary Owner

`[TBD — Product Manager, ADC Digital]` — single accountable individual for this PRD and feature delivery.

### Stakeholder Sign-off

| Stakeholder | Team | Decision Needed | Status |
|---|---|---|---|
| `[TBD]` | Product (ADC Digital) | PRD approval | Not started |
| `[TBD]` | Engineering (ADC Platform) | Feasibility sign-off — BLE SDK, multi-region infra, SaMD isolation | Not started |
| `[TBD]` | Regulatory Affairs | FDA 510(k) strategy and SaMD classification confirmation | Not started |
| `[TBD]` | Regulatory Affairs (EU) | EU MDR conformity pathway confirmation | Not started |
| `[TBD]` | Legal / Privacy | HIPAA and GDPR compliance review, BAA status | Not started |
| `[TBD]` | Clinical Affairs | Clinical claim review — correlation accuracy claims, labeling language | Not started |
| `[TBD]` | ADC Sensor Engineering | BLE SDK access and support commitment | Not started |
| `[TBD]` | Data Science | Food recognition ML feasibility and training data assessment | Not started |
| `[TBD]` | Quality Assurance | IEC 62304 compliance plan for SaMD components | Not started |

### Decision Points

| Date / Milestone | Decision | Owner |
|---|---|---|
| Q2 2026 — FDA Pre-Sub response | Confirm SaMD Class II classification for Correlation Engine. If Class III, re-scope or pivot. | `[TBD — Regulatory Affairs Lead]` |
| Q3 2026 — Pilot month 1 review | Evaluate 30-day retention rate. Continue, adjust, or kill pilot. | `[TBD — Product Manager]` |
| Q4 2026 — Pilot month 3 review | Gate decision: expand to Stage 2 or iterate on Stage 1. | `[TBD — VP ADC Digital]` |
| Q1 2027 — US full rollout decision | FDA clearance + Stage 2 metrics review. Approve US GA. | `[TBD — SVP ADC]` |

### Fail -> Action

If 30-day food logging retention is below 45% at the Stage 1 month-3 review (`[TBD — Q4 2026 date]`):
- Action: Product and Data Science conduct a logging friction audit — analyze where in the food logging flow patients drop off, run 20 patient interviews, and present findings + revised approach within 30 days.
- Owner: `[TBD — Product Manager, ADC Digital]`
- Escalation: If revised approach doesn't reach 50% retention in a second 30-day test, escalate to `[TBD — VP ADC Digital]` for continue/kill decision.

> Note: 45% is the Fail -> Action threshold. Kill Criteria (Section 3) triggers at different thresholds for operational issues (correlation accuracy < 50%, PHI incidents, crash rates). These are separate decision paths.

---

## Section 7: AI-Specific Additions

### Primary Tasks

1. **Food image recognition** — Classify a food photo into one of 2,000+ food items in the regional nutrition database. Return top-3 candidates with confidence scores.
2. **Barcode-to-nutrition lookup** — Scan UPC/EAN barcode, match to packaged food database, return nutritional profile (calories, carbs, glycemic index, fiber, protein).
3. **Food-glucose time correlation** — Align food log timestamps with glucose time-series data. Detect post-meal glucose response patterns (spike onset, peak, recovery). Classify correlation strength (strong/moderate/weak/none).
4. **Glucose pattern detection** — Identify recurring glucose patterns across multiple days (e.g., "morning coffee always causes a 40mg/dL spike within 45 minutes").
5. **Smart suggestions** — Surface frequently logged foods and recent meals for quick-log. Predict likely meal based on time of day and history.

### Inputs Available

| Task | Input Data |
|---|---|
| Food image recognition | Camera photo (JPEG, 1-12MP), device GPS (for regional food DB selection), user food history (for ranking) |
| Barcode lookup | UPC/EAN string (from camera scan), regional food database |
| Food-glucose correlation | Glucose time-series (1-min or 5-min intervals, mg/dL), food log entries (item, timestamp, portion size, nutritional profile), insulin events (if logged) |
| Pattern detection | 7-30 day rolling window of glucose + food data per patient |
| Smart suggestions | User food log history, time of day, day of week |

### Activation Logic

**When AI activates:**
- Food image recognition: User taps "Log by Photo" and captures/selects an image
- Barcode lookup: User taps "Scan Barcode" and camera detects a UPC/EAN pattern
- Food-glucose correlation: Automatically triggered 2 hours after a food log entry when corresponding glucose data is available
- Pattern detection: Runs as nightly batch job when patient has >= 7 days of food + glucose data
- Smart suggestions: Appears in food logging UI when user opens the log screen

**When system uses non-AI fallback:**
- Food image recognition fails (confidence < 0.6): Show manual food search with text input
- Barcode not found in database: Show manual entry form with barcode number displayed
- Insufficient glucose data for correlation (> 30-min gap around meal): Mark correlation as "insufficient data" and show glucose chart without correlation overlay
- < 7 days of data: Pattern detection does not run; patient sees "Building your patterns — keep logging!" message

**Examples:**

| Input Example | Path Taken | Why |
|---|---|---|
| Photo of a bowl of oatmeal with berries | AI (image recognition) | Multi-item meal, requires visual classification |
| Barcode scan of Chobani Greek Yogurt | AI (barcode lookup) | Packaged food with UPC, direct database match |
| "black coffee" typed in search | Non-AI (text search) | Simple single-item query, keyword match sufficient |
| Patient logged lunch at 12:30, glucose data available 12:00-15:00 | AI (correlation) | Full glucose window available, triggers 2hr post-meal correlation |
| Patient logged lunch at 12:30, glucose gap from 12:45-13:30 | Non-AI fallback | >30-min gap in glucose data during critical post-meal window |

### Behavior Contract

**Query 1: Photo of mixed plate (rice, grilled chicken, salad)**

- **Input:** Photo of a dinner plate with white rice, grilled chicken breast, and green salad
- **Expected:**
  - Return top-3 candidates: (1) "White rice, 1 cup" + "Grilled chicken breast, 150g" + "Green salad, mixed" — confidence 0.78
  - Display each item separately so patient can confirm, adjust portions, or remove incorrect items
  - Pre-fill nutritional data (carbs, GI, calories) from regional food database for each confirmed item
- **Edge case:** Yes — mixed plates are harder than single items. The model must decompose into individual foods, not classify the entire plate as one item.

**Query 2: Post-meal glucose correlation with clear spike**

- **Input:** Patient logged "Pasta carbonara, large portion" at 12:15. Glucose data shows: 110 mg/dL at 12:00, rising to 185 mg/dL at 13:00, returning to 125 mg/dL at 14:30.
- **Expected:**
  - Identify spike: onset at ~12:30 (15 min post-meal), peak at 13:00 (75 mg/dL rise), recovery by 14:30
  - Classify correlation as "strong" (clear temporal alignment, high-GI food, large glucose excursion)
  - Display to patient: "Pasta carbonara caused a 75 mg/dL spike peaking 45 minutes after eating. Recovery took ~2 hours."
  - Do NOT say "avoid pasta" or make dietary recommendations — correlation only, no prescription
- **Edge case:** No — this is the golden path scenario.

**Query 3: Correlation with insulin confound**

- **Input:** Patient logged "Pizza, 2 slices" at 18:00 AND logged 4 units rapid-acting insulin at 18:05. Glucose: 140 at 18:00, rises to 165 at 18:45, drops to 95 at 20:00.
- **Expected:**
  - Flag that insulin was administered in the correlation window
  - Display correlation with caveat: "Pizza was associated with a 25 mg/dL rise. Note: insulin was taken at 18:05, which may have reduced the glucose response."
  - Do NOT attribute the glucose pattern solely to food when insulin is a confound
  - Log the insulin event as a covariate in the correlation metadata
- **Edge case:** Yes — insulin confounding is a safety-critical edge case. Misattributing a low spike to "good food choice" when insulin was the cause could lead to dangerous dietary decisions.

**Query 4: Food photo in low-light / ambiguous**

- **Input:** Blurry photo of a bowl of something brown, taken in dim restaurant lighting
- **Expected:**
  - Confidence score < 0.6 for all candidates
  - Do NOT guess — fall back to manual search: "I couldn't identify this food clearly. Search for it instead?"
  - Log the failed recognition attempt for model improvement pipeline
- **Edge case:** Yes — false positive food identification could corrupt the correlation data and erode patient trust.

**Query 5: Pattern detection across 14 days**

- **Input:** 14 days of data showing glucose spikes of 60-80 mg/dL consistently 30-60 minutes after breakfast entries containing "orange juice"
- **Expected:**
  - Detect recurring pattern: "Orange juice at breakfast is associated with a 60-80 mg/dL spike within 30-60 minutes (observed 11 of 14 days)"
  - Display as a "Pattern Alert" in the patient dashboard
  - Make the pattern available to the patient's clinician and dietitian in their respective portals
  - Do NOT recommend stopping orange juice — show the pattern, let the care team advise
- **Edge case:** No — this is the core value proposition scenario.

### Guardrails

- **No clinical claims:** The AI must never state that a food "causes" a glucose response in absolute terms. Use "associated with," "correlated with," "followed by." Causation language is a regulatory labeling claim.
- **No dietary recommendations:** The AI shows correlations and patterns. It does not say "eat less of X" or "try Y instead." Dietary advice is the clinician's and dietitian's domain.
- **No insulin dosing suggestions:** The system never suggests insulin amounts, timing adjustments, or medication changes.
- **No diagnosis:** The AI does not diagnose diabetes type, complications, or comorbidities from glucose patterns.
- **Correlation requires minimum data:** The system must not display a food-glucose correlation when glucose data is missing for >30 minutes in the 3-hour post-meal window. Show "insufficient data" instead of a weak/misleading correlation.
- **Patient safety on false negatives:** If the system shows "no correlation" for a high-GI food, flag for clinical review rather than display as definitive — the absence of a detected spike doesn't mean the food is safe.

### Fallback Behavior

**When AI is uncertain (food recognition confidence < 0.6):**
- Show manual food search interface with text input
- Display "I couldn't identify this food — search for it instead?" message
- Log failed attempt with anonymized image metadata for model retraining pipeline

**When correlation data is insufficient:**
- Show glucose chart and food log side-by-side without correlation overlay
- Display: "Not enough glucose data around this meal to calculate correlation"
- Do not show partial/speculative correlations

**Handoff path:** All AI features fall back to the non-AI version of the same feature (manual search, raw glucose chart, basic time-series view)
**Trigger threshold:** Confidence < 0.6 for recognition tasks; >30-min glucose gap for correlation tasks; latency >2000ms for any AI inference (timeout to non-AI path)

---

## Section 8: Post-Ship

*[Leave blank until first evaluation — fill after pilot or initial rollout completes]*

**Results doc link**
*[Link to dashboard or experiment results]*

**What surprised us?**
*[What did users do that we didn't expect? What did data show that we didn't anticipate?]*

**What will we change?**
*[Based on results — changes to scope, metrics, rollout strategy, or behavior contract]*

**New examples to add to behavior contract**
*[Real production inputs that should be added as examples for next iteration]*

**Decision**
- ○ Iterate — continue with changes
- ○ Scale — expand rollout as planned
- ○ Retire — stop and document why
