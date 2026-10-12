import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT_DIR, exist_ok=True)

# ── Palette ─────────────────────────────────────────────────────
NAVY       = "#000050"
WHITE      = "#FFFFFF"
BG_COLOR   = "#F0F2F5"
NEAR_BLACK = "#1A1A1A"

LAYER_COLORS = {
    "device":      {"bg": "#E3F2FD", "border": "#0277BD", "header": "#0277BD"},
    "edge":        {"bg": "#E8EAF6", "border": "#3949AB", "header": "#3949AB"},
    "ingestion":   {"bg": "#FFF3E0", "border": "#E65100", "header": "#E65100"},
    "processing":  {"bg": "#E8F5E9", "border": "#2E7D32", "header": "#2E7D32"},
    "storage":     {"bg": "#FCE4EC", "border": "#AD1457", "header": "#AD1457"},
    "intelligence":{"bg": "#EDE7F6", "border": "#5E35B1", "header": "#5E35B1"},
    "api":         {"bg": "#E0F2F1", "border": "#00695C", "header": "#00695C"},
    "integration": {"bg": "#FFF8E1", "border": "#F57F17", "header": "#F57F17"},
    "frontend":    {"bg": "#F3E5F5", "border": "#6A1B9A", "header": "#6A1B9A"},
    "external":    {"bg": "#EFEBE9", "border": "#4E342E", "header": "#4E342E"},
}

# ── Layout ───────────────────────────────────────────────────────
FIG_W   = 32.0
FIG_H   = 22.0
PAD_L   = 0.35
PAD_R   = 0.35
PAD_TOP = 1.10
PAD_BOT = 0.30

