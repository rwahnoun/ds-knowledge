"""
Extract structured data from all 31 biomarker markdown sheets and generate
publication-quality summary figures for the Usense Healthcare Urinary Biomarkers
Compendium.
"""

import os, re, json, sys
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import matplotlib.patches as mpatches
from pathlib import Path

OUT = Path("D:/code/ds-knowledge/biomarkers/singleBiomarkers/outputs")
FIG = Path("D:/code/ds-knowledge/biomarkers/singleBiomarkers/figures")
FIG.mkdir(exist_ok=True)

# ── Colour palette (Usense brand: navy + amber) ──
NAVY   = "#1B2A4A"
AMBER  = "#F5A623"
TEAL   = "#2CA6A4"
CORAL  = "#E85D75"
SLATE  = "#6B7B8D"
LIGHT  = "#EBF0F5"
COLORS = [NAVY, AMBER, TEAL, CORAL, SLATE, "#8E6FBF", "#3CB371", "#CD853F", "#4682B4", "#D4A574"]

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Cambria", "Times New Roman", "DejaVu Serif"],
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "axes.edgecolor": NAVY,
    "axes.linewidth": 0.8,
    "xtick.color": NAVY,
    "ytick.color": NAVY,
    "text.color": NAVY,
    "figure.dpi": 200,
    "savefig.dpi": 200,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.15,
})

# ═══════════════════════════════════════════════════════════════════
# 1. CLASSIFY BIOMARKERS
# ═══════════════════════════════════════════════════════════════════

BIOMARKER_DATA = {
    # name: (display_name, category, MW_Da, typical_urine_conc_mM, is_normally_present)
    "porphobilinogen":       ("Porphobilinogen (PBG)", "Porphyrin Metabolite", 226.23, 0.009, True),
    "total-urinary-porphyrin": ("Total Urinary Porphyrin", "Porphyrin Metabolite", 700, 0.0003, True),
    "bacteria":              ("Bacteria", "Cellular Element", None, None, False),
    "red-blood-cells":       ("Red Blood Cells", "Cellular Element", None, None, False),
    "haemoglobin":           ("Haemoglobin", "Cellular Element", 64458, None, False),
    "nitrites":              ("Nitrites", "Infection Marker", 46.01, 0, False),
    "white-blood-cells":     ("White Blood Cells", "Cellular Element", None, None, False),
    "leukocytes":            ("Leukocyte Esterase", "Infection Marker", 27500, None, False),
    "sodium":                ("Sodium", "Electrolyte", 22.99, 100, True),
    "chloride":              ("Chloride", "Electrolyte", 35.45, 120, True),
    "creatinin":             ("Creatinine", "Renal Function", 113.12, 10, True),
    "phosphate":             ("Phosphate", "Electrolyte", 94.97, 25, True),
    "magnesium":             ("Magnesium", "Electrolyte", 24.31, 4, True),
    "usg":                   ("USG", "Physical Property", None, None, True),
    "osmolality":            ("Osmolality", "Physical Property", None, None, True),
    "glucose":               ("Glucose", "Metabolite", 180.16, 0.5, False),
    "ketone":                ("Ketone Bodies", "Metabolite", 102.09, 0.3, False),
    "bilirubin":             ("Bilirubin", "Metabolite", 584.66, 0, False),
    "urea":                  ("Urea", "Renal Function", 60.06, 300, True),
    "uric-acid":             ("Uric Acid", "Metabolite", 168.11, 3, True),
    "nadh":                  ("NADH", "Coenzyme/Vitamin", 665.44, 0.001, True),
    "fad":                   ("FAD", "Coenzyme/Vitamin", 785.55, 0.001, True),
    "riboflavin":            ("Riboflavin (B2)", "Coenzyme/Vitamin", 376.36, 0.003, True),
    "oxalate":               ("Oxalate", "Metabolite", 90.03, 1.5, True),
    "citrate":               ("Citrate", "Metabolite", 192.12, 2.5, True),
    "ph":                    ("pH", "Physical Property", None, None, True),
    "tryptophan":            ("Tryptophan", "Amino Acid", 204.23, 0.05, True),
    "copper":                ("Copper", "Trace Element", 63.55, 0.0005, True),
    "metolachlore":          ("Metolachlor", "Environmental Contaminant", 283.79, 0.00001, False),
    "pfas":                  ("PFAS", "Environmental Contaminant", 414, 0.000001, False),
    "chlorotalonil":         ("Chlorothalonil", "Environmental Contaminant", 265.91, 0.00001, False),
}

# ═══════════════════════════════════════════════════════════════════
# 2. DETECTION METHOD MATRIX
# ═══════════════════════════════════════════════════════════════════

