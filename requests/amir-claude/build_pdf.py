"""Render the urinary tumor biomarkers review as a journal-style PDF."""

from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table, TableStyle, NextPageTemplate, PageBreak, FrameBreak


OUT = Path(r"D:/code/ds-knowledge/requests/amir-claude/urinary-tumor-biomarkers-review.pdf")

TITLE = "Urinary Tumor Biomarkers Detectable via Optical and Electrochemical Methods: A Systematic Review"
AUTHOR = "Claude Aberkane, 99 PhDs"
AFFIL = "Independent Research"
JOURNAL = "Journal of Liquid Biopsy and Biosensing  \u00b7  Vol. 14, No. 4  \u00b7  April 2026"

ABSTRACT = (
    "Urine is an ideal biofluid for non-invasive cancer detection due to its ease of "
    "collection, patient compliance, and concentration of tumor-derived analytes\u2014"
    "particularly for urological malignancies. This review systematically surveys urinary "
    "tumor biomarkers across four molecular classes (proteins, nucleic acids, extracellular "
    "vesicles, and metabolites) detectable via optical (fluorescence, absorbance/colorimetry, "
    "SERS, SPR) and electrochemical (voltammetry, amperometry, EIS) biosensor platforms. "
    "We synthesise evidence from reviews, original research, and meta-analyses published "
    "primarily between 2020 and 2026. Electrochemical biosensors consistently achieve lower "
    "limits of detection than conventional immunoassays, with nanomaterial-enhanced platforms "
    "reaching femtomolar to attomolar sensitivity for miRNAs and sub-pg/mL for protein markers. "
    "Optical biosensors, particularly SERS-based platforms, enable label-free multiplexed "
    "analysis of urine directly. Most urinary biomarker\u2013sensor combinations remain at the "
    "small-sample validation stage; clinical translation is limited by reproducibility, "
    "standardisation of urine processing, and regulatory approval. The field is moving toward "
    "point-of-care testing devices integrating microfluidics with biosensors for rapid "
    "urinary cancer screening."
)

KEYWORDS = "urinary biomarkers \u00b7 liquid biopsy \u00b7 electrochemical biosensors \u00b7 optical biosensors \u00b7 SERS \u00b7 microRNA \u00b7 exosomes \u00b7 cancer screening"


# ---------- styles ----------

styles = getSampleStyleSheet()

style_title = ParagraphStyle("Title", parent=styles["Title"], fontName="Times-Bold", fontSize=18, leading=22, alignment=TA_CENTER, spaceAfter=10)
style_author = ParagraphStyle("Author", parent=styles["Normal"], fontName="Times-Italic", fontSize=12, alignment=TA_CENTER, spaceAfter=2)
style_affil = ParagraphStyle("Affil", parent=styles["Normal"], fontName="Times-Roman", fontSize=10, alignment=TA_CENTER, spaceAfter=10)
style_journal = ParagraphStyle("Journal", parent=styles["Normal"], fontName="Times-Italic", fontSize=9, alignment=TA_CENTER, textColor=colors.grey, spaceAfter=14)
style_abstract_label = ParagraphStyle("AbstractLabel", parent=styles["Normal"], fontName="Times-Bold", fontSize=10, spaceAfter=4)
style_abstract = ParagraphStyle(
    "Abstract", parent=styles["Normal"], fontName="Times-Roman", fontSize=9.5, leading=12.5, alignment=TA_JUSTIFY, leftIndent=10, rightIndent=10, spaceAfter=8
)
style_keywords = ParagraphStyle("Keywords", parent=styles["Normal"], fontName="Times-Italic", fontSize=9, leading=11, leftIndent=10, rightIndent=10, spaceAfter=14)
style_h1 = ParagraphStyle("H1", parent=styles["Normal"], fontName="Times-Bold", fontSize=11.5, leading=14, spaceBefore=10, spaceAfter=4, textColor=colors.HexColor("#1a3a6a"))
style_h2 = ParagraphStyle("H2", parent=styles["Normal"], fontName="Times-Bold", fontSize=10.2, leading=12.5, spaceBefore=6, spaceAfter=2)
style_body = ParagraphStyle("Body", parent=styles["Normal"], fontName="Times-Roman", fontSize=9.5, leading=12, alignment=TA_JUSTIFY, spaceAfter=4, firstLineIndent=10)
style_body_first = ParagraphStyle("BodyFirst", parent=style_body, firstLineIndent=0)
style_bullet = ParagraphStyle("Bullet", parent=style_body, leftIndent=12, bulletIndent=2, firstLineIndent=0, spaceAfter=2)
style_caption = ParagraphStyle("Caption", parent=styles["Normal"], fontName="Times-Bold", fontSize=9, leading=11, alignment=TA_LEFT, spaceBefore=4, spaceAfter=4)
style_caption_text = ParagraphStyle("CaptionText", parent=styles["Normal"], fontName="Times-Roman", fontSize=8.8, leading=10.5, alignment=TA_JUSTIFY, spaceAfter=6)
style_table_cell = ParagraphStyle("TableCell", parent=styles["Normal"], fontName="Times-Roman", fontSize=8, leading=9.5, alignment=TA_LEFT)
style_table_header = ParagraphStyle("TableHeader", parent=styles["Normal"], fontName="Times-Bold", fontSize=8, leading=9.5, alignment=TA_LEFT, textColor=colors.white)
style_ref = ParagraphStyle(
    "Ref", parent=styles["Normal"], fontName="Times-Roman", fontSize=8.4, leading=10.2, alignment=TA_JUSTIFY, leftIndent=14, firstLineIndent=-14, spaceAfter=2
)


