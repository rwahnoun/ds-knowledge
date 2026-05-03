---
title: Copper
aliases:
  - Copper
  - Cu
  - Cu2+
  - Cupric ion
tags:
  - topic/biomarker
  - topic/spectroscopy
  - type/reference
  - status/complete
  - class/trace-element
  - clinical/wilsons-disease
  - clinical/trace-mineral
  - modality/uv
  - modality/vis
  - modality/eis
  - presence/trace
  - subclass/transition-metal
date: 2026-04-19
status: complete
type: reference
author: Usense Healthcare
clinical-use:
  - wilsons-disease
  - trace-mineral
detection-modality:
  - uv
  - vis
  - eis
class: trace-element
subclass: transition-metal
presence: trace
parent: "[[biomarkers/compounds/metabolites/index|metabolites]]"
---
# Copper

Copper is an essential trace element serving as a cofactor for numerous redox enzymes (cytochrome c oxidase, superoxide dismutase, ceruloplasmin, lysyl oxidase, dopamine beta-hydroxylase). Total body copper: ~75–150 mg. Copper homeostasis is tightly regulated via intestinal absorption (ATP7A) and hepatic biliary excretion (ATP7B). Elevated urinary copper is the hallmark of **Wilson disease**. See [[datascience/spectroscopy-biomarkers]] for trace element context.

---

## Identity Sheet

| Property | Value |
|---|---|
| **Name** | Copper |
| **Other names** | Cu, Cu²⁺, cupric ion |
| **Chemical formula** | Cu²⁺ (predominant biological form) |
| **Atomic weight** | 63.55 g/mol |
| **CAS number** | 7440-50-8 |
| **PubChem CID** | 23978 |
| **Appearance** | Colourless to blue-green in solution (Cu²⁺ complexes) |

**Structural representation:**

```
  Cu(2+)  (transition metal divalent cation)
```

### Molecules Not to Be Confused With

| Molecule | Formula | MW | Key Difference |
|---|---|---|---|
| **Ceruloplasmin** | Protein | ~132 kDa | Copper-binding plasma protein; carries ~90% of serum Cu; low in Wilson disease |
| **Zinc (Zn²⁺)** | Zn²⁺ | 65.38 | Another essential trace metal; competes with Cu absorption |
| **Iron (Fe²⁺/Fe³⁺)** | Fe | 55.85 | Different transition metal; different metabolic roles |

---

## Medical Information

### Origin

#### Endogenous

Copper is not synthesised. Total body content: ~75–150 mg. Liver is the main storage organ. Ceruloplasmin (synthesised in liver) carries ~90% of plasma copper.

#### Exogenous

Dietary sources: shellfish, liver, nuts, seeds, whole grains, dark chocolate, mushrooms. RDA: 0.9 mg/day (adults). Typical intake: 1–2 mg/day. Absorbed in duodenum/jejunum via CTR1 transporter; regulated by ATP7A (Menkes protein).

### Primary & Secondary Biological Roles

**Primary role:**
- **Enzymatic cofactor:** Essential for cytochrome c oxidase (ETC Complex IV), Cu/Zn-SOD (antioxidant), ceruloplasmin (ferroxidase, iron metabolism), lysyl oxidase (collagen/elastin crosslinking), dopamine beta-hydroxylase (catecholamine synthesis), tyrosinase (melanin).

**Secondary roles:**
- **Iron metabolism:** Ceruloplasmin oxidises Fe²⁺ to Fe³⁺ for transferrin loading.
- **Connective tissue integrity:** Lysyl oxidase requires Cu for collagen/elastin crosslinking.
- **Immune function:** Cu deficiency impairs neutrophil function.

### Catabolism and Elimination Pathway

- **Biliary excretion** is the primary route (~80%); regulated by ATP7B in hepatocytes.
- Urinary copper excretion is normally very low (<40 µg/day) — Cu is protein-bound (ceruloplasmin, albumin) and not freely filtered.
- In Wilson disease, ATP7B dysfunction leads to copper accumulation in liver and overflow into blood (free Cu) and urine.
- D-penicillamine chelates Cu and dramatically increases urinary Cu excretion (used diagnostically and therapeutically).

### Expression in Humans

#### Normal Levels

