import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT_DIR, exist_ok=True)

NAVY      = "#000050"
WHITE     = "#FFFFFF"
BG_COLOR  = "#F4F6F9"
NEAR_BLACK = "#1A1A1A"

# Domain colors
D = {
    "sensing":     ("#DBEAFE", "#1D4ED8", "#1D4ED8"),   # bg, border, text
    "signal":      ("#DCFCE7", "#16A34A", "#14532D"),
    "clinical":    ("#EDE9FE", "#7C3AED", "#4C1D95"),
    "care":        ("#FEF3C7", "#D97706", "#92400E"),
    "research":    ("#FFE4E6", "#E11D48", "#881337"),
    "emr":         ("#FEF9C3", "#CA8A04", "#713F12"),
    "governance":  ("#F1F5F9", "#475569", "#1E293B"),
}

FIG_W = 28.0
FIG_H = 20.0


def domain_box(ax, x, y, w, h, title, bullets, key, title_fs=10.5, bullet_fs=7.8):
    bg, border, text_col = D[key]
    # Shadow
    shadow = FancyBboxPatch((x + 0.08, y - 0.08), w, h,
                            boxstyle="round,pad=0.12",
                            facecolor="#CCCCCC", edgecolor="none", zorder=1)
    ax.add_patch(shadow)
    # Main box
    patch = FancyBboxPatch((x, y), w, h,
                           boxstyle="round,pad=0.12",
                           facecolor=bg, edgecolor=border, linewidth=2.2, zorder=2)
    ax.add_patch(patch)
    # Title bar
    title_bar = FancyBboxPatch((x + 0.08, y + h - 0.72), w - 0.16, 0.62,
                               boxstyle="round,pad=0.06",
                               facecolor=border, edgecolor="none", zorder=3)
    ax.add_patch(title_bar)
    ax.text(x + w / 2, y + h - 0.40, title,
            ha="center", va="center", fontsize=title_fs, fontweight="bold",
            color=WHITE, zorder=4)
    # Bullets
    bullet_text = "\n".join(f"  {b}" for b in bullets)
    ax.text(x + w / 2, y + (h - 0.72) / 2 + 0.05, bullet_text,
            ha="center", va="center", fontsize=bullet_fs, color=text_col,
            multialignment="left", linespacing=1.6, zorder=4)


def flow_arrow(ax, x1, y1, x2, y2, label="", color="#555555",
               lw=2.0, rad=0.0, fs=7.0, label_offset=(0, 0)):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                mutation_scale=14,
                                connectionstyle=f"arc3,rad={rad}"),
                zorder=5)
    if label:
        mx = (x1 + x2) / 2 + label_offset[0]
        my = (y1 + y2) / 2 + label_offset[1]
        ax.text(mx, my, label, ha="center", va="center",
                fontsize=fs, color=color, fontweight="bold",
                bbox=dict(facecolor=BG_COLOR, edgecolor="none", pad=2),
                zorder=6)


