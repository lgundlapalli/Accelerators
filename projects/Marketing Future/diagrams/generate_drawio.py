"""
Generate draw.io XML files for:
1. Layered Architecture view
2. Domain view
3. Target Architecture
"""
import xml.etree.ElementTree as ET

# ── Color palette ──────────────────────────────────────────
AGENTS = {
    "BRANDS":   {"bg": "#D6E8FF", "border": "#003087", "text": "#003087"},
    "ALICE":    {"bg": "#FFE8D6", "border": "#C05000", "text": "#7A3000"},
    "CRAFTS":   {"bg": "#E8F4E8", "border": "#1A7A1A", "text": "#1A5C1A"},
    "SPARK":    {"bg": "#F3E5F5", "border": "#7B1FA2", "text": "#5C0E7A"},
    "ACCESS":   {"bg": "#FFF3E0", "border": "#B35A00", "text": "#7A3E00"},
    "PLATFORM": {"bg": "#E3F2FD", "border": "#0277BD", "text": "#01579B"},
    "CURRENT":  {"bg": "#F5F5F5", "border": "#888888", "text": "#333333"},
}

STATUS_ICONS = {
    "✓": "✓ POC Proceeding",
    "◐": "◐ POC In Progress",
    "⏸": "⏸ On Hold",
    "⚠": "⚠ MLR Critical",
    "→": "→ Future Target",
}

def _sc(s):
    m = {"✓": "#1A7A1A", "◐": "#B35A00", "⏸": "#888888", "⚠": "#C62828", "→": "#003087"}
    return m.get(s, "#1A1A1A")


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


def add_cell(root, cell_id, parent_id, value, style, x, y, w, h, vertex=True):
    cell = ET.SubElement(root, "mxCell",
                         id=str(cell_id),
                         value=value,
                         style=style,
                         vertex="1" if vertex else "0",
                         parent=str(parent_id))
    ET.SubElement(cell, "mxGeometry",
                  x=str(x), y=str(y), width=str(w), height=str(h),
                  **{"as": "geometry"})
    return cell


def add_arrow(root, cell_id, parent_id, source_id, target_id, label=""):
    cell = ET.SubElement(root, "mxCell",
                         id=str(cell_id),
                         value=label,
                         style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;"
                               "jettySize=auto;exitX=0.5;exitY=1;exitDx=0;exitDy=0;"
                               "entryX=0.5;entryY=0;entryDx=0;entryDy=0;"
                               "strokeColor=#555599;strokeWidth=2;fontColor=#555599;"
                               "fontSize=9;fontStyle=2;",
                         edge="1",
                         source=str(source_id),
                         target=str(target_id),
                         parent=str(parent_id))
    ET.SubElement(cell, "mxGeometry", relative="1", **{"as": "geometry"})
    return cell


def section_style(color_key, rounded=True):
    c = AGENTS[color_key]
    r = "1" if rounded else "0"
    return (f"rounded={r};whiteSpace=wrap;html=1;"
            f"fillColor={c['bg']};strokeColor={c['border']};strokeWidth=2;"
            f"fontColor={c['text']};fontSize=12;fontStyle=1;"
            f"verticalAlign=top;")


def cap_style(border_color):
    return (f"rounded=1;whiteSpace=wrap;html=1;"
            f"fillColor=#FFFFFF;strokeColor={border_color};strokeWidth=1;"
            f"fontColor=#1A1A1A;fontSize=10;fontStyle=0;"
            f"verticalAlign=middle;")


def title_style():
    return ("text;html=1;strokeColor=none;fillColor=none;"
            "align=center;verticalAlign=middle;"
            "fontColor=#000050;fontSize=16;fontStyle=1;")


def subtitle_style():
    return ("text;html=1;strokeColor=none;fillColor=none;"
            "align=center;verticalAlign=middle;"
            "fontColor=#888888;fontSize=11;fontStyle=2;")


def save_xml(mxfile, path):
    tree = ET.ElementTree(mxfile)
    ET.indent(tree, space="  ")
    tree.write(path, encoding="unicode", xml_declaration=False)
    print(f"Saved: {path}")


# ═══════════════════════════════════════════════════════════
# DIAGRAM 1 — LAYERED ARCHITECTURE
# ═══════════════════════════════════════════════════════════
mxfile, root = make_diagram("Layered Architecture")

