# GlucoSense Connected Platform — Architecture Diagrams

## Notional Architecture — Layered View

```mermaid
graph TB
    subgraph EXT["External Systems"]
        CGM[CGM Sensor<br/>BLE]
        EHR_SYS[Hospital EHR<br/>FHIR R4]
        FOOD_API[Third-Party<br/>Food APIs]
        SMS_GW[SMS Gateway<br/>Twilio]
    end

    subgraph SEC["Security & Governance"]
        direction TB
        IAM[IAM Platform<br/>OAuth2 / OIDC / RBAC / MFA]
        ENCRYPT[Encryption Service<br/>AES-256 / TLS 1.3 / KMS]
        AUDIT[Audit Service<br/>Immutable PHI Log]
        DLP[Data Classification<br/>& DLP]
        VULN[Vulnerability &<br/>Compliance]
    end

    subgraph EXP["Experience Layer"]
        direction LR
        PAT_PORT[Patient Portal<br/>Web]
        CLIN_PORT[Clinician Portal<br/>Web]
        CARE_PORT[Caregiver Portal<br/>Web]
        DIET_PORT[Dietitian Portal<br/>Web]
        ADMIN[Admin Console<br/>Web]
        MOB[Mobile App<br/>iOS / Android]
    end

    subgraph INT["Integration Layer"]
        direction LR
        APIGW[API Gateway]
        BLE_GW[Bluetooth<br/>Data Gateway]
        EVENTBUS[Event Bus<br/>Pub/Sub]
        EHR_HUB[EHR Integration<br/>Hub FHIR R4]
        NOTIF[Notification<br/>Service]
    end

    subgraph APP["Application Services Layer"]
        direction LR
        CORR[Correlation<br/>Engine ⚕️<br/>SaMD Isolated]
        ALERT[Alert<br/>Engine]
        VALID[Data Validation<br/>Engine]
        DEVICE[Device<br/>Manager]
        MSG[Secure<br/>Messaging]
        CONSENT[Consent<br/>Manager]
        EXPORT[Data Export<br/>Service]
        FOODLOG[Smart Food<br/>Logger AI]
    end

    subgraph DATA["Data Layer"]
        direction LR
        PATDB[(Patient<br/>Data Store)]
        FOODDB[(Food &<br/>Nutrition DB)]
        TSDB[(Time-Series<br/>Store)]
        ANALYTICS[(Analytics<br/>Platform)]
        CACHE[(Cache<br/>Layer)]
    end

    subgraph INFRA["Infrastructure Layer"]
        direction LR
        CLOUD[Multi-Region<br/>Cloud Platform]
        K8S[Container<br/>Orchestration K8s]
        CICD[CI/CD Pipeline<br/>IEC 62304]
        OBS[Observability<br/>Stack]
        CDN[CDN &<br/>Edge]
    end

    CGM -.->|BLE| MOB
    MOB --> APIGW
    PAT_PORT --> APIGW
    CLIN_PORT --> APIGW
    CARE_PORT --> APIGW
    DIET_PORT --> APIGW
    ADMIN --> APIGW

    MOB -->|glucose readings| BLE_GW
    BLE_GW --> EVENTBUS
    APIGW --> APP
    EVENTBUS --> CORR
    EVENTBUS --> ALERT
    EVENTBUS --> VALID
    EVENTBUS --> NOTIF

    CORR --> TSDB
    CORR --> FOODDB
    CORR --> PATDB
    ALERT --> NOTIF
    VALID --> EVENTBUS
    FOODLOG --> FOODDB
    FOODLOG --> FOOD_API
    MSG --> PATDB
    CONSENT --> PATDB
    EXPORT --> PATDB
    DEVICE --> MOB

    EHR_HUB --> EHR_SYS
    NOTIF --> SMS_GW
    ANALYTICS --> PATDB
    ANALYTICS --> TSDB

    SEC -.-> EXP
    SEC -.-> INT
    SEC -.-> APP
    SEC -.-> DATA
    SEC -.-> INFRA
```

## Data Flow — Glucose Reading to Correlation

```mermaid
sequenceDiagram
    participant S as CGM Sensor
    participant M as Mobile App
    participant BLE as BT Data Gateway
    participant EB as Event Bus
    participant V as Validation Engine
    participant TS as Time-Series Store
    participant CE as Correlation Engine
    participant AE as Alert Engine
    participant N as Notification Service
    participant P as Patient Portal

    S->>M: BLE glucose reading
    M->>BLE: Forward reading
    BLE->>EB: GlucoseReadingReceived
    EB->>V: Validate reading
    V->>TS: Store validated reading
    V->>EB: ReadingValidated

    EB->>AE: Check thresholds
    alt Threshold breached
        AE->>N: Trigger alert
        N->>M: Push notification
    end

    EB->>CE: Correlate with recent food
    CE->>TS: Fetch glucose window
    CE->>CE: Match food events to glucose response
    CE->>EB: CorrelationComputed
    EB->>P: Update dashboard
```