# For each biomarker, which detection modalities are viable?
# 0 = not applicable/not practical, 1 = research/limited, 2 = established/clinical
DETECTION_METHODS = [
    "Dipstick/POC", "Spectrophotometry", "Fluorescence", "Raman/SERS",
    "FTIR", "Electrochemical", "HPLC/LC-MS", "Flow Cytometry", "Microscopy"
]

DETECTION_MATRIX = {
    "porphobilinogen":       [1, 2, 2, 0, 0, 0, 2, 0, 0],
    "total-urinary-porphyrin":[1, 2, 2, 1, 1, 1, 2, 0, 0],
    "bacteria":              [2, 0, 1, 1, 1, 1, 0, 2, 2],
    "red-blood-cells":       [2, 2, 1, 1, 1, 1, 0, 2, 2],
    "haemoglobin":           [2, 2, 1, 1, 1, 1, 0, 0, 0],
    "nitrites":              [2, 2, 1, 1, 0, 2, 1, 0, 0],
    "white-blood-cells":     [2, 0, 1, 1, 1, 1, 0, 2, 2],
    "leukocytes":            [2, 1, 1, 0, 0, 1, 0, 0, 2],
    "sodium":                [0, 1, 1, 0, 0, 2, 0, 0, 0],
    "chloride":              [0, 2, 1, 0, 0, 2, 1, 0, 0],
    "creatinin":             [0, 2, 2, 2, 2, 2, 2, 0, 0],
    "phosphate":             [0, 2, 1, 1, 1, 2, 0, 0, 0],
    "magnesium":             [0, 2, 1, 0, 0, 1, 0, 0, 0],
    "usg":                   [2, 0, 0, 0, 1, 0, 0, 0, 0],
    "osmolality":            [0, 0, 0, 0, 0, 0, 0, 0, 0],
    "glucose":               [2, 2, 2, 1, 1, 2, 0, 0, 0],
    "ketone":                [2, 2, 1, 1, 1, 1, 0, 0, 0],
    "bilirubin":             [2, 2, 1, 0, 0, 1, 0, 0, 0],
    "urea":                  [1, 2, 2, 2, 2, 2, 0, 0, 0],
    "uric-acid":             [0, 2, 2, 2, 1, 2, 2, 0, 0],
    "nadh":                  [0, 2, 2, 0, 0, 2, 2, 0, 0],
    "fad":                   [0, 2, 2, 1, 0, 1, 2, 0, 0],
    "riboflavin":            [0, 2, 2, 1, 0, 1, 2, 0, 0],
    "oxalate":               [0, 1, 1, 1, 0, 1, 2, 0, 0],
    "citrate":               [0, 1, 1, 1, 0, 0, 2, 0, 0],
    "ph":                    [2, 0, 1, 0, 0, 2, 0, 0, 0],
    "tryptophan":            [0, 1, 2, 2, 0, 2, 2, 0, 0],
    "copper":                [0, 2, 1, 0, 0, 2, 0, 0, 0],
    "metolachlore":          [0, 1, 0, 0, 0, 1, 2, 0, 0],
    "pfas":                  [0, 0, 1, 1, 0, 1, 2, 0, 0],
    "chlorotalonil":         [0, 0, 1, 1, 1, 1, 2, 0, 0],
}

# ═══════════════════════════════════════════════════════════════════
# FIGURE 1: Biomarker Classification Treemap / Pie
# ═══════════════════════════════════════════════════════════════════