idc = 10  # id counter

# Title
add_cell(root, idc, 1, "EPD Marketer of the Future — Capability Map (Architecture Layers)",
         title_style(), 20, 10, 1580, 40, vertex=True)
idc += 1
add_cell(root, idc, 1,
         "Current state tools (Abbott evaluation)  +  Future target tools per agent | ✓ POC Proceeding  ◐ POC In Progress  ⏸ On Hold  ⚠ MLR Critical  → Future Target",
         subtitle_style(), 20, 52, 1580, 28, vertex=True)
idc += 1

LAYER_X = 20
LAYER_W = 1580
LABEL_W = 200
CAP_X_START = LAYER_X + LABEL_W + 10
CAP_AREA_W = LAYER_W - LABEL_W - 30
GAP = 8

layers = [
    {
        "key": "BRANDS", "label": "BRANDS\nBrand Strategy",
        "y": 90, "h": 100,
        "caps": [
            ("Market Intelligence",    "Neuron AI → Deepsights",         "◐"),
            ("Social Listening",        "Sprinklr → Brandwatch",          "⏸"),
            ("Strategy Modeling",       "RightSpend → ZS ZAIDYN",         "⏸"),
            ("Synthetic Research",      "None → Digital Twins",           "→"),
        ]
    },
    {
        "key": "ALICE", "label": "ALICE\nCreative Excellence",
        "y": 200, "h": 100,
        "caps": [
            ("Creative Generation",    "Adobe Express → Adobe Firefly",   "✓"),
            ("Brief Intelligence",      "None → Persado",                 "→"),
            ("Copy &amp; Claim Gen",    "Writer AI → Writer.com Ent.",    "◐"),
            ("Creative Ops",            "Dynamic Media → Workfront",      "✓"),
        ]
    },
    {
        "key": "CRAFTS", "label": "CRAFTS\nContent &amp; MLR",
        "y": 310, "h": 100,
        "caps": [
            ("MLR Review",             "None → Veeva PromoMats AI",       "⚠"),
            ("Compliance Detection",    "None → Indegene AI",             "⚠"),
            ("Modular Content",         "Writer AI → Adobe AEM+Firefly",  "◐"),
            ("Content Testing",         "DragonFly → Optimizely",         "⏸"),
        ]
    },
    {
        "key": "SPARK", "label": "SPARK\nCustomer Engagement",
        "y": 420, "h": 100,
        "caps": [
            ("Next-Best-Action",        "None → Aktana/PharmaForceIQ",    "→"),
            ("CRM &amp; HCP Journeys",  "Salesforce Einstein Mktg Cld",   "◐"),
            ("Patient Engagement",      "Five9 → Conversa Health",        "◐"),
            ("Omnichannel Personaliz.", "Salesforce → Adobe Sensei",      "◐"),
        ]
    },
    {
        "key": "ACCESS", "label": "ACCESS\nMarket Access",
        "y": 530, "h": 100,
        "caps": [
            ("Competitive Intel",       "None → IQVIA Market Edge AI",    "→"),
            ("HTA &amp; Value Dossier", "None → ZS ZAIDYN Access",        "→"),
            ("Patient Support Pgms",    "None → ConnectiveRx AI",         "→"),
            ("Regulatory Compliance",   "None → RegASK / Veripharm",      "⚠"),
        ]
    },
    {
        "key": "PLATFORM", "label": "SHARED DATA &amp; PLATFORM LAYER\nAbbott GenAI Foundation",
        "y": 640, "h": 120,
        "caps": [
            ("CRM Foundation",          "Salesforce LS Cloud / Veeva",    "✓"),
            ("Content Mgmt",            "Adobe Experience Manager",       "✓"),
            ("Data Unification",        "Salesforce Data Cloud",          "◐"),
            ("GenAI Platform",          "Azure AI Foundry",               "✓"),
            ("Enterprise LLM",          "Anthropic Claude",               "✓"),
            ("Integration &amp; API",   "MuleSoft / Azure APIM",          "✓"),
        ]
    },
]

