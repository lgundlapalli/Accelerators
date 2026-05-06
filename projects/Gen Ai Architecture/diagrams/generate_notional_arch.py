import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import numpy as np
import xml.etree.ElementTree as ET

NAVY       = "#000050"
WHITE      = "#FFFFFF"
NEAR_BLACK = "#1A1A1A"
LIGHT_GRAY = "#AAAAAA"

# ── Domain colors ──────────────────────────────────────────
DOMAINS = [
    {
        "id": "content",
        "label": "Content &\nCreative Studio",
        "maturity": "Scaling",
        "mat_col": "#1A7A1A",
        "usecases": "8 prod · 12 WIP",
        "tools": "Writer · Adobe\nFirefly · AutogenAI",
        "divisions": "ADC · Corp · EPD\nGMEA · RMDx",
        "bg": "#FFE8D6", "border": "#C05000", "text": "#7A3000",
    },
    {
        "id": "insights",
        "label": "Insights &\nAnalytics",
        "maturity": "Producing",
        "mat_col": "#003087",
        "usecases": "14 prod · 9 WIP",
        "tools": "Databricks · RADIA\nMktg Insights Acc.",
        "divisions": "GMEA · AN · RMDx\nBTS · ADC · Corp",
        "bg": "#D6E8FF", "border": "#003087", "text": "#003087",
    },
    {
        "id": "productivity",
        "label": "Productivity &\nAutomation",
        "maturity": "Scaling",
        "mat_col": "#1A7A1A",
        "usecases": "10 prod · 11 WIP",
        "tools": "M365 Copilot\nCursor · Five9",
        "divisions": "BTS · Corp · CHR\nAN · MD · EPD",
        "bg": "#E8F4E8", "border": "#1A7A1A", "text": "#1A5C1A",
    },
    {
        "id": "customer",
        "label": "Customer &\nField Engagement",
        "maturity": "Producing",
        "mat_col": "#003087",
        "usecases": "12 prod · 6 WIP",
        "tools": "SmartRep · Neuron7\nVeeva CRM AI",
        "divisions": "EPD · ADC · CoreDx\nBTS · GMEA",
        "bg": "#F3E5F5", "border": "#7B1FA2", "text": "#5C0E7A",
    },
    {
        "id": "engineering",
        "label": "Engineering &\nDev Acceleration",
        "maturity": "Scaling",
        "mat_col": "#1A7A1A",
        "usecases": "6 prod · 8 WIP",
        "tools": "Cursor · Windsurf\nAtlassian AI",
        "divisions": "BTS · MD · RMDx",
        "bg": "#FFF3E0", "border": "#B35A00", "text": "#7A3E00",
    },
    {
        "id": "governance",
        "label": "Learning,\nCompliance & Gov.",
        "maturity": "Exploring",
        "mat_col": "#C62828",
        "usecases": "2 prod · 5 WIP",
        "tools": "Veeva Vault\nCustom LLM Review",
        "divisions": "CHR · Corp · RMDx\nMD · AN · Cyber",
        "bg": "#FCE4EC", "border": "#C62828", "text": "#8E0000",
    },
]

# ── Reusable AI Capabilities (middle tier) ─────────────────
AI_CAPS = [
    ("Retrieval-Augmented\nGeneration (RAG)", "#5C0E7A"),
    ("AI Agents &\nOrchestration", "#003087"),
    ("Language Model\nInference (LLM)", "#01579B"),
    ("Multi-modal\nGeneration", "#7A3000"),
    ("Predictive\nAnalytics & ML", "#003087"),
    ("Workflow &\nProcess Automation", "#1A5C1A"),
]

# ── Shared Platform ─────────────────────────────────────────
PLATFORM = [
    ("Microsoft\nM365 Copilot", "Productivity\nPlatform"),
    ("Azure AI\nFoundry", "Model & Agent\nOrchestration"),
    ("Anthropic\nClaude", "Enterprise LLM\nReasoning"),
    ("Salesforce\nEinstein AI", "CRM-native AI\n& Journeys"),
    ("Adobe\nExperience Cloud", "Creative &\nContent AI"),
    ("Databricks\nLakehouse", "Data & ML\nPlatform"),
    ("Veeva\nVault AI", "Regulated\nContent Mgmt"),
    ("AWS\nBedrock", "Multi-model\nGateway"),
]

# ── Figure ─────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(28, 22))
ax.set_xlim(0, 28)
ax.set_ylim(0, 22)
ax.axis('off')
fig.patch.set_facecolor('#F0F2F5')