def fig1_classification():
    cats = {}
    for k, v in BIOMARKER_DATA.items():
        cat = v[1]
        cats.setdefault(cat, []).append(v[0])
    
    labels = []
    sizes = []
    cat_colors = {
        "Electrolyte": NAVY, "Renal Function": TEAL, "Metabolite": AMBER,
        "Cellular Element": CORAL, "Infection Marker": "#D4A574",
        "Porphyrin Metabolite": "#8E6FBF", "Coenzyme/Vitamin": "#3CB371",
        "Physical Property": SLATE, "Amino Acid": "#4682B4",
        "Trace Element": "#CD853F", "Environmental Contaminant": "#E8453C"
    }
    colors = []
    
    for cat, members in sorted(cats.items(), key=lambda x: -len(x[1])):
        labels.append(f"{cat}\n({len(members)})")
        sizes.append(len(members))
        colors.append(cat_colors.get(cat, SLATE))
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Donut chart
    wedges, texts, autotexts = ax1.pie(sizes, labels=None, colors=colors,
        autopct=lambda p: f'{int(round(p*sum(sizes)/100))}' if p > 5 else '',
        startangle=90, pctdistance=0.75,
        wedgeprops=dict(width=0.45, edgecolor='white', linewidth=2))
    for t in autotexts:
        t.set_fontsize(11)
        t.set_fontweight("bold")
        t.set_color("white")
    ax1.legend(wedges, [l.replace('\n', ' ') for l in labels],
               loc="center left", bbox_to_anchor=(-0.3, 0.5), fontsize=8, frameon=False)
    ax1.set_title("Biomarker Categories", fontweight="bold", pad=15)
    
    # Presence chart
    present = sum(1 for v in BIOMARKER_DATA.values() if v[4])
    absent = sum(1 for v in BIOMARKER_DATA.values() if not v[4])
    bars = ax2.barh(["Normally\npresent", "Normally\nabsent"], [present, absent],
                    color=[TEAL, CORAL], edgecolor="white", height=0.5)
    for bar, val in zip(bars, [present, absent]):
        ax2.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
                 str(val), va='center', fontweight='bold', fontsize=13)
    ax2.set_xlim(0, max(present, absent) + 3)
    ax2.set_title("Normal Presence in Urine", fontweight="bold", pad=15)
    ax2.spines[['top', 'right']].set_visible(False)
    ax2.set_xlabel("Number of Biomarkers")
    
    fig.suptitle("Figure 1 — Classification of 31 Urinary Biomarkers", 
                 fontsize=13, fontweight="bold", y=1.02)
    plt.tight_layout()
    fig.savefig(FIG / "fig1_classification.png")
    plt.close()
    print("[OK] Figure 1 saved")


# ═══════════════════════════════════════════════════════════════════
# FIGURE 2: Molecular Weight Spectrum
# ═══════════════════════════════════════════════════════════════════

def fig2_molecular_weight():
    mw_data = [(v[0], v[2], v[1]) for k, v in BIOMARKER_DATA.items() if v[2] is not None]
    mw_data.sort(key=lambda x: x[1])
    
    names = [d[0] for d in mw_data]
    mws = [d[1] for d in mw_data]
    cats = [d[2] for d in mw_data]
    
    cat_colors = {
        "Electrolyte": NAVY, "Renal Function": TEAL, "Metabolite": AMBER,
        "Cellular Element": CORAL, "Infection Marker": "#D4A574",
        "Porphyrin Metabolite": "#8E6FBF", "Coenzyme/Vitamin": "#3CB371",
        "Physical Property": SLATE, "Amino Acid": "#4682B4",
        "Trace Element": "#CD853F", "Environmental Contaminant": "#E8453C"
    }
    bar_colors = [cat_colors.get(c, SLATE) for c in cats]
    
    fig, ax = plt.subplots(figsize=(14, 7))
    bars = ax.barh(range(len(names)), mws, color=bar_colors, edgecolor="white", height=0.7)
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names, fontsize=8)
    ax.set_xscale("log")
    ax.set_xlabel("Molecular Weight (Da) — log scale")
    ax.set_title("Figure 2 — Molecular Weight Spectrum of Urinary Biomarkers", fontweight="bold")
    ax.spines[['top', 'right']].set_visible(False)
    
    # Annotate key thresholds
    ax.axvline(x=500, color=CORAL, linestyle="--", alpha=0.5, linewidth=1)
    ax.text(500, len(names)-0.5, "Small molecule\nthreshold (~500 Da)", fontsize=7,
            color=CORAL, ha="center", va="bottom")
    
    # Add MW labels
    for i, (bar, mw) in enumerate(zip(bars, mws)):
        label = f"{mw:,.0f}" if mw > 1000 else f"{mw:.1f}"
        ax.text(bar.get_width() * 1.1, bar.get_y() + bar.get_height()/2,
                f"{label} Da", va='center', fontsize=6.5, color=NAVY)
    
    # Legend
    unique_cats = list(dict.fromkeys(cats))
    handles = [mpatches.Patch(color=cat_colors.get(c, SLATE), label=c) for c in sorted(set(cats))]
    ax.legend(handles=handles, loc="lower right", fontsize=7, frameon=True, facecolor="white")
    
    plt.tight_layout()
    fig.savefig(FIG / "fig2_molecular_weight.png")
    plt.close()
    print("[OK] Figure 2 saved")


# ═══════════════════════════════════════════════════════════════════
# FIGURE 3: Detection Method Heatmap
# ═══════════════════════════════════════════════════════════════════