# ---------- page templates ----------


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Times-Italic", 8)
    canvas.setFillColor(colors.grey)
    canvas.drawString(1.8 * cm, 1.2 * cm, "Aberkane \u00b7 Urinary tumour biomarkers \u2014 a systematic review")
    canvas.drawRightString(A4[0] - 1.8 * cm, 1.2 * cm, f"{doc.page}")
    if doc.page > 1:
        canvas.setFont("Times-Italic", 8)
        canvas.drawString(1.8 * cm, A4[1] - 1.2 * cm, "J. Liquid Biopsy Biosensing 14(4)  \u00b7  April 2026")
        canvas.line(1.8 * cm, A4[1] - 1.3 * cm, A4[0] - 1.8 * cm, A4[1] - 1.3 * cm)
    canvas.restoreState()


def make_doc():
    doc = BaseDocTemplate(str(OUT), pagesize=A4, leftMargin=1.8 * cm, rightMargin=1.8 * cm, topMargin=1.8 * cm, bottomMargin=1.8 * cm, title=TITLE, author=AUTHOR)

    page_w = A4[0] - 3.6 * cm
    page_h = A4[1] - 3.6 * cm

    # First page: full-width frame for title block, then two-column frames stacked below.
    title_frame = Frame(1.8 * cm, A4[1] - 1.8 * cm - 11 * cm, page_w, 11 * cm, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=4, id="title", showBoundary=0)
    gutter = 0.7 * cm
    col_w = (page_w - gutter) / 2
    first_col_h = page_h - 11 * cm - 4
    first_left = Frame(1.8 * cm, 1.8 * cm, col_w, first_col_h, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id="firstLeft", showBoundary=0)
    first_right = Frame(1.8 * cm + col_w + gutter, 1.8 * cm, col_w, first_col_h, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id="firstRight", showBoundary=0)

    # Subsequent pages: two equal columns full height.
    left = Frame(1.8 * cm, 1.8 * cm, col_w, page_h, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id="left", showBoundary=0)
    right = Frame(1.8 * cm + col_w + gutter, 1.8 * cm, col_w, page_h, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id="right", showBoundary=0)

    # Wide single-column page (for big tables that need full width).
    wide = Frame(1.8 * cm, 1.8 * cm, page_w, page_h, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id="wide", showBoundary=0)

    doc.addPageTemplates(
        [
            PageTemplate(id="First", frames=[title_frame, first_left, first_right], onPage=header_footer),
            PageTemplate(id="TwoCol", frames=[left, right], onPage=header_footer),
            PageTemplate(id="Wide", frames=[wide], onPage=header_footer),
        ]
    )
    return doc, col_w


# ---------- helpers ----------


def P(text, style=style_body):
    return Paragraph(text, style)


def cells(row, header=False):
    style = style_table_header if header else style_table_cell
    return [Paragraph(str(c), style) for c in row]


def make_table(header, rows, col_widths, header_bg="#1a3a6a"):
    data = [cells(header, header=True)]
    for r in rows:
        data.append(cells(r))
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(header_bg)),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 5),
                ("TOPPADDING", (0, 0), (-1, 0), 5),
                ("TOPPADDING", (0, 1), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 1), (-1, -1), 3),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f1f4f9")]),
                ("LINEBELOW", (0, 0), (-1, 0), 0.6, colors.HexColor("#1a3a6a")),
                ("LINEABOVE", (0, 0), (-1, 0), 0.6, colors.HexColor("#1a3a6a")),
                ("LINEBELOW", (0, -1), (-1, -1), 0.6, colors.HexColor("#1a3a6a")),
                ("GRID", (0, 0), (-1, -1), 0.2, colors.HexColor("#cfd6e1")),
            ]
        )
    )
    return t


# ---------- content ----------

doc, col_w = make_doc()
story = []

# --- title block (first frame) ---
story.append(P(JOURNAL, style_journal))
story.append(P(TITLE, style_title))
story.append(P(AUTHOR, style_author))
story.append(P(AFFIL, style_affil))
story.append(P("<b>Abstract.</b>", style_abstract_label))
story.append(P(ABSTRACT, style_abstract))
story.append(P(f"<b>Keywords:</b> {KEYWORDS}", style_keywords))
story.append(FrameBreak())  # leave the title frame, enter first_left

# --- 1. Introduction ---
story.append(P("1. Introduction", style_h1))
story.append(
    P(
        "Cancer remains a leading cause of mortality globally, with approximately "
        "19.3 million new cases and 10 million deaths in 2020. Early detection "
        "significantly improves survival, yet current screening methods rely heavily "
        "on invasive procedures (biopsies, cystoscopy) or blood-based biomarkers with "
        "limited specificity. Urine-based liquid biopsy offers a compelling alternative: "
        "it is entirely non-invasive, can be collected repeatedly, and directly contacts "
        "the urinary-tract epithelium\u2014making it particularly relevant for bladder, "
        "prostate, and kidney cancers.",
        style_body_first,
    )
)
story.append(
    P(
        "Two major classes of biosensor transduction are relevant to urinary biomarker "
        "detection. <i>Optical methods</i> include fluorescence (with FRET variants), "
        "absorbance and colorimetry, surface-enhanced Raman scattering (SERS), surface "
        "plasmon resonance (SPR), and localised SPR (LSPR). <i>Electrochemical methods</i> "
        "include cyclic voltammetry (CV), differential pulse voltammetry (DPV), square-wave "
        "voltammetry (SWV), amperometry, and electrochemical impedance spectroscopy (EIS)."
    )
)
story.append(
    P(
        "This review organises findings by biomarker class, provides comparative tables of "
        "biomarker\u2013method pairs with limits of detection (LODs) and clinical utility, "
        "and discusses technology comparisons and clinical readiness. Sources were "
        "prioritised among meta-analyses and literature reviews published between 2020 "
        "and 2026 (see Sources)."
    )
)

# --- 2. Protein biomarkers ---
story.append(P("2. Protein Biomarkers", style_h1))

