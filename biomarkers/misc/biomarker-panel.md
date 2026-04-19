---
title: Urine Biomarker Panel — Jimini Reference
aliases:
  - biomarker panel
  - urine biomarker panel
  - jimini panel
  - detection summary
tags:
  - topic/biomarker
  - topic/spectroscopy
  - type/reference
  - status/complete
  - device/jimini
date: 2026-04-19
status: complete
type: reference
author: Usense Healthcare
---

# Urine Biomarker Panel — Jimini Reference

Reagent-free detection reference for the Jimini panel. Device specs and LED-to-biomarker mapping: [[optical-signatures]]. Literature basis: [[literature]].
**Wavelength notation:** `x->y` = excitation/absorbance at x nm, fluorescence emission at y nm | `x->` = absorbance only | `->y` = emission only (excitation broad/indirect)

---

## Soluble Metabolites

### Urea
- **Optical:** `1400->` `1800->` `2000->` `2200->` (NIR vibrational overtones of N-H and C=O bonds)
- **EIS:** Indirect — contributes to conductivity/ionic strength; not EIS-primary target.
- **Notes:** No UV chromophore. High feasibility via NIR + PLS regression (correlation >0.99 in literature). Quantification requires multivariate chemometrics — water background dominates NIR. A key anchor for normalization ratios (urea-to-creatinine).

### Creatinine
- **Optical:** `210->` `235->` `280->` (UV) | `1600->` `1700->` `1800->` `2100->` `2200->` (NIR, preferred for urine matrix)
- **EIS:** Not a primary EIS target; minor interferent in biosensors for other analytes.
- **Notes:** High feasibility. NIR preferred over UV due to fewer interferences. The 235 nm peak is least interfered in UV. Used clinically as creatinine-to-analyte ratio normalization (ACR, PCR). Essential reference analyte.

### Uric Acid
- **Optical:** `205->` `230->` `260->` `290->` `293->` (UV absorption; λ_max 292–294 nm)
- **EIS:** EIS biosensors reported using uricase-modified electrodes; feasible.
- **Notes:** High feasibility. Strong π→π* transition from purine ring. Peak at 293 nm sits on complex sloping UV background — requires derivative spectroscopy or baseline correction. Ascorbate and some drugs overlap at 260 nm. Most reliable detection at 290–294 nm window.

### Glucose
- **Optical:** `210->` `260->` `270->` (weak UV) | NIR full-spectrum fingerprint
- **EIS:** Well-documented — glucose oxidase (GOx)-based EIS biosensors; yes, EIS is strong here.
- **Notes:** Low feasibility for reagent-free spectroscopy. No distinct chromophore. Only viable via broadband spectral fingerprinting + advanced ML (Random Forest, etc.). Clinically relevant threshold ~25 mg/dL glucosuria is very challenging optically. EIS with enzyme electrode is the better route.

### Oxalate
- **Optical:** `200->` `220->` (direct UV of oxalic acid, weak) | `427->` (colorimetric with Fe/curcumin — requires reagent) | `535->` (Ag-complex, reagent-based)
- **Fluorescence:** `365->600` (CdTe quantum dot quenching) | `->613` (macrocycle EY complex)
- **EIS:** Oxalate oxidase-based electrodes reported; feasible.
- **Notes:** Direct reagent-free detection is challenging. Oxalic acid has weak UV abs at ~200–220 nm only. Most published methods require reagent (enzyme or metal complex). For reagent-free system, indirect detection via crystal formation (turbidity/MALS — see Crystals). Clinically important for calcium oxalate urolithiasis.

### Ammonia
- **Optical:** `550->` (OPA reaction product — requires reagent) | `220->` `260->` (weak direct UV)
- **Fluorescence:** `363->423` (fluorescent derivatization product) | `470->530` (aza-BODIPY optical sensor)
- **EIS:** EIS with urease or ammonia-selective electrodes; feasible.
- **Notes:** Ammonia itself is not a strong UV chromophore in physiological concentrations. In urine, ammonia is primarily produced by bacterial/enzymatic urea hydrolysis — elevated ammonia signals urinary infection or storage degradation. Reagent-free detection relies on NIR or indirect inference. Gas-phase optical sensors exist for breath/headspace but not directly applicable here.

