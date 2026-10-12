# Multi-Signal Device Capability Model — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate a persona-first capability model diagram for a hypothetical multi-signal wearable device, saved as PNG + SVG.

**Architecture:** A single Python/matplotlib script builds a swimlane diagram: 6 vertical persona columns × 3 content rows + a full-width shared data platform footer. Each cell is drawn with FancyBboxPatch following the same style conventions as `projects/Gen Ai Architecture/diagrams/generate_build_refarch.py`.

**Tech Stack:** Python 3, matplotlib, FancyBboxPatch — no new dependencies beyond what the existing diagram script uses.

**Spec:** [docs/superpowers/specs/2026-09-21-multi-signal-device-capability-model-design.md](../../superpowers/specs/2026-09-21-multi-signal-device-capability-model-design.md)

## Global Constraints

- Output directory: `projects/Multi-Signal Device/diagrams/`
- Output files: `capability-model.png` (dpi=180) and `capability-model.svg`
- Script path: `projects/Multi-Signal Device/diagrams/generate_capability_model.py`
- Style: FancyBboxPatch cells, navy/white palette consistent with existing diagrams
- Six personas: Patient, Clinician, Care Team, Researcher, Hospital Administrator, Regulatory
- Three content rows per swimlane: Insights & Actions (top), AI/ML Capabilities (middle), Analytics & Derived Metrics (bottom)
- One full-width footer row: Shared Data Platform (6 components)
- No external data; all content is hardcoded from the spec

## Review Focus

- Footer cells must span the full canvas width (not clipped to one swimlane) — verify `footer_x` and `footer_w` calculations cover full content area
- Row labels on the left must be readable at the chosen figure height — check font size and cell height are sufficient
- All six persona swimlane headers must fit without text overflow — test on narrow canvases by printing the output image
- Long cell text (e.g., "Hospital Administrator") must not overflow its header box — use `\n` linebreaks or reduce font size
- Saving to a non-existent subdirectory silently fails — the script must call `os.makedirs` before `plt.savefig`

---

### Task 1: Scaffold output directory and skeleton script

**Files:**
- Create: `projects/Multi-Signal Device/diagrams/generate_capability_model.py`

**Interfaces:**
- Produces: runnable Python file that imports correctly and creates the output directory

- [ ] **Step 1: Create the output directory in the repo**

```bash
mkdir -p "projects/Multi-Signal Device/diagrams"
```

- [ ] **Step 2: Write the skeleton script with imports, constants, and `os.makedirs` guard**

```python
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

# Persona accent colors (one per swimlane)
PERSONA_COLORS = {
    "Patient":                "#0277BD",   # blue
    "Clinician":              "#2E7D32",   # green
    "Care Team":              "#6A1B9A",   # purple
    "Researcher":             "#E65100",   # orange
    "Hospital Administrator": "#AD1457",   # pink
    "Regulatory":             "#546E7A",   # steel
}

if __name__ == "__main__":
    print("Skeleton OK")
```

- [ ] **Step 3: Run the skeleton to confirm no import errors**

```bash
cd "projects/Multi-Signal Device/diagrams" && python generate_capability_model.py
```
Expected: prints `Skeleton OK` with no errors.

- [ ] **Step 4: Commit**

```bash
git add "projects/Multi-Signal Device/diagrams/generate_capability_model.py"
git commit -m "feat: scaffold multi-signal device capability model script"
```

---

### Task 2: Define content data and layout constants

**Files:**
- Modify: `projects/Multi-Signal Device/diagrams/generate_capability_model.py`

**Interfaces:**
- Produces: `PERSONAS` list of dicts, each with keys `name`, `color`, `rows` (dict with keys `insights`, `aiml`, `analytics`)
- Produces: `PLATFORM_COMPONENTS` list of `(name, subtitle)` tuples
- Produces: layout constants `FIG_W`, `FIG_H`, `SWIMLANE_GAP`, `ROW_H`, `FOOTER_H`, `HEADER_H`, `ROW_LABEL_W`

- [ ] **Step 1: Add PERSONAS data (from spec)**

Replace the `if __name__ == "__main__"` block with the data definitions. Insert before it:

