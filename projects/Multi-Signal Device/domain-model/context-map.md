# Context Map — Multi-Signal Device

```mermaid
graph TD
    subgraph External["⬛ EXTERNAL SYSTEM"]
        EPICAURA["Epic Aura\n(Upstream EMR — not owned)"]
    end

    subgraph Core["🔴 CORE DOMAIN"]
        SP["Signal Processing\n(Core)"]
        CDS["Clinical Decision Support\n(Core)"]
    end

    subgraph Supporting["🟡 SUPPORTING"]
        PE["Patient Engagement\n(Supporting)"]
        CC["Care Coordination\n(Supporting)"]
        RA["Research Analytics\n(Supporting)"]
        PH["Population Health\n(Supporting)"]
        OBS["Platform Observability\n(Supporting)"]
    end

    subgraph Generic["🟢 GENERIC"]
        AC["Audit & Compliance\n(Generic)"]
        DC["Device Connectivity\n(Generic)"]
        EPIC["Epic Aura Integration\n(Generic — ACL)"]
    end

    EPICAURA -->|"SMART on FHIR\n(launch context + PatientReference)"| EPIC
    EPIC -->|"ACL → PatientReference\n(Conformist)"| SP
    EPIC -->|"ACL → PatientReference\n(Conformist)"| CDS
    EPIC -->|"ACL → PatientReference\n(Conformist)"| PE
    CDS -.->|"FHIR Write-back\n(Observation + SOAP draft)"| EPIC

    DC -->|"Published Language\n(signal packets)"| SP
    SP -->|"Customer-Supplier\n(derived metrics)"| CDS
    SP -->|"Customer-Supplier\n(baseline + trend)"| PE
    SP -->|"Open Host Service\n(time-series API)"| RA
    SP -->|"Open Host Service\n(aggregated signals)"| PH
    CDS -->|"Customer-Supplier\n(risk scores + alerts)"| CC
    CDS -->|"Customer-Supplier\n(risk score + summary)"| PE
    CC -->|"Customer-Supplier\n(panel + tasks)"| PH
    DC -->|"Published Language\n(device health events)"| OBS
    SP -->|"Customer-Supplier\n(pipeline metrics)"| OBS
    SP -.->|"ACL → event stream"| AC
    CDS -.->|"ACL → event stream"| AC
    OBS -.->|"ACL → event stream"| AC
```

## Relationship Key

| Pattern | Meaning |
|---|---|
| **SMART on FHIR** | Epic Aura launches the platform and passes PatientReference — Epic is upstream, this platform conforms |
| **ACL (Anti-Corruption Layer)** | Epic Aura Integration translates Epic FHIR concepts into this platform's `PatientReference` value object — Epic concepts never leak into core domain |
| **FHIR Write-back** | CDS optionally posts risk scores and SOAP drafts back to Epic as FHIR resources — one-way push only |
| **Published Language** | Shared schema for signal packets (device → platform) and device health events |
| **Customer-Supplier** | Upstream produces, downstream consumes — upstream is responsive to downstream needs |
| **Open Host Service** | Single well-defined API serving multiple downstream consumers |
| **Conformist** | Downstream adopts `PatientReference` from Epic Aura Integration as-is |

## Patient Data Boundary

This platform stores **no patient profile data**. The only patient identifier is `PatientReference` — an opaque Epic FHIR Patient ID held in session memory only, never persisted to a database. All clinical records (signal observations, risk assessments, escalations) are keyed to this reference.