| Compartment | Reference Range |
|---|---|
| **Serum copper** | 70–140 µg/dL (11–22 µmol/L) |
| **Serum ceruloplasmin** | 20–50 mg/dL |
| **Urinary copper (24-h)** | <40 µg/day (<0.6 µmol/day) |
| **Urinary Cu (Wilson disease)** | >100 µg/day (often >200 µg/day) |
| **Post-penicillamine urinary Cu** | >1600 µg/day diagnostic for Wilson |
| **Hepatic copper** | <50 µg/g dry weight (normal); >250 µg/g (Wilson) |

#### Factors Influencing Levels

**Increased urinary copper:**
- Wilson disease (ATP7B mutations)
- D-penicillamine or trientine chelation therapy
- Acute hepatitis (hepatocyte necrosis releases Cu)
- Nephrotic syndrome (ceruloplasmin loss; free Cu filtered)
- Copper poisoning (rare; occupational)
- Chronic active hepatitis

**Decreased urinary copper:**
- Normal state
- Menkes disease (ATP7A mutation; copper malabsorption; very low serum and urine Cu)

#### Associated Pathologies

| Condition | Copper Pattern | Key Symptoms |
|---|---|---|
| **Wilson disease** | Low ceruloplasmin, high urine Cu (>100 µg/day), high hepatic Cu | Liver disease, neuropsychiatric symptoms, Kayser-Fleischer rings; 1:30,000 |
| **Menkes disease** | Very low serum Cu, low ceruloplasmin, low urine Cu | Kinky hair, seizures, connective tissue defects; X-linked; ~1:100,000 |
| **Copper deficiency** | Low serum Cu | Anaemia, neutropenia, myelopathy |
| **Copper toxicity** | Very high serum Cu, high urine Cu | Nausea, liver failure (acute); rare |

### Presence in Urine

**Should it be normally present?** In **trace amounts** only (<40 µg/day). Most copper is protein-bound and not filtered.

**Normal urinary levels:** <40 µg/day (<0.6 µmol/day).

**Form in urine:** Cu²⁺ ion, partially complexed with amino acids and small organic molecules.

**Pathological significance:**

| Urinary Cu | Possible Causes | Prevalence |
|---|---|---|
| **>100 µg/day** | Wilson disease, chelation therapy | Wilson: ~1:30,000 |
| **<10 µg/day** | Normal or Menkes disease | — |

**Solubility:** Cu²⁺ salts generally soluble. No urinary crystal issues.

---

## Detection in Urine

### Available Clinical Assays

1. **Flame or graphite furnace AAS:**
   - **Principle:** Cu atoms absorb light at **324.7 nm** from a Cu hollow-cathode lamp.
   - **Detection:** Absorption at **324.7 nm**.
   - **LOD:** ~0.5 µg/L (GFAAS); ~5 µg/L (flame AAS).
   - **Advantages:** Reference method; highly specific.

2. **ICP-OES / ICP-MS:**
   - **Principle:** Plasma excitation/ionisation of Cu.
   - **Detection:** Emission at 324.7/327.4 nm (OES) or m/z 63/65 (MS).
   - **LOD:** ~0.01 µg/L (ICP-MS).
   - **Advantages:** Multi-element; ultimate sensitivity.

3. **Colorimetric (bathocuproine/BCS):**
   - **Principle:** Cu⁺ (after reduction) reacts with bathocuproine disulfonate → orange complex.
   - **Detection:** Absorbance at **484 nm**.
   - **LOD:** ~1 µg/dL.
   - **Advantages:** Simple, automatable.

### Optimal Urine Type for Measurement

- **24-hour urine** in acid-washed, metal-free containers (trace element contamination is the main preanalytical concern).
- Acidify with 6N HCl (prevents Cu adsorption to container walls).
- Avoid rubber stoppers, coloured containers.
- Random specimens unreliable due to variable concentration.

### Actual Gold Standard

**ICP-MS** is the reference method for trace copper in urine. GFAAS is widely used in clinical labs. CV: 5–10%.

### Interferences in Measurement

| Interference | Effect | Mechanism |
|---|---|---|
| **Container contamination** | Falsely high | Metal from container, stoppers |
| **Haemolysis** | Positive bias | Erythrocyte Cu release |
| **EDTA anticoagulant** | Negative bias if chelated | Chelates Cu |
| **High zinc** | Spectral interference (AAS) | Adjacent lines (AAS); resolved by ICP-MS |