### pH
- **Optical:** `434->` `578->` (indicator-based colorimetry, e.g., meta-cresol purple — requires indicator) | NIR water band shifts (reagent-free, indirect)
- **Fluorescence:** `470->530` (urease-activity pH probes) | `490->520` (fluorescent pH indicators)
- **EIS:** Direct — pH electrode (potentiometric). EIS not standard for pH.
- **Notes:** Reagent-free direct pH from spectroscopy requires indicator dye. NIR water bands shift subtly with pH but this is extremely challenging to deconvolve from other matrix components. Standard approach: glass pH electrode or optical sensor film. Urine pH range 4.5–8.0 important for crystal risk, infection assessment. Affects spectral properties of all pH-sensitive chromophores in the sample.

### Titratable Acidity
- **Optical:** Not directly measurable by spectroscopy.
- **EIS:** Indirect — total acid content correlates with conductivity; not primary EIS target.
- **Notes:** Titratable acidity = total urinary buffer capacity (primarily phosphate and organic acids). Measured by acid-base titration to pH 7.4. Cannot be detected optically without reagents. Correlates with ammonia excretion, phosphate levels, and acid-base balance. Requires electrochemical or titration approach. Consider integrating pH electrode + phosphate estimation.

### Osmolality
- **Optical:** Not directly measurable. **Refractometry:** refractive index at 589 nm (Abbe) strongly correlates with osmolality (r ~0.75–0.94). NIR spectrum indirectly reflects total solute concentration.
- **EIS:** Conductivity/total ionic strength (EIS at low frequency) correlates with osmolality; very feasible as a surrogate.
- **Notes:** Gold standard is freezing-point depression osmometry. Refractometry (specific gravity) is the standard optical proxy — strong correlation with osmolality and total solids. NIR PLS models trained to predict osmolality are feasible given its relationship to urea + creatinine + ions. A conductivity sensor would provide a direct surrogate. Critical normalization parameter.

---

## Proteins

### Protein (Total)
- **Optical:** `220->` `230->` (peptide bonds) | `280->` (aromatic residues: Trp, Tyr, Phe)
- **Fluorescence:** `280->340` `295->340` (tryptophan intrinsic fluorescence)
- **EIS:** Antibody-based or non-specific impedimetric detection feasible; used in CKD monitoring.
- **Notes:** Medium feasibility. The 280 nm absorption is non-specific (extinction coefficient varies by protein composition). Fluorescence at Ex 295/Em 340 is more sensitive and protein-selective. Strong interferences from other UV absorbers. Chemometric deconvolution essential. Clinically: normal urine protein <150 mg/day; elevated in nephropathy.

### Albumin (Microalbumin)
- **Optical:** `229->` `280->` (UV absorption; 229 nm distinct from creatinine at 249 nm)
- **Fluorescence:** `295->340` (tryptophan intrinsic fluorescence — albumin contains Trp214)
- **EIS:** Well-documented impedimetric immunosensors (anti-HSA antibody on electrode); very feasible for microalbuminuria (30–300 µg/mL range).
- **Notes:** Medium feasibility optically. Fluorescence more sensitive than UV abs for microalbumin detection. Inner filter effect and quenching are significant in complex urine matrix. EIS immunosensor is a strong alternative/complement for clinical threshold detection. Key biomarker: ACR (albumin-to-creatinine ratio) is the clinical gold standard for CKD screening.

---

## Electrolytes / Inorganic Ions

> [!IMPORTANT]
> None of these ions have direct UV-Vis-NIR chromophores or fluorescence. All direct optical methods require reagents (colorimetric complexation). Reagent-free sensing relies on indirect NIR (water structure perturbation) or electrochemical methods.

### Sodium
- **Optical:** `1450->` `1940->` (indirect NIR — ion hydration perturbs water bands; exploratory/high-risk)
- **EIS:** Strong candidate — conductivity sensor measures total ionic strength (Na+ is dominant cation). Ion-selective electrode (ISE) + EIS can give Na+ specific signal. Feasible.
- **Notes:** Most abundant urinary cation. Direct optical: not feasible reagent-free. EIS conductimetry is the practical route; combined with K+/Cl- model to parse contributions. Clinically: urinary Na+ reflects dietary intake and renal tubular function.