layer_ids = {}
for layer in layers:
    y, h = layer["y"], layer["h"]
    key = layer["key"]
    c = AGENTS[key]

    # Section background
    bg_id = idc
    add_cell(root, bg_id, 1, "",
             f"rounded=1;whiteSpace=wrap;html=1;fillColor={c['bg']};"
             f"strokeColor={c['border']};strokeWidth=2;",
             LAYER_X, y, LAYER_W, h)
    layer_ids[key] = bg_id
    idc += 1

    # Section label
    add_cell(root, idc, 1, layer["label"],
             f"text;html=1;strokeColor=none;fillColor=none;align=left;"
             f"verticalAlign=middle;fontColor={c['text']};fontSize=11;fontStyle=1;",
             LAYER_X + 8, y + 10, LABEL_W - 16, h - 20)
    idc += 1

    # Capability boxes
    caps = layer["caps"]
    n = len(caps)
    cap_w = (CAP_AREA_W - (n - 1) * GAP) / n
    cap_h = h - 20

    for i, (title, subtitle, status) in enumerate(caps):
        bx = CAP_X_START + i * (cap_w + GAP)
        by = y + 10
        label = f"<b>{title}</b><br/><font style='font-size:9px;color:#555555;'><i>{subtitle}</i></font><br/><font style='font-size:9px;color:{_sc(status)};'>{STATUS_ICONS.get(status,'')}</font>"
        add_cell(root, idc, 1, label,
                 f"rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;"
                 f"strokeColor={c['border']};strokeWidth=1;"
                 f"fontColor=#1A1A1A;fontSize=10;verticalAlign=middle;",
                 bx, by, cap_w, cap_h)
        idc += 1


save_xml(mxfile, "layered.drawio")


# ═══════════════════════════════════════════════════════════
# DIAGRAM 2 — DOMAIN VIEW (3×2 grid)
# ═══════════════════════════════════════════════════════════
mxfile2, root2 = make_diagram("Domain View")
idc2 = 10

add_cell(root2, idc2, 1, "EPD Marketer of the Future — Business Capability Map (Domain View)",
         title_style(), 20, 10, 1580, 40)
idc2 += 1
add_cell(root2, idc2, 1,
         "✓ POC Proceeding  ◐ POC In Progress  ⏸ On Hold  ⚠ MLR Critical  → Future Target",
         subtitle_style(), 20, 52, 1580, 28)
idc2 += 1

domains = [
    {
        "key": "BRANDS", "label": "BRANDS — Brand Strategy",
        "col": 0, "row": 0,
        "caps": [
            ("Market Intelligence",    "Neuron AI → Deepsights",         "◐"),
            ("Social Listening",        "Sprinklr → Brandwatch",          "⏸"),
            ("Strategy Modeling",       "RightSpend → ZS ZAIDYN",         "⏸"),
            ("Synthetic Research",      "None → Digital Twins",           "→"),
        ]
    },
    {
        "key": "ALICE", "label": "ALICE — Creative Excellence",
        "col": 1, "row": 0,
        "caps": [
            ("Creative Generation",    "Adobe Express → Adobe Firefly",   "✓"),
            ("Brief Intelligence",      "None → Persado",                 "→"),
            ("Copy &amp; Claim Gen",    "Writer AI → Writer.com Ent.",    "◐"),
            ("Creative Ops",            "Dynamic Media → Workfront",      "✓"),
        ]
    },
    {
        "key": "CRAFTS", "label": "CRAFTS — Content &amp; MLR",
        "col": 2, "row": 0,
        "caps": [
            ("MLR Review",             "None → Veeva PromoMats AI",       "⚠"),
            ("Compliance Detection",    "None → Indegene AI",             "⚠"),
            ("Modular Content",         "Writer AI → Adobe AEM+Firefly",  "◐"),
            ("Content Testing",         "DragonFly → Optimizely",         "⏸"),
        ]
    },
    {
        "key": "SPARK", "label": "SPARK — Customer Engagement",
        "col": 0, "row": 1,
        "caps": [
            ("Next-Best-Action",        "None → Aktana/PharmaForceIQ",    "→"),
            ("CRM &amp; HCP Journeys",  "Salesforce Einstein Mktg Cld",   "◐"),
            ("Patient Engagement",      "Five9 → Conversa Health",        "◐"),
            ("Personalization",         "Salesforce → Adobe Sensei",      "◐"),
        ]
    },
    {
        "key": "ACCESS", "label": "ACCESS — Market Access",
        "col": 1, "row": 1,
        "caps": [
            ("Competitive Intel",       "None → IQVIA Market Edge AI",    "→"),
            ("HTA &amp; Value Dossier", "None → ZS ZAIDYN Access",        "→"),
            ("Patient Support",         "None → ConnectiveRx AI",         "→"),
            ("Regulatory Compliance",   "None → RegASK / Veripharm",      "⚠"),
        ]
    },
    {
        "key": "PLATFORM", "label": "PLATFORM — Abbott GenAI Foundation",
        "col": 2, "row": 1,
        "caps": [
            ("CRM Foundation",          "Salesforce LS Cloud / Veeva",    "✓"),
            ("Content Mgmt",            "Adobe Experience Manager",       "✓"),
            ("GenAI Platform",          "Azure AI Foundry",               "✓"),
            ("Enterprise LLM",          "Anthropic Claude",               "✓"),
        ]
    },
]