# Each layer: (label, key, row_height, components)
# Each component: (title, subtitle/tech-stack)
LAYERS = [
    ("Device Layer", "device", 1.6, [
        ("Medical Device\n(Wearable)", "6 sensors: bio-impedance\npressure · pH · SpO₂\nH₂O₂ · temperature"),
        ("Connectivity\nModule", "BLE 5.0 / LTE-M\nover-the-air firmware\nupdate (OTA)"),
        ("On-Device\nPre-processing", "Edge MCU\nraw signal buffering\npacket framing"),
    ]),
    ("Edge & Connectivity", "edge", 1.6, [
        ("IoT Edge Gateway", "AWS IoT Greengrass\nor Azure IoT Edge\nedge pre-processing"),
        ("Packet Validator", "Python microservice\nschema validation\nnoise / artifact filter"),
        ("Device Registry", "AWS IoT Core\nor Azure IoT Hub\ndevice twin / shadow"),
    ]),
    ("Ingestion Layer", "ingestion", 1.6, [
        ("Event Stream\n(Signal Bus)", "Apache Kafka\n(MSK or Confluent)\npartitioned by device ID"),
        ("Schema Registry", "Confluent Schema\nRegistry (Avro)\nsignal packet schema"),
        ("Dead Letter Queue", "Kafka DLQ topic\nfailed-packet replay\nalert on threshold"),
    ]),
    ("Signal Processing", "processing", 1.8, [
        ("Normalization\nService", "Python / NumPy + SciPy\nunit conversion\nsignal alignment"),
        ("Feature Engineering\nService", "Impedance → tissue idx\npH + H₂O₂ → oxidative score\nSpO₂ → hypoxia flag\ntemp → fever alert"),
        ("Baseline Engine", "Redis (rolling window)\n7-day median per signal\nper-patient deviation score"),
        ("Time-Series Store", "InfluxDB or\nTimescaleDB\nraw + derived signals"),
    ]),
    ("Intelligence Layer", "intelligence", 1.8, [
        ("Risk Scoring\nModels", "MLflow + XGBoost\nscikit-learn\nIsolation Forest / LSTM"),
        ("LLM Clinical\nSummary", "Claude API\n(Haiku for speed\nSonnet for quality)"),
        ("Anomaly\nDetection", "LSTM Autoencoder\nreal-time inference\nmodel drift monitoring"),
        ("Model Registry\n& Serving", "MLflow Model Registry\nFastAPI inference endpoint\nA/B model routing"),
    ]),
    ("Storage Layer", "storage", 1.6, [
        ("Relational Store", "PostgreSQL (RDS)\nescalations · care tasks\npatient sessions"),
        ("Object Store\n(Audit / Lineage)", "S3 WORM / Azure ADLS\nimmutable event log\nOpenLineage / Marquez"),
        ("Feature Store", "Feast or Databricks\nFeature Store\nreusable ML features"),
        ("Cache / Session", "Redis\nPatientReference\nsession-only, no PII"),
    ]),
    ("API & Services Layer", "api", 1.6, [
        ("Signal API", "FastAPI (Python)\nREST + WebSocket\nsignal query endpoint"),
        ("Clinical API", "FastAPI\nrisk scores · SOAP drafts\nescalation queue"),
        ("Observability\nAPI", "FastAPI + Prometheus\ndevice health · SLA\nPagerDuty alerts"),
        ("Research API", "FastAPI + DuckDB\ncohort query\nsignal export"),
    ]),
    ("EMR Integration Gateway", "integration", 1.8, [
        ("IEMRGateway\n(Port)", "Python ABC\nvendor-agnostic interface\nFHIR R4 + SMART on FHIR"),
        ("EpicAdapter", "Epic FHIR R4 API\nEpic App Orchard\nIn-Basket alerts"),
        ("CernerAdapter", "Oracle Cerner FHIR R4\nCerner App Gallery\nMessage Center"),
        ("GenericFHIRAdapter", "Standard FHIR R4\nAthena · Meditech\nAllscripts · others"),
        ("LOINC\nCode Registry", "Static LOINC mapping\nsignal type → code\nObservation resources"),
    ]),
    ("Frontend Layer", "frontend", 1.6, [
        ("Patient\nMobile App", "React Native\niOS + Android\nSimplified vitals · alerts"),
        ("Platform\nWeb App", "React + FastAPI\nHospital Admin\nCorporate Admin · Researcher"),
        ("EMR Embedded\nApp (SMART)", "SMART on FHIR\napp launch\nClinician · Care Team"),
    ]),
    ("External Systems", "external", 1.4, [
        ("Epic Aura", "FHIR R4 + SMART\nApp Orchard\nEHR system"),
        ("Oracle Cerner", "FHIR R4 + SMART\nApp Gallery\nEHR system"),
        ("Other EMRs", "Athena · Meditech\nAllscripts · others\nFHIR R4 standard"),
        ("Analytics\nPlatform", "Databricks + Power BI\nor Tableau\npopulation health"),
    ]),
]

CONTENT_W = FIG_W - PAD_L - PAD_R
LAYER_GAP = 0.10

# ── Helpers ──────────────────────────────────────────────────────
def draw_box(ax, x, y, w, h, title, subtitle, bg, border, title_color=WHITE,
             title_fs=7.5, sub_fs=6.2):
    patch = FancyBboxPatch((x + 0.04, y + 0.04), w - 0.08, h - 0.08,
                           boxstyle="round,pad=0.04",
                           facecolor=bg, edgecolor=border, linewidth=1.1)
    ax.add_patch(patch)
    mid_x = x + w / 2
    if subtitle:
        ax.text(mid_x, y + h * 0.65, title,
                ha="center", va="center", fontsize=title_fs, fontweight="bold",
                color=NEAR_BLACK, multialignment="center", linespacing=1.25)
        ax.text(mid_x, y + h * 0.25, subtitle,
                ha="center", va="center", fontsize=sub_fs, color="#444444",
                style="italic", multialignment="center", linespacing=1.2)
    else:
        ax.text(mid_x, y + h / 2, title,
                ha="center", va="center", fontsize=title_fs, fontweight="bold",
                color=NEAR_BLACK, multialignment="center", linespacing=1.25)


