# Context Map — Multi-Signal Device

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

## Relationship Key

| Pattern | Meaning |
|---|---|
| **Published Language** | Shared schema for signal packets from device to platform |
| **Customer-Supplier** | Upstream produces, downstream consumes — upstream is responsive to downstream needs |
| **Open Host Service** | Single well-defined API serving multiple downstream consumers |
| **Conformist** | Downstream adopts upstream model as-is (IAM, consent) |
| **ACL (Anti-Corruption Layer)** | Event stream translated at boundary — audit context never leaks domain concepts back upstream |
