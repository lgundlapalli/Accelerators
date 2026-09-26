import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT_DIR, exist_ok=True)

NAVY       = "#000050"
WHITE      = "#FFFFFF"
NEAR_BLACK = "#1A1A1A"
BG_COLOR   = "#F0F2F5"

GEN_COLORS = {
    1: {"bg": "#E3F2FD", "border": "#0277BD", "header": "#0277BD", "text": "#01579B"},
    2: {"bg": "#E8F5E9", "border": "#2E7D32", "header": "#2E7D32", "text": "#1B5E20"},
    3: {"bg": "#EDE7F6", "border": "#5E35B1", "header": "#5E35B1", "text": "#311B92"},
}

GENERATIONS = [
    {
        "gen": 1,
        "label": "Generation 1",
        "tagline": "Baseline Sensing Platform",
        "signals_new": ["Bio-impedance", "Temperature"],
        "signals_carry": [],
        "derived": [
            "Tissue composition index",
            "Hemodynamic index",
            "Fever flag",
            "Baseline deviation score",
        ],
        "clinical": [
            "Simplified patient vitals view",
            "Temperature & impedance trend",
            "Personalized baseline detection",
            "Clinician threshold breach log",
            "Threshold-based alerting",
            "Care team panel view",
        ],
        "personas": ["Patient", "Clinician", "Care Team"],
    },
    {
        "gen": 2,
        "label": "Generation 2",
        "tagline": "Respiratory & Metabolic Intelligence",
        "signals_new": ["pH", "SpO₂"],
        "signals_carry": ["Bio-impedance", "Temperature"],
        "derived": [
            "Hypoxia flag",
            "SpO₂ saturation curves",
            "pH deviation from norm",
            "Oxidative metabolic index",
        ],
        "clinical": [
            "Hypoxia & respiratory risk scoring",
            "LLM clinical summary (SpO₂, pH)",
            "SOAP-note draft pre-population",
            "Escalation queue with severity",
            "Rolling 7-day SpO₂/pH/temp trend",
            "Cohort segmentation by pH/SpO₂",
        ],
        "personas": ["Patient", "Clinician", "Care Team", "Researcher"],
    },
    {
        "gen": 3,
        "label": "Generation 3",
        "tagline": "Oxidative Stress & Full Platform",
        "signals_new": ["Hydrogen Peroxide"],
        "signals_carry": ["Bio-impedance", "Temperature", "pH", "SpO₂"],
        "derived": [
            "Oxidative stress score (pH + H₂O₂)",
            "Full 6-signal risk composite",
            "Bias & fairness audit trail",
            "Population H₂O₂ cohort norms",
        ],
        "clinical": [
            "Oxidative stress predictive model",
            "Full composite risk score (0–100)",
            "Readmission risk at population scale",
            "Model card & regulatory export",
            "Algorithm lineage & audit log",
            "Research cohort H₂O₂ explorer",
        ],
        "personas": ["Patient", "Clinician", "Care Team", "Researcher", "Hospital Admin", "Corporate Admin"],
    },
]

ROWS = [
    ("New Signals", "signals_new"),
    ("Derived Metrics", "derived"),
    ("Clinical Capabilities", "clinical"),
    ("Personas Served", "personas"),
]

# ── Layout ─────────────────────────────────────────────────────
N_GENS      = 3
FIG_W       = 26.0
TITLE_H     = 0.75
HEADER_H    = 1.0
ROW_HEIGHTS = [1.4, 2.2, 2.8, 1.0]   # signals, derived, clinical, personas
ROW_GAP     = 0.12
GEN_GAP     = 0.20
ROW_LABEL_W = 1.6
BOTTOM_PAD  = 0.25

FIG_H = (TITLE_H + HEADER_H +
         sum(ROW_HEIGHTS) + (len(ROW_HEIGHTS) - 1) * ROW_GAP +
         BOTTOM_PAD + 0.10)

content_x = ROW_LABEL_W + 0.10
content_w = FIG_W - content_x - 0.15
gen_w = (content_w - (N_GENS - 1) * GEN_GAP) / N_GENS


def draw_cell(ax, x, y, w, h, text, facecolor, edgecolor, fontsize=7.2, bold=False, text_color=NEAR_BLACK):
    patch = FancyBboxPatch((x + 0.04, y + 0.04), w - 0.08, h - 0.08,
                           boxstyle="round,pad=0.04",
                           facecolor=facecolor, edgecolor=edgecolor, linewidth=1.2)
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text,
            ha="center", va="center",
            fontsize=fontsize, fontweight="bold" if bold else "normal",
            color=text_color, multialignment="center", linespacing=1.35)