# Title
ax.text(14, 21.55, "Abbott GenAI — Notional Architecture with Capabilities",
        ha='center', fontsize=16, fontweight='bold', color=NAVY)
ax.text(14, 21.1, "Three-Tier Model: Business Domains → Reusable AI Capabilities → Shared Enterprise Platform  |  220 Use Cases · 12 Divisions · 40 in Production",
        ha='center', fontsize=9.5, color="#555555")

# ── SECTION LABELS (left rail) ─────────────────────────────
def rail_label(ax, y, h, text, color):
    ax.text(0.18, y + h/2, text, ha='center', va='center',
            fontsize=8, fontweight='bold', color=color, rotation=90,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=color, alpha=0.12,
                      edgecolor=color, linewidth=1.2))

# ── TIER 1: BUSINESS DOMAINS ──────────────────────────────
TIER1_Y = 13.5
TIER1_H = 7.0
TIER1_BG = "#FAFAFA"

bg1 = FancyBboxPatch((0.3, TIER1_Y), 27.4, TIER1_H,
                     boxstyle="round,pad=0.08",
                     facecolor=TIER1_BG, edgecolor="#CCCCCC", linewidth=1.5)
ax.add_patch(bg1)
ax.text(14, TIER1_Y + TIER1_H - 0.22, "TIER 1 — BUSINESS CAPABILITY DOMAINS",
        ha='center', fontsize=10, fontweight='bold', color="#444444")

N_DOM = len(DOMAINS)
DOM_W = 27.0 / N_DOM - 0.12
DOM_H = 5.8
DOM_Y = TIER1_Y + 0.35
DOM_X_START = 0.45

for i, d in enumerate(DOMAINS):
    dx = DOM_X_START + i * (DOM_W + 0.12)
    dy = DOM_Y

    # Domain box
    box = FancyBboxPatch((dx, dy), DOM_W, DOM_H,
                         boxstyle="round,pad=0.05",
                         facecolor=d["bg"], edgecolor=d["border"], linewidth=2)
    ax.add_patch(box)

    # Domain title
    ax.text(dx + DOM_W/2, dy + DOM_H - 0.42, d["label"],
            ha='center', va='center', fontsize=9.5, fontweight='bold',
            color=d["text"], multialignment='center', linespacing=1.3)

    # Maturity badge
    mat_bg = FancyBboxPatch((dx + DOM_W/2 - 1.0, dy + DOM_H - 1.0), 2.0, 0.38,
                            boxstyle="round,pad=0.03",
                            facecolor=d["mat_col"], edgecolor="none")
    ax.add_patch(mat_bg)
    ax.text(dx + DOM_W/2, dy + DOM_H - 0.81, d["maturity"],
            ha='center', va='center', fontsize=7.5, fontweight='bold',
            color=WHITE)

    # Use case count
    ax.text(dx + DOM_W/2, dy + DOM_H - 1.3, d["usecases"],
            ha='center', va='center', fontsize=8, color="#444444",
            fontweight='bold')

    # Divider
    ax.plot([dx + 0.12, dx + DOM_W - 0.12], [dy + DOM_H - 1.55, dy + DOM_H - 1.55],
            color=d["border"], lw=0.7, alpha=0.5)

    # Tools label
    ax.text(dx + DOM_W/2, dy + DOM_H - 1.72, "Key Tools",
            ha='center', fontsize=7, color="#888888", style='italic')
    ax.text(dx + DOM_W/2, dy + DOM_H - 2.25, d["tools"],
            ha='center', va='center', fontsize=8, color=NEAR_BLACK,
            multialignment='center', linespacing=1.3)

    # Divider
    ax.plot([dx + 0.12, dx + DOM_W - 0.12], [dy + DOM_H - 2.65, dy + DOM_H - 2.65],
            color=d["border"], lw=0.7, alpha=0.5)

    # Divisions
    ax.text(dx + DOM_W/2, dy + DOM_H - 2.82, "Divisions",
            ha='center', fontsize=7, color="#888888", style='italic')
    ax.text(dx + DOM_W/2, dy + DOM_H - 3.35, d["divisions"],
            ha='center', va='center', fontsize=7.5, color="#555555",
            multialignment='center', linespacing=1.3)

# ── TIER 2: REUSABLE AI CAPABILITIES ─────────────────────
TIER2_Y = 9.5
TIER2_H = 3.3

