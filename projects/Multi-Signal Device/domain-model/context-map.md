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

    subgraph Bridge["🔀 EPIC BRIDGE GATEWAY"]
        EBG["Epic Bridge Gateway\n(ACL — data translation\n& FHIR write)"]
    end

    subgraph EpicSystem["🏥 EPIC AURA"]
        EPICAURA["Epic Aura Application\n(Upstream EMR — not owned)"]
    end

    subgraph Endpoints["📱 ACCESS ENDPOINTS"]
        MOB["Patient Mobile App\n(Phone)"]
        WEB["Platform Web App\n(Hospital Admin · Corporate Admin · Researcher)"]
    end

    DEV -->|"BLE / LTE\nsignal packets"| DC
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

    SP -->|"Customer-Supplier\n(signals + derived metrics)"| EBG
    CDS -->|"Customer-Supplier\n(risk scores + SOAP drafts)"| EBG
    CC -->|"Customer-Supplier\n(escalations + alerts)"| EBG
    EBG -->|"FHIR R4\n(Observation · DocumentReference · Alert)"| EPICAURA

    EPICAURA -->|"SMART on FHIR\n(PatientReference + launch context)"| EBG
    EBG -->|"PatientReference\n(Conformist)"| SP
    EBG -->|"PatientReference\n(Conformist)"| CDS
    EBG -->|"PatientReference\n(Conformist)"| CC

    RA --> WEB
    PH --> WEB
    OBS --> WEB
```

## Data Flow

```
Medical Device
      │  BLE / LTE
      ▼
Device Connectivity  ──►  Signal Processing  ──►  Clinical Decision Support
                                │                          │
                                ▼                          ▼
                         Patient Mobile App         Care Coordination
                                                          │
                     ┌────────────────────────────────────┘
                     ▼
            Epic Bridge Gateway  ──►  FHIR R4  ──►  Epic Aura Application
                                                    (Clinician · Care Team
                                                     via Epic Aura UI)
                     │
                     ▼
            Platform Web App
          (Hospital Admin · Corporate Admin · Researcher)
```

## Access Endpoints by Persona

| Persona | Access Channel | How |
|---|---|---|
| **Patient** | Mobile phone app | Direct — Platform App pushes simplified vitals, alerts |
| **Clinician** | Epic Aura app | SMART on FHIR embedded — risk scores, SOAP drafts appear inside Epic |
| **Care Team** | Epic Aura app | SMART on FHIR embedded — escalation queue inside Epic |
| **Researcher** | Platform web app | Direct — cohort explorer, signal export |
| **Hospital Administrator** | Platform web app | Direct — population health, readmission dashboards |
| **Corporate Administrator** | Platform web app | Direct — system health, SLA, error codes |

## Relationship Key

| Pattern | Meaning |
|---|---|
| **Epic Bridge Gateway (ACL)** | Translates platform domain objects (RiskAssessment, Escalation, SignalObservation) into FHIR R4 resources. Epic concepts never leak into core domain. |
| **SMART on FHIR** | Epic Aura passes PatientReference on launch — the only patient identifier stored on this platform (session only, never persisted) |
| **FHIR R4 Write** | Platform pushes Observation, DocumentReference, and Alert resources to Epic Aura via the bridge |
| **Published Language** | Shared schema for signal packets (device → platform) |
| **Customer-Supplier** | Upstream produces, downstream consumes |
| **Open Host Service** | Single API serving multiple downstream consumers |

## Patient Data Boundary

This platform stores **no patient profile data**. `PatientReference` is an opaque Epic FHIR Patient ID held in session memory only — never written to a database. All records are keyed to this reference.