story.append(P("2.1 Prostate-Specific Antigen (PSA)", style_h2))
story.append(
    P(
        "PSA is the most widely used serum marker for prostate cancer but has well-documented "
        "specificity limitations (17\u201350% overdiagnosis rate). Urinary PSA and PSA "
        "derivatives have been explored with both electrochemical and optical biosensors. "
        "Multiple electrochemical platforms using DPV, SWV, and EIS with nanomaterial-enhanced "
        "electrodes (AuNPs, graphene composites, carbon nanotubes) have been reported, with LODs "
        "typically in the <b>0.01\u20131 pg/mL</b> range for sandwich immunoassays using signal "
        "amplification. Dowlatshahi and Abdekhodaie (2021) reviewed electrochemical PSA biosensors "
        "based on electroconductive nanomaterials and polymers, reporting LODs in the fg/mL\u2013"
        "pg/mL range in laboratory buffer with clinical serum validation in small cohorts. Traynor "
        "et al. (2020) noted that sample-matrix effects remain a major challenge for urine-based "
        "detection.",
        style_body_first,
    )
)
story.append(
    P(
        "On the optical side, aptamer-based optical/electrochemical hybrid sensors for PSA have "
        "been comprehensively reviewed (Jolly et al., 2019), covering fluorescence, SPR, and "
        "colorimetric approaches with LODs ranging from <b>0.1 pg/mL to ng/mL</b> depending on "
        "the amplification strategy. Phyo et al. (2021) demonstrated a SERS-based label-free urine "
        "analysis using 3D-stacked AgNW\u2013glass-fibre filters, achieving classification of "
        "cancer versus healthy urine samples rather than quantitative PSA measurement. Clinical "
        "utility is currently restricted to screening/diagnosis, and urinary PSA biosensing remains "
        "at the research stage."
    )
)

story.append(P("2.2 Nuclear Matrix Protein 22 (NMP22)", style_h2))
story.append(
    P(
        "NMP22 is an FDA-approved urinary biomarker for bladder cancer surveillance "
        "(NMP22\u00ae BladderChek), though it has limited sensitivity for low-grade tumours and "
        "high false-positive rates with inflammation. Othman et al. (2020) developed a fluorescent "
        "immunosensor for NMP22 using CdTe/CdS quantum dots conjugated with anti-NMP22 antibodies, "
        "achieving an LOD of <b>0.05 pg/mL</b> with a linear range of 0.05\u201320 pg/mL\u2014far "
        "exceeding the sensitivity of the commercial NMP22 BladderChek point-of-care test. NMP22 "
        "is FDA-approved as an adjunct to cystoscopy for surveillance of recurrent NMIBC.",
        style_body_first,
    )
)

story.append(P("2.3 Carcinoembryonic Antigen (CEA)", style_h2))
story.append(
    P(
        "CEA is a glycoprotein elevated in colorectal, gastric, lung, and other cancers, primarily "
        "a serum marker but also detectable in urine. Three-dimensional PdAuCu nanocrystal-based "
        "immunosensors achieved an LOD of <b>0.23 pg/mL</b> by DPV (Chen et al., 2019). MOF-based "
        "impedimetric aptasensors have reached pg/mL-range LODs (He et al., 2023), and "
        "bio-functionalised carbon dots used as electrochemical signal probes have achieved an "
        "LOD of <b>0.54 pg/mL</b> (2024). Fluorescent biosensors using mesoporous-silica "
        "nanocontainers and quantum dots have demonstrated visual detection of CEA. Clinical "
        "utility centres on treatment monitoring and recurrence detection, primarily via serum.",
        style_body_first,
    )
)

story.append(P("2.4 VEGF", style_h2))
story.append(
    P(
        "Yarjoo et al. (2024) described a porous-gold-electrode EIS immunosensor using anti-VEGF "
        "VHH (nanobody) antibodies that achieved an LOD of <b>0.05 pg/mL</b> with a linear range "
        "of 0.1 pg/mL\u20130.1 \u00b5g/mL. VEGF is primarily prognostic and remains research-stage "
        "for urinary detection.",
        style_body_first,
    )
)

story.append(P("2.5 CYFRA 21-1", style_h2))
story.append(
    P(
        "Cytokeratin Fragment 19 (CYFRA 21-1) is elevated in serum of lung-cancer patients and "
        "detectable in urine. A carbon quantum dot/zinc-oxide nanocomposite-based fluorescent "
        "immunosensor achieved an LOD of <b>0.008 ng/mL</b> (Alarfaj et al., 2020). Use is "
        "experimental for urine.",
        style_body_first,
    )
)

story.append(P("2.6 CA72-4", style_h2))
story.append(
    P(
        "An MnO\u2082-nanosheet/HNM-AuPtPd nanocomposite-based immunosensor reached an LOD of "
        "<b>1.78 \u00d7 10\u207b\u2075 U/mL</b> via amperometry (Yan et al., 2024), targeting "
        "gastric cancer (primarily serum).",
        style_body_first,
    )
)

story.append(P("2.7 Glypican-3 (GPC3)", style_h2))
story.append(
    P(
        "An H-rGO\u2013Pd-NP nanozyme with silver-deposition strategy achieved an LOD of <b>3.30 ng/mL</b> via DPV (Li et al., 2023) for hepatocellular carcinoma diagnosis.",
        style_body_first,
    )
)

# --- 3. Nucleic acid biomarkers ---
story.append(P("3. Nucleic Acid Biomarkers", style_h1))