bg2 = FancyBboxPatch((0.3, TIER2_Y), 27.4, TIER2_H,
                     boxstyle="round,pad=0.08",
                     facecolor="#EDE7F6", edgecolor="#7B1FA2", linewidth=1.8)
ax.add_patch(bg2)
ax.text(14, TIER2_Y + TIER2_H - 0.22, "TIER 2 — REUSABLE AI CAPABILITY LAYER",
        ha='center', fontsize=10, fontweight='bold', color="#5C0E7A")
ax.text(14, TIER2_Y + TIER2_H - 0.5, "Shared capabilities consumed by all business domains",
        ha='center', fontsize=8.5, color="#7B1FA2", style='italic')

N_CAPS = len(AI_CAPS)
CAP_W = 27.0 / N_CAPS - 0.14
CAP_H = 2.1
CAP_Y = TIER2_Y + 0.32
CAP_X_START = 0.45

for i, (cap_name, cap_col) in enumerate(AI_CAPS):
    cx = CAP_X_START + i * (CAP_W + 0.14)
    cy = CAP_Y
    cap_box = FancyBboxPatch((cx, cy), CAP_W, CAP_H,
                             boxstyle="round,pad=0.04",
                             facecolor=WHITE, edgecolor=cap_col, linewidth=1.5)
    ax.add_patch(cap_box)
    ax.text(cx + CAP_W/2, cy + CAP_H/2, cap_name,
            ha='center', va='center', fontsize=8.5, fontweight='bold',
            color=cap_col, multialignment='center', linespacing=1.35)

# ── CoE GOVERNANCE BAND (vertical) ──────────────────────
coe_x = 27.0
coe_box = FancyBboxPatch((coe_x, TIER2_Y - 0.05), 0.95, TIER1_Y + TIER1_H - TIER2_Y + 0.1,
                         boxstyle="round,pad=0.04",
                         facecolor="#FCE4EC", edgecolor="#C62828", linewidth=1.5)
ax.add_patch(coe_box)
ax.text(coe_x + 0.47, (TIER1_Y + TIER1_H + TIER2_Y - 0.05) / 2,
        "CoE GOVERNANCE\n& SECURITY\n\nESC Review\nPrompt Firewall\nIAM & SSO\nAudit Log\nDLP & Privacy\nResponsible AI",
        ha='center', va='center', fontsize=7, fontweight='bold',
        color="#8E0000", multialignment='center', linespacing=1.4)

# ── ARROWS Tier1 → Tier2 ──────────────────────────────────
for i in range(N_DOM):
    dx_center = DOM_X_START + i * (DOM_W + 0.12) + DOM_W / 2
    ax.annotate("", xy=(dx_center, TIER2_Y + TIER2_H + 0.02),
                xytext=(dx_center, TIER1_Y - 0.04),
                arrowprops=dict(arrowstyle="-|>", color="#999999", lw=1.2))

# ── ARROWS Tier2 → Tier3 ──────────────────────────────────
for i in range(N_CAPS):
    cx_center = CAP_X_START + i * (CAP_W + 0.14) + CAP_W / 2
    ax.annotate("", xy=(cx_center, TIER2_Y - 0.04),
                xytext=(cx_center, TIER2_Y + 0.04),
                arrowprops=dict(arrowstyle="-|>", color="#7B1FA2", lw=1.0))

# ── TIER 3: SHARED ENTERPRISE PLATFORM ───────────────────
TIER3_Y = 1.1
TIER3_H = 7.9

bg3 = FancyBboxPatch((0.3, TIER3_Y), 27.4, TIER3_H,
                     boxstyle="round,pad=0.08",
                     facecolor="#E3F2FD", edgecolor="#0277BD", linewidth=2)
ax.add_patch(bg3)
ax.text(14, TIER3_Y + TIER3_H - 0.22, "TIER 3 — SHARED ENTERPRISE PLATFORM",
        ha='center', fontsize=10, fontweight='bold', color="#01579B")
ax.text(14, TIER3_Y + TIER3_H - 0.5, "Managed platforms with centralized access, billing, governance — Azure primary | AWS secondary",
        ha='center', fontsize=8.5, color="#0277BD", style='italic')

N_PLAT = len(PLATFORM)
PLAT_W = 27.0 / N_PLAT - 0.14
PLAT_H = 5.5
PLAT_Y = TIER3_Y + 0.55
PLAT_X_START = 0.45

