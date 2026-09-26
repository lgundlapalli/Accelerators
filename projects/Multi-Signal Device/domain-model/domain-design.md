# Multi-Signal Device — Domain-Driven Design

*Date: 2026-09-25*
*Signals: Bio-impedance · Pressure · pH · SpO₂ · Hydrogen Peroxide · Temperature*

---

## Subdomain Classification

| Bounded Context | Subdomain | Rationale |
|---|---|---|
| Signal Processing | **Core** | 6-signal fusion and derived metric computation (oxidative stress, hypoxia flag, tissue index) is the competitive moat |
| Clinical Decision Support | **Core** | Risk scoring, anomaly detection, and LLM clinical summaries differentiate the platform clinically |
| Patient Engagement | Supporting | Domain-specific but not the differentiator — simplified views, plain-language alerts |
| Care Coordination | Supporting | Necessary for clinical workflow; escalation queues, panel management |
| Research Analytics | Supporting | Cohort segmentation, feature library, raw signal access |
| Population Health | Supporting | Risk stratification and readmission scoring for hospital administrators |
| Audit & Compliance | Generic | Solved problem — immutable event log, consent, lineage, regulatory export |
| Device Connectivity | Generic | Commodity IoT — BLE/LTE uplink, edge pre-processing, packet validation |
| Identity & Consent | Generic | Standard IAM + consent management |

---

## Ubiquitous Language

### Signal Processing

| Term | Definition |
|---|---|
| **Signal** | A raw sensor reading: impedance (Ω), pH (units), SpO₂ (%), temperature (°C), H₂O₂ (μM), pressure (mmHg) |
| **Observation** | A validated, normalized multi-signal snapshot captured at a single timestamp |
| **Derived Metric** | A computed value from one or more raw signals — oxidative stress score, hypoxia flag, tissue composition index, hemodynamic index, fever flag |
| **Baseline** | Personal rolling 7-day median per signal per patient |
| **Deviation** | Signed distance from baseline in standard deviations |
| **Quality Score** | A 0–1 confidence value indicating signal integrity (noise, electrode contact, motion artifact) |

### Clinical Decision Support

| Term | Definition |
|---|---|
| **Risk Assessment** | A scored evaluation (0–100) of a patient's clinical state at a point in time |
| **Risk Factor** | A single signal deviation that contributed to the risk score, with rationale |
| **Risk Tier** | Categorical label: Low / Moderate / High / Critical |
| **Clinical Summary** | An LLM-generated narrative citing the signal evidence that drove the assessment |
| **SOAP Draft** | A structured clinical note (Subjective, Objective, Assessment, Plan) pre-populated from the assessment |

### Care Coordination

| Term | Definition |
|---|---|
| **Escalation** | A ranked work item representing a patient who requires care team attention |
| **Panel** | The set of patients assigned to a care team |
| **Deterioration Velocity** | Rate of risk score increase over a configurable window |

### Patient Engagement

| Term | Definition |
|---|---|
| **Alert** | A plain-language notification surfaced to the patient ("Your SpO₂ is slightly below your baseline today") |
| **Trend** | A 7-day sparkline of one signal |

---

## Context Map

```mermaid
graph TD
    subgraph Core["🔴 CORE DOMAIN"]
        SP["Signal Processing\n(Core)"]
        CDS["Clinical Decision Support\n(Core)"]
    end

    subgraph Supporting["🟡 SUPPORTING"]
        PE["Patient Engagement\n(Supporting)"]
        CC["Care Coordination\n(Supporting)"]
        RA["Research Analytics\n(Supporting)"]
        PH["Population Health\n(Supporting)"]
    end

    subgraph Generic["🟢 GENERIC"]
        AC["Audit & Compliance\n(Generic)"]
        DC["Device Connectivity\n(Generic)"]
        IAM["Identity & Consent\n(Generic)"]
    end

    DC -->|"Published Language\n(signal packets)"| SP
    SP -->|"Customer-Supplier\n(derived metrics)"| CDS
    SP -->|"Customer-Supplier\n(baseline + trend)"| PE
    SP -->|"Open Host Service\n(time-series API)"| RA
    SP -->|"Open Host Service\n(aggregated signals)"| PH
    CDS -->|"Customer-Supplier\n(risk scores + alerts)"| CC
    CDS -->|"Customer-Supplier\n(risk score + summary)"| PE
    CC -->|"Customer-Supplier\n(panel + tasks)"| PH
    IAM -->|"Conformist"| SP
    IAM -->|"Conformist"| CDS
    IAM -->|"Conformist"| PE
    SP -.->|"ACL → event stream"| AC
    CDS -.->|"ACL → event stream"| AC
```

---

## Aggregate Design

### Signal Processing — `SignalObservation` (Aggregate Root)

```mermaid
classDiagram
    class SignalObservation {
        +ObservationId id
        +PatientId patientId
        +Timestamp capturedAt
        +RawSignals signals
        +DerivedMetrics derived
        +QualityScore quality
        +validate()
        +derive()
    }
    class RawSignals {
        +float bioImpedance
        +float pressure
        +float pH
        +float spO2
        +float hydrogenPeroxide
        +float temperature
    }
    class DerivedMetrics {
        +float oxidativeStressScore
        +HypoxiaFlag hypoxiaFlag
        +float tissueCompositionIndex
        +float hemodynamicIndex
        +FeverFlag feverFlag
    }
    class PatientBaseline {
        +PatientId patientId
        +Map~Signal,RollingMedian~ baselines
        +update(SignalObservation)
        +deviationFrom(RawSignals) Map~Signal,float~
    }
    SignalObservation *-- RawSignals
    SignalObservation *-- DerivedMetrics
    PatientBaseline --> SignalObservation
```