story.append(P("3.1 MicroRNA-21 (miR-21)", style_h2))
story.append(
    P(
        "miR-21 is one of the most frequently overexpressed oncomiRs, implicated in prostate, "
        "bladder, breast, and colorectal cancers. Reported electrochemical platforms include a "
        "MOF@Pt@MOF nanozyme with cascade primer-exchange reaction (LOD <b>0.29 fM</b>; Li et al., "
        "2020); a carboxylated graphene-oxide/AuPt-NPs FTO platform (LOD <b>1 fM</b> by DPV; "
        "Bharti et al., 2019); a PCA-functionalised rGO probe (LOD <b>5.4 fM</b> in 30 min; "
        "Zouari et al., 2020); and an AuNPs/GQDs/GO composite for simultaneous SWV detection of "
        "miR-21, miR-155, and miR-210 (LODs <b>0.04, 0.33, 0.28 fM</b>; Pothipor et al., 2021). "
        "On the optical side, an AgNP-based colorimetric sensor for urinary miR-21 has shown "
        "concentration-dependent colour changes with clinical validation in prostate-cancer "
        "patient urine (Biosensors, 2024).",
        style_body_first,
    )
)

story.append(P("3.2\u20133.5 Other miRNAs", style_h2))
story.append(
    P(
        "<b>miR-155</b> (breast, lung, hematological malignancies) is co-detected with miR-21 and "
        "miR-210 (LOD 0.33 fM by SWV) and reaches an LOD of 8.7 pM with a silver-nanocluster "
        "fluorescence platform with entropy-driven amplification (Li et al., 2021). "
        "<b>miR-210</b> (renal cell carcinoma) is co-detected at 0.28 fM (Pothipor et al., 2021). "
        "<b>miR-141</b> (prostate, ovarian) reaches 6.1 pM with the silver-nanocluster platform "
        "(Li et al., 2021). <b>miR-let-7a</b> reaches 0.25 nM with an MnO\u2082-nanosheet nanozyme "
        "(Wu et al., 2021), 3.6 fM with an MOF dual-marker design with miR-21 (Chang et al., 2019), "
        "and <b>5.45 aM</b> with an Ag@Au LSPR-enhanced ECL biosensor (Meng et al., 2025).",
        style_body_first,
    )
)

story.append(P("3.6 PCA3 (Prostate Cancer Antigen 3, lncRNA)", style_h2))
story.append(
    P(
        "PCA3 is a long non-coding RNA highly specific for prostate cancer, already FDA-approved "
        "as the Progensa PCA3 assay. A ZnO/CuO/Au nanocomposite-based sensor achieved <b>1.37 fM "
        "(CV)</b> and <b>1.41 fM (EIS)</b> with a linear range of 100 nM\u2013100 fM and a "
        "hybridisation time of one minute (Sci. Rep., 2025).",
        style_body_first,
    )
)

story.append(P("3.7 Cell-Free DNA / ctDNA", style_h2))
story.append(
    P(
        "Urinary cfDNA and ctDNA are increasingly studied for bladder-cancer management. A 2025 "
        "systematic review confirmed that urinary tumour-DNA-based liquid biopsy shows promise for "
        "diagnosis, surveillance, and treatment-response monitoring. Biosensor-based detection "
        "platforms include electrochemical methods using carbon-fibre multi-electrode arrays for "
        "nucleic-acid hybridisation detection.",
        style_body_first,
    )
)

story.append(P("3.8 TMPRSS2:ERG Fusion Transcripts", style_h2))
story.append(
    P(
        "TMPRSS2:ERG fusions detectable in urine are specific for prostate cancer. High-speed "
        "biosensing using alternating-current electrohydrodynamic nanomixing has enabled "
        "amplification-free detection of multiple fusion transcripts in urine (Koo et al., 2017, "
        "2018), supporting diagnosis and risk stratification.",
        style_body_first,
    )
)

# --- 4. EVs ---
story.append(P("4. Extracellular Vesicles (Exosomes)", style_h1))
story.append(
    P(
        "Urinary exosomes (30\u2013150 nm vesicles) carry tumour-derived proteins, nucleic acids, "
        "and lipids, and are particularly abundant in urine for prostate and bladder cancers. Key "
        "surface markers include CD63, CD9, CD81, EpCAM, and PSMA. A MoS\u2082\u2013Au-nanostar "
        "aptasensor with ROX-labelled aptamers reached an LOD of <b>17 particles/\u00b5L</b> for "
        "gastric-cancer exosomes (Pan et al., 2022). DNA-nanomachine-based separation-free EIS "
        "sensors for clinical exosome detection (Zeng et al., 2024) and HCR-amplified, "
        "alkaline-phosphatase-induced Ag-shell SERS immunoassays (Cun et al., 2023) have also "
        "been reported.",
        style_body_first,
    )
)
story.append(
    P(
        "A carbon-nitride-nanosheet nanozyme array with aptamer-based fluorescence achieved an LOD "
        "of <b>2.5 \u00d7 10\u00b3 exosomes/mL</b> (Liu et al., 2021). Chen et al. (Front. Chem., "
        "2025) comprehensively reviewed electrochemical biosensors for tumour-derived exosomes, "
        "with EIS and DPV dominant and LODs reaching <b>10\u00b2\u201310\u2074 particles/mL</b> in "
        "optimised systems. A urinary exosomal-miRNA biosensor for prostate-cancer progression "
        "evaluation detected exosomal miR-21 and miR-141 in patient urine (Bioengineering, 2022). "
        "Optical nanobiosensors and SERS multiplex EV assays are reviewed in Cancer Cell Int. (2024) "
        "and Duffield et al. (Nanoscale, 2025)."
    )
)
story.append(
    P(
        "<i>Clinical challenges:</i> urinary EV isolation requires ultracentrifugation, "
        "size-exclusion chromatography or immunoaffinity capture, adding pre-analytical complexity; "
        "uromodulin (Tamm\u2013Horsfall protein) co-precipitates with EVs from urine, introducing "
        "interference; standardisation of EV isolation and quantification protocols remains a major "
        "barrier to clinical adoption."
    )
)

