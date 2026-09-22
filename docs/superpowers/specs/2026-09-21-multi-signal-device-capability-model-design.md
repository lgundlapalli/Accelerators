# Multi-Signal Device Capability Model — Design Spec
*Date: 2026-09-21*

## Overview

A persona-first capability model and reference architecture for a hypothetical multi-signal wearable device that generates bio-impedance, pressure, and fluid movement data. The primary deliverable is a diagram that serves both executive stakeholders (capability story) and engineering teams (reference architecture blueprint).

---

## Device Context

- **Type:** Wearable (reference/hypothetical)
- **Signals:** Bio-impedance, pressure, fluid movement
- **Scope:** Multi-signal, multi-condition — not tied to a single disease area
- **Purpose:** Demonstrate how a unified sensing platform surfaces differentiated insights to six distinct personas

---

## Diagram Design

### Layout: Persona-First Vertical Swimlanes

Six vertical swimlanes (left to right), one per persona:

| Swimlane | Persona |
|---|---|
| 1 | Patient |
| 2 | Clinician |
| 3 | Care Team |
| 4 | Researcher |
| 5 | Hospital Administrator |
| 6 | Regulatory |

Four horizontal rows (top to bottom) within each swimlane, plus one shared footer:

| Row | Label | Description |
|---|---|---|
| Row 1 | Insights & Actions | What the persona sees and acts on — dashboards, alerts, summaries, reports |
| Row 2 | AI / ML Capabilities | Intelligence applied for this persona — LLM summaries, risk scoring, anomaly detection, cohort analysis |
| Row 3 | Analytics & Derived Metrics | Computed signals — fluid volume estimates, hemodynamic indices, trend baselines, deviation flags |
| Footer | Shared Data Platform | Full-width row spanning all swimlanes — signal ingestion → normalization → time-series store → feature engineering → model serving |

---

## Persona Capability Detail

### Patient
- **Insights & Actions:** Simplified vitals view, daily fluid balance trend, symptom logging prompt, escalation alert ("contact your care team")
- **AI / ML:** Personalized baseline deviation detection, plain-language LLM summary ("Your fluid levels are slightly elevated today")
- **Analytics:** Relative change from personal baseline, rolling 7-day trend

### Clinician
- **Insights & Actions:** Clinical dashboard, risk score (0–100), SOAP-note draft, threshold breach log, medication titration prompt
- **AI / ML:** Predictive risk scoring (decompensation, fluid overload), LLM-generated clinical summary with cited signal evidence, anomaly detection
- **Analytics:** Absolute impedance values, pressure waveform indices, fluid volume estimates vs. population norms

### Care Team
- **Insights & Actions:** Escalation queue (ranked by risk), care coordination timeline, task assignment, cross-patient panel view
- **AI / ML:** Priority ranking across panel, triage recommendation, alert fatigue suppression (noise filtering)
- **Analytics:** Multi-patient aggregated trends, deterioration velocity

### Researcher
- **Insights & Actions:** Cohort explorer, signal export, hypothesis annotation, model performance dashboard
- **AI / ML:** Cohort segmentation, feature importance explainability, model drift monitoring
- **Analytics:** Raw time-series access, derived feature library, signal quality scores

### Hospital Administrator
- **Insights & Actions:** Utilization dashboard (device uptime, patient enrollment), compliance status, cost-per-patient metrics, readmission flags
- **AI / ML:** Population-level risk stratification, predictive readmission scoring
- **Analytics:** Aggregate signal coverage, SLA adherence, cohort outcome summaries

### Regulatory
- **Insights & Actions:** Audit log viewer, data lineage trace, consent status per patient, algorithm version history
- **AI / ML:** Bias and fairness monitoring reports, model card export
- **Analytics:** Signal provenance chain, algorithm input/output snapshots

---

## Shared Data Platform (Footer)

| Component | Responsibility |
|---|---|
| Signal Ingestion | BLE/LTE device uplink, edge pre-processing, packet validation |
| Normalization | Unit conversion, noise filtering, signal alignment across modalities |
| Time-Series Store | Raw + derived signal storage, partitioned by patient and modality |
| Feature Engineering | Derived metrics computation — impedance → fluid volume, pressure → hemodynamic indices |
| Model Serving | Real-time inference endpoint for risk scoring and anomaly detection |
| Audit & Lineage | Immutable event log, data provenance, consent management |

---

## Implementation

### Output
- Python-generated diagram using matplotlib (consistent with existing diagrams in `projects/Gen Ai Architecture/diagrams/`)
- Saved to `projects/Multi-Signal Device/diagrams/` as PNG + SVG
- Color-coded by persona; shared platform in neutral dark footer

### Style
- Consistent with existing build reference architecture style (navy/white palette, FancyBboxPatch cells)
- Persona swimlanes use distinct accent colors
- Shared platform footer spans full width in dark navy

---

## File Layout

```
projects/Multi-Signal Device/
  diagrams/
    capability-model.png
    capability-model.svg
    generate_capability_model.py
```

---

## Out of Scope

- Real device specifications or clinical validation data
- Integration with specific Abbott systems
- Tier 2 / engineering detail (API specs, data schemas)