def draw_diagram():
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.set_xlim(0, FIG_W)
    ax.set_ylim(0, FIG_H)
    ax.axis("off")
    fig.patch.set_facecolor(BG_COLOR)

    # ── Title ──────────────────────────────────────────────────
    y_title = FIG_H - TITLE_H * 0.38
    ax.text(FIG_W / 2, y_title,
            "Multi-Signal Wearable Device — Generational Roadmap",
            ha="center", va="center", fontsize=13, fontweight="bold", color=NAVY)
    ax.text(FIG_W / 2, y_title - 0.34,
            "Gen 1: Bio-impedance + Temperature  ·  Gen 2: + pH + SpO₂  ·  Gen 3: + Hydrogen Peroxide",
            ha="center", va="center", fontsize=8, color="#555555", style="italic")

    # ── Row y positions (top-down) ─────────────────────────────
    y_header_bot = FIG_H - TITLE_H - 0.05 - HEADER_H
    y_rows = []
    y_cur = y_header_bot
    for rh in ROW_HEIGHTS:
        y_cur -= rh
        y_rows.append(y_cur)
        y_cur -= ROW_GAP

    # ── Row labels ─────────────────────────────────────────────
    row_label_texts = [lbl for lbl, _ in ROWS]
    for i, lbl in enumerate(row_label_texts):
        ry = y_rows[i]
        rh = ROW_HEIGHTS[i]
        patch = FancyBboxPatch((0.05, ry), ROW_LABEL_W - 0.12, rh,
                               boxstyle="round,pad=0.03",
                               facecolor=NAVY, edgecolor="none")
        ax.add_patch(patch)
        ax.text(0.05 + (ROW_LABEL_W - 0.12) / 2, ry + rh / 2, lbl,
                ha="center", va="center", fontsize=8.0, fontweight="bold",
                color=WHITE, multialignment="center", linespacing=1.3)

    # ── Generation columns ─────────────────────────────────────
    for gi, gen in enumerate(GENERATIONS):
        gx = content_x + gi * (gen_w + GEN_GAP)
        c  = GEN_COLORS[gen["gen"]]

        # Header
        hdr = FancyBboxPatch((gx, y_header_bot), gen_w, HEADER_H,
                             boxstyle="round,pad=0.03",
                             facecolor=c["header"], edgecolor="none")
        ax.add_patch(hdr)
        ax.text(gx + gen_w / 2, y_header_bot + HEADER_H * 0.64,
                gen["label"],
                ha="center", va="center", fontsize=10.5, fontweight="bold", color=WHITE)
        ax.text(gx + gen_w / 2, y_header_bot + HEADER_H * 0.24,
                gen["tagline"],
                ha="center", va="center", fontsize=7.5, color=WHITE, style="italic")

        # Arrow between generations
        if gi < N_GENS - 1:
            ax_mid_y = y_header_bot + HEADER_H / 2
            ax.annotate("", xy=(gx + gen_w + GEN_GAP, ax_mid_y),
                        xytext=(gx + gen_w + 0.04, ax_mid_y),
                        arrowprops=dict(arrowstyle="-|>", color=WHITE, lw=2.0))

        # Row 0 — New Signals (patch only, text drawn separately to avoid doubling)
        ry0 = y_rows[0]
        rh0 = ROW_HEIGHTS[0]
        new_text = "\n".join(f"+ {s}" for s in gen["signals_new"])
        carry_text = "  ·  ".join(gen["signals_carry"]) if gen["signals_carry"] else ""
        patch0 = FancyBboxPatch((gx + 0.04, ry0 + 0.04), gen_w - 0.08, rh0 - 0.08,
                                boxstyle="round,pad=0.04",
                                facecolor=c["bg"], edgecolor=c["border"], linewidth=1.2)
        ax.add_patch(patch0)
        ax.text(gx + gen_w / 2, ry0 + rh0 * (0.70 if carry_text else 0.50),
                new_text,
                ha="center", va="center", fontsize=9.0, fontweight="bold",
                color=c["border"], multialignment="center", linespacing=1.4)
        if carry_text:
            ax.text(gx + gen_w / 2, ry0 + rh0 * 0.22,
                    "Carries: " + carry_text,
                    ha="center", va="center", fontsize=6.5,
                    color="#888888", style="italic", multialignment="center")

        # Row 1 — Derived Metrics
        ry1 = y_rows[1]
        rh1 = ROW_HEIGHTS[1]
        draw_cell(ax, gx, ry1, gen_w, rh1,
                  "\n".join(gen["derived"]),
                  facecolor=WHITE, edgecolor=c["border"],
                  fontsize=7.0, text_color=NEAR_BLACK)

        # Row 2 — Clinical Capabilities
        ry2 = y_rows[2]
        rh2 = ROW_HEIGHTS[2]
        draw_cell(ax, gx, ry2, gen_w, rh2,
                  "\n".join(gen["clinical"]),
                  facecolor=WHITE, edgecolor=c["border"],
                  fontsize=7.0, text_color=NEAR_BLACK)

        # Row 3 — Personas
        ry3 = y_rows[3]
        rh3 = ROW_HEIGHTS[3]
        draw_cell(ax, gx, ry3, gen_w, rh3,
                  "  ·  ".join(gen["personas"]),
                  facecolor=c["bg"], edgecolor=c["border"],
                  fontsize=7.0, bold=True, text_color=c["text"])

    return fig, ax


if __name__ == "__main__":
    fig, ax = draw_diagram()
    out_png = os.path.join(OUT_DIR, "device-generations.png")
    out_svg = os.path.join(OUT_DIR, "device-generations.svg")
    plt.savefig(out_png, dpi=180, bbox_inches="tight", facecolor=BG_COLOR)
    plt.savefig(out_svg, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close()
    print(f"Saved: {out_png}")
    print(f"Saved: {out_svg}")