CELL_W = 510
CELL_H = 340
H_GAP = 20
V_GAP = 20
START_X = 20
START_Y = 90

for d in domains:
    col, row = d["col"], d["row"]
    cx = START_X + col * (CELL_W + H_GAP)
    cy = START_Y + row * (CELL_H + V_GAP)
    key = d["key"]
    c = AGENTS[key]

    # Domain background
    add_cell(root2, idc2, 1, "",
             f"rounded=1;whiteSpace=wrap;html=1;fillColor={c['bg']};"
             f"strokeColor={c['border']};strokeWidth=2;",
             cx, cy, CELL_W, CELL_H)
    idc2 += 1

    # Domain label
    add_cell(root2, idc2, 1, d["label"],
             f"text;html=1;strokeColor=none;fillColor=none;align=left;"
             f"verticalAlign=middle;fontColor={c['text']};fontSize=11;fontStyle=1;",
             cx + 8, cy + 6, CELL_W - 16, 30)
    idc2 += 1

    caps = d["caps"]
    nc = 2
    nr = 2
    cap_w2 = (CELL_W - 20 - 8) / nc
    cap_h2 = (CELL_H - 50 - 8) / nr

    for i, (title, subtitle, status) in enumerate(caps):
        r = i // nc
        c2 = i % nc
        bx = cx + 8 + c2 * (cap_w2 + 8)
        by = cy + 44 + r * (cap_h2 + 8)
        label = (f"<b>{title}</b><br/>"
                 f"<font style='font-size:9px;color:#555555;'><i>{subtitle}</i></font><br/>"
                 f"<font style='font-size:9px;color:{_sc(status)};'>{STATUS_ICONS.get(status,'')}</font>")
        add_cell(root2, idc2, 1, label,
                 f"rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;"
                 f"strokeColor={c['border']};strokeWidth=1;"
                 f"fontColor=#1A1A1A;fontSize=10;verticalAlign=middle;",
                 bx, by, cap_w2, cap_h2)
        idc2 += 1

save_xml(mxfile2, "domain.drawio")


# ═══════════════════════════════════════════════════════════
# DIAGRAM 3 — TARGET ARCHITECTURE
# ═══════════════════════════════════════════════════════════
mxfile3, root3 = make_diagram("Target Architecture")
idc3 = 10

add_cell(root3, idc3, 1, "EPD Marketer of the Future — Target Architecture",
         title_style(), 20, 10, 1580, 40)
idc3 += 1
add_cell(root3, idc3, 1,
         "How the Five Agents connect with platforms, tools, and data  |  Current → Future state",
         subtitle_style(), 20, 52, 1580, 28)
idc3 += 1

