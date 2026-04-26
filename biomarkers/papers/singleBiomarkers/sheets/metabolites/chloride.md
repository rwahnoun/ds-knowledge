---
title: Chloride
aliases:
  - Chloride
  - Cl-
  - Chloride ion
tags:
  - topic/biomarker
  - topic/spectroscopy
  - type/reference
  - status/complete
date: 2026-04-19
status: complete
type: reference
author: Usense Healthcare
---

# [[chloride|Chloride]]

[[chloride|Chloride]] is the **principal extracellular anion** in the body. It accompanies [[sodium]] in maintaining ECF volume, osmolality, and electrical neutrality. In urine, [[chloride]] excretion largely parallels [[sodium]] excretion and is clinically valuable in assessing volume status, metabolic alkalosis aetiology, and acid-base disorders. See [[datascience/spectroscopy-biomarkers]] for electrolyte context; Cl⁻ is not detectable by [[optical-properties|direct optical methods]].

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | [[chloride\|Chloride]] |
| **Other names** | [[chloride\|Chloride]] ion, Cl⁻ |
| **Chemical formula** | Cl⁻ |
| **Atomic/molecular weight** | 35.45 g/mol |
| **CAS number** | 16887-00-6 ([[chloride]] ion) |
| **PubChem CID** | 312 |
| **Appearance** | Colourless in solution |

**Structural formula:**

```
  Cl(-)   (monovalent anion, fully hydrated in solution)
```

### Molecules Not to Be Confused With

| Molecule | Formula | MW (g/mol) | Key Difference |
|---|---|---|---|
| **Bicarbonate (HCO₃⁻)** | HCO₃⁻ | 61.02 | Second major ECF anion; inversely related to Cl⁻ in acid-base disorders |
| **Bromide (Br⁻)** | Br⁻ | 79.90 | Halide analogue; can interfere with some Cl⁻ assays |
| **Fluoride (F⁻)** | F⁻ | 19.00 | Another halide; different biological role (dental health) |

---

## Medical Information

### Origin

#### Endogenous

[[chloride|Chloride]] is not synthesised. Total body Cl⁻: ~33 mmol/kg (~2,300 mmol in a 70 kg adult). Predominantly extracellular (~88% in ECF). Also in gastric HCl secretion (~150 mmol/L in gastric juice).

#### Exogenous

Dietary NaCl is the primary source. Typical intake: 100–250 mmol/day Cl⁻ (matching Na⁺). Found in processed foods, table salt, bread, dairy, and cured meats.

### Primary & Secondary Biological Roles

**Primary role:**
- **Electrical neutrality and osmolality:** Cl⁻ is the main counter-ion to Na⁺ in ECF.
- **Gastric acid production:** Parietal cells secrete HCl for digestion and antimicrobial defence.

**Secondary roles:**
- **Acid-base balance:** Cl⁻ shifts ([[chloride]]-responsive vs -resistant alkalosis); renal Cl⁻ handling linked to H⁺ and HCO₃⁻ transport.
- **GABA receptor function:** Cl⁻ channels mediate inhibitory neurotransmission.
- **Immune function:** Myeloperoxidase uses Cl⁻ to generate hypochlorous acid (HOCl) for microbial killing.

### Catabolism and Elimination Pathway

- Cl⁻ is freely filtered (~18,000 mmol/day) and ~99% reabsorbed, primarily in the proximal tubule (paracellular), loop of Henle (NKCC2), and distal nephron.
- Urinary Cl⁻ excretion matches dietary intake at steady state.
- Other losses: sweat (~10–40 mmol/L), GI (vomiting: significant Cl⁻ loss; diarrhoea: variable).

### Expression in Humans

#### Normal Levels

| Compartment | Reference Range |
|---|---|
| **Serum [[chloride]]** | 96–106 mmol/L |
| **Urinary [[chloride]] (24-h)** | 110–250 mmol/day |
| **Urinary [[chloride]] (spot)** | 20–200 mmol/L |
| **Sweat [[chloride]]** | <30 mmol/L normal; >60 mmol/L diagnostic for CF |