### Research Detection Methods

#### Spectroscopy Detection (UV-Vis / NIR)

- **AAS at 324.7 nm:** See clinical assay. Reference.
- **UV-Vis colorimetric (bathocuproine, 484 nm):** LOD ~1 µg/dL.
- **Cu²⁺ d-d transitions:** Very weak absorption at ~600–900 nm (blue-green); not useful for trace analysis.

#### Fluorescence Detection

- Cu²⁺ is a fluorescence quencher (paramagnetic d9). Indirect approaches:
- **Turn-off probes:** Fluorescent chelators quenched by Cu²⁺ (e.g., calcein: Ex 490/Em 515 nm). LOD: ~0.1 µmol/L.
- **Turn-on probes:** Cu²⁺-triggered dequenching or reaction-based probes. Various Ex/Em. LOD: ~0.01–0.1 µmol/L.
- **Quantum dots (CdTe):** Cu²⁺ quenches QD fluorescence. Ex 350/Em 540 nm. LOD: ~5 nM.

#### Raman Detection

- Cu²⁺ (monatomic ion) has no Raman modes. Not directly detectable.
- **Cu complexes** with organic ligands have Raman-active modes.

#### FTIR Detection

- Not applicable for Cu²⁺ ion detection.

#### Voltammetry Detection

- **Anodic stripping voltammetry (ASV):** Cu is deposited on electrode at -0.4 V, then stripped (oxidised) at ~+0.05 V vs Ag/AgCl. Peak current proportional to Cu concentration.
  - LOD: ~0.1–1 µg/L (ppb level).
  - **Electrode:** Mercury film (HMDE), bismuth film, or carbon.
  - **Advantages:** Very sensitive, inexpensive, field-deployable.
- **Potentiometric Cu-ISE:** LOD ~0.01 µmol/L.

### Other Detection Technologies

1. **Total reflection XRF (TXRF):** LOD ~0.1 µg/L. Multi-element, no digestion needed.
2. **Neutron activation analysis (NAA):** LOD ~0.01 µg/L. Ultimate reference. Limited access.
3. **Paper-based colorimetric:** Dithizone or bathocuproine on paper. LOD: ~50 µg/L.

---

## Detection Methods Comparison

| Method | LOD | Key Parameter | Sample Prep | Strengths |
|---|---|---|---|---|
| **GFAAS** | ~0.5 µg/L | 324.7 nm absorption | Acid-washed | Reference |
| **ICP-MS** | ~0.01 µg/L | m/z 63/65 | Dilution | Multi-element, ultimate |
| **Colorimetric (BCS)** | ~10 µg/L | 484 nm | Reduction | Simple |
| **ASV** | ~0.1 µg/L | Strip at +0.05 V | Deposition | Sensitive, cheap |
| **QD fluorescence** | ~5 nM | Ex 350/Em 540 nm | Probe | Sensitive |
| **Cu-ISE** | ~0.01 µmol/L | Potentiometric | None | Real-time |

---

## Sources

| # | Citation |
|---|---|
| 1 | AASLD — Wilson Disease Practice Guidelines. https://www.aasld.org/ |
| 2 | StatPearls — Wilson Disease. https://www.ncbi.nlm.nih.gov/books/NBK441990/ |
| 3 | StatPearls — Menkes Disease. https://www.ncbi.nlm.nih.gov/books/NBK560917/ |
| 4 | ACS — Ca and Mg in Urine by AAS (analogous Cu method). https://pubs.acs.org/doi/abs/10.1021/ac60172a021 |
| 5 | PubChem — Copper, CID 23978. https://pubchem.ncbi.nlm.nih.gov/compound/23978 |

## Gaps

- Fluorescent turn-on probes for Cu²⁺ in urine matrix have not been validated at clinical concentrations (<40 µg/day / sub-µM range).
- No POC test for urinary copper exists; Wilson disease diagnosis still requires lab-based ICP-MS or GFAAS.
- The diagnostic threshold of >100 µg/day for Wilson disease has variable sensitivity; some patients present at lower levels.
- Speciation of urinary copper (free vs complexed) is not routinely characterised.

[datascience/spectroscopy-biomarkers]: ../../../../../datascience/spectroscopy-biomarkers.md "Urine Spectroscopy & Biomarker Prediction with LED-Based Portable Devices"