for i, (plat_name, plat_sub) in enumerate(PLATFORM):
    px = PLAT_X_START + i * (PLAT_W + 0.14)
    py = PLAT_Y

    plat_box = FancyBboxPatch((px, py), PLAT_W, PLAT_H,
                              boxstyle="round,pad=0.04",
                              facecolor=WHITE, edgecolor="#0277BD", linewidth=1.2)
    ax.add_patch(plat_box)

    ax.text(px + PLAT_W/2, py + PLAT_H/2 + 0.35, plat_name,
            ha='center', va='center', fontsize=9, fontweight='bold',
            color=NEAR_BLACK, multialignment='center', linespacing=1.3)

    ax.plot([px + 0.12, px + PLAT_W - 0.12],
            [py + PLAT_H/2 - 0.05, py + PLAT_H/2 - 0.05],
            color="#0277BD", lw=0.6, alpha=0.4)

    ax.text(px + PLAT_W/2, py + PLAT_H/2 - 0.5, plat_sub,
            ha='center', va='center', fontsize=8, color="#0277BD",
            style='italic', multialignment='center', linespacing=1.3)

# ── DATA BACKBONE bar at bottom of Tier 3 ─────────────────
data_y = TIER3_Y + 0.08
data_h = 0.38
data_box = FancyBboxPatch((0.45, data_y), 26.5, data_h,
                          boxstyle="round,pad=0.03",
                          facecolor="#B3E5FC", edgecolor="#0277BD", linewidth=1)
ax.add_patch(data_box)
ax.text(13.7, data_y + data_h/2,
        "DATA BACKBONE — Salesforce Data Cloud · Databricks Lakehouse · SharePoint / OneDrive · Veeva Vault · SAP ERP · Vector Databases",
        ha='center', va='center', fontsize=7.5, color="#01579B", fontweight='bold')

# ── Arrow Tier2 → Tier3 (bulk) ────────────────────────────
ax.annotate("", xy=(14, TIER3_Y + TIER3_H + 0.02),
            xytext=(14, TIER2_Y - 0.04),
            arrowprops=dict(arrowstyle="-|>", color="#0277BD", lw=2.0))

# ── Legend ──────────────────────────────────────────────────
legend_data = [
    ("Producing  (strong prod. deployments)", "#003087"),
    ("Scaling  (in prod, expanding)", "#1A7A1A"),
    ("Exploring  (pilot/POC stage)", "#C62828"),
]
for i, (lbl, col) in enumerate(legend_data):
    lb = FancyBboxPatch((0.5 + i*6.5, 0.08), 6.2, 0.35,
                        boxstyle="round,pad=0.02",
                        facecolor=WHITE, edgecolor=col, linewidth=1.5)
    ax.add_patch(lb)
    ax.text(0.5 + i*6.5 + 3.1, 0.255, lbl,
            ha='center', va='center', fontsize=8, color=col, fontweight='bold')

ax.set_xlim(0, 28)
plt.tight_layout(pad=0.15)
plt.savefig("notional-architecture.png", dpi=180,
            bbox_inches='tight', facecolor='#F0F2F5')
plt.savefig("notional-architecture.svg",
            bbox_inches='tight', facecolor='#F0F2F5')
plt.close()
print("Notional architecture PNG/SVG saved.")


# ── draw.io version ────────────────────────────────────────
def make_diagram(name):
    mxfile = ET.Element("mxfile", host="app.diagrams.net")
    diagram = ET.SubElement(mxfile, "diagram", name=name)
    mxgraph = ET.SubElement(diagram, "mxGraphModel",
                             dx="1422", dy="762", grid="0", gridSize="10",
                             guides="1", tooltips="1", connect="1",
                             arrows="1", fold="1", page="0",
                             pageScale="1", pageWidth="1654", pageHeight="1169",
                             math="0", shadow="0")
    root = ET.SubElement(mxgraph, "root")
    ET.SubElement(root, "mxCell", id="0")
    ET.SubElement(root, "mxCell", id="1", parent="0")
    return mxfile, root

def add_cell(root, cell_id, value, style, x, y, w, h, parent="1"):
    cell = ET.SubElement(root, "mxCell", id=str(cell_id), value=value,
                         style=style, vertex="1", parent=parent)
    ET.SubElement(cell, "mxGeometry",
                  x=str(x), y=str(y), width=str(w), height=str(h),
                  **{"as": "geometry"})
    return cell

mxfile, root = make_diagram("GenAI Notional Architecture")
idc = 10

# Title
add_cell(root, idc,
         "Abbott GenAI — Notional Architecture with Capabilities",
         "text;html=1;strokeColor=none;fillColor=none;align=center;"
         "verticalAlign=middle;fontColor=#000050;fontSize=20;fontStyle=1;",
         20, 10, 1600, 50); idc += 1
