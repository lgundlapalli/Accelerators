import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# ── Color palette ──────────────────────────────────────────
NAVY       = "#000050"
MED_BLUE   = "#3333AA"
LAVENDER   = "#DDDDFF"
SOFT_LAV   = "#F0F0FF"
WHITE      = "#FFFFFF"
NEAR_BLACK = "#1A1A1A"
LIGHT_GRAY = "#888888"

AGENT_COLORS = {
    "ALICE":   {"bg": "#FFE8D6", "border": "#C05000", "text": "#7A3000"},
    "BRANDS":  {"bg": "#D6E8FF", "border": "#003087", "text": "#003087"},
    "CRAFTS":  {"bg": "#E8F4E8", "border": "#1A7A1A", "text": "#1A5C1A"},
    "SPARK":   {"bg": "#F3E5F5", "border": "#7B1FA2", "text": "#5C0E7A"},
    "ACCESS":  {"bg": "#FFF3E0", "border": "#B35A00", "text": "#7A3E00"},
    "PLATFORM":{"bg": "#E3F2FD", "border": "#0277BD", "text": "#01579B"},
}

def rounded_box(ax, x, y, w, h, bg, border, text, fontsize=8.5, bold=False, text_color=NEAR_BLACK):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.015",
                         facecolor=bg, edgecolor=border, linewidth=1.2)
    ax.add_patch(box)
    ax.text(x + w/2, y + h/2, text, ha='center', va='center',
            fontsize=fontsize, color=text_color, fontweight='bold' if bold else 'normal',
            multialignment='center', linespacing=1.3, wrap=True)

def section_header(ax, x, y, w, h, label, color, text_color=WHITE):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.01",
                         facecolor=color, edgecolor=color, linewidth=0)
    ax.add_patch(box)
    ax.text(x + w/2, y + h/2, label, ha='center', va='center',
            fontsize=9.5, color=text_color, fontweight='bold')


# ═══════════════════════════════════════════════════════════
# DIAGRAM 1: LAYERED ARCHITECTURE VIEW
# ═══════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(24, 15))
ax.set_xlim(0, 24)
ax.set_ylim(0, 15)
ax.axis('off')
fig.patch.set_facecolor('#F8F9FA')
ax.set_facecolor('#F8F9FA')

ax.text(12, 14.6, "EPD Marketer of the Future — Business Capability Map (Architecture Layers)",
        ha='center', va='center', fontsize=14, fontweight='bold', color=NAVY)

layers = [
    {
        "label": "ALICE — CREATIVE EXCELLENCE",
        "y": 12.1, "h": 1.65,
        "bg": AGENT_COLORS["ALICE"]["bg"], "border": AGENT_COLORS["ALICE"]["border"],
        "text_col": AGENT_COLORS["ALICE"]["text"],
        "caps": ["Creative Generation\n(Adobe Firefly / GenStudio)",
                 "Brief Intelligence\n(Persado)",
                 "Copy & Claim Generation\n(Writer.com)",
                 "Creative Ops & Workflow\n(Adobe Workfront)"]
    },
    {
        "label": "BRANDS — BRAND STRATEGY",
        "y": 10.0, "h": 1.65,
        "bg": AGENT_COLORS["BRANDS"]["bg"], "border": AGENT_COLORS["BRANDS"]["border"],
        "text_col": AGENT_COLORS["BRANDS"]["text"],
        "caps": ["Market Intelligence\n(Deepsights / IQVIA)",
                 "Social Listening\n(Brandwatch / Synthesio)",
                 "Strategy Modeling\n(ZS ZAIDYN / McKinsey Lilli)",
                 "Synthetic Research\n(Digital Twins)"]
    },
    {
        "label": "CRAFTS — CONTENT EXCELLENCE",
        "y": 7.9, "h": 1.65,
        "bg": AGENT_COLORS["CRAFTS"]["bg"], "border": AGENT_COLORS["CRAFTS"]["border"],
        "text_col": AGENT_COLORS["CRAFTS"]["text"],
        "caps": ["MLR Review\n(Veeva PromoMats AI)",
                 "Compliance Detection\n(Indegene AI)",
                 "Modular Content Creation\n(Writer.com / AEM)",
                 "Content Testing\n(Optimizely / VWO AI)"]
    },
    {
        "label": "SPARK — CUSTOMER ENGAGEMENT",
        "y": 5.8, "h": 1.65,
        "bg": AGENT_COLORS["SPARK"]["bg"], "border": AGENT_COLORS["SPARK"]["border"],
        "text_col": AGENT_COLORS["SPARK"]["text"],
        "caps": ["Next-Best-Action\n(Aktana / PharmaForceIQ)",
                 "CRM & HCP Journeys\n(Veeva Vault CRM AI)",
                 "Patient Engagement\n(Conversa Health)",
                 "Omnichannel Personalization\n(Adobe Sensei)"]
    },
    {
        "label": "ACCESS — MARKET ACCESS",
        "y": 3.7, "h": 1.65,
        "bg": AGENT_COLORS["ACCESS"]["bg"], "border": AGENT_COLORS["ACCESS"]["border"],
        "text_col": AGENT_COLORS["ACCESS"]["text"],
        "caps": ["Competitive Intelligence\n(IQVIA Market Edge AI)",
                 "HTA & Value Dossier\n(ZS ZAIDYN Access)",
                 "Patient Support Programs\n(ConnectiveRx AI)",
                 "Regulatory Compliance\n(RegASK / Veripharm)"]
    },
    {
        "label": "SHARED PLATFORM & DATA LAYER",
        "y": 1.2, "h": 2.0,
        "bg": AGENT_COLORS["PLATFORM"]["bg"], "border": AGENT_COLORS["PLATFORM"]["border"],
        "text_col": AGENT_COLORS["PLATFORM"]["text"],
        "caps": ["Data & Analytics\n(Salesforce Einstein /\nIQVIA)",
                 "CRM Foundation\n(Salesforce LS Cloud /\nVeeva CRM)",
                 "Content Management\n(Adobe Experience\nManager)",
                 "Identity & Access\n(Abbott IAM /\nSSO)",
                 "Integration & API\n(MuleSoft /\nAzure APIM)",
                 "Compliance & Audit\n(Veeva Vault /\nAudit Platform)"]
    },
]