def agent_block_drawio(root, idc, cx, cy, w, h, key, label, tools):
    c = AGENTS[key]
    # Outer box
    block_id = idc
    add_cell(root, block_id, 1, "",
             f"rounded=1;whiteSpace=wrap;html=1;fillColor={c['bg']};"
             f"strokeColor={c['border']};strokeWidth=2.5;",
             cx, cy, w, h)
    idc += 1
    # Label
    add_cell(root, idc, 1, label,
             f"text;html=1;strokeColor=none;fillColor=none;align=center;"
             f"verticalAlign=middle;fontColor={c['text']};fontSize=12;fontStyle=1;",
             cx, cy + 6, w, 28)
    idc += 1
    # Tool chips
    n = len(tools)
    tw = (w - 20 - (n-1)*8) / n
    th = 55
    for i, (tname, tclass, tstatus) in enumerate(tools):
        tx = cx + 10 + i*(tw+8)
        ty = cy + h - th - 10
        tlabel = (f"<b style='font-size:9px;'>{tname}</b><br/>"
                  f"<font style='font-size:8px;color:{_sc(tstatus)};'>{tclass}</font>")
        add_cell(root, idc, 1, tlabel,
                 f"rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;"
                 f"strokeColor={c['border']};strokeWidth=1;"
                 f"fontColor=#1A1A1A;fontSize=9;verticalAlign=middle;",
                 tx, ty, tw, th)
        idc += 1
    return idc, block_id

# Layout positions
AW3, AH3 = 480, 130

# CURRENT STATE box
cs_id = idc3
add_cell(root3, cs_id, 1, "CURRENT STATE — Abbott Tools In Evaluation",
         f"rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;"
         f"strokeColor=#888888;strokeWidth=1.5;dashed=1;"
         f"fontColor=#333333;fontSize=11;fontStyle=1;verticalAlign=top;",
         20, 90, 900, 100)
idc3 += 1

cs_tools = [
    ("Adobe Express ✓","POC Proceeding","✓"),
    ("Writer AI ◐","EPD POC","◐"),
    ("Dynamic Media ✓","POC Proceeding","✓"),
    ("Salesforce Einstein ◐","Mktg Cloud","◐"),
    ("Neuron AI ◐","POC Progress","◐"),
    ("Five9 ◐","POC To Start","◐"),
    ("Sprinklr ⏸","On Hold","⏸"),
    ("Azure AI Foundry","Enterprise","✓"),
]
n_cs = len(cs_tools)
cs_tw = (900 - 20 - (n_cs-1)*6) / n_cs
for i, (tn, tc, ts) in enumerate(cs_tools):
    tx = 30 + i*(cs_tw+6)
    tlabel = (f"<b style='font-size:8px;'>{tn}</b><br/>"
              f"<font style='font-size:7px;color:{_sc(ts)};'>{tc}</font>")
    add_cell(root3, idc3, 1, tlabel,
             f"rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;"
             f"strokeColor=#888888;strokeWidth=1;fontColor=#1A1A1A;fontSize=8;verticalAlign=middle;",
             tx, 118, cs_tw, 62)
    idc3 += 1

# BRANDS center top
brands_cx = 790
idc3, brands_id = agent_block_drawio(root3, idc3, brands_cx, 210, AW3, AH3,
    "BRANDS", "BRANDS — Brand Strategy", [
    ("Deepsights","Market Leader","→"),
    ("Brandwatch","Market Leader","→"),
    ("ZS ZAIDYN","Emerging","→"),
    ("Salesforce Einstein","Core","◐"),
])

# ALICE left
alice_cx = 160
idc3, alice_id = agent_block_drawio(root3, idc3, alice_cx, 390, AW3, AH3,
    "ALICE", "ALICE — Creative Excellence", [
    ("Adobe Firefly","Market Leader","→"),
    ("Persado","Market Leader","→"),
    ("Writer.com","Market Leader","◐"),
    ("Workfront","Core","→"),
])

# CRAFTS center
crafts_cx = 790
idc3, crafts_id = agent_block_drawio(root3, idc3, crafts_cx, 390, AW3, AH3,
    "CRAFTS", "CRAFTS — Content &amp; MLR", [
    ("Veeva PromoMats AI","MLR-Critical","⚠"),
    ("Indegene AI","MLR-Critical","⚠"),
    ("Adobe AEM + Firefly","Market Leader","→"),
    ("Optimizely","Core","→"),
])

# SPARK right
spark_cx = 1140
idc3, spark_id = agent_block_drawio(root3, idc3, spark_cx, 390, AW3, AH3,
    "SPARK", "SPARK — Customer Engagement", [
    ("Aktana/PharmaForceIQ","Market Leader","→"),
    ("Veeva CRM AI","Market Leader","→"),
    ("Conversa Health","Emerging","→"),
    ("Adobe Sensei","Core","◐"),
])

