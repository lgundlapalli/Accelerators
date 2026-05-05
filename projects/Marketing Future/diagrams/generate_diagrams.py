import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# ── Colors ─────────────────────────────────────────────────
NAVY       = "#000050"
WHITE      = "#FFFFFF"
NEAR_BLACK = "#1A1A1A"
LIGHT_GRAY = "#AAAAAA"

AGENTS = {
    "ALICE":    {"bg": "#FFE8D6", "border": "#C05000", "text": "#7A3000"},
    "BRANDS":   {"bg": "#D6E8FF", "border": "#003087", "text": "#003087"},
    "CRAFTS":   {"bg": "#E8F4E8", "border": "#1A7A1A", "text": "#1A5C1A"},
    "SPARK":    {"bg": "#F3E5F5", "border": "#7B1FA2", "text": "#5C0E7A"},
    "ACCESS":   {"bg": "#FFF3E0", "border": "#B35A00", "text": "#7A3E00"},
    "PLATFORM": {"bg": "#E3F2FD", "border": "#0277BD", "text": "#01579B"},
    "CURRENT":  {"bg": "#F5F5F5", "border": "#888888", "text": "#333333"},
}

STATUS_COLOR = {
    "✓":  "#1A7A1A",   # green  = POC Proceeding
    "◐":  "#B35A00",   # amber  = POC In Progress
    "⏸":  "#888888",   # gray   = On Hold
    "⚠":  "#C62828",   # red    = MLR Critical
    "→":  "#003087",   # navy   = Future Target
}

def cap_box(ax, x, y, w, h, title, subtitle, status_icon="→",
            bg=WHITE, border=NEAR_BLACK, fontsize=8.5):
    sc = STATUS_COLOR.get(status_icon, NEAR_BLACK)
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02",
                         facecolor=bg, edgecolor=border, linewidth=0.9)
    ax.add_patch(box)
    # Status dot
    ax.text(x + 0.12, y + h - 0.22, status_icon, fontsize=9,
            color=sc, va='center', ha='center', fontweight='bold')
    # Title
    ax.text(x + w/2, y + h/2 + 0.1, title, ha='center', va='center',
            fontsize=fontsize, color=NEAR_BLACK, fontweight='bold',
            multialignment='center', linespacing=1.2)
    # Subtitle (tool name)
    ax.text(x + w/2, y + 0.22, subtitle, ha='center', va='center',
            fontsize=7.5, color="#555555", style='italic',
            multialignment='center')

def section_bg(ax, x, y, w, h, label, color_key):
    c = AGENTS[color_key]
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05",
                         facecolor=c["bg"], edgecolor=c["border"], linewidth=2)
    ax.add_patch(box)
    ax.text(x + 0.15, y + h - 0.28, label, ha='left', va='center',
            fontsize=10, fontweight='bold', color=c["text"])


# ═══════════════════════════════════════════════════════════
# DIAGRAM 1 — LAYERED ARCHITECTURE (Current + Future)
# ═══════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(26, 17))
ax.set_xlim(0, 26); ax.set_ylim(0, 17)
ax.axis('off'); fig.patch.set_facecolor('#F8F9FA')

ax.text(13, 16.6, "EPD Marketer of the Future — Capability Map (Architecture Layers)",
        ha='center', fontsize=14, fontweight='bold', color=NAVY)
ax.text(13, 16.2, "Current state tools (Abbott evaluation) + Future target tools per agent",
        ha='center', fontsize=10, color=LIGHT_GRAY)

# Legend
legend = [("✓ POC Proceeding","#1A7A1A"), ("◐ POC In Progress","#B35A00"),
          ("⏸ On Hold","#888888"), ("⚠ MLR Critical","#C62828"), ("→ Future Target","#003087")]
for i, (lbl, col) in enumerate(legend):
    ax.text(0.4 + i*5.1, 15.75, lbl, fontsize=8.5, color=col, fontweight='bold')

