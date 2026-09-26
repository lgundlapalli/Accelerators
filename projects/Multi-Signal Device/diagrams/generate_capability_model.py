import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT_DIR, exist_ok=True)

# ── Palette ────────────────────────────────────────────────────
NAVY       = "#000050"
WHITE      = "#FFFFFF"
NEAR_BLACK = "#1A1A1A"
BG_COLOR   = "#F0F2F5"

PERSONA_COLORS = {
    "Patient":                "#0277BD",
    "Clinician":              "#2E7D32",
    "Care Team":              "#6A1B9A",
    "Researcher":             "#E65100",
    "Hospital\nAdministrator": "#AD1457",
    "Regulatory":             "#546E7A",
}

# ── Content (aligned to updated spec: pH, SpO2, H₂O₂, temperature) ──
PERSONAS = [
    {
        "name": "Patient",
        "color": PERSONA_COLORS["Patient"],
        "rows": {
            "insights":  "Simplified vitals view\nSpO2 & pH trend\nSymptom logging prompt\nEscalation alert",
            "aiml":      "Personalized baseline\ndeviation detection\nPlain-language LLM summary\n(SpO2, temp, pH)",
            "analytics": "Relative change from\npersonal baseline\nRolling 7-day SpO2/pH trend",
        },
    },
    {
        "name": "Clinician",
        "color": PERSONA_COLORS["Clinician"],
        "rows": {
            "insights":  "Clinical dashboard\nRisk score (0–100)\nSOAP-note draft\nThreshold breach log",
            "aiml":      "Predictive risk scoring\n(hypoxia, oxidative stress)\nLLM clinical summary\nAnomaly detection",
            "analytics": "SpO2 saturation curves\npH deviation from norm\nH₂O₂ concentration trend\nImpedance & pressure indices",
        },
    },
    {
        "name": "Care Team",
        "color": PERSONA_COLORS["Care Team"],
        "rows": {
            "insights":  "Escalation queue\n(ranked by risk)\nCare coordination\ntimeline & task assign",
            "aiml":      "Priority ranking\nacross panel\nTriage recommendation\nAlert fatigue suppression",
            "analytics": "Multi-patient\naggregated trends\nDeterioration velocity",
        },
    },
    {
        "name": "Researcher",
        "color": PERSONA_COLORS["Researcher"],
        "rows": {
            "insights":  "Cohort explorer\nSignal export\nHypothesis annotation\nModel performance dash",
            "aiml":      "Cohort segmentation\nFeature importance\nexplainability\nModel drift monitoring",
            "analytics": "Raw time-series access\nDerived feature library\nSignal quality scores",
        },
    },
    {
        "name": "Hospital\nAdministrator",
        "color": PERSONA_COLORS["Hospital\nAdministrator"],
        "rows": {
            "insights":  "Utilization dashboard\nCompliance status\nCost-per-patient metrics\nReadmission flags",
            "aiml":      "Population-level risk\nstratification\nPredictive readmission\nscoring",
            "analytics": "Aggregate signal\ncoverage\nSLA adherence\nCohort outcome summaries",
        },
    },
    {
        "name": "Regulatory",
        "color": PERSONA_COLORS["Regulatory"],
        "rows": {
            "insights":  "Audit log viewer\nData lineage trace\nConsent status\nAlgorithm version history",
            "aiml":      "Bias & fairness\nmonitoring reports\nModel card export",
            "analytics": "Signal provenance chain\nAlgorithm input/output\nsnapshots",
        },
    },
]

PLATFORM_COMPONENTS = [
    ("Signal\nIngestion",     "BLE/LTE uplink\nedge pre-processing"),
    ("Normalization",         "Unit conversion\nnoise filtering\nsignal alignment"),
    ("Time-Series\nStore",    "Raw + derived signals\npartitioned by patient"),
    ("Feature\nEngineering",  "Impedance → tissue idx\npH + H₂O₂ → oxidative score\nSpO2 → hypoxia flag\nTemp → fever alert"),
    ("Model\nServing",        "Real-time inference\nrisk & anomaly detection"),
    ("Audit &\nLineage",      "Immutable event log\nconsent management"),
]

ROW_LABELS = ["Insights &\nActions", "AI / ML\nCapabilities", "Analytics &\nDerived Metrics"]

# ── Layout ─────────────────────────────────────────────────────
N_PERSONAS   = len(PERSONAS)
FIG_W        = 30.0
HEADER_H     = 0.9
ROW_H        = 2.8
ROW_GAP      = 0.12
FOOTER_H     = 1.8
ROW_LABEL_W  = 1.5
SWIMLANE_GAP = 0.10
TITLE_H      = 0.75
BOTTOM_PAD   = 0.25
FIG_H = TITLE_H + HEADER_H + 3 * ROW_H + 2 * ROW_GAP + ROW_GAP + FOOTER_H + BOTTOM_PAD + 0.10