add_cell(root, idc,
         "Three-Tier Model: Business Domains → Reusable AI Capabilities → Shared Enterprise Platform  |  220 Use Cases · 12 Divisions · 40 in Production",
         "text;html=1;strokeColor=none;fillColor=none;align=center;"
         "verticalAlign=middle;fontColor=#555555;fontSize=11;fontStyle=2;",
         20, 60, 1600, 30); idc += 1

# ── TIER 1 ────────────────────────────────────────────────
T1_Y = 100
T1_H = 380
T1_W = 1580
add_cell(root, idc, "",
         f"rounded=1;whiteSpace=wrap;html=1;fillColor=#FAFAFA;strokeColor=#CCCCCC;strokeWidth=2;",
         20, T1_Y, T1_W, T1_H); idc += 1
add_cell(root, idc, "TIER 1 — BUSINESS CAPABILITY DOMAINS",
         "text;html=1;strokeColor=none;fillColor=none;align=center;"
         "verticalAlign=middle;fontColor=#444444;fontSize=13;fontStyle=1;",
         20, T1_Y + 6, T1_W, 30); idc += 1

N_DOM = len(DOMAINS)
DW = (T1_W - 40 - (N_DOM-1)*10) // N_DOM
DH = 330
DX0 = 30

for i, d in enumerate(DOMAINS):
    dx = 20 + DX0 + i*(DW+10)
    dy = T1_Y + 40
    mat_colors = {"Producing": "#003087", "Scaling": "#1A7A1A", "Exploring": "#C62828"}
    mc = mat_colors.get(d["maturity"], "#888888")
    label = (f"<b style='font-size:13px;'>{d['label'].replace(chr(10),' ')}</b><br/>"
             f"<font style='background-color:{mc};color:#ffffff;font-size:10px;'>&nbsp;{d['maturity']}&nbsp;</font><br/><br/>"
             f"<font style='font-size:10px;color:#444444;'>{d['usecases']}</font><br/><br/>"
             f"<font style='color:#888888;font-size:9px;font-style:italic;'>Key Tools</font><br/>"
             f"<font style='font-size:10px;'>{d['tools'].replace(chr(10),' · ')}</font><br/><br/>"
             f"<font style='color:#888888;font-size:9px;font-style:italic;'>Divisions</font><br/>"
             f"<font style='font-size:9px;color:#555555;'>{d['divisions'].replace(chr(10),' ')}</font>")
    add_cell(root, idc, label,
             f"rounded=1;whiteSpace=wrap;html=1;fillColor={d['bg']};"
             f"strokeColor={d['border']};strokeWidth=2;"
             f"fontColor=#1A1A1A;fontSize=11;verticalAlign=top;spacingTop=10;",
             dx, dy, DW, DH); idc += 1

# ── TIER 2 ────────────────────────────────────────────────
T2_Y = T1_Y + T1_H + 20
T2_H = 180
add_cell(root, idc, "",
         "rounded=1;whiteSpace=wrap;html=1;fillColor=#EDE7F6;strokeColor=#7B1FA2;strokeWidth=2;",
         20, T2_Y, T1_W, T2_H); idc += 1
add_cell(root, idc, "TIER 2 — REUSABLE AI CAPABILITY LAYER",
         "text;html=1;strokeColor=none;fillColor=none;align=center;"
         "verticalAlign=middle;fontColor=#5C0E7A;fontSize=13;fontStyle=1;",
         20, T2_Y + 6, T1_W, 30); idc += 1
add_cell(root, idc, "Shared capabilities consumed by all business domains",
         "text;html=1;strokeColor=none;fillColor=none;align=center;"
         "verticalAlign=middle;fontColor=#7B1FA2;fontSize=10;fontStyle=2;",
         20, T2_Y + 32, T1_W, 20); idc += 1

N_CAPS = len(AI_CAPS)
CW = (T1_W - 40 - (N_CAPS-1)*10) // N_CAPS
CH = 100
CX0 = 30

for i, (cap_name, cap_col) in enumerate(AI_CAPS):
    cx = 20 + CX0 + i*(CW+10)
    cy = T2_Y + 60
    add_cell(root, idc, f"<b>{cap_name.replace(chr(10),'<br/>')}</b>",
             f"rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;"
             f"strokeColor={cap_col};strokeWidth=2;fontColor={cap_col};fontSize=11;verticalAlign=middle;",
             cx, cy, CW, CH); idc += 1