**Invariants:**
- `quality` must be ≥ 0.6 for `derived` to be populated
- All six raw signal fields must be present or the observation is rejected
- `capturedAt` must not be in the future

### Clinical Decision Support — `RiskAssessment` (Aggregate Root)

```mermaid
classDiagram
    class RiskAssessment {
        +AssessmentId id
        +PatientId patientId
        +RiskScore score
        +List~RiskFactor~ factors
        +ClinicalSummary summary
        +Timestamp assessedAt
        +escalate()
        +generateSOAPDraft()
    }
    class RiskScore {
        +int value
        +RiskTier tier
        +validate()
    }
    class RiskFactor {
        +SignalType signal
        +float deviation
        +string rationale
    }
    class ClinicalSummary {
        +string narrative
        +List~Evidence~ citedSignals
    }
    RiskAssessment *-- RiskScore
    RiskAssessment *-- RiskFactor
    RiskAssessment *-- ClinicalSummary
```

**Invariants:**
- `score.value` must be 0–100
- At least one `RiskFactor` must exist if `score.tier` is Moderate or higher
- `summary.citedSignals` must reference only signals present in the triggering `SignalObservation`

### Care Coordination — `Escalation` (Aggregate Root)

| Field | Type | Notes |
|---|---|---|
| `id` | EscalationId | |
| `patientId` | PatientId | |
| `riskScore` | int | Snapshot from CDS at escalation time |
| `severity` | Low / Moderate / High / Critical | |
| `assignedTo` | CareTeamMemberId? | Nullable until assigned |
| `status` | Open / Acknowledged / Resolved | |
| `deteriorationVelocity` | float | Risk score delta per hour |
| `openedAt` | Timestamp | |
| `resolvedAt` | Timestamp? | |

---

## Domain Events Catalog

| Event | Raised By | Payload | Consumed By |
|---|---|---|---|
| `SignalObservationRecorded` | Signal Processing | observationId, patientId, capturedAt, qualityScore | CDS, Patient Engagement, Research Analytics |
| `BaselineUpdated` | Signal Processing | patientId, signal, newMedian | CDS |
| `HypoxiaFlagRaised` | Signal Processing | patientId, spO2Value, deviation | CDS, Care Coordination |
| `OxidativeStressSpikeDetected` | Signal Processing | patientId, score, pH, H₂O₂ | CDS |
| `FeverFlagRaised` | Signal Processing | patientId, temperatureValue | CDS, Patient Engagement |
| `RiskAssessmentCompleted` | CDS | assessmentId, patientId, score, tier | Care Coordination, Patient Engagement, Population Health |
| `EscalationTriggered` | Care Coordination | escalationId, patientId, severity | Patient Engagement |
| `EscalationResolved` | Care Coordination | escalationId, resolvedBy, resolvedAt | Population Health |
| `ConsentGranted` | Identity & Consent | patientId, scope[], grantedAt | All contexts |
| `ConsentRevoked` | Identity & Consent | patientId, scope[], revokedAt | All contexts |

---

## Tech Stack Mapping

| Bounded Context | Component | Technology |
|---|---|---|
| **Device Connectivity** | Edge gateway | AWS IoT Greengrass / Azure IoT Hub |
| **Device Connectivity** | Packet validation | Python microservice on edge |
| **Signal Processing** | Signal ingestion | Apache Kafka (event stream) |
| **Signal Processing** | Normalization + derivation | Python service (NumPy / SciPy) |
| **Signal Processing** | Time-series store | InfluxDB or TimescaleDB |
| **Signal Processing** | Baseline engine | Redis (rolling window per patient) |
| **Clinical Decision Support** | Risk scoring models | MLflow + scikit-learn / XGBoost |
| **Clinical Decision Support** | LLM clinical summaries | Claude API (Haiku for speed, Sonnet for quality) |
| **Clinical Decision Support** | Anomaly detection | Isolation Forest / LSTM autoencoder |
| **Patient Engagement** | API | FastAPI (Python) |
| **Patient Engagement** | Mobile / web UI | React Native / React |
| **Care Coordination** | API + queue engine | FastAPI + PostgreSQL |
| **Care Coordination** | Real-time push | WebSocket / Firebase |
| **Research Analytics** | Cohort query engine | DuckDB or Databricks SQL |
| **Research Analytics** | Feature store | Feast or Databricks Feature Store |
| **Population Health** | Dashboards | Databricks + Power BI / Tableau |
| **Audit & Compliance** | Immutable event log | Apache Kafka + S3 (WORM) / Azure Event Hubs |
| **Audit & Compliance** | Lineage tracking | OpenLineage / Marquez |
| **Identity & Consent** | Auth | Azure AD B2C or Auth0 |
| **Identity & Consent** | Consent store | PostgreSQL with audit trail |

---

## Repository Interfaces

```python
# Signal Processing
class SignalObservationRepository:
    def save(self, observation: SignalObservation) -> None: ...
    def find_by_patient(self, patient_id: PatientId, since: datetime) -> list[SignalObservation]: ...

class PatientBaselineRepository:
    def find_by_patient(self, patient_id: PatientId) -> PatientBaseline | None: ...
    def save(self, baseline: PatientBaseline) -> None: ...

# Clinical Decision Support
class RiskAssessmentRepository:
    def save(self, assessment: RiskAssessment) -> None: ...
    def latest_for_patient(self, patient_id: PatientId) -> RiskAssessment | None: ...
    def find_by_tier(self, tier: RiskTier, since: datetime) -> list[RiskAssessment]: ...

# Care Coordination
class EscalationRepository:
    def save(self, escalation: Escalation) -> None: ...
    def open_by_severity(self, severity: Severity) -> list[Escalation]: ...
    def assign(self, escalation_id: EscalationId, member_id: CareTeamMemberId) -> None: ...
```