layers = [
    {
        "key": "BRANDS", "label": "BRANDS — Brand Strategy",
        "y": 13.5, "h": 1.7,
        "caps": [
            ("Market Intelligence",   "Neuron AI / Deepsights",        "◐"),
            ("Social Listening",       "Sprinklr → Brandwatch",         "⏸"),
            ("Strategy Modeling",      "RightSpend → ZS ZAIDYN",        "⏸"),
            ("Synthetic Research",     "Digital Twins (Future)",         "→"),
        ]
    },
    {
        "key": "ALICE", "label": "ALICE — Creative Excellence",
        "y": 11.3, "h": 1.7,
        "caps": [
            ("Creative Generation",   "Adobe Express → Firefly",        "✓"),
            ("Brief Intelligence",     "None → Persado",                "→"),
            ("Copy & Claim Gen",       "Writer AI → Writer.com Ent.",   "◐"),
            ("Creative Ops",           "Dynamic Media → Workfront",     "✓"),
        ]
    },
    {
        "key": "CRAFTS", "label": "CRAFTS — Content & MLR",
        "y": 9.1, "h": 1.7,
        "caps": [
            ("MLR Review",             "None → Veeva PromoMats AI",     "⚠"),
            ("Compliance Detection",   "None → Indegene AI",            "⚠"),
            ("Modular Content",        "Writer AI → Adobe AEM+Firefly", "◐"),
            ("Content Testing",        "DragonFly → Optimizely",        "⏸"),
        ]
    },
    {
        "key": "SPARK", "label": "SPARK — Customer Engagement",
        "y": 6.9, "h": 1.7,
        "caps": [
            ("Next-Best-Action",       "None → Aktana/PharmaForceIQ",   "→"),
            ("CRM & HCP Journeys",     "Salesforce Einstein Mktg Cld",  "◐"),
            ("Patient Engagement",     "Five9 → Conversa Health",       "◐"),
            ("Omnichannel Personaliz.","Salesforce → Adobe Sensei",     "◐"),
        ]
    },
    {
        "key": "ACCESS", "label": "ACCESS — Market Access",
        "y": 4.7, "h": 1.7,
        "caps": [
            ("Competitive Intel",      "None → IQVIA Market Edge AI",   "→"),
            ("HTA & Value Dossier",    "None → ZS ZAIDYN Access",       "→"),
            ("Patient Support Pgms",   "None → ConnectiveRx AI",        "→"),
            ("Regulatory Compliance",  "None → RegASK / Veripharm",     "⚠"),
        ]
    },
    {
        "key": "PLATFORM", "label": "SHARED DATA & PLATFORM LAYER — Abbott GenAI Foundation",
        "y": 1.5, "h": 2.7,
        "caps": [
            ("CRM Foundation",         "Salesforce LS Cloud / Veeva",   "✓"),
            ("Content Mgmt",           "Adobe Experience Manager",      "✓"),
            ("Data Unification",       "Salesforce Data Cloud",         "◐"),
            ("GenAI Platform",         "Azure AI Foundry",              "✓"),
            ("Enterprise LLM",         "Anthropic Claude",              "✓"),
            ("Integration & API",      "MuleSoft / Azure APIM",         "✓"),
        ]
    },
]

LABEL_W = 2.4
LEFT    = 0.25
TOTAL_W = 25.5
CAP_AREA = TOTAL_W - LABEL_W - 0.15
GAP = 0.12

for layer in layers:
    y, h = layer["y"], layer["h"]
    caps = layer["caps"]
    n = len(caps)
    cap_w = (CAP_AREA - (n - 1) * GAP) / n

    section_bg(ax, LEFT, y, TOTAL_W, h, layer["label"], layer["key"])

    for i, (title, subtitle, status) in enumerate(caps):
        bx = LEFT + LABEL_W + i * (cap_w + GAP)
        cap_box(ax, bx, y + 0.18, cap_w, h - 0.35,
                title, subtitle, status,
                bg=WHITE, border=AGENTS[layer["key"]]["border"])

plt.tight_layout(pad=0.3)
plt.savefig("layered.svg", bbox_inches='tight', facecolor='#F8F9FA')
plt.savefig("layered.png", dpi=180, bbox_inches='tight', facecolor='#F8F9FA')
plt.close()
print("Layered saved.")