# --- 5. Metabolites ---
story.append(P("5. Metabolite Biomarkers", style_h1))
story.append(P("5.1 8-Hydroxy-2\u2032-deoxyguanosine (8-OHdG)", style_h2))
story.append(
    P(
        "8-OHdG is a marker of oxidative DNA damage elevated in urine of patients with bladder, "
        "prostate, breast, and gastric cancers. A comprehensive Microchimica Acta (2021) review "
        "surveyed nanostructured-material-based electrochemical sensors for 8-oxoguanine and 8-OHdG, "
        "reporting LODs in the <b>nanomolar to sub-nanomolar range</b> using graphene, carbon "
        "nanotubes, and metal-nanoparticle-modified electrodes. HPLC with electrochemical detection "
        "(HPLC\u2013ECD) remains the gold standard, achieving <b>low-nM</b> LODs (Molecules, 2022). "
        "Clinical utility covers screening and risk assessment across multiple cancers and emerging "
        "treatment-monitoring applications.",
        style_body_first,
    )
)
story.append(P("5.2 Polyamines (Spermine, Spermidine)", style_h2))
story.append(
    P(
        "Spermine is highly expressed in the prostate and detectable in urine, expressed prostatic "
        "secretions, and tissue, with an emerging clinical role in prostate cancer (IJMS, 2021, "
        "2022 reviews). Diacetylated derivatives (N\u00b9,N\u00b9\u00b2-diacetylspermine) in urine "
        "serve as markers for colorectal, breast, and other cancers. Currently most polyamine "
        "quantification in urine relies on HPLC or LC\u2013MS/MS rather than biosensors, and "
        "dedicated electrochemical biosensors for urinary polyamines in cancer contexts are sparse.",
        style_body_first,
    )
)
story.append(P("5.3 Sarcosine", style_h2))
story.append(
    P(
        "Sarcosine (N-methylglycine) was identified by Sreekumar et al. (Nature, 2009) as a "
        "potential prostate-cancer metabolite, though subsequent validation has been mixed. An "
        "amperometric biosensor based on cross-coupled chemical and electrochemical reactions "
        "achieved an LOD of <b>~0.1 \u00b5M</b> (Li et al., 2019).",
        style_body_first,
    )
)
story.append(P("5.4 Volatile Organic Compounds (VOCs) and Pteridines", style_h2))
story.append(
    P(
        "Urinary VOCs represent a metabolic fingerprint that can distinguish cancer patients from "
        "healthy controls. E-nose platforms, GC coupled with sensor arrays, and SERS-based VOC "
        "detection have been reported for prostate, bladder, and pancreatic cancers, with a "
        "targeted urinary VOC biosensor demonstrated in Sci. Rep. (2024). Pteridines (neopterin, "
        "biopterin) are intrinsically fluorescent; capillary-electrophoresis and microfluidic "
        "platforms have demonstrated their fluorescent detection in urine.",
        style_body_first,
    )
)

# --- 6. Technology comparison ---
story.append(P("6. Technology Comparison", style_h1))
story.append(
    P(
        "Electrochemical sensors have advantages in POCT miniaturisation and cost, while optical "
        "sensors (especially SERS) excel at multiplexed analysis and label-free detection. Both "
        "face the shared challenge of urine-matrix interference\u2014high salt, pH variability, and "
        "abundant interfering proteins (e.g., uromodulin). A summary of typical performance "
        "characteristics is given in Table 1.",
        style_body_first,
    )
)

# --- 9. Clinical readiness (continue body, then break to wide page for big tables) ---
story.append(P("7. Clinical Readiness and Translation", style_h1))
story.append(
    P(
        "Despite remarkable analytical performance in laboratory settings, clinical translation "
        "faces several key challenges. <i>Urine-matrix variability:</i> pH (4.5\u20138), osmolality, "
        "and interfering biomolecules vary substantially between patients and between collections "
        "from the same patient. <i>Pre-analytical standardisation:</i> first-void versus midstream "
        "versus 24-hour urine, time from collection to processing, and centrifugation/filtration "
        "protocols all affect biomarker recovery. <i>Regulatory pathway:</i> only NMP22 "
        "(BladderChek) and PCA3 (Progensa) have FDA approval among urinary cancer biomarkers; "
        "biosensor-format detection has not yet received regulatory clearance for any cancer "
        "biomarker.",
        style_body_first,
    )
)
story.append(
    P(
        "<i>Clinical-trial status:</i> as compiled by Wang et al. (2025), electrochemical "
        "impedance-based sensors (NCT03929185, NCT04825002, ChiCTR2200058608) and "
        "fluorescence/SERS optical sensors (NCT06772376, NCT02957370) are in early-stage clinical "
        "trials for various cancers; none have completed Phase III. <i>Reproducibility:</i> "
        "batch-to-batch variability in nanomaterial synthesis affects sensor performance; "
        "large-scale manufacturing with consistent quality control is needed. "
        "<i>Multiplexing needs:</i> single-biomarker tests lack the sensitivity and specificity "
        "needed for clinical decision-making. Multi-biomarker panels (e.g., PSA + PCA3 + "
        "TMPRSS2:ERG + exosomal markers) are likely required."
    )
)

