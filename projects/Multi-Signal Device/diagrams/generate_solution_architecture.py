import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.patheffects import withStroke

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT_DIR, exist_ok=True)

# ── Palette ─────────────────────────────────────────────────────
NAVY        = "#000050"
WHITE       = "#FFFFFF"
BG_COLOR    = "#F0F2F5"
NEAR_BLACK  = "#1A1A1A"

ZONE_COLORS = {
    "users":      {"bg": "#E8EAF6", "border": "#3949AB", "label": "#3949AB"},
    "device":     {"bg": "#E3F2FD", "border": "#0277BD", "label": "#0277BD"},
    "platform":   {"bg": "#E8F5E9", "border": "#2E7D32", "label": "#1B5E20"},
    "emr_gw":     {"bg": "#FFF3E0", "border": "#E65100", "label": "#BF360C"},
    "emr_ext":    {"bg": "#EFEBE9", "border": "#4E342E", "label": "#3E2723"},
}

COMP_COLORS = {
    "blue":   ("#BBDEFB", "#0277BD"),
    "green":  ("#C8E6C9", "#2E7D32"),
    "purple": ("#D1C4E9", "#512DA8"),
    "orange": ("#FFE0B2", "#E65100"),
    "pink":   ("#F8BBD0", "#AD1457"),
    "teal":   ("#B2DFDB", "#00695C"),
    "indigo": ("#C5CAE9", "#283593"),
    "brown":  ("#D7CCC8", "#4E342E"),
    "navy":   ("#CFD8DC", "#37474F"),
}

FIG_W = 36.0
FIG_H = 24.0


def box(ax, x, y, w, h, title, subtitle="", color="blue", title_fs=7.8, sub_fs=6.3):
    bg, border = COMP_COLORS[color]
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.06",
                       facecolor=bg, edgecolor=border, linewidth=1.4, zorder=3)
    ax.add_patch(p)
    mid_x, mid_y = x + w / 2, y + h / 2
    if subtitle:
        ax.text(mid_x, y + h * 0.64, title, ha="center", va="center",
                fontsize=title_fs, fontweight="bold", color=NEAR_BLACK,
                multialignment="center", linespacing=1.2, zorder=4)
        ax.text(mid_x, y + h * 0.26, subtitle, ha="center", va="center",
                fontsize=sub_fs, color="#444444", style="italic",
                multialignment="center", linespacing=1.2, zorder=4)
    else:
        ax.text(mid_x, mid_y, title, ha="center", va="center",
                fontsize=title_fs, fontweight="bold", color=NEAR_BLACK,
                multialignment="center", linespacing=1.2, zorder=4)


def zone(ax, x, y, w, h, label, key, alpha=0.18):
    c = ZONE_COLORS[key]
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.10",
                       facecolor=c["bg"], edgecolor=c["border"],
                       linewidth=2.0, alpha=alpha, zorder=1)
    ax.add_patch(p)
    ax.text(x + 0.22, y + h - 0.32, label,
            ha="left", va="top", fontsize=9.0, fontweight="bold",
            color=c["label"], zorder=2)


def arrow(ax, x1, y1, x2, y2, label="", color="#555555", style="-|>", lw=1.5, rad=0.0):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color, lw=lw,
                                connectionstyle=f"arc3,rad={rad}"),
                zorder=5)
    if label:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mx, my, label, ha="center", va="center", fontsize=5.8,
                color=color, style="italic",
                bbox=dict(facecolor=BG_COLOR, edgecolor="none", pad=1.0),
                zorder=6)