# ═══════════════════════════════════════════════════════════
# DIAGRAM 2 — DOMAIN VIEW (3×2 grid)
# ═══════════════════════════════════════════════════════════
fig2, ax2 = plt.subplots(figsize=(26, 17))
ax2.set_xlim(0, 26); ax2.set_ylim(0, 17)
ax2.axis('off'); fig2.patch.set_facecolor('#F8F9FA')

ax2.text(13, 16.6, "EPD Marketer of the Future — Business Capability Map (Domain View)",
         ha='center', fontsize=14, fontweight='bold', color=NAVY)
ax2.text(13, 16.2, "Current state tools (Abbott evaluation) + Future target tools per domain",
         ha='center', fontsize=10, color=LIGHT_GRAY)

for i, (lbl, col) in enumerate(legend):
    ax2.text(0.4 + i*5.1, 15.75, lbl, fontsize=8.5, color=col, fontweight='bold')

domains = [
    {
        "key": "BRANDS", "label": "BRANDS\nBrand Strategy",
        "col": 0, "row": 1,
        "caps": [
            ("Market Intelligence",   "Neuron AI → Deepsights",        "◐"),
            ("Social Listening",       "Sprinklr → Brandwatch",         "⏸"),
            ("Strategy Modeling",      "RightSpend → ZS ZAIDYN",        "⏸"),
            ("Synthetic Research",     "None → Digital Twins",          "→"),
        ]
    },
    {
        "key": "ALICE", "label": "ALICE\nCreative Excellence",
        "col": 1, "row": 1,
        "caps": [
            ("Creative Generation",   "Adobe Express → Adobe Firefly",  "✓"),
            ("Brief Intelligence",     "None → Persado",                "→"),
            ("Copy & Claim Gen",       "Writer AI → Writer.com Ent.",   "◐"),
            ("Creative Ops",           "Dynamic Media → Workfront",     "✓"),
        ]
    },
    {
        "key": "CRAFTS", "label": "CRAFTS\nContent & MLR",
        "col": 2, "row": 1,
        "caps": [
            ("MLR Review",             "None → Veeva PromoMats AI",     "⚠"),
            ("Compliance Detection",   "None → Indegene AI",            "⚠"),
            ("Modular Content",        "Writer AI → Adobe AEM+Firefly", "◐"),
            ("Content Testing",        "DragonFly → Optimizely",        "⏸"),
        ]
    },
    {
        "key": "SPARK", "label": "SPARK\nCustomer Engagement",
        "col": 0, "row": 0,
        "caps": [
            ("Next-Best-Action",       "None → Aktana/PharmaForceIQ",   "→"),
            ("CRM & HCP Journeys",     "Salesforce Einstein Mktg Cld",  "◐"),
            ("Patient Engagement",     "Five9 → Conversa Health",       "◐"),
            ("Personalization",        "Salesforce → Adobe Sensei",     "◐"),
        ]
    },
    {
        "key": "ACCESS", "label": "ACCESS\nMarket Access",
        "col": 1, "row": 0,
        "caps": [
            ("Competitive Intel",      "None → IQVIA Market Edge AI",   "→"),
            ("HTA & Value Dossier",    "None → ZS ZAIDYN Access",       "→"),
            ("Patient Support",        "None → ConnectiveRx AI",        "→"),
            ("Regulatory Compliance",  "None → RegASK / Veripharm",     "⚠"),
        ]
    },
    {
        "key": "PLATFORM", "label": "PLATFORM\nAbbott GenAI Foundation",
        "col": 2, "row": 0,
        "caps": [
            ("CRM Foundation",         "Salesforce LS Cloud / Veeva",   "✓"),
            ("Content Mgmt",           "Adobe Experience Manager",      "✓"),
            ("GenAI Platform",         "Azure AI Foundry",              "✓"),
            ("Enterprise LLM",         "Anthropic Claude",              "✓"),
        ]
    },
]

COLS, ROWS = 3, 2
CELL_W = 26 / COLS
CELL_H = 14.5 / ROWS
PAD, GAP2 = 0.25, 0.1