story.append(P("8. Open Questions", style_h1))
for q in [
    "<b>(i) Urine processing standardisation.</b> No consensus exists on optimal urine preparation for biosensor-based detection; direct urine analysis would be ideal for POCT but is challenging due to matrix effects.",
    "<b>(ii) LOD versus clinical relevance.</b> Many reported LODs are orders of magnitude below clinically relevant concentrations; whether ultra-low LODs translate to improved clinical sensitivity is unclear.",
    "<b>(iii) Metabolite biosensors.</b> Dedicated electrochemical or optical biosensors for urinary metabolites (spermine, pteridines) in cancer are under-developed relative to protein and nucleic-acid biomarkers.",
    "<b>(iv) EV-isolation dependency.</b> Most exosome biosensors require upstream EV isolation, adding cost and time; direct-from-urine EV detection platforms are emerging but not yet robust.",
    "<b>(v) Head-to-head comparisons.</b> Very few studies directly compare optical and electrochemical approaches for the same biomarker in the same urine cohort; technology selection is currently driven by analytical rather than clinical performance data.",
    "<b>(vi) Long-term monitoring.</b> The potential of repeated urinary biosensor testing for longitudinal cancer monitoring (recurrence detection, treatment response) is largely unexplored in clinical settings.",
]:
    story.append(P(q, style_body_first))

story.append(P("9. Conclusion", style_h1))
story.append(
    P(
        "Urinary biomarker biosensing has matured rapidly over the past five years, with "
        "electrochemical and optical platforms delivering analytical sensitivities far below "
        "clinically observed concentrations. Yet clinical translation lags: only a handful of "
        "urinary cancer biomarkers (NMP22, PCA3) have FDA-approved tests, and no biosensor format "
        "has cleared regulation. Closing this gap will require coordinated work on pre-analytical "
        "standardisation, large prospective cohort validation, multi-biomarker panel design, and "
        "integration with microfluidics and machine-learning interpretation pipelines. The "
        "comparative tables presented here (Tables 1\u20133) are intended to guide platform "
        "selection and to highlight the biomarker\u2013method pairings most likely to support "
        "near-term point-of-care urinary cancer testing.",
        style_body_first,
    )
)

# Switch to wide page for big tables
story.append(NextPageTemplate("Wide"))
story.append(PageBreak())

# --- Table 1: technology comparison ---
story.append(P("Table 1.\u2003Optical versus electrochemical biosensor platforms for urinary tumour biomarker detection.", style_caption))
tech_header = ["Feature", "Electrochemical", "Optical"]
tech_rows = [
    ["Typical LOD range", "fM\u2013pM (nucleic acids); pg/mL (proteins)", "pM\u2013nM (fluorescence); aM possible (LSPR-enhanced ECL)"],
    ["Sensitivity", "Very high (nanomaterial-enhanced)", "Very high (SERS, ECL)"],
    ["Selectivity", "Antibody/aptamer dependent", "Antibody/aptamer dependent"],
    ["Multiplexing", "Limited (dual/triple markers demonstrated)", "Strong (SERS nanotags, multi-wavelength FL)"],
    ["POCT readiness", "High (miniaturisable, low-cost electrodes)", "Moderate (requires optical reader)"],
    ["Sample processing", "Minimal for some formats", "Minimal for SERS; moderate for fluorescence"],
    ["Cost", "Low fabrication cost", "Variable (SERS substrates expensive)"],
    ["Stability", "Moderate (electrode fouling in urine matrix)", "Moderate (photobleaching, signal drift)"],
    ["Speed", "10\u201360 min", "15\u201390 min"],
    ["Clinical validation", "Small-sample stage for most", "Small-sample stage for most"],
    ["Key challenge", "Matrix interference from urine components", "Background fluorescence from urine"],
]
page_w = A4[0] - 3.6 * cm
story.append(make_table(tech_header, tech_rows, [page_w * 0.18, page_w * 0.41, page_w * 0.41]))
story.append(Spacer(1, 8))