```python
PERSONAS = [
    {
        "name": "Patient",
        "color": PERSONA_COLORS["Patient"],
        "rows": {
            "insights":  "Simplified vitals view\nDaily fluid balance trend\nSymptom logging prompt\nEscalation alert",
            "aiml":      "Personalized baseline\ndeviation detection\nPlain-language LLM summary",
            "analytics": "Relative change from\npersonal baseline\nRolling 7-day trend",
        },
    },
    {
        "name": "Clinician",
        "color": PERSONA_COLORS["Clinician"],
        "rows": {
            "insights":  "Clinical dashboard\nRisk score (0–100)\nSOAP-note draft\nThreshold breach log",
            "aiml":      "Predictive risk scoring\nLLM clinical summary\nAnomaly detection",
            "analytics": "Absolute impedance values\nPressure waveform indices\nFluid volume vs. norms",
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
        "color": PERSONA_COLORS["Hospital Administrator"],
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
    ("Normalization",         "Unit conversion\nnoise filtering"),
    ("Time-Series\nStore",    "Raw + derived signals\npartitioned by patient"),
    ("Feature\nEngineering",  "Impedance → fluid vol\npressure → hemo indices"),
    ("Model\nServing",        "Real-time inference\nrisk & anomaly detection"),
    ("Audit &\nLineage",      "Immutable event log\nconsent management"),
]

ROW_LABELS = ["Insights &\nActions", "AI / ML\nCapabilities", "Analytics &\nDerived Metrics"]

# ── Layout ─────────────────────────────────────────────────────
N_PERSONAS    = len(PERSONAS)
FIG_W         = 28.0
HEADER_H      = 0.9     # persona name bar
ROW_H         = 2.8     # height of each of the 3 content rows
ROW_GAP       = 0.12
FOOTER_H      = 1.6     # shared platform footer
ROW_LABEL_W   = 1.5     # left column for row labels
SWIMLANE_GAP  = 0.10
TITLE_H       = 0.7
BOTTOM_PAD    = 0.20
FIG_H = TITLE_H + HEADER_H + 3 * ROW_H + 2 * ROW_GAP + ROW_GAP + FOOTER_H + BOTTOM_PAD + 0.10
```

- [ ] **Step 2: Verify data loads without error**

```bash
cd "projects/Multi-Signal Device/diagrams" && python -c "import generate_capability_model; print('data OK')"
```
Expected: prints `data OK`.

---

### Task 3: Draw swimlane headers and content cells

**Files:**
- Modify: `projects/Multi-Signal Device/diagrams/generate_capability_model.py`

**Interfaces:**
- Consumes: `PERSONAS`, `ROW_LABELS`, all layout constants from Task 2
- Produces: matplotlib figure with persona header bars and 3×6 content cells rendered

- [ ] **Step 1: Replace the `if __name__` block with the drawing code**

Add this complete drawing section (replacing `if __name__ == "__main__": print("Skeleton OK")`):

```python
def draw_diagram():
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.set_xlim(0, FIG_W)
    ax.set_ylim(0, FIG_H)
    ax.axis("off")
    fig.patch.set_facecolor(BG_COLOR)

    # ── Title ──────────────────────────────────────────────────
    y_title = FIG_H - TITLE_H * 0.4
    ax.text(FIG_W / 2, y_title,
            "Multi-Signal Wearable Device — Persona Capability Model",
            ha="center", va="center", fontsize=13, fontweight="bold", color=NAVY)
    ax.text(FIG_W / 2, y_title - 0.32,
            "Bio-impedance · Pressure · Fluid Movement  |  Six Personas  |  Shared Data Platform",
            ha="center", va="center", fontsize=8, color="#555555", style="italic")

    # ── Geometry helpers ───────────────────────────────────────
    content_x     = ROW_LABEL_W + 0.10    # x where swimlanes start
    content_w     = FIG_W - content_x - 0.15
    sw_w          = (content_w - (N_PERSONAS - 1) * SWIMLANE_GAP) / N_PERSONAS

    # y positions (top-down: title → header → row1 → row2 → row3 → footer)
    y_header_top  = FIG_H - TITLE_H - 0.05
    y_header_bot  = y_header_top - HEADER_H
    y_row = []   # y_row[i] = bottom y of row i (i=0 top = Insights, i=2 bottom = Analytics)
    y_cur = y_header_bot
    for i in range(3):
        y_cur -= ROW_H
        y_row.append(y_cur)
        y_cur -= ROW_GAP
    y_footer_top  = y_row[2] - ROW_GAP
    y_footer_bot  = y_footer_top - FOOTER_H

    # ── Row labels (left column) ────────────────────────────────
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
    ROW_KEYS = ["insights", "aiml", "analytics"]
    for pi, persona in enumerate(PERSONAS):
        sx = content_x + pi * (sw_w + SWIMLANE_GAP)
        col = persona["color"]

        # Header bar
        hdr = FancyBboxPatch((sx, y_header_bot), sw_w, HEADER_H,
                             boxstyle="round,pad=0.03",
                             facecolor=col, edgecolor="none")
        ax.add_patch(hdr)
        ax.text(sx + sw_w / 2, y_header_bot + HEADER_H / 2, persona["name"],
                ha="center", va="center", fontsize=9.5, fontweight="bold",
                color=WHITE, multialignment="center", linespacing=1.25)

        # Content cells
        for ri, key in enumerate(ROW_KEYS):
            ry = y_row[ri]
            cell = FancyBboxPatch((sx + 0.04, ry + 0.04), sw_w - 0.08, ROW_H - 0.08,
                                  boxstyle="round,pad=0.04",
                                  facecolor=WHITE, edgecolor=col, linewidth=1.2)
            ax.add_patch(cell)
            ax.text(sx + sw_w / 2, ry + ROW_H / 2, persona["rows"][key],
                    ha="center", va="center", fontsize=7.0, color=NEAR_BLACK,
                    multialignment="center", linespacing=1.3)

    return fig, ax, content_x, content_w, y_footer_top, y_footer_bot
```