for d in domains:
    col, row = d["col"], d["row"]
    cx = col * CELL_W + PAD
    cy = row * CELL_H + PAD + 0.8
    cw = CELL_W - 2*PAD
    ch = CELL_H - 2*PAD

    section_bg(ax2, cx, cy, cw, ch, d["label"], d["key"])

    caps = d["caps"]
    nc = 2; nr = int(np.ceil(len(caps)/nc))
    cap_w2 = (cw - 0.2 - GAP2) / nc
    cap_h2 = (ch - 0.85 - GAP2) / nr

    for i, (title, subtitle, status) in enumerate(caps):
        r = i // nc; c2 = i % nc
        bx = cx + 0.1 + c2*(cap_w2+GAP2)
        by = cy + 0.1 + (nr-1-r)*(cap_h2+GAP2)
        cap_box(ax2, bx, by, cap_w2, cap_h2, title, subtitle, status,
                bg=WHITE, border=AGENTS[d["key"]]["border"])

plt.tight_layout(pad=0.3)
plt.savefig("domain.svg", bbox_inches='tight', facecolor='#F8F9FA')
plt.savefig("domain.png", dpi=180, bbox_inches='tight', facecolor='#F8F9FA')
plt.close()
print("Domain saved.")


# ═══════════════════════════════════════════════════════════
# DIAGRAM 3 — TARGET ARCHITECTURE (agent flow + tools)
# ═══════════════════════════════════════════════════════════
fig3, ax3 = plt.subplots(figsize=(28, 20))
ax3.set_xlim(0, 28); ax3.set_ylim(0, 20)
ax3.axis('off'); fig3.patch.set_facecolor('#F8F9FA')

ax3.text(14, 19.6, "EPD Marketer of the Future — Target Architecture",
         ha='center', fontsize=15, fontweight='bold', color=NAVY)
ax3.text(14, 19.1, "How the Five Agents connect with platforms, tools, and data | Current → Future state",
         ha='center', fontsize=10, color=LIGHT_GRAY)

for i, (lbl, col) in enumerate(legend):
    ax3.text(0.4 + i*5.5, 18.7, lbl, fontsize=8.5, color=col, fontweight='bold')

def agent_block(ax, cx, cy, w, h, agent_key, agent_label, tools):
    """Draw an agent block with tool chips inside."""
    c = AGENTS[agent_key]
    box = FancyBboxPatch((cx-w/2, cy-h/2), w, h, boxstyle="round,pad=0.06",
                         facecolor=c["bg"], edgecolor=c["border"], linewidth=2.2)
    ax.add_patch(box)
    ax.text(cx, cy+h/2-0.38, agent_label, ha='center', va='center',
            fontsize=11, fontweight='bold', color=c["text"])

    n = len(tools)
    tw = (w - 0.3) / n - 0.08
    th = 0.75
    for i, (tname, tclass, tstatus) in enumerate(tools):
        tx = cx - w/2 + 0.15 + i*(tw+0.08)
        ty = cy - h/2 + 0.12
        sc = STATUS_COLOR.get(tstatus, NEAR_BLACK)
        tb = FancyBboxPatch((tx, ty), tw, th, boxstyle="round,pad=0.01",
                            facecolor=WHITE, edgecolor=c["border"], linewidth=0.8)
        ax.add_patch(tb)
        ax.text(tx+tw/2, ty+th/2+0.1, tname, ha='center', va='center',
                fontsize=7.5, color=NEAR_BLACK, fontweight='bold', multialignment='center')
        ax.text(tx+tw/2, ty+0.13, tclass, ha='center', va='center',
                fontsize=7, color=sc, style='italic')
    return (cx, cy)

def arrow(ax, x1, y1, x2, y2, label="", color="#666699"):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.8,
                                connectionstyle="arc3,rad=0.0"))
    if label:
        mx, my = (x1+x2)/2, (y1+y2)/2
        ax.text(mx+0.1, my+0.1, label, fontsize=8, color=color, style='italic',
                bbox=dict(boxstyle='round,pad=0.15', facecolor='white',
                          edgecolor='none', alpha=0.9))

AW, AH = 8.5, 2.1

# CURRENT STATE box (top left)
cs_x, cs_y = 5, 17.2
cs_w, cs_h = 10, 1.3
box = FancyBboxPatch((cs_x-cs_w/2, cs_y-cs_h/2), cs_w, cs_h,
                     boxstyle="round,pad=0.04", facecolor="#F5F5F5",
                     edgecolor="#888888", linewidth=1.5, linestyle='dashed')