### Potassium
- **Optical:** `1450->` `1940->` (indirect NIR, exploratory — similar to Na+)
- **EIS:** Ion-selective electrode (K+-ISE) combined with EIS feasible. Total conductivity reflects K+ among other ions.
- **Notes:** Potassium has no optical signature. ISE electrochemistry is the standard analytical approach. In a multi-sensor device, a K+-selective film on an impedimetric electrode can provide selectivity. Clinically: urinary K+ for hypokalemia/hyperkalemia, aldosterone effects.

### Chloride
- **Optical:** No direct chromophore. Not detectable by spectroscopy reagent-free.
- **EIS:** Conductivity sensor (Cl- is dominant anion). Chloride-selective ISE + EIS feasible.
- **Notes:** Similar to Na+/K+ — electrochemical ISE is the only viable reagent-free route. Cl- tracks closely with Na+ in urine. Important for acid-base and hydration assessment.

### Calcium
- **Optical:** `210->` `230->` (very weak UV, only as Ca-oxalate or Ca-urate precipitates; turbidity at 660 nm)
- **EIS:** Calcium-selective electrodes (ISE) combined with EIS reported. Feasible.
- **Notes:** Ca²⁺ itself is UV-transparent. Detection as dissolved ion requires reagents. As crystals (Ca-oxalate), detectable via MALS/turbidity. ISE + EIS is more tractable for ionic calcium. Clinically: hypercalciuria (>7.5 mmol/day) is a major risk factor for urolithiasis.

### Magnesium
- **Optical:** No direct chromophore. Not detectable by spectroscopy reagent-free.
- **EIS:** Magnesium-selective ISE feasible but less developed than Na/K/Ca. Total ionic strength from conductivity provides a surrogate.
- **Notes:** Mg²⁺ optically invisible. Lower concentration than Na/K/Ca in urine. NIR indirect approach highly speculative. ISE is the route. Clinically: low urinary Mg linked to nephrolithiasis and hypomagnesemia.

### Phosphorus / Phosphate
- **Optical:** No direct chromophore for inorganic phosphate (PO₄³⁻) reagent-free. `210->` (very weak, requires reagent for colorimetric methods: molybdate blue at 820 nm)
- **EIS:** Phosphate-selective sensors (molybdate or phosphate binding protein-based) reported with EIS. Feasible.
- **Notes:** Phosphate is UV-transparent. Standard method uses ammonium molybdate + reducing agent (colorimetric at 820 nm) — requires reagent. In NIR, phosphate contributes subtle signals but deconvolution is very challenging. EIS with functionalized electrode is the more tractable non-optical approach. Clinically: hyperphosphaturia in Fanconi syndrome, renal tubular acidosis.

---

## Cellular / Particulate Elements

> [!NOTE]
> All particulate elements are detected via **light scattering** (turbidimetry or MALS) and **ML-based classification**. A 635 nm laser is a common MALS source.

### Red Blood Cells (RBC)
- **Optical:** `660->` (turbidity/scattering) | `415->` `541->` `577->` (oxyhemoglobin Soret + Q-bands, after hemolysis)
- **EIS:** RBC lysis releases hemoglobin; impedance changes with RBC concentration (hematocrit-type measurements). Feasible for cell counting.
- **Notes:** Intact RBCs scatter at 660 nm. Hemolysis releases Hb with strong Soret band at 415 nm — can be used as a secondary detection. MALS provides size (~7 µm biconcave disk) for classification. Overlaps with WBC size range — ML classifier required. Clinically: hematuria >3 RBC/HPF is significant.

### White Blood Cells (WBC)
- **Optical:** `660->` (turbidity/scattering) | `260->` (DNA/RNA released on lysis) | `280->` (protein, post-lysis)
- **EIS:** Leukocyte impedance-based cell counters well established; EIS feasible.
- **Notes:** WBCs slightly larger than RBCs (~10–15 µm vs ~7 µm). Lysis releases nucleic acids (260 nm) and proteins (280 nm). MALS with ML needed to differentiate from RBCs and large epithelial cells. Clinically: pyuria (>5 WBC/HPF) indicates UTI or inflammation.

### Epithelial Cells
- **Optical:** `660->` (scattering/turbidity) | MALS (multi-angle scattering profile)
- **EIS:** Not a primary EIS target.
- **Notes:** Squamous epithelial cells are large (>20 µm), tubular cells smaller. High morphological variability makes classification challenging. MALS angular profile differs from RBC/WBC. Clinically: squamous cells indicate contamination; tubular epithelial cells indicate tubular injury.