LABEL_W = 2.2
LEFT = 0.3
TOTAL_W = 23.4
CAP_AREA = TOTAL_W - LABEL_W - 0.2
GAP = 0.1

for layer in layers:
    y = layer["y"]
    h = layer["h"]
    caps = layer["caps"]
    n = len(caps)
    cap_w = (CAP_AREA - (n - 1) * GAP) / n

    # Background band
    bg_box = FancyBboxPatch((LEFT, y), TOTAL_W, h, boxstyle="round,pad=0.04",
                            facecolor=layer["bg"], edgecolor=layer["border"], linewidth=1.5)
    ax.add_patch(bg_box)

    # Label
    ax.text(LEFT + 0.1, y + h/2, layer["label"], ha='left', va='center',
            fontsize=9, fontweight='bold', color=layer["text_col"])

    # Capability boxes
    for i, cap in enumerate(caps):
        bx = LEFT + LABEL_W + i * (cap_w + GAP)
        by = y + 0.15
        rounded_box(ax, bx, by, cap_w, h - 0.3, WHITE, layer["border"], cap,
                    fontsize=8, text_color=NEAR_BLACK)

plt.tight_layout(pad=0.4)
plt.savefig("marketing-capability-layered.png", dpi=180, bbox_inches='tight', facecolor='#F8F9FA')
plt.savefig("marketing-capability-layered.svg", bbox_inches='tight', facecolor='#F8F9FA')
plt.close()
print("Layered diagram saved.")


# ═══════════════════════════════════════════════════════════
# DIAGRAM 2: DOMAIN VIEW
# ═══════════════════════════════════════════════════════════
fig2, ax2 = plt.subplots(figsize=(26, 16))
ax2.set_xlim(0, 26)
ax2.set_ylim(0, 16)
ax2.axis('off')
fig2.patch.set_facecolor('#F8F9FA')
ax2.text(13, 15.5, "EPD Marketer of the Future — Business Capability Map (Domain View)",
         ha='center', va='center', fontsize=14, fontweight='bold', color=NAVY)