# ── TIER 3 ────────────────────────────────────────────────
T3_Y = T2_Y + T2_H + 20
T3_H = 320
add_cell(root, idc, "",
         "rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#0277BD;strokeWidth=2;",
         20, T3_Y, T1_W, T3_H); idc += 1
add_cell(root, idc, "TIER 3 — SHARED ENTERPRISE PLATFORM",
         "text;html=1;strokeColor=none;fillColor=none;align=center;"
         "verticalAlign=middle;fontColor=#01579B;fontSize=13;fontStyle=1;",
         20, T3_Y + 6, T1_W, 30); idc += 1
add_cell(root, idc,
         "Managed platforms with centralized access, billing, governance — Azure primary | AWS secondary",
         "text;html=1;strokeColor=none;fillColor=none;align=center;"
         "verticalAlign=middle;fontColor=#0277BD;fontSize=10;fontStyle=2;",
         20, T3_Y + 32, T1_W, 20); idc += 1

# Data backbone
add_cell(root, idc,
         "DATA BACKBONE — Salesforce Data Cloud · Databricks Lakehouse · SharePoint / OneDrive · Veeva Vault · SAP ERP · Vector Databases",
         "rounded=1;whiteSpace=wrap;html=1;fillColor=#B3E5FC;strokeColor=#0277BD;strokeWidth=1;"
         "fontColor=#01579B;fontSize=10;fontStyle=1;",
         30, T3_Y + 270, T1_W - 20, 36); idc += 1

N_PLAT = len(PLATFORM)
PW = (T1_W - 40 - (N_PLAT-1)*10) // N_PLAT
PH = 200
PX0 = 30

for i, (plat_name, plat_sub) in enumerate(PLATFORM):
    px = 20 + PX0 + i*(PW+10)
    py = T3_Y + 58
    label = (f"<b style='font-size:12px;'>{plat_name.replace(chr(10),'<br/>')}</b>"
             f"<hr style='border-color:#0277BD;margin:4px 0;'/>"
             f"<font style='font-size:10px;color:#0277BD;font-style:italic;'>{plat_sub.replace(chr(10),'<br/>')}</font>")
    add_cell(root, idc, label,
             "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;"
             "strokeColor=#0277BD;strokeWidth=1.5;"
             "fontColor=#1A1A1A;fontSize=11;verticalAlign=middle;",
             px, py, PW, PH); idc += 1

# ── CoE Governance (right rail) ───────────────────────────
coe_y = T1_Y
coe_h = T2_Y + T2_H - T1_Y
add_cell(root, idc,
         "<b>CoE GOVERNANCE &amp; SECURITY</b><br/><br/>ESC Review<br/>Prompt Firewall<br/>IAM &amp; SSO<br/>Audit Log<br/>DLP &amp; Privacy<br/>Responsible AI",
         "rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE4EC;strokeColor=#C62828;strokeWidth=1.5;"
         "fontColor=#8E0000;fontSize=10;verticalAlign=middle;",
         1620, coe_y, 120, coe_h); idc += 1

# ── Arrows ────────────────────────────────────────────────
# T1 -> T2
arrow1 = ET.SubElement(root, "mxCell",
                        id=str(idc), value="",
                        style="edgeStyle=orthogonalEdgeStyle;strokeColor=#999999;strokeWidth=2;"
                              "exitX=0.5;exitY=1;exitDx=0;exitDy=0;"
                              "entryX=0.5;entryY=0;entryDx=0;entryDy=0;",
                        edge="1", parent="1",
                        source="12", target="14")
ET.SubElement(arrow1, "mxGeometry", relative="1", **{"as": "geometry"})
idc += 1

# T2 -> T3
arrow2 = ET.SubElement(root, "mxCell",
                        id=str(idc), value="",
                        style="edgeStyle=orthogonalEdgeStyle;strokeColor=#7B1FA2;strokeWidth=2.5;"
                              "exitX=0.5;exitY=1;exitDx=0;exitDy=0;"
                              "entryX=0.5;entryY=0;entryDx=0;entryDy=0;",
                        edge="1", parent="1",
                        source="14", target=str(idc - N_PLAT - 6))
ET.SubElement(arrow2, "mxGeometry", relative="1", **{"as": "geometry"})
idc += 1

tree = ET.ElementTree(mxfile)
ET.indent(tree, space="  ")
tree.write("notional-architecture.drawio", encoding="unicode", xml_declaration=False)
print("draw.io notional architecture saved.")
print("\nAll notional architecture files complete.")