ax3.add_patch(box)
ax3.text(cs_x, cs_y+cs_h/2-0.28, "CURRENT STATE — Abbott Tools In Evaluation",
         ha='center', fontsize=9, fontweight='bold', color="#444444")
current_tools = [
    ("Adobe Express ✓","POC Proceeding","✓"),
    ("Writer AI ◐","EPD POC","◐"),
    ("Dynamic Media ✓","POC Proceeding","✓"),
    ("Salesforce Einstein ◐","Mktg Cloud","◐"),
    ("Neuron AI ◐","POC Progress","◐"),
    ("Five9 ◐","POC To Start","◐"),
    ("Sprinklr ⏸","On Hold","⏸"),
    ("Azure AI Foundry","Enterprise","✓"),
]
n_ct = len(current_tools)
ct_w = (cs_w - 0.3) / n_ct - 0.06
ct_h = 0.55
for i, (tn, tc, ts) in enumerate(current_tools):
    tx = cs_x - cs_w/2 + 0.15 + i*(ct_w+0.06)
    ty = cs_y - cs_h/2 + 0.08
    sc = STATUS_COLOR.get(ts, NEAR_BLACK)
    tb = FancyBboxPatch((tx, ty), ct_w, ct_h, boxstyle="round,pad=0.01",
                        facecolor=WHITE, edgecolor="#888888", linewidth=0.7)
    ax3.add_patch(tb)
    ax3.text(tx+ct_w/2, ty+ct_h/2+0.08, tn, ha='center', va='center',
             fontsize=7, color=NEAR_BLACK, fontweight='bold', multialignment='center')
    ax3.text(tx+ct_w/2, ty+0.1, tc, ha='center', va='center',
             fontsize=6.5, color=sc, style='italic')

# BRANDS (top center)
agent_block(ax3, 14, 14.8, AW, AH, "BRANDS", "BRANDS — Brand Strategy", [
    ("Deepsights","Market Leader","→"),
    ("Brandwatch","Market Leader","→"),
    ("ZS ZAIDYN","Emerging","→"),
    ("Salesforce Einstein","Core","◐"),
])

# ALICE (left mid)
agent_block(ax3, 5, 11.5, AW, AH, "ALICE", "ALICE — Creative Excellence", [
    ("Adobe Firefly","Market Leader","→"),
    ("Persado","Market Leader","→"),
    ("Writer.com","Market Leader","◐"),
    ("Workfront","Core","→"),
])

# CRAFTS (center mid)
agent_block(ax3, 14, 11.5, AW, AH, "CRAFTS", "CRAFTS — Content & MLR", [
    ("Veeva PromoMats AI","MLR-Critical","⚠"),
    ("Indegene AI","MLR-Critical","⚠"),
    ("Adobe AEM + Firefly","Market Leader","→"),
    ("Optimizely","Core","→"),
])

# SPARK (right mid)
agent_block(ax3, 23, 11.5, AW, AH, "SPARK", "SPARK — Customer Engagement", [
    ("Aktana/PharmaForceIQ","Market Leader","→"),
    ("Veeva CRM AI","Market Leader","→"),
    ("Conversa Health","Emerging","→"),
    ("Adobe Sensei","Core","◐"),
])

# ACCESS (center lower)
agent_block(ax3, 14, 8.2, AW, AH, "ACCESS", "ACCESS — Market Access", [
    ("IQVIA Market Edge AI","Market Leader","→"),
    ("ZS ZAIDYN Access","Emerging","→"),
    ("ConnectiveRx AI","Market Leader","→"),
    ("RegASK / Veripharm","MLR-Critical","⚠"),
])

# PLATFORM (bottom bar)
plat_y = 5.2
plat_h = 2.2
box2 = FancyBboxPatch((0.4, plat_y-plat_h/2), 27.2, plat_h,
                      boxstyle="round,pad=0.06",
                      facecolor=AGENTS["PLATFORM"]["bg"],
                      edgecolor=AGENTS["PLATFORM"]["border"], linewidth=2)