def draw_diagram():
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.set_xlim(0, FIG_W)
    ax.set_ylim(0, FIG_H)
    ax.axis("off")
    fig.patch.set_facecolor(BG_COLOR)

    # ── Title ──────────────────────────────────────────────────────
    ax.text(FIG_W / 2, FIG_H - 0.44,
            "Multi-Signal Wearable Device — Solution Architecture",
            ha="center", va="center", fontsize=15, fontweight="bold", color=NAVY, zorder=10)
    ax.text(FIG_W / 2, FIG_H - 0.82,
            "Bio-impedance · Pressure · pH · SpO₂ · H₂O₂ · Temperature  |  "
            "FHIR R4 + SMART on FHIR  |  Port & Adapter EMR Integration",
            ha="center", va="center", fontsize=8.5, color="#555555", style="italic", zorder=10)

    # ════════════════════════════════════════════════════════════════
    # ZONE 1 — USERS (top strip)
    # ════════════════════════════════════════════════════════════════
    zone(ax, 0.3, 20.0, 35.4, 2.8, "Users & Access Channels", "users", alpha=0.25)

    box(ax, 0.7,  20.4, 4.2, 2.0, "Patient\n(Mobile App)",
        "React Native · iOS/Android\nSimplified vitals · alerts\nSpO₂/pH/temp trends", "blue")
    box(ax, 5.4,  20.4, 4.8, 2.0, "Clinician + Care Team\n(EMR Embedded App)",
        "SMART on FHIR launch\nRisk scores · SOAP drafts\nEscalation queue", "green")
    box(ax, 10.7, 20.4, 4.8, 2.0, "Hospital Administrator\n(Platform Web App)",
        "React + FastAPI\nPopulation health\nReadmission dashboards", "pink")
    box(ax, 16.0, 20.4, 4.8, 2.0, "Corporate Administrator\n(Platform Web App)",
        "React + FastAPI\nDevice fleet health\nSLA · error codes", "navy")
    box(ax, 21.3, 20.4, 4.8, 2.0, "Researcher\n(Platform Web App)",
        "React + FastAPI\nCohort explorer\nSignal export", "orange")
    box(ax, 26.6, 20.4, 4.8, 2.0, "Clinician / Care Team\n(Epic Aura · Cerner · other)",
        "EMR native UI\nembeds platform via\nSMART on FHIR", "brown")

    # ════════════════════════════════════════════════════════════════
    # ZONE 2 — DEVICE + EDGE (left column)
    # ════════════════════════════════════════════════════════════════
    zone(ax, 0.3, 1.0, 6.8, 18.6, "Device & Edge", "device", alpha=0.22)

    box(ax, 0.7, 16.8, 5.9, 1.8, "Wearable Device",
        "6 sensors\nBLE 5.0 / LTE-M\nOTA firmware", "blue")
    box(ax, 0.7, 14.5, 5.9, 1.8, "On-Device MCU",
        "Signal buffering\nPacket framing\nEdge pre-processing", "indigo")
    box(ax, 0.7, 12.2, 5.9, 1.8, "IoT Edge Gateway",
        "AWS IoT Greengrass\nor Azure IoT Edge\nedge compute", "blue")
    box(ax, 0.7,  9.9, 5.9, 1.8, "Packet Validator",
        "Python microservice\nSchema validation\nNoise / artifact filter", "indigo")
    box(ax, 0.7,  7.6, 5.9, 1.8, "Device Registry",
        "AWS IoT Core\nor Azure IoT Hub\nDevice twin / shadow", "blue")
    box(ax, 0.7,  5.3, 5.9, 1.8, "Platform Observability",
        "Prometheus + Grafana\nDevice uptime · packet loss\nSignal completeness · SLA", "navy")
    box(ax, 0.7,  3.0, 5.9, 1.8, "PagerDuty / Azure Monitor",
        "SLA breach alerts\nError code log\nOn-call escalation", "navy")

    # ════════════════════════════════════════════════════════════════
    # ZONE 3 — PLATFORM CORE (center)
    # ════════════════════════════════════════════════════════════════
    zone(ax, 7.5, 1.0, 19.8, 18.6, "Platform Core", "platform", alpha=0.18)

    # -- Ingestion row --
    box(ax,  7.9, 16.8, 4.8, 1.8, "Event Stream\n(Signal Bus)",
        "Apache Kafka (MSK)\npartitioned by device ID\nAvro Schema Registry", "green")
    box(ax, 13.2, 16.8, 4.8, 1.8, "Dead Letter Queue",
        "Kafka DLQ topic\nfailed-packet replay\nalert on threshold", "teal")
    box(ax, 18.5, 16.8, 4.0, 1.8, "Audit & Lineage",
        "S3 WORM / ADLS\nOpenLineage · Marquez\nImmutable event log", "teal")

    # -- Signal Processing row --
    box(ax,  7.9, 14.2, 4.8, 2.0, "Normalization\nService",
        "Python / NumPy + SciPy\nUnit conversion\nSignal alignment", "green")
    box(ax, 13.2, 14.2, 4.8, 2.0, "Feature Engineering\nService",
        "Impedance → tissue idx\npH + H₂O₂ → oxidative score\nSpO₂ → hypoxia flag", "green")
    box(ax, 18.5, 14.2, 4.0, 2.0, "Baseline Engine",
        "Redis (rolling window)\n7-day median per signal\nDeviation scoring", "teal")

    # -- Storage row --
    box(ax,  7.9, 11.8, 4.8, 1.8, "Time-Series Store",
        "InfluxDB or\nTimescaleDB\nRaw + derived signals", "green")
    box(ax, 13.2, 11.8, 4.8, 1.8, "Relational Store",
        "PostgreSQL (RDS)\nEscalations · care tasks\nPatient sessions", "teal")
    box(ax, 18.5, 11.8, 4.0, 1.8, "Feature Store",
        "Feast or Databricks\nReusable ML features\nCohort attributes", "teal")

    # -- Intelligence row --
    box(ax,  7.9,  9.3, 4.8, 2.0, "Risk Scoring\nModels",
        "MLflow + XGBoost\nscikit-learn\nIsolation Forest / LSTM", "purple")
    box(ax, 13.2,  9.3, 4.8, 2.0, "LLM Clinical\nSummary",
        "Claude API\nHaiku (speed)\nSonnet (quality)", "purple")
    box(ax, 18.5,  9.3, 4.0, 2.0, "Model Registry\n& Serving",
        "MLflow Model Registry\nFastAPI inference\nA/B model routing", "purple")

    # -- API row --
    box(ax,  7.9,  6.9, 4.8, 1.8, "Signal API",
        "FastAPI · REST + WS\nSignal query\nBaseline endpoint", "green")
    box(ax, 13.2,  6.9, 4.8, 1.8, "Clinical API",
        "FastAPI\nRisk scores · SOAP drafts\nEscalation queue", "green")
    box(ax, 18.5,  6.9, 4.0, 1.8, "Research API",
        "FastAPI + DuckDB\nCohort query\nSignal export", "teal")

    # -- Analytics --
    box(ax,  7.9,  4.4, 4.8, 1.8, "Population Health",
        "Databricks SQL\nReadmission risk\nRisk stratification", "pink")
    box(ax, 13.2,  4.4, 4.8, 1.8, "Care Coordination",
        "PostgreSQL + FastAPI\nEscalation queue\nPanel management", "pink")
    box(ax, 18.5,  4.4, 4.0, 1.8, "Analytics Dashboard",
        "Power BI / Tableau\nDatabricks\nPopulation reporting", "pink")

    # -- Session cache --
    box(ax,  7.9,  2.2, 9.4, 1.8, "Session Cache (Redis)",
        "PatientReference (opaque FHIR Patient ID, session-only, never persisted to DB)  ·  "
        "SMART on FHIR token", "teal")
    box(ax, 18.5,  2.2, 4.0, 1.8, "Consent &\nCompliance",
        "Consent records\nAudit export\nRegulatory reports", "navy")

    # ════════════════════════════════════════════════════════════════
    # ZONE 4 — EMR INTEGRATION GATEWAY (right column upper)
    # ════════════════════════════════════════════════════════════════
    zone(ax, 27.7, 9.5, 8.0, 10.1, "EMR Integration Gateway", "emr_gw", alpha=0.25)

    box(ax, 28.1, 17.0, 7.2, 1.8, "IEMRGateway\n(Port — Python ABC)",
        "FHIR R4 + SMART on FHIR\nVendor-agnostic interface\nget_patient_reference · write_*", "orange")
    box(ax, 28.1, 14.6, 7.2, 1.8, "EpicAdapter",
        "Epic FHIR R4 API\nApp Orchard registration\nIn-Basket alerts", "orange")
    box(ax, 28.1, 12.2, 7.2, 1.8, "CernerAdapter",
        "Oracle Cerner FHIR R4\nApp Gallery registration\nMessage Center", "orange")
    box(ax, 28.1,  9.9, 7.2, 1.8, "GenericFHIRAdapter",
        "Standard FHIR R4\nAthena · Meditech · others\nObservation · DocumentRef · Communication", "orange")

    # ════════════════════════════════════════════════════════════════
    # ZONE 5 — EXTERNAL EMR SYSTEMS (right column lower)
    # ════════════════════════════════════════════════════════════════
    zone(ax, 27.7, 1.0, 8.0, 8.0, "External EMR Systems", "emr_ext", alpha=0.22)

    box(ax, 28.1, 7.4, 7.2, 1.6, "Epic Aura",
        "FHIR R4 · App Orchard\nSMART on FHIR launch\nEHR system", "brown")
    box(ax, 28.1, 5.4, 7.2, 1.6, "Oracle Cerner",
        "FHIR R4 · App Gallery\nSMART on FHIR launch\nEHR system", "brown")
    box(ax, 28.1, 3.4, 7.2, 1.6, "Athena / Meditech\n/ Allscripts",
        "FHIR R4 standard\nSMART on FHIR launch\nGenericFHIRAdapter", "brown")
    box(ax, 28.1, 1.4, 7.2, 1.6, "Databricks\n+ Power BI / Tableau",
        "Population analytics\nCohort reporting\nExternal BI platform", "brown")

    # ════════════════════════════════════════════════════════════════
    # ARROWS — key data flows
    # ════════════════════════════════════════════════════════════════
    AC = "#0277BD"   # device flows
    PC = "#2E7D32"   # platform flows
    OC = "#E65100"   # EMR flows
    RC = "#AD1457"   # return / write-back
    GC = "#555555"   # generic

    # Device chain
    arrow(ax, 3.65, 18.6, 3.65, 18.3, color=AC)   # device → MCU
    arrow(ax, 3.65, 16.3, 3.65, 16.0, color=AC)   # MCU → edge gw
    arrow(ax, 3.65, 14.0, 3.65, 13.7, color=AC)   # edge gw → validator
    arrow(ax, 3.65, 11.7, 3.65, 11.4, color=AC)   # validator → registry
    arrow(ax, 3.65,  9.4, 3.65,  7.1, color=AC, label="DeviceOffline\nPacketLoss")   # → observability

    # Device → Kafka
    arrow(ax, 6.6, 15.9, 7.9, 17.7, color=AC, label="validated\npackets")

    # Kafka → normalization
    arrow(ax, 10.3, 16.8, 10.3, 16.2, color=PC)
    # Normalization → Feature Eng
    arrow(ax, 12.7, 15.2, 13.2, 15.2, color=PC)
    # Feature Eng → Baseline Engine
    arrow(ax, 18.0, 15.2, 18.5, 15.2, color=PC)
    # Normalization → Time Series
    arrow(ax, 10.3, 14.2, 10.3, 13.6, color=PC, label="SignalObservation\nRecorded")
    # Feature Eng → Risk Scoring
    arrow(ax, 15.6, 14.2, 15.6, 11.3, color=PC)
    arrow(ax, 15.6, 11.3, 15.6, 11.3, color=PC)
    # Time Series → Risk Scoring
    arrow(ax, 10.3, 11.8, 10.3, 11.3, color=PC)
    arrow(ax, 10.3, 11.3, 9.3,  11.3, color=PC)
    arrow(ax, 9.3,  11.3, 9.3,   9.3, color=PC)
    # Risk Scoring → LLM
    arrow(ax, 12.7,  10.3, 13.2, 10.3, color=PC, label="RiskFactor[]")
    # Risk Scoring → Care Coord
    arrow(ax, 10.3,  9.3, 10.3,  6.2, color=PC, label="Escalation\nTriggered")
    # Clinical API → Care Coord
    arrow(ax, 15.6,  6.9, 15.6,  6.2, color=PC)
    # Signal API → Population Health
    arrow(ax, 10.3,  6.9, 10.3,  6.2, color=PC)

    # Platform → EMR Gateway
    arrow(ax, 22.5, 11.3, 28.1, 15.7, color=OC, rad=-0.15,
          label="risk scores · SOAP drafts\nescalations (FHIR R4)")

    # SMART on FHIR launch
    arrow(ax, 28.1, 14.5, 22.5, 10.3, color=RC, rad=0.15,
          label="SMART launch\nPatientReference")

    # Gateway → EMR systems
    arrow(ax, 31.7,  9.9, 31.7,  9.0, color=OC)
    arrow(ax, 31.7,  7.4, 31.7,  7.0, color=OC)
    arrow(ax, 31.7,  5.4, 31.7,  5.0, color=OC)
    arrow(ax, 31.7,  3.4, 31.7,  3.0, color=OC)

    # PatientReference → Session Cache
    arrow(ax, 28.1, 10.8, 18.5,  3.1, color=RC, rad=0.25,
          label="PatientReference\n(session only)")

    # Users → APIs
    arrow(ax,  2.8, 20.4,  2.8, 20.0, color=GC)    # Patient → mobile
    arrow(ax,  7.8, 20.4, 14.6, 18.6, color=GC)    # Clinician → platform
    arrow(ax, 13.1, 20.4, 10.3,  8.7, color=GC, rad=-0.1)  # HospAdmin → APIs
    arrow(ax, 18.4, 20.4, 10.3,  8.7, color=GC, rad=-0.15) # CorpAdmin → Observ.
    arrow(ax, 23.7, 20.4, 20.5,  8.7, color=GC, rad=0.1)   # Researcher → Research API
    arrow(ax, 29.0, 20.4, 29.0, 18.8, color=GC)    # Clinician EMR UI ↔ Gateway

    # ── Legend ──────────────────────────────────────────────────
    legend_items = [
        (AC, "Device data flow"),
        (PC, "Platform processing"),
        (OC, "EMR write-back (FHIR R4)"),
        (RC, "SMART on FHIR / PatientReference"),
        (GC, "User access"),
    ]
    lx, ly = 0.5, 0.35
    ax.text(lx, ly + 0.55, "Data Flows:", fontsize=7, fontweight="bold",
            color=NEAR_BLACK, va="center")
    for i, (color, label) in enumerate(legend_items):
        ax.annotate("", xy=(lx + 0.9 + i * 5.5, ly + 0.28),
                    xytext=(lx + 0.3 + i * 5.5, ly + 0.28),
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=1.8))
        ax.text(lx + 1.0 + i * 5.5, ly + 0.28, label,
                fontsize=6.5, color=color, va="center")

    return fig, ax


if __name__ == "__main__":
    fig, ax = draw_diagram()
    out_png = os.path.join(OUT_DIR, "solution-architecture.png")
    out_svg = os.path.join(OUT_DIR, "solution-architecture.svg")
    plt.savefig(out_png, dpi=180, bbox_inches="tight", facecolor=BG_COLOR)
    plt.savefig(out_svg, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close()
    print(f"Saved: {out_png}")
    print(f"Saved: {out_svg}")