### Crystals
- **Optical:** `660->` (turbidity; high-refractive-index particles) | MALS (distinctive crystalline scattering)
- **EIS:** Not a primary EIS target. Ca²⁺ and oxalate concentrations (EIS/spectroscopy) help predict crystallization risk.
- **Notes:** Crystal types — calcium oxalate (envelope-shaped), uric acid (rhomboid), struvite (coffin-lid), Ca-phosphate (star-shaped). High RI generates strong MALS signal distinct from cells. Polarized light scattering can exploit birefringence of crystals. ML classification of scattering fingerprints needed for crystal typing.

### Cylinders (Casts)
- **Optical:** `660->` (scattering) | MALS (large cylindrical structure, highly anisotropic scattering)
- **EIS:** Not a primary EIS target.
- **Notes:** Formed from Tamm-Horsfall mucoprotein in renal tubules. Large size and cylindrical shape give distinctive MALS angular profile (anisotropic, forward-scattered). Differentiation of cast types (hyaline, granular, cellular) requires detailed scattering + ML. Low abundance in typical samples. Clinically: granular/cellular casts indicate significant renal pathology.

### Bacteria (Total Count)
- **Optical:** `260->` (DNA/RNA absorption) | `660->` (turbidity at >10⁵ CFU/mL)
- **Fluorescence:** `260->340` (nucleic acid fluorescence)
- **EIS:** Label-free impedimetric detection of bacteria well documented. EIS very feasible (impedance changes with bacterial adhesion/growth).
- **Notes:** Bacteria are smaller than eukaryotic cells (~1–5 µm), giving a more isotropic MALS profile. Simple turbidimetry at 600–660 nm effective for high loads. DNA absorbance at 260 nm adds specificity. EIS biosensors for bacteria (E. coli, etc.) demonstrated in literature. Significant bacteriuria: >10⁵ CFU/mL.

### Bacteria Type 2 (bacteria2Type)
- **Optical:** Same as bacteria above; type differentiation via MALS scattering profile shape.
- **EIS:** Antibody-functionalized EIS biosensors can provide species-level differentiation; feasible.
- **Notes:** Likely refers to a second bacterial population or gram-classification. Gram-positive vs. gram-negative bacteria differ in cell wall thickness → different RI → subtly different MALS profiles. Full ML-based classification from MALS is the primary approach. EIS with species-selective antibodies provides the most specific route.

---

## Other Parameters

### Urinary Output (urineOutput)
- **Optical:** Volume measurement — not a spectroscopic parameter.
- **EIS:** Flow cell volume measurement (capacitive/conductive level sensing). Possible.
- **Notes:** Total urine volume (mL/24h or mL/min). Measured by volume collection or inline flow sensor. Critical denominator for all concentration-to-excretion-rate conversions. Pairs with all biomarker concentrations to calculate 24h excretion (e.g., sodium excretion = [Na+] × volume). Not directly detectable by spectroscopy but essential clinical parameter.

### Body Surface (bodySurface)
- **Optical:** Not a directly measured urine biomarker. Calculated parameter.
- **EIS:** Not applicable.
- **Notes:** Likely refers to Body Surface Area (BSA, m²), calculated from patient height and weight (Du Bois formula or Mosteller formula). Used to normalize 24h excretion values for inter-patient comparison (e.g., mg/1.73 m² BSA). Not measurable from urine spectroscopy — requires patient demographics input to the data model.

---

## Quick Reference Table