## Data Flow — Food Logging to Correlation

```mermaid
sequenceDiagram
    participant M as Mobile App
    participant FL as Smart Food Logger
    participant FDB as Food & Nutrition DB
    participant EB as Event Bus
    participant V as Validation Engine
    participant PDB as Patient Data Store
    participant CE as Correlation Engine
    participant P as Patient Portal

    M->>FL: Log meal (photo / barcode / manual)
    FL->>FDB: Lookup nutritional data
    FDB-->>FL: Nutritional profile + glycemic index
    FL->>EB: FoodLoggedEvent
    EB->>V: Validate food entry
    V->>PDB: Store food log
    V->>EB: FoodEntryValidated

    EB->>CE: Trigger correlation
    CE->>CE: Match meal to upcoming glucose response
    CE->>EB: CorrelationComputed
    EB->>P: Update glucose-food correlation view
    EB->>M: Push correlation insight
```

## Alert Escalation Flow

```mermaid
sequenceDiagram
    participant AE as Alert Engine
    participant N as Notification Service
    participant P as Patient
    participant CG as Caregiver
    participant CL as Clinician

    AE->>AE: Threshold breached (glucose > 250 mg/dL)
    AE->>N: Level 1 — Notify Patient
    N->>P: Push + In-app alert

    alt Patient acknowledges
        P->>AE: Acknowledged
    else No response (15 min)
        AE->>N: Level 2 — Notify Caregiver
        N->>CG: Push + SMS alert
    end

    alt Caregiver acknowledges
        CG->>AE: Acknowledged
    else No response (30 min) OR critical threshold
        AE->>N: Level 3 — Notify Clinician
        N->>CL: Push + SMS + Email alert
    end
```

## Closed Loop Validation Flow

```mermaid
flowchart TD
    RAW[Raw Data Captured<br/>Glucose reading or Food entry] --> VALIDATE{Validation Engine}

    VALIDATE -->|Glucose| G_CHECK{Reading valid?}
    G_CHECK -->|Anomaly / Gap / Out of range| FLAG[Flag for review<br/>Check sensor health]
    G_CHECK -->|Valid| STORE_G[Store in Time-Series DB]

    VALIDATE -->|Food| F_CHECK{Entry complete?}
    F_CHECK -->|Missing portion / time| PROMPT[Prompt patient<br/>for missing info]
    F_CHECK -->|Complete| STORE_F[Store in Patient DB]

    STORE_G --> CORRELATE[Correlation Engine]
    STORE_F --> CORRELATE

    CORRELATE --> RESULT[Correlation Result<br/>Pizza caused +80 mg/dL spike]
    RESULT --> FEEDBACK{Patient / Clinician<br/>confirms or rejects?}
    FEEDBACK -->|Confirmed| LEARN[Improve correlation model]
    FEEDBACK -->|Rejected| ADJUST[Adjust attribution<br/>Re-correlate]
    ADJUST --> CORRELATE
```

## Multi-Region Deployment

```mermaid
graph TB
    subgraph US["US Region (HIPAA)"]
        US_DATA[(Patient Data<br/>US Residents)]
        US_APP[App Services]
        US_TS[(Time-Series<br/>Store)]
    end

    subgraph EU["EU Region (GDPR + EU MDR)"]
        EU_DATA[(Patient Data<br/>EU Residents)]
        EU_APP[App Services]
        EU_TS[(Time-Series<br/>Store)]
    end

    subgraph APAC["APAC Region (PDPA / APPI)"]
        APAC_DATA[(Patient Data<br/>APAC Residents)]
        APAC_APP[App Services]
        APAC_TS[(Time-Series<br/>Store)]
    end

    subgraph GLOBAL["Global Services"]
        CDN[CDN / Edge]
        FOOD[Food & Nutrition DB<br/>Localized per region]
        ANALYTICS[Analytics Platform<br/>Anonymized aggregates only]
        IAM[IAM Platform<br/>Global identity federation]
    end

    CDN --> US_APP
    CDN --> EU_APP
    CDN --> APAC_APP

    US_APP --> US_DATA
    US_APP --> US_TS
    EU_APP --> EU_DATA
    EU_APP --> EU_TS
    APAC_APP --> APAC_DATA
    APAC_APP --> APAC_TS

    US_APP -.->|anonymized| ANALYTICS
    EU_APP -.->|anonymized| ANALYTICS
    APAC_APP -.->|anonymized| ANALYTICS
```
