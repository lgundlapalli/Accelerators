"""
Abbott GenAI Blueprint — Diagram Generator
Generates PNG + SVG versions of 3 diagrams using matplotlib.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import os

OUT = "/Users/GUNDLLX/learn-claude/projects/Gen Ai Architecture/diagrams"
os.makedirs(OUT, exist_ok=True)

# ── Brand colors ──────────────────────────────────────────────
NAVY   = "#000050"
LAVENDER = "#DDDDF8"
WHITE  = "#FFFFFF"
MED_BLUE = "#3333AA"
LIGHT_GRAY = "#888888"
SOFT_LAVENDER = "#F0F0FF"

DOMAIN_COLORS = [
    "#4472C4",  # Content & Creative
    "#ED7D31",  # Insights & Analytics
    "#A9D18E",  # Productivity & Automation
    "#FF99CC",  # Customer & Field Engagement
    "#FFD966",  # Engineering & Development
    "#9DC3E6",  # Learning & Governance
]

DOMAINS = [
    "Content &\nCreative Studio",
    "Insights &\nAnalytics Acceleration",
    "Productivity &\nAutomation",
    "Customer &\nField Engagement",
    "Engineering &\nDevelopment",
    "Learning, Compliance\n& Governance",
]

SUB_CAPS = [
    ["Creative Content Draft", "Writing Drafts & Data Entry", "Personalize Content", "Translation"],
    ["Search, Screen & Insights", "Reporting & Observability", "Forecast"],
    ["Enterprise Productivity Tools", "Writing Drafts & Data Entry"],
    ["Assistants", "Personalize Content", "Search & CRM Insights"],
    ["Code Creation with Platform", "Code Creation IDE & Test Authoring"],
    ["Learning, Training & Coaching", "Image Identification / Analysis"],
]

TOOLS = [
    "Writer Newsroom, Adobe Firefly, AutogenAI",
    "Mktg Insights Accelerator, RADIA Research, Databricks",
    "M365 Copilot, Cursor/Windsurf, Five9 GSD",
    "SmartRep, Neuron7, Five9 GSD",
    "Cursor/Windsurf/Atlassian AI, Azure AI Sandbox",
    "(Pilots in CHR, Corp, RMDx, Cyber)",
]

DIV_COUNTS = [7, 6, 6, 5, 3, 6]
MATURITY   = ["Scaling", "Producing", "Scaling", "Producing", "Scaling", "Exploring"]


# ══════════════════════════════════════════════════════════════
# DIAGRAM A — Capability Model (horizontal bands)
# ══════════════════════════════════════════════════════════════
def make_capability_model():
    fig, ax = plt.subplots(figsize=(18, 12))
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 12)
    ax.axis("off")
    fig.patch.set_facecolor(WHITE)

    # Title bar
    ax.add_patch(FancyBboxPatch((0, 11), 18, 1, boxstyle="square,pad=0",
                                facecolor=NAVY, edgecolor="none"))
    ax.text(9, 11.5, "Abbott GenAI Capability Model — Enterprise Blueprint",
            ha="center", va="center", fontsize=18, fontweight="bold", color=WHITE)

    band_h = 10 / 6
    for i, (domain, subs, color) in enumerate(zip(DOMAINS, SUB_CAPS, DOMAIN_COLORS)):
        y_bot = (5 - i) * band_h + 0.05
        # Domain band background
        ax.add_patch(FancyBboxPatch((0.1, y_bot), 17.8, band_h - 0.1,
                                    boxstyle="round,pad=0.05",
                                    facecolor=color + "33", edgecolor=color, linewidth=1.5))
        # Domain label
        ax.text(1.2, y_bot + (band_h - 0.1) / 2, domain,
                ha="center", va="center", fontsize=11, fontweight="bold", color=NAVY,
                wrap=True)
        # Sub-capability boxes
        box_w = 2.8
        start_x = 2.8
        for j, sub in enumerate(subs):
            bx = start_x + j * (box_w + 0.25)
            by = y_bot + 0.12
            ax.add_patch(FancyBboxPatch((bx, by), box_w, band_h - 0.35,
                                        boxstyle="round,pad=0.04",
                                        facecolor=WHITE, edgecolor=color, linewidth=1))
            ax.text(bx + box_w / 2, by + (band_h - 0.35) / 2, sub,
                    ha="center", va="center", fontsize=8.5, color="#333333",
                    wrap=True, multialignment="center")

    # Footer
    ax.text(9, 0.15, "Source: Abbott GenAI Historical Catalog — 1Q26 | 220 Use Cases | 12 Divisions",
            ha="center", va="center", fontsize=8, color=LIGHT_GRAY, style="italic")

    plt.tight_layout(pad=0.2)
    for ext in ("png", "svg"):
        path = os.path.join(OUT, f"capability-model.{ext}")
        plt.savefig(path, format=ext, dpi=150 if ext == "png" else None,
                    bbox_inches="tight", facecolor=WHITE)
        print(f"  Saved {path}")
    plt.close()


# ══════════════════════════════════════════════════════════════
# DIAGRAM B — Domain Model (3×2 grid)
# ══════════════════════════════════════════════════════════════
def make_domain_model():
    fig, axes = plt.subplots(2, 3, figsize=(18, 11))
    fig.patch.set_facecolor(WHITE)
    fig.suptitle("Abbott GenAI Domain Model — Use Case Distribution",
                 fontsize=18, fontweight="bold", color=NAVY, y=0.98)

    for idx, ax in enumerate(axes.flat):
        color = DOMAIN_COLORS[idx]
        ax.set_facecolor(color + "22")
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis("off")
        for spine in ax.spines.values():
            spine.set_visible(False)

        # Header
        ax.add_patch(FancyBboxPatch((0, 8.2), 10, 1.8, boxstyle="square,pad=0",
                                    facecolor=color, edgecolor="none"))
        ax.text(5, 9.1, DOMAINS[idx], ha="center", va="center",
                fontsize=12, fontweight="bold", color=WHITE, multialignment="center")

        # Maturity badge
        mat = MATURITY[idx]
        mat_color = {"Producing": "#228822", "Scaling": "#3333AA", "Exploring": "#CC8800"}[mat]
        ax.add_patch(mpatches.FancyBboxPatch((0.3, 7.3), 2.5, 0.7,
                                              boxstyle="round,pad=0.1",
                                              facecolor=mat_color, edgecolor="none"))
        ax.text(1.55, 7.65, mat, ha="center", va="center",
                fontsize=9, fontweight="bold", color=WHITE)

        # Div count
        ax.text(9.5, 7.65, f"{DIV_COUNTS[idx]} Divs", ha="right", va="center",
                fontsize=10, fontweight="bold", color=NAVY)

        # Sub-capabilities
        ax.text(0.4, 6.8, "Sub-capabilities:", fontsize=9, fontweight="bold", color=NAVY)
        for j, sub in enumerate(SUB_CAPS[idx]):
            ax.text(0.6, 6.2 - j * 0.75, f"• {sub}", fontsize=8.5, color="#333333")

        # Tools
        tool_y = 6.2 - len(SUB_CAPS[idx]) * 0.75 - 0.3
        ax.text(0.4, tool_y, "In-Production Tools:", fontsize=9, fontweight="bold", color=NAVY)
        ax.text(0.4, tool_y - 0.65, TOOLS[idx], fontsize=7.5, color="#555555",
                wrap=True, multialignment="left")

    plt.tight_layout(rect=[0, 0, 1, 0.96], pad=1.2, h_pad=1.5, w_pad=1.2)
    for ext in ("png", "svg"):
        path = os.path.join(OUT, f"domain-model.{ext}")
        plt.savefig(path, format=ext, dpi=150 if ext == "png" else None,
                    bbox_inches="tight", facecolor=WHITE)
        print(f"  Saved {path}")
    plt.close()


# ══════════════════════════════════════════════════════════════
# DIAGRAM C — Blueprint Architecture (3-tier)
# ══════════════════════════════════════════════════════════════
def make_blueprint():
    fig, ax = plt.subplots(figsize=(20, 13))
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 13)
    ax.axis("off")
    fig.patch.set_facecolor(WHITE)

    # Title
    ax.add_patch(FancyBboxPatch((0, 12), 20, 1, boxstyle="square,pad=0",
                                facecolor=NAVY, edgecolor="none"))
    ax.text(10, 12.5, "Abbott GenAI Enterprise Blueprint — 3-Tier Architecture",
            ha="center", va="center", fontsize=17, fontweight="bold", color=WHITE)

    # ── TIER 1: Business Domains ──────────────────────────────
    ax.add_patch(FancyBboxPatch((0.2, 9.0), 19.6, 2.8, boxstyle="round,pad=0.1",
                                facecolor=SOFT_LAVENDER, edgecolor=MED_BLUE, linewidth=1.5))
    ax.text(0.6, 11.55, "TIER 1 — BUSINESS DOMAINS", fontsize=11,
            fontweight="bold", color=NAVY)

    tier1_labels = [
        "Content &\nCreative Studio",
        "Insights &\nAnalytics",
        "Productivity &\nAutomation",
        "Customer &\nField Engagement",
        "Engineering &\nDevelopment",
        "Learning, Compliance\n& Governance",
    ]
    box_w = 2.9
    for i, (lbl, col) in enumerate(zip(tier1_labels, DOMAIN_COLORS)):
        bx = 0.5 + i * (box_w + 0.2)
        ax.add_patch(FancyBboxPatch((bx, 9.2), box_w, 2.0,
                                    boxstyle="round,pad=0.1",
                                    facecolor=col, edgecolor="none"))
        ax.text(bx + box_w / 2, 10.2, lbl, ha="center", va="center",
                fontsize=9.5, fontweight="bold", color=WHITE, multialignment="center")

    # ── Arrows down from domains to capabilities ──────────────
    for i in range(6):
        bx = 0.5 + i * (box_w + 0.2) + box_w / 2
        ax.annotate("", xy=(bx, 8.05), xytext=(bx, 9.2),
                    arrowprops=dict(arrowstyle="->", color="#666666", lw=1.5))

    # ── TIER 2: GenAI Capabilities ────────────────────────────
    ax.add_patch(FancyBboxPatch((0.2, 5.5), 19.6, 2.4, boxstyle="round,pad=0.1",
                                facecolor=LAVENDER, edgecolor=NAVY, linewidth=1.5))
    ax.text(0.6, 7.65, "TIER 2 — GENAI CAPABILITIES", fontsize=11,
            fontweight="bold", color=NAVY)

    caps = [
        "Creative Content\nDraft & Translation",
        "Search, Screen\n& Insights",
        "Enterprise\nProductivity Tools",
        "Assistants &\nPersonalization",
        "Code Creation\n& IDE Tools",
        "Learning, Training\n& Compliance",
    ]
    for i, cap in enumerate(caps):
        bx = 0.5 + i * (box_w + 0.2)
        ax.add_patch(FancyBboxPatch((bx, 5.65), box_w, 1.8,
                                    boxstyle="round,pad=0.08",
                                    facecolor=WHITE, edgecolor=MED_BLUE, linewidth=1))
        ax.text(bx + box_w / 2, 6.55, cap, ha="center", va="center",
                fontsize=8.5, color=NAVY, multialignment="center")

    # ── Arrows down from capabilities to platform ─────────────
    for i in range(6):
        bx = 0.5 + i * (box_w + 0.2) + box_w / 2
        ax.annotate("", xy=(bx, 4.55), xytext=(bx, 5.65),
                    arrowprops=dict(arrowstyle="->", color="#666666", lw=1.5))

    # ── TIER 3: Shared Platform ───────────────────────────────
    ax.add_patch(FancyBboxPatch((0.2, 1.0), 19.6, 3.4, boxstyle="round,pad=0.1",
                                facecolor="#E8F0FE", edgecolor=NAVY, linewidth=2))
    ax.text(0.6, 4.15, "TIER 3 — SHARED PLATFORM FOUNDATION", fontsize=11,
            fontweight="bold", color=NAVY)

    platforms = [
        ("Azure AI\nFoundry", "#0078D4"),
        ("Anthropic\nClaude", "#CC8800"),
        ("Salesforce\nEinstein", "#00A1E0"),
        ("Adobe Experience\nCloud", "#FF0000"),
        ("Veeva\nVault AI", "#F26724"),
        ("Microsoft M365\nCopilot", "#00B4F0"),
    ]
    pw = 2.9
    for i, (plat, col) in enumerate(platforms):
        bx = 0.5 + i * (pw + 0.2)
        ax.add_patch(FancyBboxPatch((bx, 1.15), pw, 2.65,
                                    boxstyle="round,pad=0.1",
                                    facecolor=col + "22", edgecolor=col, linewidth=1.5))
        ax.add_patch(FancyBboxPatch((bx, 3.2), pw, 0.55,
                                    boxstyle="square,pad=0",
                                    facecolor=col, edgecolor="none"))
        ax.text(bx + pw / 2, 3.475, plat, ha="center", va="center",
                fontsize=8.5, fontweight="bold", color=WHITE, multialignment="center")
        # CoE / Governance label
        ax.text(bx + pw / 2, 2.2, "CoE Governed\nEnterprise License",
                ha="center", va="center", fontsize=7.5, color="#444444",
                multialignment="center", style="italic")

    # Footer
    ax.text(10, 0.4, "Source: Abbott BTS-DTS GenAI CoE | Enterprise Platform Strategy 1Q26",
            ha="center", fontsize=8, color=LIGHT_GRAY, style="italic")

    plt.tight_layout(pad=0.2)
    for ext in ("png", "svg"):
        path = os.path.join(OUT, f"blueprint.{ext}")
        plt.savefig(path, format=ext, dpi=150 if ext == "png" else None,
                    bbox_inches="tight", facecolor=WHITE)
        print(f"  Saved {path}")
    plt.close()


if __name__ == "__main__":
    print("Generating diagrams...")
    make_capability_model()
    make_domain_model()
    make_blueprint()
    print("Done.")