domains = [
    {
        "label": "ALICE\nCreative Excellence", "col": 0, "row": 1,
        "color": AGENT_COLORS["ALICE"],
        "caps": [
            ("Creative Generation", "Adobe Firefly / GenStudio"),
            ("Brief Intelligence", "Persado"),
            ("Copy & Claim Generation", "Writer.com"),
            ("Creative Ops & Workflow", "Adobe Workfront"),
        ]
    },
    {
        "label": "BRANDS\nBrand Strategy", "col": 1, "row": 1,
        "color": AGENT_COLORS["BRANDS"],
        "caps": [
            ("Market Intelligence", "Deepsights / IQVIA"),
            ("Social Listening", "Brandwatch / Synthesio"),
            ("Strategy Modeling", "ZS ZAIDYN / McKinsey Lilli"),
            ("Synthetic Research", "Digital Twins"),
        ]
    },
    {
        "label": "CRAFTS\nContent Excellence", "col": 2, "row": 1,
        "color": AGENT_COLORS["CRAFTS"],
        "caps": [
            ("MLR Review", "Veeva PromoMats + AI"),
            ("Compliance Detection", "Indegene AI"),
            ("Modular Content", "Writer.com / Adobe AEM"),
            ("Content Testing", "Optimizely / VWO AI"),
        ]
    },
    {
        "label": "SPARK\nCustomer Engagement", "col": 0, "row": 0,
        "color": AGENT_COLORS["SPARK"],
        "caps": [
            ("Next-Best-Action", "Aktana / PharmaForceIQ"),
            ("CRM & HCP Journeys", "Veeva Vault CRM AI"),
            ("Patient Engagement", "Conversa Health"),
            ("Omnichannel Personalization", "Adobe Sensei"),
        ]
    },
    {
        "label": "ACCESS\nMarket Access", "col": 1, "row": 0,
        "color": AGENT_COLORS["ACCESS"],
        "caps": [
            ("Competitive Intelligence", "IQVIA Market Edge AI"),
            ("HTA & Value Dossier", "ZS ZAIDYN Access"),
            ("Patient Support Programs", "ConnectiveRx AI"),
            ("Regulatory Compliance", "RegASK / Veripharm"),
        ]
    },
    {
        "label": "SHARED PLATFORM\n& DATA LAYER", "col": 2, "row": 0,
        "color": AGENT_COLORS["PLATFORM"],
        "caps": [
            ("Data & Analytics", "Salesforce Einstein / IQVIA"),
            ("CRM Foundation", "Salesforce LS Cloud / Veeva"),
            ("Content Management", "Adobe Experience Manager"),
            ("Identity & Integration", "Abbott IAM / MuleSoft"),
        ]
    },
]

COLS = 3
ROWS = 2
CELL_W = 26 / COLS
CELL_H = 14.5 / ROWS
PAD = 0.3
CAP_GAP = 0.08

for d in domains:
    col, row = d["col"], d["row"]
    cx = col * CELL_W + PAD
    cy = row * CELL_H + PAD + 0.5
    cw = CELL_W - 2 * PAD
    ch = CELL_H - 2 * PAD

    # Domain background
    bg = FancyBboxPatch((cx, cy), cw, ch, boxstyle="round,pad=0.08",
                        facecolor=d["color"]["bg"], edgecolor=d["color"]["border"], linewidth=2)
    ax2.add_patch(bg)

    # Domain label
    ax2.text(cx + cw/2, cy + ch - 0.35, d["label"],
             ha='center', va='center', fontsize=11, fontweight='bold',
             color=d["color"]["text"], multialignment='center')

    # Capability + tool boxes in 2x2 grid
    caps = d["caps"]
    n_cols = 2
    n_rows = 2
    cap_w = (cw - 0.2 - CAP_GAP) / n_cols
    cap_h = (ch - 0.9 - CAP_GAP) / n_rows

    for i, (cap_name, tool) in enumerate(caps):
        r = i // n_cols
        c = i % n_cols
        bx = cx + 0.1 + c * (cap_w + CAP_GAP)
        by = cy + 0.1 + (n_rows - 1 - r) * (cap_h + CAP_GAP)
        rounded_box(ax2, bx, by, cap_w, cap_h, WHITE, d["color"]["border"],
                    f"{cap_name}\n{tool}", fontsize=8.5, text_color=NEAR_BLACK)

plt.tight_layout(pad=0.3)
plt.savefig("marketing-capability-domain.png", dpi=180, bbox_inches='tight', facecolor='#F8F9FA')
plt.savefig("marketing-capability-domain.svg", bbox_inches='tight', facecolor='#F8F9FA')
plt.close()
print("Domain diagram saved.")


# ═══════════════════════════════════════════════════════════
# DIAGRAM 3: TARGET ARCHITECTURE — Agent connections + tools
# ═══════════════════════════════════════════════════════════
fig3, ax3 = plt.subplots(figsize=(26, 18))
ax3.set_xlim(0, 26)
ax3.set_ylim(0, 18)
ax3.axis('off')
fig3.patch.set_facecolor('#F8F9FA')

ax3.text(13, 17.5, "EPD Marketer of the Future — Target Architecture",
         ha='center', va='center', fontsize=15, fontweight='bold', color=NAVY)
ax3.text(13, 17.0, "How the Five Agents Connect with Platforms, Tools, and Data",
         ha='center', va='center', fontsize=11, color=LIGHT_GRAY)