def fig3_detection_heatmap():
    # Order biomarkers by category
    ordered_keys = sorted(DETECTION_MATRIX.keys(), 
                         key=lambda k: (BIOMARKER_DATA[k][1], BIOMARKER_DATA[k][0]))
    display_names = [BIOMARKER_DATA[k][0] for k in ordered_keys]
    matrix = np.array([DETECTION_MATRIX[k] for k in ordered_keys])
    
    fig, ax = plt.subplots(figsize=(12, 14))
    
    # Custom colormap: white -> light amber -> dark navy
    from matplotlib.colors import ListedColormap
    cmap = ListedColormap(["#F5F5F5", "#FFE4B5", TEAL])
    
    im = ax.imshow(matrix, cmap=cmap, aspect="auto", vmin=0, vmax=2)
    
    ax.set_xticks(range(len(DETECTION_METHODS)))
    ax.set_xticklabels(DETECTION_METHODS, rotation=45, ha="right", fontsize=9)
    ax.set_yticks(range(len(display_names)))
    ax.set_yticklabels(display_names, fontsize=8)
    
    # Add text annotations
    labels_map = {0: "—", 1: "R", 2: "C"}
    for i in range(len(display_names)):
        for j in range(len(DETECTION_METHODS)):
            val = matrix[i, j]
            color = "white" if val == 2 else NAVY
            ax.text(j, i, labels_map[val], ha="center", va="center",
                   fontsize=8, fontweight="bold" if val == 2 else "normal", color=color)
    
    # Category separators
    cats_ordered = [BIOMARKER_DATA[k][1] for k in ordered_keys]
    prev_cat = None
    for i, cat in enumerate(cats_ordered):
        if cat != prev_cat and prev_cat is not None:
            ax.axhline(y=i-0.5, color=NAVY, linewidth=1.5, alpha=0.3)
        prev_cat = cat
    
    # Legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0],[0], marker='s', color='w', markerfacecolor="#F5F5F5", markersize=12, label='Not applicable (—)'),
        Line2D([0],[0], marker='s', color='w', markerfacecolor="#FFE4B5", markersize=12, label='Research stage (R)'),
        Line2D([0],[0], marker='s', color='w', markerfacecolor=TEAL, markersize=12, label='Clinical/established (C)'),
    ]
    ax.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, -0.05),
             ncol=3, fontsize=9, frameon=True, facecolor="white")
    
    ax.set_title("Figure 3 — Detection Method Applicability Matrix\nC = Clinical / Established   R = Research Stage   — = Not Applicable",
                fontweight="bold", pad=15)
    
    plt.tight_layout()
    fig.savefig(FIG / "fig3_detection_heatmap.png")
    plt.close()
    print("[OK] Figure 3 saved")


# ═══════════════════════════════════════════════════════════════════
# FIGURE 4: Urinary Concentration Ranges (log scale)
# ═══════════════════════════════════════════════════════════════════

def fig4_concentration_ranges():
    conc_data = [(v[0], v[3], v[1]) for k, v in BIOMARKER_DATA.items() 
                 if v[3] is not None and v[3] > 0]
    conc_data.sort(key=lambda x: x[1])
    
    names = [d[0] for d in conc_data]
    concs = [d[1] for d in conc_data]
    cats = [d[2] for d in conc_data]
    
    cat_colors = {
        "Electrolyte": NAVY, "Renal Function": TEAL, "Metabolite": AMBER,
        "Cellular Element": CORAL, "Infection Marker": "#D4A574",
        "Porphyrin Metabolite": "#8E6FBF", "Coenzyme/Vitamin": "#3CB371",
        "Physical Property": SLATE, "Amino Acid": "#4682B4",
        "Trace Element": "#CD853F", "Environmental Contaminant": "#E8453C"
    }
    bar_colors = [cat_colors.get(c, SLATE) for c in cats]
    
    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.barh(range(len(names)), concs, color=bar_colors, edgecolor="white", height=0.7)
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names, fontsize=8)
    ax.set_xscale("log")
    ax.set_xlabel("Typical Urinary Concentration (mmol/L) — log scale")
    ax.set_title("Figure 4 — Urinary Concentration Ranges: 8 Orders of Magnitude",
                fontweight="bold")
    ax.spines[['top', 'right']].set_visible(False)
    
    # Add concentration labels
    for i, (bar, c) in enumerate(zip(bars, concs)):
        if c >= 1:
            label = f"{c:.0f} mM"
        elif c >= 0.001:
            label = f"{c*1000:.1f} µM"
        else:
            label = f"{c*1e6:.1f} nM"
        ax.text(bar.get_width() * 1.3, bar.get_y() + bar.get_height()/2,
                label, va='center', fontsize=7, color=NAVY)
    
    # Annotate zones
    ax.axvspan(0.1, 1000, alpha=0.03, color=TEAL)
    ax.axvspan(1e-7, 0.001, alpha=0.03, color=CORAL)
    ax.text(50, len(names)-0.5, "Major solutes", fontsize=8, color=TEAL, alpha=0.7, style="italic")
    ax.text(1e-5, len(names)-0.5, "Trace analytes", fontsize=8, color=CORAL, alpha=0.7, style="italic")
    
    handles = [mpatches.Patch(color=cat_colors.get(c, SLATE), label=c) for c in sorted(set(cats))]
    ax.legend(handles=handles, loc="lower right", fontsize=7, frameon=True, facecolor="white")
    
    plt.tight_layout()
    fig.savefig(FIG / "fig4_concentration_ranges.png")
    plt.close()
    print("[OK] Figure 4 saved")