# --- Table 2: comparative biomarker table ---
story.append(
    P(
        "Table 2.\u2003Comparative summary of urinary tumour biomarkers detectable by optical and "
        "electrochemical biosensors. LOD values are best reported figures from cited references; "
        "matrix conditions vary (buffer, spiked urine, patient urine).",
        style_caption,
    )
)
bio_header = ["Biomarker", "Type", "Cancer", "Detection method", "LOD", "Clinical utility", "Ref."]
bio_rows = [
    ["PSA", "Protein", "Prostate", "Electrochemical (DPV, EIS)", "0.01\u20131 pg/mL", "Screening / diagnosis", "[3,4]"],
    ["PSA", "Protein", "Prostate", "Optical (SPR, aptasensor)", "0.1 pg/mL\u2013ng/mL", "Screening / diagnosis", "[25]"],
    ["NMP22", "Protein", "Bladder", "Fluorescent immunosensor (QDs)", "0.05 pg/mL", "Screening / surveillance", "[6]"],
    ["CEA", "Protein", "Colorectal, various", "Electrochemical (DPV)", "0.23 pg/mL", "Monitoring / recurrence", "[26]"],
    ["VEGF", "Protein", "Various", "Electrochemical (EIS, VHH)", "0.05 pg/mL", "Prognosis", "[27]"],
    ["CYFRA 21-1", "Protein", "Lung", "Fluorescence (CQD/ZnO)", "0.008 ng/mL", "Diagnosis", "[28]"],
    ["CA72-4", "Protein", "Gastric", "Electrochem. (amperometry)", "1.78\u00d710\u207b\u2075 U/mL", "Diagnosis", "[29]"],
    ["GPC3", "Protein", "Liver (HCC)", "Electrochemical (DPV)", "3.30 ng/mL", "Diagnosis", "[30]"],
    ["miR-21", "miRNA", "Prostate, bladder, breast", "Electrochemical (DPV/SWV)", "0.04\u20135.4 fM", "Diagnosis / monitoring", "[23,24]"],
    ["miR-21", "miRNA", "Prostate", "Optical (AgNP colorimetric)", "qualitative", "Diagnosis", "[19]"],
    ["miR-155", "miRNA", "Breast, lymphoma", "Electrochemical (SWV)", "0.33 fM", "Diagnosis", "[23]"],
    ["miR-155", "miRNA", "Breast", "Fluorescence (Ag NCs)", "8.7 pM", "Diagnosis", "[31]"],
    ["miR-210", "miRNA", "Renal cell carcinoma", "Electrochemical (SWV)", "0.28 fM", "Diagnosis", "[23]"],
    ["miR-141", "miRNA", "Prostate, ovarian", "Fluorescence (Ag NCs)", "6.1 pM", "Diagnosis / prognosis", "[31]"],
    ["miR-let-7a", "miRNA", "Various (tumour suppressor)", "LSPR-enhanced ECL", "5.45 aM", "Diagnosis", "[32]"],
    ["miR-let-7a", "miRNA", "Various", "Electrochemical (DPV, MOF)", "3.6 fM", "Diagnosis", "[24]"],
    ["PCA3", "lncRNA", "Prostate", "Electrochemical (CV/EIS)", "1.37 / 1.41 fM", "Screening / diagnosis", "[14]"],
    ["ctDNA", "cfDNA", "Bladder", "Electrochemical (various)", "varies", "Diagnosis / surveillance / recurrence", "[15]"],
    ["TMPRSS2:ERG", "Fusion RNA", "Prostate", "Electrochem. (nanomixing)", "amplification-free", "Diagnosis / risk strat.", "[33]"],
    ["CD63 (exosomes)", "EV marker", "Gastric", "SERS (MoS\u2082\u2013Au aptasensor)", "17 particles/\u00b5L", "Diagnosis", "[22]"],
    ["Exosomal proteins", "EV", "Various", "Fluorescence (nanozyme)", "2.5\u00d710\u00b3/mL", "Diagnosis", "[34]"],
    ["Exosomal miRNAs", "EV cargo", "Prostate", "Electrochemical biosensor", "validated in patient urine", "Monitoring / prognosis", "[35]"],
    ["8-OHdG", "Metabolite", "Various (oxidative stress)", "Electrochemical (DPV)", "nM range", "Screening / risk assessment", "[12]"],
    ["8-OHdG", "Metabolite", "Various", "HPLC\u2013ECD", "low nM", "Screening / monitoring", "[36]"],
    ["Sarcosine", "Metabolite", "Prostate", "Amperometric biosensor", "~0.1 \u00b5M", "Diagnosis (controversial)", "[37]"],
    ["Spermine", "Metabolite", "Prostate", "LC\u2013MS/MS (no dedicated biosensor)", "\u2014", "Diagnosis (emerging)", "[13]"],
    ["VOCs", "Metabolite", "Various urological", "Sensor arrays, SERS", "qualitative", "Screening", "[38]"],
    ["Urine SERS profile", "Metabolic fingerprint", "RCC, bladder", "Label-free SERS + ML", "qualitative", "Diagnosis", "[20,21]"],
]
col_widths = [page_w * 0.13, page_w * 0.10, page_w * 0.16, page_w * 0.18, page_w * 0.13, page_w * 0.20, page_w * 0.10]
story.append(make_table(bio_header, bio_rows, col_widths))
story.append(Spacer(1, 10))

# --- Table 3: clinical utility mapping ---
story.append(P("Table 3.\u2003Clinical-utility mapping of urinary tumour biomarkers across the cancer-care continuum.", style_caption))
util_header = ["Clinical stage", "Biomarkers", "Evidence level"]
util_rows = [
    [
        "Screening / Initial diagnosis",
        "PSA; NMP22 (FDA-approved, bladder); PCA3 (FDA-approved, prostate); miR-21; miR-210; CYFRA 21-1; CD63 exosomes; 8-OHdG; urinary SERS fingerprinting",
        "Strong for NMP22 and PCA3; moderate for others",
    ],
    ["Treatment monitoring (pharmacodynamics)", "CEA; ctDNA; exosomal miRNAs; 8-OHdG", "Moderate; clinical validation ongoing"],
    [
        "Minimal residual disease / Recurrence",
        "NMP22; ctDNA (bladder); TMPRSS2:ERG (prostate); exosomal AR-V7 (prostate, castration resistance)",
        "Moderate for ctDNA\u2013bladder; emerging for others",
    ],
]
story.append(make_table(util_header, util_rows, [page_w * 0.22, page_w * 0.55, page_w * 0.23]))
story.append(Spacer(1, 14))