# ── Row layout ──────────────────────────────────────────────
# Row 1 (top): BRANDS (center top, strategy feeds all)
# Row 2: ALICE | CRAFTS | SPARK
# Row 3: ACCESS
# Row 4: Shared Data & Platform Layer
# Arrows connect agents to each other and to tools

def agent_box(ax, cx, cy, w, h, name, subtitle, tools, color_key):
    c = AGENT_COLORS[color_key]
    bg = FancyBboxPatch((cx - w/2, cy - h/2), w, h, boxstyle="round,pad=0.05",
                        facecolor=c["bg"], edgecolor=c["border"], linewidth=2)
    ax.add_patch(bg)
    ax.text(cx, cy + h/2 - 0.35, name, ha='center', va='center',
            fontsize=11, fontweight='bold', color=c["text"])
    ax.text(cx, cy + h/2 - 0.7, subtitle, ha='center', va='center',
            fontsize=8, color=c["text"], style='italic')

    # Tools as sub-boxes
    n = len(tools)
    tool_w = (w - 0.3) / n - 0.05
    tool_h = 0.65
    for i, (tool_name, tool_class) in enumerate(tools):
        tx = cx - w/2 + 0.15 + i * (tool_w + 0.05)
        ty = cy - h/2 + 0.12
        tool_bg = FancyBboxPatch((tx, ty), tool_w, tool_h, boxstyle="round,pad=0.01",
                                 facecolor=WHITE, edgecolor=c["border"], linewidth=0.8)
        ax.add_patch(tool_bg)
        ax.text(tx + tool_w/2, ty + tool_h/2 + 0.08, tool_name,
                ha='center', va='center', fontsize=7, color=NEAR_BLACK, fontweight='bold',
                multialignment='center')
        ax.text(tx + tool_w/2, ty + 0.12, tool_class,
                ha='center', va='center', fontsize=6.5, color=LIGHT_GRAY,
                multialignment='center', style='italic')
    return (cx, cy)

def arrow(ax, x1, y1, x2, y2, label="", color="#666666"):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.5))
    if label:
        mx, my = (x1+x2)/2, (y1+y2)/2
        ax.text(mx + 0.1, my, label, ha='left', va='center', fontsize=7.5,
                color=color, style='italic',
                bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor='none', alpha=0.8))

# ── Agent positions ──────────────────────────────────────────
AW = 7.5   # agent box width
AH = 2.0   # agent box height

# BRANDS — center top
brands_pos = agent_box(ax3, 13, 14.5, AW, AH, "BRANDS", "Brand Strategy Planning System",
    [("Deepsights", "Market Leader"), ("Brandwatch", "Market Leader"),
     ("ZS ZAIDYN", "Emerging"), ("Salesforce Einstein", "Core")],
    "BRANDS")

# ALICE — left mid
alice_pos = agent_box(ax3, 5, 11.0, AW, AH, "ALICE", "Creative Excellence",
    [("Adobe Firefly", "Market Leader"), ("Persado", "Market Leader"),
     ("Writer.com", "Market Leader"), ("Workfront", "Core")],
    "ALICE")

# CRAFTS — center mid
crafts_pos = agent_box(ax3, 13, 11.0, AW, AH, "CRAFTS", "Content Lifecycle Management",
    [("Veeva PromoMats AI", "MLR-Critical"), ("Indegene AI", "MLR-Critical"),
     ("Adobe AEM", "Market Leader"), ("Optimizely", "Core")],
    "CRAFTS")

# SPARK — right mid
spark_pos = agent_box(ax3, 21, 11.0, AW, AH, "SPARK", "Customer Engagement",
    [("Aktana/PharmaForceIQ", "Market Leader"), ("Veeva CRM AI", "Market Leader"),
     ("Conversa Health", "Emerging"), ("Adobe Sensei", "Core")],
    "SPARK")

# ACCESS — center lower
access_pos = agent_box(ax3, 13, 7.5, AW, AH, "ACCESS", "Market Access",
    [("IQVIA Market Edge", "Market Leader"), ("ZS ZAIDYN Access", "Emerging"),
     ("ConnectiveRx AI", "Market Leader"), ("RegASK", "MLR-Critical")],
    "ACCESS")

# ── Shared Platform Layer ────────────────────────────────────
plat_y = 4.8
plat_h = 2.0
plat_box = FancyBboxPatch((0.4, plat_y - plat_h/2), 25.2, plat_h,
                           boxstyle="round,pad=0.06",
                           facecolor=AGENT_COLORS["PLATFORM"]["bg"],
                           edgecolor=AGENT_COLORS["PLATFORM"]["border"], linewidth=2)