def draw_diagram():
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.set_xlim(0, FIG_W)
    ax.set_ylim(0, FIG_H)
    ax.axis("off")
    fig.patch.set_facecolor(BG_COLOR)

    # ── Title ──────────────────────────────────────────────────────
    ax.text(FIG_W / 2, FIG_H - 0.50,
            "Multi-Signal Wearable Device — Conceptual Logical Architecture",
            ha="center", va="center", fontsize=15, fontweight="bold", color=NAVY, zorder=10)
    ax.text(FIG_W / 2, FIG_H - 0.90,
            "Six capability domains  |  Logical information flows  |  Technology-independent",
            ha="center", va="center", fontsize=9, color="#666666", style="italic", zorder=10)

    # ── GOVERNANCE (full-width base) ───────────────────────────────
    gov_y = 0.4
    gov_h = 1.55
    bg, border, text_col = D["governance"]
    gov_patch = FancyBboxPatch((0.5, gov_y), FIG_W - 1.0, gov_h,
                               boxstyle="round,pad=0.10",
                               facecolor=bg, edgecolor=border, linewidth=2.0, zorder=2)
    ax.add_patch(gov_patch)
    ax.text(FIG_W / 2, gov_y + gov_h / 2 + 0.18,
            "GOVERNANCE & OPERATIONS",
            ha="center", va="center", fontsize=10.5, fontweight="bold",
            color=border, zorder=3)
    ax.text(FIG_W / 2, gov_y + gov_h / 2 - 0.22,
            "Audit & Lineage: S3 WORM / OpenLineage   ·   Consent: custom service   ·   "
            "Device Health: Prometheus + Grafana   ·   Alerting: PagerDuty / Azure Monitor   ·   Compliance: AWS Config / Azure Policy",
            ha="center", va="center", fontsize=8.0, color=text_col, zorder=3)

    # Dashed vertical lines showing governance underpins all
    for xpos in [4.0, 9.8, 15.6, 21.4]:
        ax.plot([xpos, xpos], [gov_y + gov_h, 2.4], color=border,
                linestyle="--", linewidth=0.9, alpha=0.4, zorder=1)

    # ── DOMAIN 1: SENSING & ACQUISITION (top-left) ─────────────────
    domain_box(ax, 0.5, 13.5, 6.2, 4.8,
               "SENSING & ACQUISITION",
               ["Wearable: 6-signal BLE 5.0 / LTE-M",
                "Edge compute: AWS IoT Greengrass",
                "  or Azure IoT Edge",
                "Device registry: AWS IoT Core",
                "  or Azure IoT Hub",
                "OTA firmware: AWS IoT Jobs"],
               "sensing")

    # ── DOMAIN 2: SIGNAL INTELLIGENCE (top-center) ─────────────────
    domain_box(ax, 7.2, 13.5, 6.2, 4.8,
               "SIGNAL INTELLIGENCE",
               ["Event stream: Apache Kafka (MSK)",
                "Processing: Python / NumPy / SciPy",
                "Feature eng: AWS Lambda / AKS",
                "Time-series: InfluxDB / TimescaleDB",
                "Baseline cache: Redis (ElastiCache)",
                "Schema: Confluent Schema Registry"],
               "signal")

    # ── DOMAIN 3: CLINICAL INTELLIGENCE (top-right) ────────────────
    domain_box(ax, 13.9, 13.5, 6.2, 4.8,
               "CLINICAL INTELLIGENCE",
               ["Risk models: MLflow + XGBoost",
                "Anomaly: LSTM / Isolation Forest",
                "LLM: Claude API (Haiku / Sonnet)",
                "Model registry: MLflow on SageMaker",
                "  or Azure ML",
                "Inference: FastAPI on EKS / AKS"],
               "clinical")

    # ── DOMAIN 4: CARE DELIVERY (center-left) ──────────────────────
    domain_box(ax, 0.5, 7.8, 6.2, 4.8,
               "CARE DELIVERY",
               ["API: FastAPI on AWS EKS / AKS",
                "Mobile: React Native (iOS + Android)",
                "Push: Firebase / AWS SNS",
                "Real-time: WebSocket / AWS API GW",
                "Escalation store: PostgreSQL (RDS)",
                "Web: React + CloudFront / Azure CDN"],
               "care")

    # ── DOMAIN 5: RESEARCH & POPULATION HEALTH (center-right) ──────
    domain_box(ax, 13.9, 7.8, 6.2, 4.8,
               "RESEARCH & POPULATION HEALTH",
               ["Query: Databricks SQL / DuckDB",
                "Feature store: Feast / Databricks FS",
                "Data lake: S3 / Azure ADLS Gen2",
                "BI: Power BI / Tableau",
                "Cohort API: FastAPI + DuckDB",
                "ML tracking: MLflow"],
               "research")

    # ── DOMAIN 6: EMR INTEGRATION (center-center) ──────────────────
    domain_box(ax, 7.2, 7.8, 6.2, 4.8,
               "EMR INTEGRATION",
               ["Auth: SMART on FHIR OAuth2",
                "Port: IEMRGateway (Python ABC)",
                "EpicAdapter: Epic FHIR R4 API",
                "CernerAdapter: Oracle FHIR R4",
                "GenericFHIRAdapter: standard R4",
                "Session cache: Redis (no DB write)"],
               "emr")

    # ── DOMAIN FLOW ARROWS ─────────────────────────────────────────

    # 1. Sensing → Signal Intelligence
    flow_arrow(ax, 6.7, 16.0, 7.2, 16.0,
               label="raw signal\nstream",
               color=D["sensing"][1], lw=2.2, label_offset=(0, 0.35))

    # 2. Signal Intelligence → Clinical Intelligence
    flow_arrow(ax, 13.4, 16.0, 13.9, 16.0,
               label="derived\nmetrics",
               color=D["signal"][1], lw=2.2, label_offset=(0, 0.35))

    # 3. Signal Intelligence → Care Delivery (down-left)
    flow_arrow(ax, 10.3, 13.5, 3.6, 12.6,
               label="baseline\ntrends",
               color=D["signal"][1], lw=1.8, rad=0.25, label_offset=(-0.8, 0.3))

    # 4. Signal Intelligence → Research (down-right)
    flow_arrow(ax, 10.3, 13.5, 17.0, 12.6,
               label="time-series\naccess",
               color=D["signal"][1], lw=1.8, rad=-0.25, label_offset=(0.8, 0.3))

    # 5. Clinical Intelligence → Care Delivery
    flow_arrow(ax, 17.0, 13.5, 10.3, 12.6,
               label="risk scores\nalerts",
               color=D["clinical"][1], lw=2.2, rad=0.2, label_offset=(0, 0.35))

    # 6. Clinical Intelligence → EMR Integration
    flow_arrow(ax, 17.0, 13.5, 10.3, 12.6,
               color=D["clinical"][1], lw=0.0)  # placeholder
    flow_arrow(ax, 20.1, 13.5, 13.4, 12.2,
               label="risk score\nSOAP draft",
               color=D["clinical"][1], lw=2.0, rad=-0.15, label_offset=(0.5, 0.35))

    # 7. Clinical Intelligence → Research
    flow_arrow(ax, 17.0, 13.5, 17.0, 12.6,
               label="cohort\nfeatures",
               color=D["clinical"][1], lw=1.8, label_offset=(0.9, 0))

    # 8. EMR Integration ↔ External EMRs (right side)
    flow_arrow(ax, 13.4, 10.2, 20.7, 10.2,
               label="FHIR R4\nwrite-back",
               color=D["emr"][1], lw=2.0, label_offset=(0, 0.32))

    # 9. External EMRs → EMR Integration (SMART launch)
    flow_arrow(ax, 20.7, 9.4, 13.4, 9.4,
               label="SMART on FHIR\nPatientReference",
               color="#CA8A04", lw=2.0, label_offset=(0, -0.32))

    # 10. EMR Integration → Care Delivery
    flow_arrow(ax, 7.2, 10.2, 6.7, 10.2,
               label="clinician\ncontext",
               color=D["emr"][1], lw=1.8, label_offset=(0, 0.32))

    # ── EXTERNAL SYSTEMS BOX ───────────────────────────────────────
    ext_bg, ext_border, ext_text = D["emr"]
    ext = FancyBboxPatch((21.1, 8.4), 6.2, 3.6,
                         boxstyle="round,pad=0.12",
                         facecolor="#FFFBEB", edgecolor=ext_border,
                         linewidth=2.0, linestyle="dashed", zorder=2)
    ax.add_patch(ext)
    ax.text(24.2, 11.6, "EXTERNAL EMR SYSTEMS",
            ha="center", va="center", fontsize=9.5, fontweight="bold",
            color=ext_border, zorder=3)
    ax.text(24.2, 10.85, "Epic Aura", ha="center", va="center",
            fontsize=8.5, color=ext_text, zorder=3)
    ax.text(24.2, 10.25, "Oracle Cerner", ha="center", va="center",
            fontsize=8.5, color=ext_text, zorder=3)
    ax.text(24.2,  9.65, "Athena  ·  Meditech", ha="center", va="center",
            fontsize=8.5, color=ext_text, zorder=3)
    ax.text(24.2,  9.05, "Allscripts  ·  others", ha="center", va="center",
            fontsize=8.5, color=ext_text, zorder=3)

    # ── USER PERSONAS (bottom persona strip) ──────────────────────
    persona_y = 2.3
    persona_h = 0.85
    personas = [
        (0.5,  "Patient",              "#0277BD", "Mobile app"),
        (5.0,  "Clinician",            "#2E7D32", "EMR embedded"),
        (9.5,  "Care Team",            "#6A1B9A", "EMR embedded"),
        (14.0, "Researcher",           "#E65100", "Platform web app"),
        (18.5, "Hospital Admin",       "#AD1457", "Platform web app"),
        (23.0, "Corporate Admin",      "#546E7A", "Platform web app"),
    ]
    for px, name, color, channel in personas:
        p = FancyBboxPatch((px, persona_y), 4.0, persona_h,
                           boxstyle="round,pad=0.08",
                           facecolor=color, edgecolor="none", zorder=2)
        ax.add_patch(p)
        ax.text(px + 2.0, persona_y + persona_h * 0.62, name,
                ha="center", va="center", fontsize=8.0, fontweight="bold",
                color=WHITE, zorder=3)
        ax.text(px + 2.0, persona_y + persona_h * 0.22, channel,
                ha="center", va="center", fontsize=6.5, color="#EEEEEE",
                style="italic", zorder=3)

    ax.text(FIG_W / 2, persona_y + persona_h + 0.15,
            "Personas & Channels",
            ha="center", va="bottom", fontsize=8.0, fontweight="bold",
            color="#475569")

    # ── Governance upward arrows ───────────────────────────────────
    for xpos, domain_y in [(3.6, 7.8), (10.3, 7.8), (17.0, 7.8),
                            (3.6, 13.5), (10.3, 13.5), (17.0, 13.5)]:
        ax.annotate("", xy=(xpos, domain_y),
                    xytext=(xpos, gov_y + gov_h),
                    arrowprops=dict(arrowstyle="-", color="#94A3B8",
                                    lw=1.0, linestyle="dotted"),
                    zorder=1)

    # ── Legend ─────────────────────────────────────────────────────
    ax.text(0.6, 7.45, "Information Flows:", fontsize=7.5,
            fontweight="bold", color=NEAR_BLACK)
    items = [
        (D["sensing"][1],  "Raw signal stream"),
        (D["signal"][1],   "Derived metrics / baseline"),
        (D["clinical"][1], "Risk scores / clinical outputs"),
        (D["emr"][1],      "FHIR R4 / SMART on FHIR"),
    ]
    for i, (col, lbl) in enumerate(items):
        bx = 0.6 + i * 6.4
        ax.annotate("", xy=(bx + 1.1, 7.15), xytext=(bx + 0.3, 7.15),
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=1.8,
                                    mutation_scale=10), zorder=6)
        ax.text(bx + 1.25, 7.15, lbl, va="center", fontsize=6.8, color=col)

    return fig, ax


if __name__ == "__main__":
    fig, ax = draw_diagram()
    out_png = os.path.join(OUT_DIR, "conceptual-architecture.png")
    out_svg = os.path.join(OUT_DIR, "conceptual-architecture.svg")
    plt.savefig(out_png, dpi=180, bbox_inches="tight", facecolor=BG_COLOR)
    plt.savefig(out_svg, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close()
    print(f"Saved: {out_png}")
    print(f"Saved: {out_svg}")