ax3.add_patch(box2)
ax3.text(14, plat_y+plat_h/2-0.3, "SHARED DATA & PLATFORM LAYER — Abbott GenAI Foundation",
         ha='center', fontsize=11, fontweight='bold', color=AGENTS["PLATFORM"]["text"])

plat_items = [
    ("Salesforce LS Cloud\n/ Veeva CRM","CRM Foundation","✓"),
    ("Adobe Experience\nManager","Content Mgmt","✓"),
    ("Salesforce Data Cloud","Data Unification","◐"),
    ("Azure AI Foundry","GenAI Platform","✓"),
    ("Anthropic Claude","Enterprise LLM","✓"),
    ("MuleSoft / Azure APIM","Integration & API","✓"),
    ("Abbott IAM / SSO","Identity & Access","✓"),
    ("Veeva Vault","Compliance & Audit","→"),
]
n_p = len(plat_items)
pi_w = (27.2 - 0.4) / n_p - 0.1
pi_h = plat_h - 0.6
for i, (tn, tc, ts) in enumerate(plat_items):
    px = 0.6 + i*(pi_w+0.1)
    py = plat_y - plat_h/2 + 0.15
    sc = STATUS_COLOR.get(ts, NEAR_BLACK)
    pb = FancyBboxPatch((px, py), pi_w, pi_h, boxstyle="round,pad=0.01",
                        facecolor=WHITE, edgecolor=AGENTS["PLATFORM"]["border"], linewidth=0.8)
    ax3.add_patch(pb)
    ax3.text(px+pi_w/2, py+pi_h/2+0.1, tn, ha='center', va='center',
             fontsize=8, color=NEAR_BLACK, fontweight='bold', multialignment='center')
    ax3.text(px+pi_w/2, py+0.15, tc, ha='center', va='center',
             fontsize=7, color=sc, style='italic')

# Arrows
col_arr = "#555599"
arrow(ax3, 5, 17.2-0.65, 14-AW/2, 14.8, "Evolves to Future State", "#888888")
arrow(ax3, 14-AW/2, 14.8, 5+AW/2, 11.5+AH/2-0.2, "Strategy & Brand Voice", col_arr)
arrow(ax3, 14, 14.8-AH/2, 14, 11.5+AH/2, "Brand Guidelines", col_arr)
arrow(ax3, 14+AW/2, 14.8, 23-AW/2, 11.5+AH/2-0.2, "Audience Segments", col_arr)
arrow(ax3, 5+AW/2, 11.5, 14-AW/2, 11.5, "Creative Assets", col_arr)
arrow(ax3, 14+AW/2, 11.5, 23-AW/2, 11.5, "Approved Content", col_arr)
arrow(ax3, 23, 11.5-AH/2, 14+AW/2-0.5, 8.2+AH/2, "Engagement Signals", col_arr)
arrow(ax3, 14, 11.5-AH/2, 14, 8.2+AH/2, "Compliance Docs", col_arr)
arrow(ax3, 14, 8.2-AH/2, 14, plat_y+plat_h/2, "Data Exchange", AGENTS["PLATFORM"]["border"])

# Legend box
leg_items = [
    ("Market Leader","#C05000"), ("Core Enablement","#0277BD"),
    ("Emerging","#7B1FA2"), ("MLR-Critical","#C62828"),
]
ax3.text(0.4, 3.0, "Tool Classification:", fontsize=9, fontweight='bold', color=NAVY)
for i, (lbl2, col2) in enumerate(leg_items):
    rb = FancyBboxPatch((0.4+i*4.5, 2.4), 4.2, 0.45,
                        boxstyle="round,pad=0.02", facecolor=WHITE,
                        edgecolor=col2, linewidth=1.5)
    ax3.add_patch(rb)
    ax3.text(0.4+i*4.5+2.1, 2.62, lbl2, ha='center', va='center',
             fontsize=8.5, color=col2, fontweight='bold')

plt.tight_layout(pad=0.3)
plt.savefig("target-architecture.svg", bbox_inches='tight', facecolor='#F8F9FA')
plt.savefig("target-architecture.png", dpi=180, bbox_inches='tight', facecolor='#F8F9FA')
plt.close()
print("Target architecture saved.")
print("\nAll 3 diagrams complete.")