# ═══════════════════════════════════════════════════════════════════
# FIGURE 5: Spectroscopic Fingerprint Map
# ═══════════════════════════════════════════════════════════════════

def wavelength_to_rgb(nm):
    """Return an (r,g,b) tuple approximating the visible spectrum colour at `nm`."""
    if nm < 380:
        return (0.25, 0.0, 0.4)   # UV → deep violet
    if nm > 780:
        return (0.4, 0.0, 0.0)    # NIR → dark red
    # Piecewise mapping based on CIE approximation
    if nm < 440:
        r, g, b = -(nm - 440) / 60, 0.0, 1.0
    elif nm < 490:
        r, g, b = 0.0, (nm - 440) / 50, 1.0
    elif nm < 510:
        r, g, b = 0.0, 1.0, -(nm - 510) / 20
    elif nm < 580:
        r, g, b = (nm - 510) / 70, 1.0, 0.0
    elif nm < 645:
        r, g, b = 1.0, -(nm - 645) / 65, 0.0
    else:
        r, g, b = 1.0, 0.0, 0.0
    # Intensity falloff near edges
    if nm < 420:
        f = 0.3 + 0.7 * (nm - 380) / 40
    elif nm > 700:
        f = 0.3 + 0.7 * (780 - nm) / 80
    else:
        f = 1.0
    return (r * f, g * f, b * f)


# Extracted from the 31 biomarker sheets (values verbatim from outputs/*.md)
# Stored here so multiple figures can share one source of truth.
SPECTRO_DATA = {
    "Urea":        {"abs": [], "ex": [], "em": [],
                    "Raman": [(1003, "ν(C–N)")],
                    "FTIR":  [(1468, "ν_as(C–N)")]},
    "Creatinine":  {"abs": [234], "ex": [571], "em": [585],
                    "Raman": [(680, "ring"), (1490, "C=N")],
                    "FTIR":  [(1492, "C=N"), (1670, "C=O")]},
    "Uric Acid":   {"abs": [293], "ex": [], "em": [],
                    "Raman": [(630, "ring"), (1370, "C=N")],
                    "FTIR":  [(1590, "C=C"), (1680, "C=O")]},
    "Glucose":     {"abs": [505], "ex": [], "em": [],
                    "Raman": [(1065, "C–O"), (1130, "C–O–H")],
                    "FTIR":  [(1035, "C–O")]},
    "Bilirubin":   {"abs": [453], "ex": [], "em": [],
                    "Raman": [(1575, "pyrrole"), (1615, "C=C")],
                    "FTIR":  [(1620, "C=C"), (1690, "C=O")]},
    "Haemoglobin": {"abs": [415, 542, 577], "ex": [], "em": [],
                    "Raman": [(675, "pyrrole"), (1375, "ν₄"), (1580, "spin")],
                    "FTIR":  [(1650, "amide I")]},
    "Tryptophan":  {"abs": [280], "ex": [280], "em": [348],
                    "Raman": [(760, "indole"), (1550, "W3")],
                    "FTIR":  [(1580, "indole")]},
    "NADH":        {"abs": [340], "ex": [340], "em": [460],
                    "Raman": [(1030, "nic. ring"), (1580, "C=C")],
                    "FTIR":  [(1580, "C=C"), (1690, "amide")]},
    "FAD":         {"abs": [450], "ex": [450], "em": [525],
                    "Raman": [(1350, "isoallox."), (1580, "C=C")],
                    "FTIR":  [(1580, "C=C"), (1650, "C=O")]},
    "Riboflavin":  {"abs": [450], "ex": [450], "em": [525],
                    "Raman": [(1350, "isoallox."), (1500, "C=N"), (1580, "C=C")],
                    "FTIR":  [(1580, "C=C"), (1650, "C=O")]},
    "Porphyrins":  {"abs": [405], "ex": [405], "em": [620],
                    "Raman": [(755, "pyrrole"), (1375, "half-ring"), (1555, "Cβ–Cβ")],
                    "FTIR":  [(1605, "C=C"), (1710, "C=O")]},
    "Nitrites":    {"abs": [354, 540], "ex": [], "em": [],
                    "Raman": [(1240, "NO₂ as"), (1330, "NO₂ s")],
                    "FTIR":  [(1275, "NO₂ as"), (1330, "NO₂ s")]},
    "Oxalate":     {"abs": [], "ex": [], "em": [],
                    "Raman": [(890, "C–C"), (1460, "C–O s"), (1620, "C=O as")],
                    "FTIR":  [(1320, "C–O s"), (1620, "C=O as")]},
    "Citrate":     {"abs": [], "ex": [], "em": [],
                    "Raman": [(1390, "COO⁻ s"), (1580, "COO⁻ as")],
                    "FTIR":  [(1390, "COO⁻ s"), (1580, "COO⁻ as")]},
    "Ketones":     {"abs": [], "ex": [], "em": [],
                    "Raman": [(1365, "CH₃"), (1710, "C=O")],
                    "FTIR":  [(1720, "C=O")]},
}