# ACCESS center lower
access_cx = 790
idc3, access_id = agent_block_drawio(root3, idc3, access_cx, 570, AW3, AH3,
    "ACCESS", "ACCESS — Market Access", [
    ("IQVIA Market Edge AI","Market Leader","→"),
    ("ZS ZAIDYN Access","Emerging","→"),
    ("ConnectiveRx AI","Market Leader","→"),
    ("RegASK / Veripharm","MLR-Critical","⚠"),
])

# PLATFORM bottom bar
plat_id = idc3
add_cell(root3, plat_id, 1, "SHARED DATA &amp; PLATFORM LAYER — Abbott GenAI Foundation",
         f"rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;"
         f"strokeColor=#0277BD;strokeWidth=2;"
         f"fontColor=#01579B;fontSize=12;fontStyle=1;verticalAlign=top;",
         20, 760, 1580, 130)
idc3 += 1

plat_items = [
    ("Salesforce LS Cloud / Veeva CRM","CRM Foundation","✓"),
    ("Adobe Experience Manager","Content Mgmt","✓"),
    ("Salesforce Data Cloud","Data Unification","◐"),
    ("Azure AI Foundry","GenAI Platform","✓"),
    ("Anthropic Claude","Enterprise LLM","✓"),
    ("MuleSoft / Azure APIM","Integration &amp; API","✓"),
    ("Abbott IAM / SSO","Identity &amp; Access","✓"),
    ("Veeva Vault","Compliance &amp; Audit","→"),
]
n_p = len(plat_items)
pi_w = (1580 - 20 - (n_p-1)*8) / n_p
for i, (tn, tc, ts) in enumerate(plat_items):
    px = 30 + i*(pi_w+8)
    tlabel = (f"<b style='font-size:9px;'>{tn}</b><br/>"
              f"<font style='font-size:8px;color:{_sc(ts)};'>{tc}</font>")
    add_cell(root3, idc3, 1, tlabel,
             f"rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;"
             f"strokeColor=#0277BD;strokeWidth=1;fontColor=#1A1A1A;fontSize=9;verticalAlign=middle;",
             px, 790, pi_w, 90)
    idc3 += 1

# Arrows
def arr3(root, idc, src, tgt, label=""):
    cell = ET.SubElement(root, "mxCell",
                         id=str(idc), value=label,
                         style="edgeStyle=orthogonalEdgeStyle;rounded=1;"
                               "strokeColor=#555599;strokeWidth=1.8;"
                               "fontColor=#555599;fontSize=9;fontStyle=2;"
                               "exitX=0.5;exitY=1;exitDx=0;exitDy=0;",
                         edge="1", source=str(src), target=str(tgt), parent="1")
    ET.SubElement(cell, "mxGeometry", relative="1", **{"as": "geometry"})
    return idc + 1

idc3 = arr3(root3, idc3, brands_id, alice_id,  "Strategy &amp; Brand Voice")
idc3 = arr3(root3, idc3, brands_id, crafts_id, "Brand Guidelines")
idc3 = arr3(root3, idc3, brands_id, spark_id,  "Audience Segments")
idc3 = arr3(root3, idc3, alice_id,  crafts_id, "Creative Assets")
idc3 = arr3(root3, idc3, crafts_id, spark_id,  "Approved Content")
idc3 = arr3(root3, idc3, spark_id,  access_id, "Engagement Signals")
idc3 = arr3(root3, idc3, crafts_id, access_id, "Compliance Docs")
idc3 = arr3(root3, idc3, access_id, plat_id,   "Data Exchange")

# Dashed evolve arrow from current state to BRANDS
cell = ET.SubElement(root3, "mxCell",
                     id=str(idc3), value="Evolves to Future State",
                     style="edgeStyle=orthogonalEdgeStyle;rounded=1;"
                           "strokeColor=#888888;strokeWidth=1.5;dashed=1;"
                           "fontColor=#888888;fontSize=9;fontStyle=2;",
                     edge="1", source=str(cs_id), target=str(brands_id), parent="1")
ET.SubElement(cell, "mxGeometry", relative="1", **{"as": "geometry"})
idc3 += 1

save_xml(mxfile3, "target-architecture.drawio")

print("\nAll 3 draw.io files generated.")
print("Open at https://app.diagrams.net or import into Miro via the draw.io plugin.")
