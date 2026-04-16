# GlucoSense Connected Platform — Notional Architecture

## Strategic Context

### Vision
A connected glucose management platform with both patient-facing and clinician-facing experiences. A CGM sensor transmits blood glucose data to web and mobile apps where patients log food intake and visualize glucose-food correlations. Clinicians monitor their patient panels, review glucose trends, and make care recommendations based on the data. Caregivers and dietitians have dedicated views for their respective roles.

### Mission
Solve three interconnected problems: (1) Patients can't easily see the real-time impact of food choices on glucose levels, (2) Clinicians lack visibility into patient glucose data between appointments, and (3) Existing CGM apps show raw glucose data but don't correlate it to dietary patterns — leaving both patients and clinicians without the insights needed to make informed dietary and care decisions.

### Current State Pain Points
1. **Manual food logging fatigue** — Tedious data entry causes patients to stop logging, creating gaps in dietary data
2. **Data silos** — Glucose data, food logs, and clinician notes live in separate systems with no unified view
3. **Delayed feedback loops** — Patients don't learn what caused a glucose spike until days later
4. **Incorrect glucose administration** — Root cause of spikes is unclear, leading to improper insulin dosing or dietary overcorrection

### Value Proposition
1. Food-glucose correlation as a first-class feature — not an afterthought
2. Unified platform for all actors (patient, clinician, caregiver, dietitian, admin)
3. Real-time insights — immediate feedback on how food impacts glucose

### Outcomes Expected
1. Patient engagement — % actively logging food at 30/60/90 days
2. Glucose spike reduction — Decrease in spike frequency per patient
3. Time-in-range improvement — % of time glucose stays within target
4. Clinician adoption — Active clinicians reviewing data between appointments
5. Time to insight — Speed of food-glucose correlation after a meal
6. Patient outcomes — HbA1c improvement over 3/6/12 months

### Success Drivers
1. Reliable Bluetooth data transmission — no data gaps
2. Frictionless food logging — under 30 seconds per entry
3. Clinical data accuracy — trustworthy for clinician decision-making
4. Health data privacy and security — PHI protection non-negotiable
5. Correlation accuracy — reliable food-glucose attribution

### Regional Contexts
- **Global deployment:** US (HIPAA, FDA SaMD), EU (GDPR, EU MDR), UK (UK GDPR, MHRA), APAC (PDPA, APPI), Canada (PIPEDA, Health Canada)
- Multi-region cloud with data residency per jurisdiction
- Consent management engine with region-specific rules
- Encryption at rest (AES-256) and in transit (TLS 1.3)
- Multi-language / i18n with regional food databases
- SaMD regulatory isolation for the correlation engine

## Actors & Journeys

### Actors
| Actor | Role |
|-------|------|
| Patient | Wears sensor, logs food, views correlations, learns from patterns |
| Clinician | Monitors patient panel, reviews trends, makes care recommendations |
| Caregiver / Family Member | Monitors loved one's glucose, receives alerts |
| Dietitian / Nutritionist | Reviews food-glucose correlations, provides dietary guidance |
| Admin | Manages platform, onboards clinicians/practices, configures settings |

### Journey Experience Matrix

| Journey Stage | Patient | Clinician | Caregiver | Dietitian | Admin |
|---|---|---|---|---|---|
| Onboarding | IAM, Device Mgmt, Consent | IAM, Admin Mgmt | IAM, Consent | IAM | Admin Mgmt, IAM |
| Sensor Setup | Device Mgmt, Data Ingestion, Validation | — | — | — | Device Mgmt |
| Daily Data Capture | Data Ingestion, Food Logging, Validation, Food DB | — | — | — | — |
| Real-time Monitoring | Glucose Viz, Alerts, Notifications | Clinician Dashboard, Alerts | Caregiver View, Alerts | — | Monitoring |
| Insight & Correlation | Correlation Engine, Patient Dashboard, Validation | Clinician Dashboard, Analytics | Caregiver View | Dietitian View, Validation, Food DB | — |
| Care Collaboration | Messaging, Notifications | Messaging, Clinician Dashboard | Caregiver View, Notifications | Dietitian View, Messaging | — |
| Threshold & Alert Mgmt | Threshold Config, Snooze/Ack | Threshold Config, Escalation, Monitoring | Alert Escalation | Alert Escalation | Monitoring |
| Reporting & Trends | Patient Dashboard, Data Export | Analytics, Data Export | Caregiver View | Dietitian View, Analytics | Analytics |
| Compliance & Data Rights | Consent, Data Export | Audit Trail | Consent | Audit Trail | Audit, Consent, Admin |
| EHR Sync | — | EHR Integration | — | EHR Integration | EHR Integration |