def fig5_spectroscopic_map():
    """Two-panel Raman+FTIR fingerprint map for the key small-molecule biomarkers."""
    # Keep only analytes that have vibrational data
    order = [n for n in SPECTRO_DATA if SPECTRO_DATA[n]["Raman"] or SPECTRO_DATA[n]["FTIR"]]
    # Reverse so the first entry sits on top
    order = list(reversed(order))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), sharey=True,
                                    gridspec_kw={"width_ratios": [1, 1], "wspace": 0.05})

    for i, name in enumerate(order):
        d = SPECTRO_DATA[name]
        for cm, lbl in d["Raman"]:
            ax1.scatter(cm, i, marker="o", s=80, color=CORAL, edgecolor="white",
                        linewidth=0.8, zorder=5)
            ax1.annotate(f"{cm}", (cm, i), textcoords="offset points",
                         xytext=(0, 9), fontsize=6.5, ha="center", color=NAVY,
                         fontweight="bold")
            ax1.annotate(lbl, (cm, i), textcoords="offset points",
                         xytext=(0, -13), fontsize=5.5, ha="center",
                         color=SLATE, style="italic")
        for cm, lbl in d["FTIR"]:
            ax2.scatter(cm, i, marker="s", s=80, color=NAVY, edgecolor="white",
                        linewidth=0.8, zorder=5)
            ax2.annotate(f"{cm}", (cm, i), textcoords="offset points",
                         xytext=(0, 9), fontsize=6.5, ha="center", color=NAVY,
                         fontweight="bold")
            ax2.annotate(lbl, (cm, i), textcoords="offset points",
                         xytext=(0, -13), fontsize=5.5, ha="center",
                         color=SLATE, style="italic")

    for ax, title, xlim in [
        (ax1, "A. Raman-active bands", (550, 1800)),
        (ax2, "B. FTIR absorption bands", (950, 1800)),
    ]:
        ax.set_yticks(range(len(order)))
        ax.set_yticklabels(order, fontsize=9)
        ax.set_xlabel("Wavenumber (cm⁻¹)")
        ax.set_xlim(xlim)
        ax.set_ylim(-0.7, len(order) - 0.3)
        ax.grid(True, axis="x", linestyle=":", alpha=0.4, color=SLATE)
        ax.spines[['top', 'right']].set_visible(False)
        ax.set_title(title, fontweight="bold", pad=10)

        # Shade the "biological fingerprint" region 1000–1700 cm⁻¹
        ax.axvspan(1000, 1700, alpha=0.04, color=TEAL, zorder=0)

    fig.suptitle("Figure 5 — Vibrational Fingerprint Atlas (Raman & FTIR) of 15 Key Urinary Biomarkers",
                 fontsize=13, fontweight="bold", y=1.00)
    plt.tight_layout()
    fig.savefig(FIG / "fig5_spectroscopic_map.png")
    plt.close()
    print("[OK] Figure 5 saved")