#### Factors Influencing Levels

**Increased urinary Cl:**
- High NaCl diet
- Diuretics (loop, thiazide)
- Salt-wasting nephropathy
- Bartter syndrome, Gitelman syndrome
- Mineralocorticoid excess (with metabolic alkalosis)
- SIADH

**Decreased urinary Cl:**
- Vomiting (Cl⁻ loss in gastric fluid; renal conservation)
- Volume depletion
- [[chloride|Chloride]]-responsive metabolic alkalosis (UCl <20 mmol/L)
- Heart failure, cirrhosis
- Low-salt diet

#### Associated Pathologies

| Condition | Urine Cl Pattern | Key Symptoms |
|---|---|---|
| **[[chloride\|Chloride]]-responsive alkalosis (vomiting, NG suction)** | UCl <20 mmol/L | Metabolic alkalosis corrected by saline |
| **[[chloride\|Chloride]]-resistant alkalosis (hyperaldosteronism)** | UCl >20 mmol/L | Hypertension, hypokalaemia |
| **Cystic fibrosis** | Sweat Cl >60 mmol/L (not urine) | Recurrent lung infections, pancreatic insufficiency |
| **Bartter/Gitelman syndromes** | High UCl despite hypokalaemia | Metabolic alkalosis, normotension |

### Presence in Urine

**Should it be normally present?** **Yes** — [[chloride]] is a normal major urinary electrolyte.

**Normal urinary levels:** 110–250 mmol/day (24-h); spot 20–200 mmol/L.

**Form in urine:** **Cl⁻ ion** — fully dissociated. No crystallisation.

**Pathological significance:**

| Urinary Cl | Possible Causes | Prevalence |
|---|---|---|
| **High** | High salt diet, diuretics, salt-wasting | Common |
| **Low (<20 mmol/L)** | Vomiting, volume depletion, Cl-responsive alkalosis | Common |

**Solubility:** [[chloride|Chloride]] salts (NaCl, KCl) are highly soluble. No crystalluria.

---

## Detection in Urine

### Available Clinical Assays

1. **Ion-selective electrode (ISE):**
   - **Principle:** Ag/AgCl-based or polymer membrane ISE generates Nernstian potential for Cl⁻.
   - **Detection:** Potentiometric.
   - **LOD:** ~1 mmol/L. CV <2%.
   - **Advantages:** Standard on automated analysers; rapid.

2. **Coulometric-amperometric titration (Cotlove chloridometer):**
   - **Principle:** Cl⁻ reacts with Ag⁺ generated coulometrically; endpoint detected amperometrically.
   - **Detection:** Current change at silver electrodes.
   - **LOD:** ~1 mmol/L.
   - **Advantages:** Reference method; very precise.
   - **Disadvantages:** Manual; time-consuming.

3. **Mercurimetric titration:**
   - **Principle:** Hg(NO₃)₂ titrant reacts with Cl⁻ to form soluble, un-ionised HgCl₂; endpoint by diphenylcarbazone indicator (blue-violet).
   - **Detection:** Visual endpoint or 515 nm photometric.
   - **LOD:** ~5 mmol/L.

### Optimal Urine Type for Measurement

- **24-hour urine** for total excretion assessment.
- **Spot urine** for metabolic alkalosis workup (UCl <20 or >20 mmol/L determines Cl-responsive vs -resistant).
- No special preservatives. Stable at room temperature.

### Actual Gold Standard

**Coulometric-amperometric titration (chloridometer)** is the reference method. ISE on automated platforms (Roche, Siemens, Abbott) is the universal clinical method.

### Interferences in Measurement

| Interference | Effect | Mechanism |
|---|---|---|
| **Bromide** | Positive bias (ISE) | Cross-reactivity of Cl⁻ ISE membrane |
| **Iodide** | Positive bias (ISE) | Similar cross-reactivity |
| **High protein** | Minor effect | Excluded volume (indirect ISE) |
| **Thiocyanate** | Positive bias | Halide-like behaviour |

### Research Detection Methods