## Capability-to-Enabler-to-Component Mapping

| # | Business Capability | Category | Technical Enabler | Component | Layer |
|---|---|---|---|---|---|
| 1 | Sensor Data Ingestion | Integration | BLE Gateway + Event Streaming | Bluetooth Data Gateway | Integration |
| 2 | Food Logging | Experience + App Services | Mobile UI + Food API + Image Recognition | Smart Food Logger + Mobile App | Experience + App Services |
| 3 | Glucose-Food Correlation | Process | ML/Analytics Engine + Rules Engine | Correlation Engine | Application Services |
| 4 | Real-time Glucose Visualization | Experience | Web/Mobile Charting + WebSocket | Patient Portal + Mobile App | Experience |
| 5 | Patient Dashboard | Experience | Web Application (React/Next.js) | Patient Portal | Experience |
| 6 | Clinician Dashboard | Experience | Web Application (React/Next.js) | Clinician Portal | Experience |
| 7 | Caregiver View | Experience | Web/Mobile shared view | Caregiver Portal | Experience |
| 8 | Dietitian View | Experience | Web Application | Dietitian Portal | Experience |
| 9 | Admin Management | Experience | Admin Web Application | Admin Console | Experience |
| 10 | Notifications & Alerts | Integration | Multi-channel Notification Service | Notification Service | Integration |
| 11 | Threshold Config & Alert Engine | Process | Rules Engine + Event Processor | Alert Engine | Application Services |
| 12 | Patient-Clinician Communication | Process | Secure Messaging Service | Secure Messaging | Application Services |
| 13 | Consent Management | Process | Consent Platform | Consent Manager | Application Services |
| 14 | Identity & Access Management | Platform | IAM Platform (OAuth2/OIDC/RBAC) | IAM Platform | Security & Governance |
| 15 | EHR Integration | Integration | FHIR R4 Adapter | EHR Integration Hub | Integration |
| 16 | Analytics & Reporting | Data | BI Platform + Data Warehouse | Analytics Platform | Data |
| 17 | Data Export & Portability | Process | Export Service + Object Storage | Data Export Service | Application Services |
| 18 | Device Management | Process | IoT Device Management | Device Manager | Application Services |
| 19 | Regional Food Database | Data | Localized Nutrition API + Database | Food & Nutrition Database | Data |
| 20 | Data Validation & Closed Loop | Process | Validation Service + Feedback Engine | Data Validation Engine | Application Services |
| 21 | Audit Trail | Platform | Immutable Audit Log | Audit Service | Security & Governance |

## Architecture Layers

### Experience Layer
| Component | Description | Actors |
|---|---|---|
| Patient Portal | Web app: glucose trends, food log, correlations, recovery patterns | Patient |
| Clinician Portal | Web app: patient panel, drill-down, care recommendations | Clinician |
| Caregiver Portal | Shared view of patient glucose data and alerts | Caregiver |
| Dietitian Portal | Food-glucose correlation focus, dietary pattern analysis | Dietitian |
| Admin Console | Platform management, onboarding, configuration | Admin |
| Mobile App | Sensor pairing, food logging (photo/barcode/favorites), real-time glucose, push alerts | Patient, Caregiver |

### Integration Layer
| Component | Description |
|---|---|
| API Gateway | Single entry point, rate limiting, auth token validation |
| Bluetooth Data Gateway | Receives BLE glucose readings from mobile, validates, streams to event bus |
| Event Bus | Pub/sub backbone: glucose events, food events, alerts, correlation results |
| EHR Integration Hub | FHIR R4 adapter for hospital EHR push/pull |
| Notification Service | Multi-channel delivery: push, SMS, email — routed by severity and preference |