def fig8_wavelength_landscape():
    """Visible-spectrum landscape showing absorption, fluorescence ex/em wavelengths."""
    # Only analytes with UV-Vis/fluorescence data
    order = [n for n in SPECTRO_DATA if SPECTRO_DATA[n]["abs"] or SPECTRO_DATA[n]["ex"]]
    # Sort by primary absorption (or ex) wavelength
    def sort_key(n):
        d = SPECTRO_DATA[n]
        if d["abs"]:
            return min(d["abs"])
        if d["ex"]:
            return min(d["ex"])
        return 9999
    order.sort(key=sort_key)

    fig, ax = plt.subplots(figsize=(14, 7))

    # Background visible-spectrum gradient from 380–780 nm
    xmin, xmax = 200, 700
    n_bins = 500
    wls = np.linspace(xmin, xmax, n_bins)
    rgb = np.array([wavelength_to_rgb(w) for w in wls])
    rgba = np.concatenate([rgb, np.full((n_bins, 1), 0.25)], axis=1).reshape(1, n_bins, 4)
    ax.imshow(rgba, aspect="auto", extent=[xmin, xmax, -0.6, len(order) - 0.4],
              zorder=0, interpolation="bilinear")

    # UV region shading (<380 nm) in grey
    ax.axvspan(xmin, 380, color="#4A4A4A", alpha=0.10, zorder=0)
    ax.text(285, len(order) - 0.1, "UV", fontsize=10, color=SLATE, fontweight="bold",
            ha="center", va="top", style="italic")
    ax.text(550, len(order) - 0.1, "Visible", fontsize=10, color=NAVY, fontweight="bold",
            ha="center", va="top", style="italic")

    for i, name in enumerate(order):
        d = SPECTRO_DATA[name]
        # Faint baseline
        ax.plot([xmin, xmax], [i, i], color=SLATE, alpha=0.15, linewidth=0.5, zorder=1)
        # Absorption (diamonds)
        for wl in d["abs"]:
            ax.scatter(wl, i, marker="D", s=110, color=NAVY, edgecolor="white",
                       linewidth=1.2, zorder=5)
            ax.annotate(f"{wl}", (wl, i), textcoords="offset points",
                        xytext=(0, 10), fontsize=7, ha="center", color=NAVY,
                        fontweight="bold")
        # Fluorescence ex (up triangles) and em (down triangles), with arrow for Stokes shift
        if d["ex"] and d["em"]:
            ex_wl, em_wl = d["ex"][0], d["em"][0]
            # Stokes shift arrow
            ax.annotate("", xy=(em_wl, i), xytext=(ex_wl, i),
                        arrowprops=dict(arrowstyle="->", color=CORAL, lw=1.8,
                                         alpha=0.65, shrinkA=7, shrinkB=7),
                        zorder=3)
        for wl in d["ex"]:
            ax.scatter(wl, i, marker="^", s=130, color=TEAL, edgecolor="white",
                       linewidth=1.2, zorder=5)
            ax.annotate(f"ex {wl}", (wl, i), textcoords="offset points",
                        xytext=(0, -15), fontsize=6.5, ha="center", color=TEAL,
                        fontweight="bold")
        for wl in d["em"]:
            ax.scatter(wl, i, marker="v", s=130, color=AMBER, edgecolor="white",
                       linewidth=1.2, zorder=5)
            ax.annotate(f"em {wl}", (wl, i), textcoords="offset points",
                        xytext=(0, -15), fontsize=6.5, ha="center", color="#B8761A",
                        fontweight="bold")

    ax.set_yticks(range(len(order)))
    ax.set_yticklabels(order, fontsize=10)
    ax.set_xlabel("Wavelength (nm)", fontsize=11)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(-0.6, len(order) - 0.4)
    ax.spines[['top', 'right']].set_visible(False)
    ax.set_title("Figure 8 — Optical Spectral Landscape: Absorption & Fluorescence of Urinary Biomarkers",
                 fontweight="bold", fontsize=13, pad=15)

    # Common laser / LED excitation lines
    common_lines = [(365, "UV LED"), (405, "405 nm"), (488, "488 nm"),
                    (532, "532 nm"), (633, "633 nm")]
    for wl, lbl in common_lines:
        ax.axvline(wl, color="white", linestyle="--", alpha=0.35, linewidth=0.8, zorder=2)
        ax.text(wl, -0.55, lbl, fontsize=6, ha="center", color=NAVY,
                fontstyle="italic", alpha=0.8)

    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='D', color='w', markerfacecolor=NAVY, markersize=10,
               markeredgecolor="white", label='Absorption λ_max'),
        Line2D([0], [0], marker='^', color='w', markerfacecolor=TEAL, markersize=10,
               markeredgecolor="white", label='Fluorescence excitation'),
        Line2D([0], [0], marker='v', color='w', markerfacecolor=AMBER, markersize=10,
               markeredgecolor="white", label='Fluorescence emission'),
        Line2D([0], [0], color=CORAL, lw=2, label='Stokes shift'),
    ]
    ax.legend(handles=legend_elements, loc="upper left", bbox_to_anchor=(1.01, 1.0),
              fontsize=9, frameon=True, facecolor="white", framealpha=0.95)

    plt.tight_layout()
    fig.savefig(FIG / "fig8_wavelength_landscape.png")
    plt.close()
    print("[OK] Figure 8 saved")