ax3.add_patch(plat_box)
ax3.text(13, plat_y + plat_h/2 - 0.3, "SHARED DATA & PLATFORM LAYER",
         ha='center', va='center', fontsize=11, fontweight='bold',
         color=AGENT_COLORS["PLATFORM"]["text"])

plat_items = [
    ("Salesforce LS Cloud\n/ Veeva CRM", "CRM Foundation"),
    ("Adobe Experience\nManager", "Content Mgmt"),
    ("IQVIA / Salesforce\nEinstein", "Data & Analytics"),
    ("MuleSoft /\nAzure APIM", "Integration & API"),
    ("Abbott IAM\n/ SSO", "Identity & Access"),
    ("Veeva Vault\n/ Audit Platform", "Compliance & Audit"),
]
n_plat = len(plat_items)
plat_item_w = (25.2 - 0.4) / n_plat - 0.1
for i, (name, label) in enumerate(plat_items):
    px = 0.6 + i * (plat_item_w + 0.1)
    py = plat_y - plat_h/2 + 0.15
    pb = FancyBboxPatch((px, py), plat_item_w, plat_h - 0.45,
                        boxstyle="round,pad=0.01",
                        facecolor=WHITE, edgecolor=AGENT_COLORS["PLATFORM"]["border"], linewidth=0.8)
    ax3.add_patch(pb)
    ax3.text(px + plat_item_w/2, py + (plat_h - 0.45)/2 + 0.08, name,
             ha='center', va='center', fontsize=8, color=NEAR_BLACK, fontweight='bold',
             multialignment='center')
    ax3.text(px + plat_item_w/2, py + 0.14, label,
             ha='center', va='center', fontsize=7, color=LIGHT_GRAY, style='italic')

# ── Arrows: agent-to-agent flows ────────────────────────────
col = "#555599"
# BRANDS → ALICE (strategy feeds creative)
arrow(ax3, 13 - AW/2, 14.5, 5 + AW/2, 11 + AH/2 - 0.2, "Strategy & Brand Voice", col)
# BRANDS → CRAFTS
arrow(ax3, 13, 14.5 - AH/2, 13, 11 + AH/2, "Brand Guidelines", col)
# BRANDS → SPARK
arrow(ax3, 13 + AW/2, 14.5, 21 - AW/2, 11 + AH/2 - 0.2, "Audience Segments", col)
# ALICE → CRAFTS (assets feed content)
arrow(ax3, 5 + AW/2, 11, 13 - AW/2, 11, "Creative Assets", col)
# CRAFTS → SPARK (approved content feeds engagement)
arrow(ax3, 13 + AW/2, 11, 21 - AW/2, 11, "Approved Content", col)
# SPARK → ACCESS (engagement signals feed market access)
arrow(ax3, 21, 11 - AH/2, 13 + AW/2 - 0.5, 7.5 + AH/2, "Engagement Signals", col)
# CRAFTS → ACCESS
arrow(ax3, 13, 11 - AH/2, 13, 7.5 + AH/2, "Compliance Docs", col)
# All agents → Platform
arrow(ax3, 13, 7.5 - AH/2, 13, plat_y + plat_h/2, "Data Exchange", AGENT_COLORS["PLATFORM"]["border"])

# ── Legend ───────────────────────────────────────────────────
legend_items = [
    ("Market Leader", "#C05000"), ("Core Enablement", "#0277BD"),
    ("Emerging", "#7B1FA2"), ("MLR-Critical", "#C62828"),
]
lx, ly = 0.5, 2.8
ax3.text(lx, ly + 0.2, "Tool Classification:", fontsize=9, fontweight='bold', color=NAVY)
for i, (label, col2) in enumerate(legend_items):
    rect = FancyBboxPatch((lx + i * 3.5, ly - 0.35), 3.2, 0.4,
                          boxstyle="round,pad=0.02", facecolor=WHITE,
                          edgecolor=col2, linewidth=1.5)
    ax3.add_patch(rect)
    ax3.text(lx + i * 3.5 + 1.6, ly - 0.15, label,
             ha='center', va='center', fontsize=8, color=col2, fontweight='bold')

plt.tight_layout(pad=0.3)
plt.savefig("marketing-target-architecture.png", dpi=180, bbox_inches='tight', facecolor='#F8F9FA')
plt.savefig("marketing-target-architecture.svg", bbox_inches='tight', facecolor='#F8F9FA')
plt.close()
print("Target architecture diagram saved.")
print("\nAll diagrams complete.")