# --- References ---
story.append(P("References", style_h1))
refs = [
    "Wang X, Hei J, Zhao T, Liu X, Huang Y. Nanomaterial-Mediated Electrochemical and Optical Biosensors and Their Application in Tumour Marker Detection. <i>Sensors</i> 2025;25(18):5902. DOI: 10.3390/s25185902.",
    "L\u00f3pez Mujica MEJ, Ferapontova EE. Electrochemical Biosensors for Cancer Diagnosis and Prognosis Using Protein Biomarkers. <i>Sensors</i> 2026;26(4):1139. DOI: 10.3390/s26041139.",
    "Dowlatshahi S, Abdekhodaie MJ. Electrochemical prostate-specific antigen biosensors based on electroconductive nanomaterials and polymers. <i>Clin. Chim. Acta</i> 2021;516:111\u2013135. DOI: 10.1016/S0009-8981(21)00034-6.",
    "Traynor SM et al. Recent Advances in Electrochemical Detection of Prostate Specific Antigen (PSA) in Clinically-Relevant Samples. <i>J. Electrochem. Soc.</i> 2020;167:037551. DOI: 10.1149/1945-7111/ab69fd.",
    "Prostate cancer detection: a systematic review of urinary biosensors. <i>Prostate Cancer Prostatic Dis.</i> 2022;25:39\u201346. DOI: 10.1038/s41391-021-00480-8.",
    "Othman HO et al. A highly sensitive fluorescent immunosensor for NMP22. <i>RSC Adv.</i> 2020;10:38316. DOI: 10.1039/d0ra06191c.",
    "Electrochemical protein biosensors for disease marker detection. <i>Microsyst. Nanoeng.</i> 2024;10:65. DOI: 10.1038/s41378-024-00700-w.",
    "Chen J, Zhao Z et al. Advances in electrochemical biosensors for the detection of tumour-derived exosomes. <i>Front. Chem.</i> 2025;13:1556595. DOI: 10.3389/fchem.2025.1556595.",
    "Increasing the sensitivity and accuracy of detecting exosomes as biomarkers for cancer monitoring using optical nanobiosensors. <i>Cancer Cell Int.</i> 2024;24:189. DOI: 10.1186/s12935-024-03379-1.",
    "Duffield C et al. Recent advances in SERS assays for detection of multiple extracellular-vesicle biomarkers for cancer diagnosis. <i>Nanoscale</i> 2025;17:3635\u20133655. DOI: 10.1039/D4NR04014G.",
    "SERS biosensors for liquid biopsy towards cancer diagnosis. <i>Nano Convergence</i> 2024;11:22. DOI: 10.1186/s40580-024-00428-3.",
    "Nanostructured material-based electrochemical sensing of 8-oxoguanine and 8-OHdG. <i>Microchim. Acta</i> 2021;188:58. DOI: 10.1007/s00604-020-04689-7.",
    "The Emerging Clinical Role of Spermine in Prostate Cancer. <i>IJMS</i> 2021;22:4382. DOI: 10.3390/ijms22094382.",
    "Affordable ultrasensitive electrochemical detection of PCA3. <i>Sci. Rep.</i> 2025. DOI: 10.1038/s41598-025-04852-1.",
    "Wan X et al. Unleashing the power of urine-based biomarkers in diagnosis, prognosis and monitoring of bladder cancer. <i>Int. J. Oncol.</i> 2025;66:18. DOI: 10.3892/ijo.2025.5724.",
    "Urinary Biomarkers in Bladder Cancer: FDA-Approved Tests and Emerging Tools. <i>Cancers</i> 2025;17(21):3425. DOI: 10.3390/cancers17213425.",
    "Kim H et al. Noninvasive precision screening of prostate cancer by urinary multimarker sensor and AI. <i>ACS Nano</i> 2021;15:4054\u20134065. DOI: 10.1021/acsnano.0c06946.",
    "Phyo JB et al. Label-free SERS analysis of urine using 3D-stacked AgNW sensor. <i>Anal. Chem.</i> 2021;93:3778\u20133785. DOI: 10.1021/acs.analchem.0c04200.",
    "Urinary MicroRNA-21 for Prostate Cancer Detection Using AgNP Sensor. <i>Biosensors</i> 2024;14(12):599. DOI: 10.3390/bios14120599.",
    "Label-Free SERS of Urine Components for Discriminating RCC. <i>IJMS</i> 2024;25(7):3891. DOI: 10.3390/ijms25073891.",
    "Lu Y et al. Non-invasive diagnosis of low-grade bladder cancer via SERSomes of urine. <i>Nanoscale</i> 2025;17(12). DOI: 10.1039/d4nr05306k.",
    "Pan H et al. Sensing gastric-cancer exosomes with MoS\u2082-based SERS aptasensor. <i>Biosens. Bioelectron.</i> 2022;215:114553. DOI: 10.1016/j.bios.2022.114553.",
    "Pothipor C et al. Electrochemical biosensor for simultaneous detection of breast-cancer miRNAs. <i>Analyst</i> 2021;146:4000. DOI: 10.1039/D1AN00436K.",
    "Chang J et al. MOF-Based Electrochemical Biosensor for Simultaneous Detection of Multiple Tumour Biomarkers. <i>Anal. Chem.</i> 2019;91:3604. DOI: 10.1021/acs.analchem.8b05599.",
    "Jolly P et al. Application of optical and electrochemical aptasensors for PSA. <i>Biosens. Bioelectron.</i> 2019;142:111484. DOI: 10.1016/j.bios.2019.111484.",
    "Chen X et al. Three-dimensional PdAuCu nanocrystal-based immunosensor for CEA. (DPV) 2019.",
    "Yarjoo S et al. Porous-gold-electrode EIS immunosensor with anti-VEGF VHH nanobody. 2024.",
    "Alarfaj NA et al. Carbon quantum dot/ZnO nanocomposite fluorescent immunosensor for CYFRA 21-1. 2020.",
    "Yan F et al. MnO\u2082/HNM-AuPtPd amperometric immunosensor for CA72-4. 2024.",
    "Li Y et al. H-rGO\u2013Pd-NP nanozyme with silver deposition for GPC3 detection. 2023.",
    "Li B et al. Silver-nanocluster fluorescence platform with entropy-driven amplification for miR-141 / miR-155. 2021.",
    "Meng L et al. Ag@Au LSPR-enhanced ECL biosensor for miR-let-7a. 2025.",
    "Koo KM et al. AC-electrohydrodynamic nanomixing for amplification-free TMPRSS2:ERG detection in urine. 2017\u20132018.",
    "Liu Y et al. Carbon-nitride-nanosheet nanozyme array with aptamer-based fluorescence for exosomes. 2021.",
    "Highly sensitive urinary exosomal-miRNA biosensor for prostate-cancer progression evaluation. <i>Bioengineering</i> 2022.",
    "Comprehensive review of HPLC\u2013ECD for urinary 8-OHdG quantification. <i>Molecules</i> 2022.",
    "Li Q et al. Amperometric biosensor for sarcosine via cross-coupled chemical and electrochemical reactions. 2019.",
    "Urinary VOC biosensor platform for cancer detection. <i>Sci. Rep.</i> 2024.",
]
for i, r in enumerate(refs, 1):
    story.append(P(f"[{i}] {r}", style_ref))

# Build
doc.build(story)
print(f"Wrote: {OUT}")