- [ ] **Step 2: Add the `if __name__` block that calls draw_diagram and saves PNG/SVG (add this after the function)**

```python
if __name__ == "__main__":
    fig, ax, content_x, content_w, y_footer_top, y_footer_bot = draw_diagram()

    # ── Shared Data Platform footer ────────────────────────────
    footer_x = content_x
    footer_w = content_w
    footer_y = y_footer_bot

    # Footer outer box
    footer_bg = FancyBboxPatch((footer_x, footer_y), footer_w, FOOTER_H,
                               boxstyle="round,pad=0.04",
                               facecolor=NAVY, edgecolor="none")
    ax.add_patch(footer_bg)

    # Footer title
    ax.text(footer_x + footer_w / 2, footer_y + FOOTER_H - 0.28,
            "SHARED DATA PLATFORM",
            ha="center", va="center", fontsize=9.5, fontweight="bold", color=WHITE)

    # Footer component chips
    n_comp  = len(PLATFORM_COMPONENTS)
    chip_gap = 0.10
    chip_w  = (footer_w - (n_comp - 1) * chip_gap - 0.20) / n_comp
    chip_h  = FOOTER_H - 0.60
    for ci, (name, subtitle) in enumerate(PLATFORM_COMPONENTS):
        cx = footer_x + 0.10 + ci * (chip_w + chip_gap)
        cy = footer_y + 0.10
        chip = FancyBboxPatch((cx, cy), chip_w, chip_h,
                              boxstyle="round,pad=0.03",
                              facecolor="#1A3A6B", edgecolor="#4A7CC7", linewidth=1.0)
        ax.add_patch(chip)
        ax.text(cx + chip_w / 2, cy + chip_h * 0.65, name,
                ha="center", va="center", fontsize=8.0, fontweight="bold",
                color=WHITE, multialignment="center", linespacing=1.2)
        ax.text(cx + chip_w / 2, cy + chip_h * 0.25, subtitle,
                ha="center", va="center", fontsize=6.5, color="#AACCFF",
                style="italic", multialignment="center", linespacing=1.2)

    # ── Footer row label ───────────────────────────────────────
    fl_patch = FancyBboxPatch((0.05, footer_y), ROW_LABEL_W - 0.12, FOOTER_H,
                              boxstyle="round,pad=0.03",
                              facecolor="#0D1A3A", edgecolor="none")
    ax.add_patch(fl_patch)
    ax.text(0.05 + (ROW_LABEL_W - 0.12) / 2, footer_y + FOOTER_H / 2,
            "Shared\nData\nPlatform",
            ha="center", va="center", fontsize=7.5, fontweight="bold",
            color=WHITE, multialignment="center", linespacing=1.3)

    plt.tight_layout(pad=0.15)
    out_png = os.path.join(OUT_DIR, "capability-model.png")
    out_svg = os.path.join(OUT_DIR, "capability-model.svg")
    plt.savefig(out_png, dpi=180, bbox_inches="tight", facecolor=BG_COLOR)
    plt.savefig(out_svg, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close()
    print(f"Saved: {out_png}")
    print(f"Saved: {out_svg}")
```

- [ ] **Step 3: Run the script and verify both output files are created**

```bash
cd "projects/Multi-Signal Device/diagrams" && python generate_capability_model.py
ls -lh capability-model.png capability-model.svg
```
Expected: two files exist, PNG > 100 KB.

- [ ] **Step 4: Open the PNG and visually verify**
  - 6 persona header bars visible across the top
  - 3 content rows with correct labels on the left
  - Dark navy footer with 6 component chips

- [ ] **Step 5: Commit**

```bash
git add "projects/Multi-Signal Device/diagrams/generate_capability_model.py" \
        "projects/Multi-Signal Device/diagrams/capability-model.png" \
        "projects/Multi-Signal Device/diagrams/capability-model.svg"
git commit -m "feat: add multi-signal device capability model diagram (PNG + SVG)

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```
