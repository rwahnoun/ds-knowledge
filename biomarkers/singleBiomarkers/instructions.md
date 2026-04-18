# Generation of Biomarker Sheets

Perform a full literature review on the biomarkers listed at the bottom. For each biomarker, generate a `{biomarker}.md` file that follows the structure below, then convert it to PDF with `/md2pdf {biomarker}.md {biomarker}.pdf`.

## Required Front Matter

Every sheet starts with YAML front matter and a single H1:


```markdown
title: {Biomarker name}
author: Usense Healthcare
date: {YYYY-MM-DD}
```

## Document Structure

The body is organised in three top-level sections — **Identity Sheet**, **Medical Information**, **Detection in Urine** — plus a comparison summary table and references. Use `---` horizontal rules between the three top-level sections.

### `## Identity Sheet`

A two-column property table followed by a visual structural formula and, if relevant, a "not to be confused with" table.

**Property table** — include these rows when available:

| Property | Value |
|---|---|
| **Name** | Canonical name |
| **Other names** | Synonyms, trivial names |
| **Chemical formula** | Molecular and/or condensed form |
| **Molecular weight** | g/mol |
| **CAS number** | — |
| **PubChem CID** | — |
| **SMILES** | — |
| **Appearance** | Physical description |
| **Density** | g/cm³ |
| **Melting point** | °C |

**Structural formula** — render as an ASCII/unicode code block, e.g.:

````markdown
**Structural formula:**

```
        O
        ‖
   H₂N—C—NH₂
```
````

Follow with one paragraph describing salient chemistry (polarity, hydrogen bonding, charge state at physiological pH, etc.).

**`### Molecules Not to Be Confused With`** — include when the biomarker has similar-sounding or structurally related species that clinicians/engineers may confuse it with:

| Molecule | Formula | MW (g/mol) | Key Difference |
|---|---|---|---|
| **…** | … | … | … |

### `## Medical Information`

#### `### Origin`

Two `####` subsections:

- **`#### Endogenous: Biosynthesis — {pathway name}`** — main site of synthesis, enzymes, cofactors, regulation, rate-limiting step, typical daily production.
- **`#### Exogenous`** — dietary or environmental sources; topical / pharmaceutical uses.

#### `### Primary & Secondary Biological Roles`

Use bolded bullet lists:

- **Primary role:** one or two items
- **Secondary roles:** a list with one paragraph per item (physiological, mechanical, osmotic, etc.)

#### `### Catabolism and Elimination Pathway`

Bullets describing glomerular filtration, tubular reabsorption/secretion, enterohepatic recycling, minor routes (sweat, breath), and typical fractional excretion.

#### `### Expression in Humans`

Three `####` subsections:

- **`#### Normal Levels`** — table of serum/plasma/urine reference ranges by compartment and demographic.

| Compartment | Reference Range |
|---|---|
| **Serum/Plasma {biomarker}** | … |
| **Urinary {biomarker}** | … |

- **`#### Factors Influencing Levels`** — two bolded bullet lists: **Increased** and **Decreased**, each with ≥5 concrete causes.

- **`#### Associated Pathologies`** — table:

| Condition | {Biomarker} Level | Key Symptoms |
|---|---|---|
| **…** | … | … |

#### `### Presence in Urine`

Narrative + tables that answer the five required questions:

- **Should it be normally present?** Yes/No + typical fraction of total urinary solids.
- **Normal urinary levels:** 24-h excretion, concentration range, ancillary ratios (e.g. BUN).
- **Form in urine:** native vs. conjugated/ionised; pKa behaviour across urinary pH 4.5–8.0.
- **Pathological significance of abnormal urinary {biomarker}:**

| Urinary {biomarker} | Possible Causes | Prevalence |
|---|---|---|
| **Elevated** | … | … |
| **Decreased** | … | … |

- **Solubility:** aqueous solubility at 20 °C and temperature dependence; stone/crystalluria relevance.

### `## Detection in Urine`

#### `### Available Clinical Assays`

Numbered list, one entry per routine clinical method. For each, bolded sub-fields:

1. **{Method name}:**
   - **Principle:** chemistry / physics
   - **Detection:** signal read (wavelength, electrode potential, etc.)
   - **Advantages:** …
   - **Disadvantages:** …

#### `### Optimal Urine Type for Measurement`

Bullets on 24-h vs. spot, morning vs. random, creatinine normalisation, preservation (temperature, additives).

#### `### Actual Gold Standard`

One or two paragraphs naming the reference method on major automated platforms, CV, precision.

#### `### Interferences in Measurement`

| Interference | Effect | Mechanism |
|---|---|---|
| **…** | … | … |

#### `### Research Detection Methods`

One `####` subsection per modality, each covering **LOD, excitation/emission/absorption wavelengths, sample pretreatment**:

- **`#### Spectroscopy Detection (UV-Vis / NIR)`**
- **`#### Fluorescence Detection`** — enumerate enzyme-coupled, QD, carbon-dot, ratiometric sensors
- **`#### Raman Detection`** — include a peak-assignment table:

| Peak (cm⁻¹) | Assignment |
|---|---|
| **…** | … |

  then discuss conventional Raman and SERS (substrate, enhancement factor, excitation wavelengths)

- **`#### FTIR Detection`** — include a band table:

| Band (cm⁻¹) | Assignment | Notes |
|---|---|---|
| **…** | … | … |

  then discuss ATR-FTIR, quantification band, hydration effects

- **`#### Voltammetry Detection`** — enzymatic vs. non-enzymatic, electrode material, LOD, linear range

#### `### Other Detection Technologies`

Numbered list: paper/lateral-flow, microfluidic, MIP, conductimetric, calorimetric, etc. Each with LOD and sample-prep notes.

### `## Summary Table: Detection Methods Comparison`

Six-column table summarising every method covered above:

| Method | LOD | Wavelength / Key Parameter | Sample Prep | Strengths | Limitations |
|---|---|---|---|---|---|
| **{Method}** | … | … | … | … | … |

### `## References`

Numbered list of sources with full URLs. Mix authoritative references (PubChem, StatPearls, NCBI Bookshelf, MedlinePlus, UCSF Health) with recent primary literature (≤10 years old where possible) for each detection modality.

## Mandatory Reporting for Every Detection Method

Whenever a detection technique is described — clinical assay, research method, or "other" — it **must** report:

- **Limit of detection (LOD)** in absolute units (µM, mM, ng/mL)
- **Excitation / emission / absorption wavelengths** (nm) where applicable
- **Sample pretreatment**: centrifugation, dilution, buffer, enzyme addition, pH adjustment, etc.
- **Linear range** when available
- **Key citation** for non-routine / research methods

## Rendering to PDF

After the markdown file is written:

```
/md2pdf {biomarker}.md {biomarker}.pdf
```

The `md2pdf` skill applies the Usense branded template (Cambria body text with full Unicode coverage, navy/amber palette, banner with logo). URLs wrap automatically and the References section renders at `\footnotesize`.

---

# Biomarkers List

- porphobilinogen
- total urinary porphyrin (TUP)
- bacteria
- red blood cells
- haemoglobin
- nitrites
- white blood cells
- leukocytes
- sodium
- chloride
- creatinin
- phosphate
- magnesium
- urine specific gravity (USG)
- osmolality
- glucose
- ketone
- bilirubin
- urea
- uric acid
- NADH
- FAD
- riboflavin
- oxalate
- citrate
- pH
- tryptophan
- copper
- metolachlore
- PFAs
- chlorotalonil
