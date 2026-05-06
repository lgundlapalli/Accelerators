"""
Abbott GenAI Blueprint — draw.io XML Generator
Generates 3 editable draw.io files.
"""

import xml.etree.ElementTree as ET
import os

OUT = "/Users/GUNDLLX/learn-claude/projects/Gen Ai Architecture/diagrams"
os.makedirs(OUT, exist_ok=True)

DOMAIN_COLORS = [
    "#4472C4", "#ED7D31", "#A9D18E", "#FF99CC", "#FFD966", "#9DC3E6"
]
DOMAINS = [
    "Content &amp; Creative Studio",
    "Insights &amp; Analytics Acceleration",
    "Productivity &amp; Automation",
    "Customer &amp; Field Engagement",
    "Engineering &amp; Development",
    "Learning, Compliance &amp; Governance",
]
SUB_CAPS = [
    ["Creative Content Draft", "Writing Drafts &amp; Data Entry", "Personalize Content", "Translation"],
    ["Search, Screen &amp; Insights", "Reporting &amp; Observability", "Forecast"],
    ["Enterprise Productivity Tools", "Writing Drafts &amp; Data Entry"],
    ["Assistants", "Personalize Content", "Search &amp; CRM Insights"],
    ["Code Creation with Platform", "Code Creation IDE &amp; Test Authoring"],
    ["Learning, Training &amp; Coaching", "Image Identification / Analysis"],
]
TOOLS = [
    "Writer Newsroom, Adobe Firefly, AutogenAI",
    "Mktg Insights Accelerator, RADIA Research, Databricks",
    "M365 Copilot, Cursor/Windsurf, Five9 GSD",
    "SmartRep, Neuron7, Five9 GSD",
    "Cursor/Windsurf/Atlassian AI, Azure AI Sandbox",
    "Pilots in CHR, Corp, RMDx, Cyber",
]
MATURITY = ["Scaling", "Producing", "Scaling", "Producing", "Scaling", "Exploring"]
DIV_COUNTS = [7, 6, 6, 5, 3, 6]
PLATFORMS = [
    "Azure AI Foundry", "Anthropic Claude", "Salesforce Einstein",
    "Adobe Experience Cloud", "Veeva Vault AI", "Microsoft M365 Copilot",
]


def make_diagram(name):
    mxfile = ET.Element("mxfile", host="app.diagrams.net")
    diagram = ET.SubElement(mxfile, "diagram", name=name)
    mxgraph = ET.SubElement(diagram, "mxGraphModel",
                             dx="1422", dy="762", grid="0", gridSize="10",
                             guides="1", tooltips="1", connect="1", arrows="1",
                             fold="1", page="0", pageScale="1",
                             pageWidth="1654", pageHeight="1169",
                             math="0", shadow="0")
    root = ET.SubElement(mxgraph, "root")
    ET.SubElement(root, "mxCell", id="0")
    ET.SubElement(root, "mxCell", id="1", parent="0")
    return mxfile, root


def add_cell(root, cell_id, parent_id, value, style, x, y, w, h):
    cell = ET.SubElement(root, "mxCell",
                         id=str(cell_id), value=value, style=style,
                         vertex="1", parent=str(parent_id))
    ET.SubElement(cell, "mxGeometry",
                  x=str(x), y=str(y), width=str(w), height=str(h),
                  **{"as": "geometry"})
    return cell


def add_arrow(root, arrow_id, src, tgt, parent_id="1"):
    cell = ET.SubElement(root, "mxCell",
                         id=str(arrow_id), value="", edge="1",
                         source=str(src), target=str(tgt), parent=str(parent_id))
    cell.set("style", "endArrow=block;endFill=1;strokeColor=#666666;")
    ET.SubElement(cell, "mxGeometry", relative="1", **{"as": "geometry"})
    return cell


def save_xml(mxfile, path):
    tree = ET.ElementTree(mxfile)
    ET.indent(tree, space="  ")
    tree.write(path, encoding="unicode", xml_declaration=False)
    print(f"  Saved {path}")


