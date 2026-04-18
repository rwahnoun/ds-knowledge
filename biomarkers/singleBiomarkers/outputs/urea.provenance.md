# Provenance Record — Urea Biomarker Sheet

**Date:** 2026-04-17  
**Slug:** urea  
**Output:** `outputs/urea.md` → `papers/urea.pdf`

## Sources Consulted vs. Accepted

| Source | Type | Status | Used For |
|---|---|---|---|
| PubChem CID 1176 | Web/DB | ✅ Accepted | Identity, formula, MW |
| ChemEurope/Bionity Encyclopedia | Web | ✅ Accepted | Physical properties, solubility |
| StatPearls — Urea Cycle Physiology | Web/Med | ✅ Accepted | Biosynthesis pathway |
| NCBI Basic Neurochemistry — Urea Cycle | Web/Med | ✅ Accepted | Urea cycle enzymology |
| StatPearls — Azotemia | Web/Med | ✅ Accepted | Pathologies, BUN ranges |
| MedlinePlus — BUN Test | Web/Med | ✅ Accepted | Reference ranges, clinical context |
| MedlinePlus — Urine Urea Nitrogen Test | Web/Med | ✅ Accepted | Urinary urea, 24-hour collection |
| UCSF Health — Urea Nitrogen Urine Test | Web/Med | ✅ Accepted | Urinary urea method |
| DrOracle — Normal Urine Urea | Web/Med | ✅ Accepted | Urinary concentration ranges |
| Labpedia — Urine 24h Urea | Web/Med | ✅ Accepted | Preservation, reference ranges |
| LabReadAI — Blood Urea BUN | Web/Med | ✅ Accepted | Age-stratified reference ranges |
| UK Lab Med Catalogue — Urea | Clinical ref | ✅ Accepted | Analytical methods overview |
| Atlas Medical — Urease-GLDH Kit | Reagent doc | ✅ Accepted | Gold standard assay principle |
| Langenfeld et al. (2021) PLoS ONE | Paper | ✅ Accepted | DAM method details |
| Barbour & Welch (1992) | Paper | ✅ Accepted | Kinetic DAM for urine |
| Rich & Sheringham (2017) Appl Spectrosc | Paper | ✅ Accepted | FTIR hydration states, key reference |
| Shaw et al. (2000) Clin Chem | Paper | ✅ Accepted | Mid-IR quantification in urine |
| RSC Advances (2025) Fe₃O₄@C@Ag SERS | Paper | ✅ Accepted | SERS urea detection, LOD |
| MDPI Biosensors (2024) SERS review | Review | ✅ Accepted | SERS landscape |
| Anal Sciences (2018) AuNP@Al SERS | Paper | ✅ Accepted | Cost-effective SERS |
| Springer (2023) ZnS QDs-Urease | Paper | ✅ Accepted | Fluorescence QD probe |
| Springer (2024) Ratiometric fluorescence | Paper | ✅ Accepted | Dual-emission CD system |
| ScienceDirect (2007) CdSe/ZnS QDs | Paper | ✅ Accepted | QD-based urea sensor |
| RSC Advances (2018) N-CDs | Paper | ✅ Accepted | Carbon nanodots for urea |
| ScienceDirect (2013) CuInS₂ QDs | Paper | ✅ Accepted | Dopamine-QD probe |
| Sci Rep (2025) NiNPs | Paper | ✅ Accepted | Non-enzymatic electrochemical |
| Adv Sensor Res (2025) Review | Review | ✅ Accepted | Electrochemical biosensor landscape |
| RSC Advances (2016) NiO | Paper | ✅ Accepted | NiO nanostructure sensor |
| Electrochim Acta (2021) Ni(bzimpy) | Paper | ✅ Accepted | Organometallic Ni sensor |
| Harrison's Manual — Azotemia chapter | Textbook | ✅ Accepted | Clinical definitions |
| Kirk-Othmer — Urea entry | Encyclopedia | ✅ Accepted | Solubility data |

## Rejected / Not Used

| Source | Reason |
|---|---|
| MDPI papers on MIP for food contaminants | Not specific to urea in urine |
| Protein denaturation papers (urea-water interactions) | Off-topic for biomarker sheet |
| Milk adulteration FTIR papers | Different matrix (milk, not urine) |

## Verification Status

- ✅ Chemical identity cross-checked: PubChem, ChemEurope, Kirk-Othmer agree on formula, MW, CAS
- ✅ Reference ranges cross-checked: MedlinePlus, LabReadAI, StatPearls consistent
- ✅ Urea cycle steps verified against StatPearls and NCBI Bookshelf
- ✅ Gold standard assay confirmed as urease-GLDH from multiple clinical chemistry sources
- ✅ FTIR bands verified against Rich (2017) primary data
- ✅ SERS LOD (5.68 nM) sourced from primary paper with recovery data
- ⚠️ Some fluorescence LOD values are from buffer studies; performance in real urine may be worse
- ⚠️ Electrochemical sensors require alkaline media — not directly compatible with native urine pH

## Files

| File | Role |
|---|---|
| `outputs/.plans/urea.md` | Research plan |
| `outputs/urea.md` | Final Markdown deliverable |
| `outputs/urea.provenance.md` | This file |
| `papers/urea.pdf` | PDF output |