def draw_diagram():
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.set_xlim(0, FIG_W)
    ax.set_ylim(0, FIG_H)
    ax.axis("off")
    fig.patch.set_facecolor(BG_COLOR)

    # ── Title ──────────────────────────────────────────────────
    y_title = FIG_H - TITLE_H * 0.38
    ax.text(FIG_W / 2, y_title,
            "Multi-Signal Wearable Device — Persona Capability Model",
            ha="center", va="center", fontsize=13, fontweight="bold", color=NAVY)
    ax.text(FIG_W / 2, y_title - 0.34,
            "Bio-impedance · Pressure · pH · SpO2 · Hydrogen Peroxide · Temperature  |  Six Personas  |  Shared Data Platform",
            ha="center", va="center", fontsize=8, color="#555555", style="italic")

    # ── Geometry ───────────────────────────────────────────────
    content_x = ROW_LABEL_W + 0.10
    content_w = FIG_W - content_x - 0.15
    sw_w = (content_w - (N_PERSONAS - 1) * SWIMLANE_GAP) / N_PERSONAS

    y_header_top = FIG_H - TITLE_H - 0.05
    y_header_bot = y_header_top - HEADER_H
    y_row = []
    y_cur = y_header_bot
    for i in range(3):
        y_cur -= ROW_H
        y_row.append(y_cur)
        y_cur -= ROW_GAP
    y_footer_top = y_row[2] - ROW_GAP
    y_footer_bot = y_footer_top - FOOTER_H

    # ── Row labels ─────────────────────────────────────────────
    for i, lbl in enumerate(ROW_LABELS):
        ry = y_row[i]
        rl_patch = FancyBboxPatch((0.05, ry), ROW_LABEL_W - 0.12, ROW_H,
                                  boxstyle="round,pad=0.03",
                                  facecolor=NAVY, edgecolor="none")
        ax.add_patch(rl_patch)
        ax.text(0.05 + (ROW_LABEL_W - 0.12) / 2, ry + ROW_H / 2, lbl,
                ha="center", va="center", fontsize=8.5, fontweight="bold",
                color=WHITE, multialignment="center", linespacing=1.3)

    # ── Persona swimlanes ───────────────────────────────────────
    for pi, persona in enumerate(PERSONAS):
        sx = content_x + pi * (sw_w + SWIMLANE_GAP)
        col = persona["color"]

        hdr = FancyBboxPatch((sx, y_header_bot), sw_w, HEADER_H,
                             boxstyle="round,pad=0.03",
                             facecolor=col, edgecolor="none")
        ax.add_patch(hdr)
        ax.text(sx + sw_w / 2, y_header_bot + HEADER_H / 2, persona["name"],
                ha="center", va="center", fontsize=9.0, fontweight="bold",
                color=WHITE, multialignment="center", linespacing=1.2)

        for ri, key in enumerate(["insights", "aiml", "analytics"]):
            ry = y_row[ri]
            cell = FancyBboxPatch((sx + 0.04, ry + 0.04), sw_w - 0.08, ROW_H - 0.08,
                                  boxstyle="round,pad=0.04",
                                  facecolor=WHITE, edgecolor=col, linewidth=1.2)
            ax.add_patch(cell)
            ax.text(sx + sw_w / 2, ry + ROW_H / 2, persona["rows"][key],
                    ha="center", va="center", fontsize=6.8, color=NEAR_BLACK,
                    multialignment="center", linespacing=1.3)

    # ── Shared Data Platform footer ────────────────────────────
    footer_x = content_x
    footer_w = content_w
    footer_y = y_footer_bot

    footer_bg = FancyBboxPatch((footer_x, footer_y), footer_w, FOOTER_H,
                               boxstyle="round,pad=0.04",
                               facecolor=NAVY, edgecolor="none")
    ax.add_patch(footer_bg)

    ax.text(footer_x + footer_w / 2, footer_y + FOOTER_H - 0.30,
            "SHARED DATA PLATFORM",
            ha="center", va="center", fontsize=9.5, fontweight="bold", color=WHITE)

    n_comp   = len(PLATFORM_COMPONENTS)
    chip_gap = 0.10
    chip_w   = (footer_w - (n_comp - 1) * chip_gap - 0.20) / n_comp
    chip_h   = FOOTER_H - 0.65
    for ci, (name, subtitle) in enumerate(PLATFORM_COMPONENTS):
        cx = footer_x + 0.10 + ci * (chip_w + chip_gap)
        cy = footer_y + 0.12
        chip = FancyBboxPatch((cx, cy), chip_w, chip_h,
                              boxstyle="round,pad=0.03",
                              facecolor="#1A3A6B", edgecolor="#4A7CC7", linewidth=1.0)
        ax.add_patch(chip)
        ax.text(cx + chip_w / 2, cy + chip_h * 0.68, name,
                ha="center", va="center", fontsize=8.0, fontweight="bold",
                color=WHITE, multialignment="center", linespacing=1.2)
        ax.text(cx + chip_w / 2, cy + chip_h * 0.25, subtitle,
                ha="center", va="center", fontsize=6.5, color="#AACCFF",
                style="italic", multialignment="center", linespacing=1.2)

    # Footer row label
    fl_patch = FancyBboxPatch((0.05, footer_y), ROW_LABEL_W - 0.12, FOOTER_H,
                              boxstyle="round,pad=0.03",
                              facecolor="#0D1A3A", edgecolor="none")
    ax.add_patch(fl_patch)
    ax.text(0.05 + (ROW_LABEL_W - 0.12) / 2, footer_y + FOOTER_H / 2,
            "Shared\nData\nPlatform",
            ha="center", va="center", fontsize=7.5, fontweight="bold",
            color=WHITE, multialignment="center", linespacing=1.3)

    return fig, ax


if __name__ == "__main__":
    fig, ax = draw_diagram()
    out_png = os.path.join(OUT_DIR, "capability-model.png")
    out_svg = os.path.join(OUT_DIR, "capability-model.svg")
    plt.savefig(out_png, dpi=180, bbox_inches="tight", facecolor=BG_COLOR)
    plt.savefig(out_svg, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close()
    print(f"Saved: {out_png}")
    print(f"Saved: {out_svg}")