# ══════════════════════════════════════════════════════════════
# capability-model.drawio
# ══════════════════════════════════════════════════════════════
def make_capability_model_drawio():
    mxfile, root = make_diagram("Capability Model")
    cid = 10

    # Title
    add_cell(root, cid, "1",
             "Abbott GenAI Capability Model — Enterprise Blueprint",
             "text;html=1;strokeColor=none;fillColor=#000050;align=center;"
             "verticalAlign=middle;whiteSpace=wrap;rounded=0;"
             "fontColor=#FFFFFF;fontSize=18;fontStyle=1;",
             10, 10, 1500, 50)
    cid += 1

    band_h = 120
    for i, (domain, subs, color) in enumerate(zip(DOMAINS, SUB_CAPS, DOMAIN_COLORS)):
        y = 70 + i * (band_h + 8)
        # Band background
        add_cell(root, cid, "1", "",
                 f"rounded=1;whiteSpace=wrap;html=1;fillColor={color}33;"
                 f"strokeColor={color};strokeWidth=2;",
                 10, y, 1500, band_h)
        bg_id = cid
        cid += 1
        # Domain label
        add_cell(root, cid, str(bg_id), domain,
                 f"text;html=1;strokeColor=none;fillColor=none;align=center;"
                 f"verticalAlign=middle;whiteSpace=wrap;fontColor=#000050;"
                 f"fontSize=13;fontStyle=1;",
                 10, 10, 160, band_h - 20)
        cid += 1
        # Sub-capability boxes
        sub_w = min(250, (1300 // max(len(subs), 1)) - 15)
        for j, sub in enumerate(subs):
            bx = 190 + j * (sub_w + 15)
            add_cell(root, cid, str(bg_id), sub,
                     "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;"
                     f"strokeColor={color};strokeWidth=1;fontSize=10;",
                     bx, 15, sub_w, band_h - 30)
            cid += 1

    save_xml(mxfile, os.path.join(OUT, "capability-model.drawio"))


# ══════════════════════════════════════════════════════════════
# domain-model.drawio
# ══════════════════════════════════════════════════════════════
def make_domain_model_drawio():
    mxfile, root = make_diagram("Domain Model")
    cid = 10

    # Title
    add_cell(root, cid, "1",
             "Abbott GenAI Domain Model — Use Case Distribution",
             "text;html=1;strokeColor=none;fillColor=#000050;align=center;"
             "verticalAlign=middle;whiteSpace=wrap;rounded=0;"
             "fontColor=#FFFFFF;fontSize=18;fontStyle=1;",
             10, 10, 1500, 50)
    cid += 1

    card_w, card_h = 470, 340
    cols, rows = 3, 2
    for i in range(6):
        row = i // cols
        col = i % cols
        x = 20 + col * (card_w + 20)
        y = 80 + row * (card_h + 20)
        color = DOMAIN_COLORS[i]

        # Card background
        add_cell(root, cid, "1", "",
                 f"rounded=1;whiteSpace=wrap;html=1;fillColor={color}22;"
                 f"strokeColor={color};strokeWidth=2;",
                 x, y, card_w, card_h)
        card_id = cid
        cid += 1

        # Header
        add_cell(root, cid, str(card_id), DOMAINS[i],
                 f"text;html=1;strokeColor=none;fillColor={color};align=center;"
                 "verticalAlign=middle;whiteSpace=wrap;fontColor=#FFFFFF;"
                 "fontSize=13;fontStyle=1;",
                 0, 0, card_w, 50)
        cid += 1

        # Maturity
        mat = MATURITY[i]
        mat_colors = {"Producing": "#228822", "Scaling": "#3333AA", "Exploring": "#CC8800"}
        add_cell(root, cid, str(card_id), mat,
                 f"rounded=1;whiteSpace=wrap;html=1;fillColor={mat_colors[mat]};"
                 "strokeColor=none;fontColor=#FFFFFF;fontSize=9;fontStyle=1;",
                 10, 55, 90, 25)
        cid += 1

        # Div count
        add_cell(root, cid, str(card_id), f"{DIV_COUNTS[i]} Divisions",
                 "text;html=1;strokeColor=none;fillColor=none;align=right;"
                 "verticalAlign=middle;fontColor=#000050;fontSize=10;fontStyle=1;",
                 card_w - 110, 55, 100, 25)
        cid += 1

        # Sub-capabilities
        sub_text = "<b>Sub-capabilities:</b><br/>" + "<br/>".join(f"• {s}" for s in SUB_CAPS[i])
        add_cell(root, cid, str(card_id), sub_text,
                 "text;html=1;strokeColor=none;fillColor=none;align=left;"
                 "verticalAlign=top;whiteSpace=wrap;fontColor=#333333;fontSize=9;",
                 10, 90, card_w - 20, 130)
        cid += 1

        # Tools
        add_cell(root, cid, str(card_id),
                 f"<b>In-Production:</b><br/>{TOOLS[i]}",
                 "text;html=1;strokeColor=none;fillColor=none;align=left;"
                 "verticalAlign=top;whiteSpace=wrap;fontColor=#555555;fontSize=9;fontStyle=2;",
                 10, 230, card_w - 20, 95)
        cid += 1

    save_xml(mxfile, os.path.join(OUT, "domain-model.drawio"))


# ══════════════════════════════════════════════════════════════
# blueprint.drawio
# ══════════════════════════════════════════════════════════════
def make_blueprint_drawio():
    mxfile, root = make_diagram("Blueprint Architecture")
    cid = 10

    # Title
    add_cell(root, cid, "1",
             "Abbott GenAI Enterprise Blueprint — 3-Tier Architecture",
             "text;html=1;strokeColor=none;fillColor=#000050;align=center;"
             "verticalAlign=middle;whiteSpace=wrap;rounded=0;"
             "fontColor=#FFFFFF;fontSize=18;fontStyle=1;",
             10, 10, 1500, 50)
    cid += 1

    tier_cfg = [
        # (label, y, bg_color, border_color, box_color_list)
        ("TIER 1 — BUSINESS DOMAINS", 80, "#F0F0FF", "#3333AA", DOMAIN_COLORS),
        ("TIER 2 — GENAI CAPABILITIES", 380, "#DDDDF8", "#000050",
         ["#DDDDF8"] * 6),
        ("TIER 3 — SHARED PLATFORM FOUNDATION", 640, "#E8F0FE", "#000050",
         ["#0078D422", "#CC880022", "#00A1E022", "#FF000022", "#F2672422", "#00B4F022"]),
    ]

    tier_labels = [
        DOMAINS,
        ["Creative Content\nDraft &amp; Translation",
         "Search, Screen\n&amp; Insights",
         "Enterprise\nProductivity Tools",
         "Assistants &amp;\nPersonalization",
         "Code Creation\n&amp; IDE Tools",
         "Learning, Training\n&amp; Compliance"],
        PLATFORMS,
    ]

    arrow_ids = []
    tier_box_ids = [[], [], []]

    for ti, (tier_lbl, ty, bg_col, border_col, box_colors) in enumerate(tier_cfg):
        tier_h = 270
        # Tier container
        add_cell(root, cid, "1", "",
                 f"rounded=1;whiteSpace=wrap;html=1;fillColor={bg_col};"
                 f"strokeColor={border_col};strokeWidth=2;",
                 10, ty, 1500, tier_h)
        tier_id = cid
        cid += 1

        # Tier label
        add_cell(root, cid, str(tier_id), tier_lbl,
                 f"text;html=1;strokeColor=none;fillColor=none;align=left;"
                 "verticalAlign=middle;fontColor=#000050;fontSize=11;fontStyle=1;",
                 10, 5, 500, 30)
        cid += 1

        bw = 220
        bh = 180 if ti < 2 else 200
        for bi, (lbl, bcol) in enumerate(zip(tier_labels[ti], box_colors)):
            bx = 20 + bi * (bw + 15)
            by = 45
            fill = bcol if ti == 1 else bcol
            stroke = DOMAIN_COLORS[bi] if ti != 1 else "#3333AA"
            font_color = "#FFFFFF" if ti != 1 else "#000050"

            if ti == 0:
                style = (f"rounded=1;whiteSpace=wrap;html=1;fillColor={bcol};"
                         "strokeColor=none;fontColor=#FFFFFF;fontSize=11;fontStyle=1;"
                         "verticalAlign=middle;align=center;")
            elif ti == 1:
                style = ("rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;"
                         "strokeColor=#3333AA;fontColor=#000050;fontSize=10;"
                         "verticalAlign=middle;align=center;")
            else:
                pcolors = ["#0078D4", "#CC8800", "#00A1E0", "#FF0000", "#F26724", "#00B4F0"]
                pc = pcolors[bi]
                style = (f"rounded=1;whiteSpace=wrap;html=1;fillColor={pc}22;"
                         f"strokeColor={pc};fontColor=#000050;fontSize=10;"
                         "verticalAlign=middle;align=center;")
                lbl = f"<b>{lbl}</b><br/><font color='#666666' size='2'>CoE Governed Enterprise License</font>"

            cell = add_cell(root, cid, str(tier_id), lbl, style, bx, by, bw, bh)
            tier_box_ids[ti].append(cid)
            cid += 1

    # Arrows between tiers
    for bi in range(6):
        add_arrow(root, cid, tier_box_ids[0][bi], tier_box_ids[1][bi])
        cid += 1
        add_arrow(root, cid, tier_box_ids[1][bi], tier_box_ids[2][bi])
        cid += 1

    save_xml(mxfile, os.path.join(OUT, "blueprint.drawio"))


if __name__ == "__main__":
    print("Generating draw.io files...")
    make_capability_model_drawio()
    make_domain_model_drawio()
    make_blueprint_drawio()
    print("Done.")