### Application Services Layer
| Component | Description |
|---|---|
| Correlation Engine | Core differentiator. Time-aligned glucose + food correlation, pattern detection. Isolated for SaMD regulatory traceability. |
| Alert Engine | Configurable thresholds, escalation chains, snooze/acknowledge |
| Data Validation Engine | Glucose anomaly detection, food entry completeness, correlation feedback loop |
| Device Manager | Sensor pairing, BLE health, firmware status, battery monitoring |
| Secure Messaging | Encrypted patient-clinician/dietitian communication |
| Consent Manager | Region-specific consent, withdrawal, GDPR data subject requests |
| Data Export Service | Data portability (GDPR), clinical export (PDF, CSV, FHIR) |
| Smart Food Logger | AI-assisted food recognition, barcode scanning, favorites, quick-log (<30s) |

### Data Layer
| Component | Description |
|---|---|
| Patient Data Store | Patient profiles, glucose readings, food logs, correlations — regional deployment |
| Food & Nutrition Database | Localized per region: food names, nutritional data, portion sizes, glycemic index |
| Time-Series Store | Optimized for high-frequency glucose reading storage and retrieval |
| Analytics Platform | Data warehouse + BI: population analytics, outcome tracking, engagement metrics |
| Cache Layer | Real-time glucose cache, session cache, patient summaries |

### Infrastructure Layer
| Component | Description |
|---|---|
| Multi-Region Cloud Platform | AWS/Azure/GCP with regional deployments (US, EU, APAC). Data stays in-region. |
| Container Orchestration | Kubernetes: service deployment, auto-scaling, service mesh |
| CI/CD Pipeline | Automated build/test/deploy with SaMD traceability (IEC 62304) |
| Observability Stack | Logging, metrics, tracing, alerting |
| CDN & Edge | Global content delivery, edge caching |

### Security & Governance (Cross-Cutting)
| Component | Description |
|---|---|
| IAM Platform | OAuth2/OIDC, RBAC (5 roles), MFA, SSO |
| Encryption Service | AES-256 at rest, TLS 1.3 in transit, regional key management |
| Audit Service | Immutable PHI access log — HIPAA + EU MDR compliant |
| Data Classification & DLP | Automatic PHI tagging, data residency enforcement |
| Vulnerability & Compliance | SAST/DAST scanning, SaMD traceability, compliance dashboards |

## Journey-to-Component Traceability

| Journey Stage | Components Involved |
|---|---|
| Onboarding | IAM Platform, Device Manager, Consent Manager, Admin Console |
| Sensor Setup | Mobile App, Device Manager, Bluetooth Data Gateway, Data Validation Engine |
| Daily Data Capture | Mobile App, Smart Food Logger, Bluetooth Data Gateway, Data Validation Engine, Food & Nutrition DB, Event Bus |
| Real-time Monitoring | Patient/Clinician/Caregiver Portal, Mobile App, Alert Engine, Notification Service, Cache Layer, Time-Series Store |
| Insight & Correlation | Correlation Engine, Patient/Clinician/Dietitian Portal, Data Validation Engine, Analytics Platform |
| Care Collaboration | Secure Messaging, Notification Service, Clinician/Dietitian Portal |
| Threshold & Alert Mgmt | Alert Engine, Admin Console, Notification Service, Event Bus |
| Reporting & Trends | Analytics Platform, Data Export Service, Patient/Clinician Portal |
| Compliance & Data Rights | Consent Manager, Audit Service, Data Export Service, Data Classification & DLP |
| EHR Sync | EHR Integration Hub, API Gateway, Patient Data Store |

## Cross-Cutting Concerns

### Security
- All PHI encrypted at rest (AES-256) and in transit (TLS 1.3)
- Role-based access: Patient, Clinician, Caregiver, Dietitian, Admin — each sees only what they should
- MFA required for clinician and admin roles
- API Gateway enforces OAuth2 token validation on every request
- Secure messaging uses end-to-end encryption for patient-clinician communication

### Governance
- Immutable audit trail for all PHI access and modifications
- SaMD regulatory isolation: Correlation Engine is a separate, versioned service with full traceability for FDA 510(k) / EU MDR certification
- CI/CD pipeline enforces IEC 62304 software lifecycle traceability
- Data classification automatically tags PHI and enforces residency rules

### Regional Requirements
- Patient data stays in-region (US data in US, EU data in EU, APAC data in APAC)
- Consent Manager enforces region-specific rules (GDPR right to deletion, HIPAA authorization, PIPEDA consent)
- Food & Nutrition Database localized per market
- Multi-language UI support via i18n framework
- Cloud provider BAA in place for all regions handling PHI