def draw_diagram():
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.set_xlim(0, FIG_W)
    ax.set_ylim(0, FIG_H)
    ax.axis("off")
    fig.patch.set_facecolor(BG_COLOR)

    # Title
    ax.text(FIG_W / 2, FIG_H - 0.42,
            "Multi-Signal Wearable Device — Technical Reference Architecture",
            ha="center", va="center", fontsize=14, fontweight="bold", color=NAVY)
    ax.text(FIG_W / 2, FIG_H - 0.78,
            "Bio-impedance · Pressure · pH · SpO₂ · Hydrogen Peroxide · Temperature  "
            "|  Port & Adapter EMR Integration  |  FHIR R4 + SMART on FHIR",
            ha="center", va="center", fontsize=8, color="#555555", style="italic")

    # Layout layers bottom-up
    total_layer_h = sum(h for _, _, h, _ in LAYERS)
    total_gap_h   = (len(LAYERS) - 1) * LAYER_GAP
    available_h   = FIG_H - PAD_TOP - PAD_BOT
    scale = available_h / (total_layer_h + total_gap_h)

    y_cur = PAD_BOT
    layer_rects = []
    for lbl, key, rh, comps in reversed(LAYERS):
        layer_rects.insert(0, (lbl, key, rh * scale, comps, y_cur))
        y_cur += rh * scale + LAYER_GAP

    # Draw downward arrows between layers (center)
    arrow_x = FIG_W / 2
    for i in range(len(layer_rects) - 1):
        _, _, h_cur, _, y_cur2 = layer_rects[i]
        _, _, _, _, y_next = layer_rects[i + 1]
        top_cur = y_cur2 + h_cur
        bot_next = y_next
        if bot_next > top_cur + 0.02:
            mid_y = (top_cur + bot_next) / 2
            ax.annotate("", xy=(arrow_x, bot_next), xytext=(arrow_x, top_cur),
                        arrowprops=dict(arrowstyle="-|>", color="#AAAAAA",
                                        lw=1.2, mutation_scale=10))

    # Draw layers
    for lbl, key, rh, comps, y_bot in layer_rects:
        c = LAYER_COLORS[key]

        # Layer background band
        band = FancyBboxPatch((PAD_L, y_bot), CONTENT_W, rh,
                              boxstyle="round,pad=0.05",
                              facecolor=c["bg"], edgecolor=c["border"],
                              linewidth=1.4, alpha=0.35)
        ax.add_patch(band)

        # Layer label (left side)
        label_w = 1.55
        lbl_patch = FancyBboxPatch((PAD_L + 0.06, y_bot + 0.06),
                                   label_w, rh - 0.12,
                                   boxstyle="round,pad=0.04",
                                   facecolor=c["header"], edgecolor="none")
        ax.add_patch(lbl_patch)
        ax.text(PAD_L + 0.06 + label_w / 2, y_bot + rh / 2, lbl,
                ha="center", va="center", fontsize=7.5, fontweight="bold",
                color=WHITE, multialignment="center", linespacing=1.3)

        # Components
        comp_area_x = PAD_L + label_w + 0.22
        comp_area_w = CONTENT_W - label_w - 0.28
        n = len(comps)
        comp_gap = 0.10
        comp_w = (comp_area_w - (n - 1) * comp_gap) / n

        for ci, (title, subtitle) in enumerate(comps):
            cx = comp_area_x + ci * (comp_w + comp_gap)
            draw_box(ax, cx, y_bot, comp_w, rh,
                     title, subtitle,
                     bg=WHITE, border=c["border"])

    return fig, ax


if __name__ == "__main__":
    fig, ax = draw_diagram()
    out_png = os.path.join(OUT_DIR, "reference-architecture.png")
    out_svg = os.path.join(OUT_DIR, "reference-architecture.svg")
    plt.savefig(out_png, dpi=180, bbox_inches="tight", facecolor=BG_COLOR)
    plt.savefig(out_svg, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close()
    print(f"Saved: {out_png}")
    print(f"Saved: {out_svg}")