#### Spectroscopy Detection (UV-Vis / NIR)

- Cl⁻ has **no UV-Vis absorption** in aqueous solution. No direct spectroscopic detection.
- **Indirect colorimetric:** [[chloride|Chloride]] displaces thiocyanate from Hg(SCN)₂; free SCN⁻ reacts with Fe³⁺ → red Fe(SCN)₃ complex (460–480 nm). LOD: ~0.5 mmol/L. Sample prep: reagent addition.
- **NIR:** Not applicable.

#### Fluorescence Detection

- Cl⁻ is non-fluorescent. Indirect methods:
- **[[chloride|Chloride]]-quenching probes:** Lucigenin (bis-N-methylacridinium, Ex 368 / Em 505 nm) and SPQ (6-methoxy-N-(3-sulfopropyl)quinolinium, Ex 344 / Em 443 nm) are quenched by Cl⁻ via collisional quenching. LOD: ~1 mmol/L.
- **Sample prep:** Add probe to urine or diluted sample; measure fluorescence decrease.

#### Raman Detection

Cl⁻ (monatomic ion) has no Raman-active vibrational modes. Not detectable by Raman.

#### FTIR Detection

Cl⁻ has no IR absorption in solution (monatomic). Not detectable by FTIR.

#### Voltammetry Detection

- **Potentiometric ISE** is the standard (see above).
- **Amperometric titration** (chloridometer) at silver electrodes.
- Direct voltammetric oxidation of Cl⁻ (Cl⁻ → Cl₂) requires very high potentials (+1.36 V vs SHE) — not practical in urine.

### Other Detection Technologies

1. **Ion chromatography (IC):** Anion exchange + conductivity detection. LOD: ~0.01 mmol/L. Multi-anion (Cl⁻, SO₄²⁻, NO₃⁻, PO₄³⁻). Reference for research.
2. **Capillary electrophoresis:** UV indirect detection. LOD: ~0.1 mmol/L.
3. **Paper-based AgNO₃ test:** Ag⁺ + Cl⁻ → AgCl precipitate (white). Semi-quantitative. LOD: ~10 mmol/L.

---

## Detection Methods Comparison

| Method | LOD | Key Parameter | Sample Prep | Strengths |
|---|---|---|---|---|
| **ISE** | ~1 mmol/L | Potentiometric | None | Standard, fast |
| **Chloridometer** | ~1 mmol/L | Amperometric | Dilution | Reference, precise |
| **Colorimetric (Hg/Fe)** | ~0.5 mmol/L | 460–480 nm | Reagent | Simple, cheap |
| **Lucigenin fluorescence** | ~1 mmol/L | Ex 368/Em 505 nm | Probe addition | Imaging capable |
| **Ion chromatography** | ~0.01 mmol/L | Conductivity | Dilution | Multi-anion |
| **Raman / FTIR** | N/A | N/A | N/A | Not applicable |

---

## Sources

| # | Citation |
|---|---|
| 1 | PMC — Urine Electrolytes in Clinical Diagnosis. https://ncbi.nlm.nih.gov/pmc/articles/PMC8116912/ |
| 2 | AAFP — [[sodium\|Sodium]] Disorders (Cl discussed). https://www.aafp.org/pubs/afp/issues/2015/0301/p299.html |
| 3 | StatPearls — Metabolic Alkalosis. https://www.ncbi.nlm.nih.gov/books/NBK482291/ |
| 4 | MedlinePlus — Sweat Electrolytes Test. https://www.medlineplus.gov/ency/article/003630.htm |
| 5 | PubChem — [[chloride\|Chloride]], CID 312. https://pubchem.ncbi.nlm.nih.gov/compound/312 |

## Gaps

- No optical (Raman/FTIR/fluorescence) method has been validated for quantitative Cl⁻ measurement in urine at clinical concentrations.
- The diagnostic utility of spot urine Cl for acid-base classification outside of research settings is not well-validated in large prospective studies.
- Sweat [[chloride]] measurement (CF diagnostic) is a distinct matrix — methods do not translate directly to urine.
