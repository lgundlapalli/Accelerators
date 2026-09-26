# Context Map — Multi-Signal Device

```mermaid
graph TD
    subgraph Devices["📡 DEVICES"]
        DEV["Medical Device\nBio-impedance · Pressure · pH\nSpO₂ · H₂O₂ · Temperature"]
    end

    subgraph Platform["🔵 PLATFORM APP"]
        DC["Device Connectivity\n(Generic)"]
        SP["Signal Processing\n(Core)"]
        CDS["Clinical Decision Support\n(Core)"]
        CC["Care Coordination\n(Supporting)"]
        RA["Research Analytics\n(Supporting)"]
        PH["Population Health\n(Supporting)"]
        OBS["Platform Observability\n(Supporting)"]
        AC["Audit & Compliance\n(Generic)"]
    end

    subgraph Gateway["🔀 EMR INTEGRATION GATEWAY (ACL)"]
        PORT["IEMRGateway\n(Port — FHIR R4 + SMART on FHIR)"]
        EA["EpicAdapter\n(Epic Aura)"]
        CA["CernerAdapter\n(Oracle Cerner)"]
        GA["GenericFHIRAdapter\n(Any FHIR R4 EMR)"]
    end

    subgraph EMRs["🏥 EXTERNAL EMR SYSTEMS (not owned)"]
        EPIC["Epic Aura"]
        CERNER["Oracle Cerner"]
        OTHER["Athena · Meditech\nAllscripts · others"]
    end

    subgraph Endpoints["📱 ACCESS ENDPOINTS"]
        MOB["Patient Mobile App\n(Phone)"]
        WEB["Platform Web App\n(Hospital Admin · Corporate Admin · Researcher)"]
        EMRUI["EMR App UI\n(Clinician · Care Team\nembedded via SMART on FHIR)"]
    end

    DEV -->|"BLE / LTE"| DC
    DC -->|"Published Language\n(validated packets)"| SP
    SP -->|"Customer-Supplier\n(derived metrics)"| CDS
    SP -->|"Customer-Supplier\n(baseline + trend)"| MOB
    SP -->|"Open Host Service\n(time-series API)"| RA
    SP -->|"Open Host Service\n(aggregated signals)"| PH
    SP -->|"Customer-Supplier\n(pipeline metrics)"| OBS
    CDS -->|"Customer-Supplier\n(risk scores + alerts)"| CC
    CDS -->|"Customer-Supplier\n(risk score + summary)"| MOB
    CC -->|"Customer-Supplier\n(panel + tasks)"| PH
    DC -->|"Published Language\n(device health events)"| OBS
    SP -.->|"ACL → event stream"| AC
    CDS -.->|"ACL → event stream"| AC
    OBS -.->|"ACL → event stream"| AC
    RA --> WEB
    PH --> WEB
    OBS --> WEB

    SP -->|"Customer-Supplier\n(signals + metrics)"| PORT
    CDS -->|"Customer-Supplier\n(risk scores + SOAP drafts)"| PORT
    CC -->|"Customer-Supplier\n(escalations)"| PORT

    PORT --> EA
    PORT --> CA
    PORT --> GA

    EA -->|"FHIR R4\n+ Epic extensions"| EPIC
    CA -->|"FHIR R4\n+ Cerner extensions"| CERNER
    GA -->|"FHIR R4\n(standard)"| OTHER

    EPIC -->|"SMART on FHIR\nPatientReference"| PORT
    CERNER -->|"SMART on FHIR\nPatientReference"| PORT
    OTHER -->|"SMART on FHIR\nPatientReference"| PORT

    PORT -->|"PatientReference\n(Conformist)"| SP
    PORT -->|"PatientReference\n(Conformist)"| CDS
    PORT -->|"PatientReference\n(Conformist)"| CC

    EPIC --> EMRUI
    CERNER --> EMRUI
    OTHER --> EMRUI
```

## Data Flow

```
Medical Device (BLE / LTE)
        │
        ▼
Device Connectivity  ──►  Signal Processing  ──►  Clinical Decision Support
                                │                          │
                                ▼                          ▼
                         Patient Mobile App         Care Coordination
                                                          │
               ┌──────────────────────────────────────────┘
               ▼
   IEMRGateway Port  (FHIR R4 + SMART on FHIR)
        │            │              │
        ▼            ▼              ▼
  EpicAdapter  CernerAdapter  GenericFHIRAdapter
        │            │              │
        ▼            ▼              ▼
   Epic Aura    Oracle Cerner   Athena · Meditech · others
        │            │              │
        └────────────┴──────────────┘
                     │
                     ▼
              EMR App UI
          (Clinician · Care Team
           embedded via SMART on FHIR)
```

## Port & Adapter Interface

```python
class IEMRGateway:
    """Port — implemented by each vendor adapter."""

    def get_patient_reference(self, launch_token: str) -> PatientReference: ...
    def write_observation(self, ref: PatientReference, obs: SignalObservation) -> str: ...
    def write_risk_score(self, ref: PatientReference, assessment: RiskAssessment) -> str: ...
    def write_soap_draft(self, ref: PatientReference, assessment: RiskAssessment) -> str: ...
    def write_escalation_alert(self, ref: PatientReference, esc: Escalation) -> str: ...
```

Each adapter implements this interface and handles vendor-specific FHIR extensions, auth scopes, and non-standard fields internally. The platform domain never calls an adapter directly — only through the port.

## What is Generic vs. Vendor-Specific

| Concern | Generic (works everywhere) | Vendor-Specific (adapter handles) |
|---|---|---|
| Auth | SMART on FHIR OAuth2 | App marketplace registration (App Orchard, Cerner Gallery) |
| Patient identity | FHIR `Patient` resource ID | Custom MRN formats, Epic EPI vs Cerner MPI |
| Signal write-back | FHIR R4 `Observation` | Custom LOINC code mappings per EMR |
| SOAP draft | FHIR R4 `DocumentReference` | Epic-specific note type codes |
| Escalation | FHIR R4 `Communication` | Epic In-Basket vs Cerner Message Center |
| Launch | SMART on FHIR launch URL | Epic App Orchard vs Cerner App Gallery |

## Access Endpoints by Persona

| Persona | Channel | How |
|---|---|---|
| **Patient** | Mobile phone app | Platform App pushes simplified vitals, alerts directly |
| **Clinician** | EMR app (Epic / Cerner / other) | SMART on FHIR embedded — risk scores and SOAP drafts appear inside their EMR |
| **Care Team** | EMR app (Epic / Cerner / other) | SMART on FHIR embedded — escalation queue inside their EMR |
| **Researcher** | Platform web app | Direct — cohort explorer, signal export |
| **Hospital Administrator** | Platform web app | Direct — population health, readmission dashboards |
| **Corporate Administrator** | Platform web app | Direct — system health, SLA, error codes |

## Patient Data Boundary

This platform stores **no patient profile data**. `PatientReference` is an opaque FHIR Patient ID from whichever EMR is connected, held in session memory only — never written to a database. All records (signal observations, risk assessments, escalations) are keyed to this reference.