# ═══════════════════════════════════════════════════════════════════
# FIGURE 6: Detection Method Technology Radar
# ═══════════════════════════════════════════════════════════════════

def fig6_method_coverage():
    """Bar chart showing how many biomarkers each detection method covers."""
    matrix = np.array([DETECTION_MATRIX[k] for k in DETECTION_MATRIX.keys()])
    
    clinical_counts = (matrix == 2).sum(axis=0)
    research_counts = (matrix == 1).sum(axis=0)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.arange(len(DETECTION_METHODS))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, clinical_counts, width, label="Clinical/Established",
                   color=TEAL, edgecolor="white")
    bars2 = ax.bar(x + width/2, research_counts, width, label="Research Stage",
                   color=AMBER, edgecolor="white")
    
    ax.set_xticks(x)
    ax.set_xticklabels(DETECTION_METHODS, rotation=30, ha="right", fontsize=9)
    ax.set_ylabel("Number of Biomarkers")
    ax.set_title("Figure 6 — Detection Technology Coverage Across 31 Biomarkers",
                fontweight="bold")
    ax.spines[['top', 'right']].set_visible(False)
    ax.legend(frameon=True, facecolor="white")
    
    # Add value labels
    for bar in bars1:
        if bar.get_height() > 0:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                   str(int(bar.get_height())), ha='center', fontsize=9, fontweight='bold', color=TEAL)
    for bar in bars2:
        if bar.get_height() > 0:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                   str(int(bar.get_height())), ha='center', fontsize=9, fontweight='bold', color=AMBER)
    
    plt.tight_layout()
    fig.savefig(FIG / "fig6_method_coverage.png")
    plt.close()
    print("[OK] Figure 6 saved")


# ═══════════════════════════════════════════════════════════════════
# FIGURE 7: Clinical vs Research LOD gap
# ═══════════════════════════════════════════════════════════════════

def fig7_lod_comparison():
    """Compare best clinical LOD vs best research LOD for selected biomarkers (normalised to clinical range)."""
    
    # (biomarker, clinical_LOD_mM, best_research_LOD_mM, typical_clinical_mM)
    lod_data = [
        ("Urea",        0.1,      5.68e-6,    300),
        ("Creatinine",  0.009,    0.0005,     10),
        ("Uric Acid",   0.006,    0.0001,     3),
        ("Glucose",     2.8,      0.001,      0.5),
        ("Bilirubin",   0.085,    0.00085,    0),
        ("NADH",        0.001,    0.00001,    0.001),
        ("Riboflavin",  0.0001,   0.0000001,  0.003),
        ("Tryptophan",  0.005,    0.00001,    0.05),
        ("Nitrites",    0.011,    0.000001,   0),
        ("Copper",      0.008,    0.00008,    0.0005),
    ]
    
    names = [d[0] for d in lod_data]
    clinical = [d[1] for d in lod_data]
    research = [d[2] for d in lod_data]
    
    fig, ax = plt.subplots(figsize=(12, 6))
    y = np.arange(len(names))
    
    ax.barh(y + 0.18, clinical, height=0.32, color=TEAL, label="Clinical Assay LOD", edgecolor="white")
    ax.barh(y - 0.18, research, height=0.32, color=AMBER, label="Best Research LOD", edgecolor="white")
    
    # Improvement factor
    for i, (c, r) in enumerate(zip(clinical, research)):
        factor = c / r
        ax.text(max(c, r) * 2.5, i, f"×{factor:,.0f}", va='center', fontsize=8,
               fontweight='bold', color=CORAL)

    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=9)
    ax.set_xscale("log")
    # Extend xlim so ×factor labels are fully visible
    xmin = min(research) / 5
    xmax = max(clinical) * 100
    ax.set_xlim(xmin, xmax)
    ax.set_xlabel("Limit of Detection (mmol/L) — log scale")
    ax.set_title("Figure 7 — Clinical vs. Research LOD: Sensitivity Gains from Emerging Technologies",
                fontweight="bold")
    ax.spines[['top', 'right']].set_visible(False)
    ax.legend(loc="lower right", frameon=True, facecolor="white")
    
    plt.tight_layout()
    fig.savefig(FIG / "fig7_lod_comparison.png")
    plt.close()
    print("[OK] Figure 7 saved")


# ═══════════════════════════════════════════════════════════════════
# RUN ALL
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    fig1_classification()
    fig2_molecular_weight()
    fig3_detection_heatmap()
    fig4_concentration_ranges()
    fig5_spectroscopic_map()
    fig6_method_coverage()
    fig7_lod_comparison()
    fig8_wavelength_landscape()
    print("\n=== All 8 figures generated in", FIG, "===")