| Biomarker | Absorbance / Fluorescence | EIS? | Feasibility |
|-----------|--------------------------|------|-------------|
| **Urea** | `1400->` `1800->` `2000->` `2200->` | Indirect | High |
| **Creatinine** | `210->` `235->` `280->` `1600->` `1700->` `1800->` `2100->` `2200->` | Interferent | High |
| **Uric Acid** | `205->` `230->` `260->` `293->` | Yes (enzyme) | High |
| **Glucose** | `210->` `260->` (NIR full spectrum) | Yes (GOx) | Low (optical); High (EIS) |
| **Oxalate** | `200->` `220->` (weak, reagent-free) | Yes (enzyme) | Low (optical) |
| **Ammonia** | `220->` `260->` (reagent-free weak) | Yes | Low (optical) |
| **pH** | `434->` `578->` (indicator) | Yes (electrode) | Reagent-needed |
| **Titratable Acidity** | — | Indirect | Not optical |
| **Osmolality** | Refractometry 589 nm proxy | Yes (conductivity) | Medium (indirect) |
| **Protein (total)** | `220->` `280->` · `280->340` `295->340` | Yes | Medium |
| **Albumin** | `229->` `280->` · `295->340` | Yes (immunosensor) | Medium |
| **Sodium** | `1450->` `1940->` (exploratory) | Yes (ISE) | Exploratory (optical); High (EIS) |
| **Potassium** | `1450->` `1940->` (exploratory) | Yes (ISE) | Exploratory (optical); High (EIS) |
| **Chloride** | — | Yes (ISE) | Not optical |
| **Calcium** | `210->` `230->` (weak, crystal turbidity 660) | Yes (ISE) | Low (optical) |
| **Magnesium** | — | Yes (ISE) | Not optical |
| **Phosphorus / Phosphate** | — (820 nm with molybdate reagent) | Yes (func. electrode) | Not optical (reagent-free) |
| **Red Blood Cells** | `660->` (scattering) · `415->` `541->` (Hb post-lysis) | Yes (impedance) | Medium |
| **White Blood Cells** | `660->` (scattering) · `260->` `280->` (post-lysis) | Yes (impedance) | Medium |
| **Epithelial Cells** | `660->` (scattering) + MALS | No | Medium |
| **Crystals** | `660->` (turbidity) + MALS | No | Medium |
| **Cylinders** | `660->` (scattering) + MALS | No | Medium |
| **Bacteria (total)** | `260->` `660->` | Yes (label-free) | Medium |
| **Bacteria Type 2** | `260->` `660->` + MALS | Yes (antibody EIS) | Medium |
| **Urine Output** | Volume (flow sensor) | Possible (flow) | N/A (not spectroscopy) |
| **Body Surface** | Calculated (BSA formula) | N/A | N/A (external input) |

---

## EIS Summary for This Panel

EIS is most useful for:
- **Electrolytes** (Na+, K+, Cl-, Ca2+, Mg2+) via ISE-EIS — the only feasible reagent-free path for individual ion quantification
- **Glucose** via GOx enzyme electrode — well-established, high accuracy
- **Albumin** via immunosensor — excellent sensitivity for microalbuminuria range
- **Bacteria** via label-free impedimetry — changes in charge transfer resistance upon bacterial adhesion
- **Osmolality** via conductivity (low-frequency EIS) — practical surrogate for total ionic strength
- **pH** via potentiometric electrode integrated alongside EIS cell

EIS is **not applicable** to: crystals, casts, epithelial cells (morphological/particulate parameters best addressed by MALS).

---

## Key Detection Challenges

| Challenge | Impact | Mitigation |
|-----------|--------|------------|
| Complex UV background | All UV analytes (creatinine, albumin, uric acid) | Derivative spectroscopy, PLS regression |
| Water dominance in NIR | Urea, creatinine, ions | High-SNR instrument, robust PLS, temperature control |
| No chromophore on ions | Na, K, Cl, Mg, phosphate | EIS with ISE or conductivity sensor |
| Weak glucose signal | Glucose | GOx-EIS + ML full-spectrum fingerprinting |
| Particle overlap (RBC/WBC/epith.) | Cellular classification | MALS + trained ML classifier (SVM/CNN) |
| Urochrome/bilirubin background | All visible-range analytes | 2nd derivative, PCA outlier removal |
| Temperature drift | All measurements | Peltier-controlled cell, ±0.1°C tolerance |
| Sample dilution variability | All concentrations | Normalize to creatinine (ACR, PCR ratios) |

---

## Sources

| Reference | Notes |
|-----------|-------|
| Al-Awthan et al. *Spectrochim Acta A* 2020;229:117995 | NIR urea/creatinine feasibility |
| Fossati et al. *Clin Chem* 1980;26(2):227–231 | UV uric acid absorbance |
| Peters T. *Adv Clin Chem* 1970;13:37–111 | Protein UV absorption |
| See [[literature]] for full citation list | Jimini-specific literature review |

## Gaps

- Individual ion quantification beyond total conductivity: exploratory only; EIS-ISE is the practical route
- Titratable acidity: no optical path reagent-free; requires titration or pH electrode
- BSA normalization: calculated from patient demographics, not measurable from urine spectroscopy
- Oxalate reagent-free detection: indirect via crystal turbidity only; direct requires reagent
