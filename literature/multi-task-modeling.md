# Multi-Task & Multi-Output Prediction for Spectral Biomarker Analysis

**Research question:** When and how should multiple urine biomarkers be predicted jointly from the same spectral/EIS input? What architectures, loss functions, and task-grouping strategies yield the best results?

**Context:** Jimini pen-sized spectrophotometer. Inputs: LED signals at 275/365/405/455 nm + broadband visible + 1070 nm NIR + EIS. Targets: WBC, BAC, RBC, epiCells, Crystals, Creatinine, Osmolality, TUP, PBG, Sodium, Chloride, Nitrites, Uric acid, Bilirubin, Protein, NADH — a mix of binary classifiers and continuous regressors.

**Date:** 2026-04-09  
**Status:** Comprehensive first pass — 20+ sources synthesized

---

## Table of Contents

1. [Why Multi-Task? The Core Argument](#1-why-multi-task-the-core-argument)
2. [Taxonomy of Approaches](#2-taxonomy-of-approaches)
3. [Classical Chemometrics: PLS2 and Multi-Response Methods](#3-classical-chemometrics-pls2-and-multi-response-methods)
4. [Deep Learning Architectures](#4-deep-learning-architectures)
5. [Loss Functions and Gradient Balancing](#5-loss-functions-and-gradient-balancing)
6. [Science-Informed Task Relations](#6-science-informed-task-relations)
7. [Hierarchical and Cascade Prediction](#7-hierarchical-and-cascade-prediction)
8. [Negative Transfer: When Multi-Task Hurts](#8-negative-transfer-when-multi-task-hurts)
9. [Comparison Matrix: MTL vs Single-Task](#9-comparison-matrix-mtl-vs-single-task)
10. [Decision Guide for Jimini V20 Targets](#10-decision-guide-for-jimini-v20-targets)
11. [Practical Implementation Notes](#11-practical-implementation-notes)
12. [Gaps & Open Questions](#12-gaps--open-questions)
13. [Sources](#13-sources)

---

## 1. Why Multi-Task? The Core Argument

Multi-task learning (MTL) trains a single model to predict multiple targets simultaneously by sharing intermediate representations. The theoretical justification is **inductive transfer**: by learning correlated tasks jointly, the model receives additional gradient signal that regularizes the shared representation and can generalize better than n independent single-task models.

For urine spectroscopy specifically, the argument is compelling:

| Phenomenon | Why it favors MTL |
|---|---|
| **Same physical input** | All biomarkers come from the same spectrum; shared feature extraction is natural |
| **Chemical correlations** | Osmolality correlates with creatinine; hematuria correlates with WBC count; porphyrins correlate with PBG |
| **Scarce labeled data** | n < 500 per target is common in clinical pilots; joint training effectively multiplies useful signal |
| **Shared confounders** | Turbidity, pH, and concentration all affect multiple targets simultaneously — a shared encoder can learn to factor these out once |
| **Mixed task types** | Binary classifiers (WBC, BAC) and regressors (creatinine, osmolality) can share a spectral encoder while having task-specific output heads |

**The key empirical result across all spectroscopy literature:** MTL consistently outperforms single-task models when:
1. Training data is limited (n < 500 per task)
2. Tasks share the same input space  
3. Some tasks provide strong gradient signal that benefits weaker tasks

---

## 2. Taxonomy of Approaches

```
Multi-Task / Multi-Output Spectral Prediction
                    │
    ┌───────────────┼───────────────┐
    │               │               │
Classical      Deep Learning    Hierarchical
Chemometrics   (Neural MTL)     / Cascade
    │               │               │
  PLS2          Hard sharing    Two-stage
  SO-PLS        Soft sharing    Predict easy
  MB-PLS        Cross-stitch    first → use
  PARAFAC       Attention MTL   as features
                Science-MTL     for hard
```

---

## 3. Classical Chemometrics: PLS2 and Multi-Response Methods

### 3.1 PLS2 — The Multi-Response Baseline

**PLS2** (multi-response PLS) is the standard chemometric baseline for predicting multiple analytes from spectra simultaneously. It decomposes both X (spectra) and Y (responses) into shared latent components:

$$\mathbf{X} = \mathbf{T}\mathbf{P}^T + \mathbf{E}_X \qquad \mathbf{Y} = \mathbf{U}\mathbf{Q}^T + \mathbf{E}_Y$$

The decomposition maximizes covariance between X-scores (T) and Y-scores (U). The key property: **all response variables are explained by the same set of latent components**, which forces a shared representation.

**Strengths:**
- Handles high collinearity in spectral data natively
- Interpretable: loading vectors show which wavelengths matter per component
- Fast to train, no GPU required
- Well-understood statistical properties

**Weaknesses:**
- Linear — cannot capture Beer-Lambert nonlinearities or pH-dependent spectral shifts
- Forces shared latent space even for unrelated targets (implicit negative transfer)
- PLS2 often performs worse than individual PLS1 models per-target when tasks are poorly correlated — see Mishra & Passos (2022)

**PLS2 vs individual PLS1 — empirical findings (Mishra & Passos, 2022, NIR pear fruit):**

| Metric | PLS2 (MC) | PLS2 (SSC) | PLS1-MC | PLS1-SSC |
|---|---|---|---|---|
| RMSE | 0.67% | 0.65% | — | — |
| DL multi-output | 0.551% | 0.548% | 0.538% | 0.539% |

PLS2 baseline was beaten by multi-output DL (~13% lower RMSE). Importantly, **individual single-output DL models slightly outperformed multi-output DL** for well-conditioned problems. Multi-task DL wins most when targets are correlated and data is scarce.

### 3.2 SO-PLS — Sequential Orthogonalized PLS

**SO-PLS** (Sequential Orthogonalized PLS) is designed for multi-block data (multiple sensor modalities). It sequentially orthogonalizes each new data block with respect to previous ones, then applies PLS:

$$\text{Block}_2^{\perp} = \text{Block}_2 - \mathbf{P}_1 \mathbf{P}_1^T \text{Block}_2$$

**For Jimini:** Directly applicable to the multi-modal setup (UV LEDs + visible + NIR + EIS as separate blocks). SO-PLS can naturally fuse spectra from C12 (321–870 nm), C14 (570–1078 nm), and EIS signals without re-scaling issues. The PROSAC-SO-PLS variant (KU Leuven, 2025) adds automated preprocessing selection per block.

### 3.3 MB-PLS — Multiblock PLS

**MB-PLS** handles multiple input blocks (same principle as SO-PLS but uses a different deflation scheme). Both SO-PLS and MB-PLS are relevant when EIS and spectral data need to be fused — each block has very different physical units and correlation structure.

---

## 4. Deep Learning Architectures

### 4.1 Hard Parameter Sharing (Shared Encoder + Task Heads) ★

The standard MTL architecture. A single **shared encoder** processes the raw spectrum (or feature vector); **task-specific heads** produce outputs for each target.

```
Input: A(275), A(365), A(405), A(455), A(white@λ), A(1070), EIS features
           │
    ┌──────┴──────┐
    │  Shared      │
    │  Encoder     │  ← 1D-CNN or Transformer layers
    │  (spectral   │    learning domain-general features
    │   features)  │
    └──────┬──────┘
           │
    ┌──────┴─────────────────────────────┐
    │      Task-Specific Heads            │
    ├─ WBC head  → sigmoid → {0,1}        │
    ├─ BAC head  → sigmoid → {0,1}        │
    ├─ RBC head  → sigmoid → {0,1}        │
    ├─ Creatinine head → linear → float   │
    ├─ Osmolality head → linear → float   │
    ├─ TUP head  → sigmoid → {0,1}        │
    └─ ...                                │
```

**Key design choice:** How deep is the shared encoder vs. how much is task-specific? The more correlated the tasks, the more sharing is beneficial.

**Evidence from FTIRNet (Bachinin et al., 2025, Colorado State):**
- Shared Transformer encoder → task-specific Transformer heads for 7 soil properties from FTIR spectra
- Result: R² > 0.98 for all 5 primary targets vs R² 0.86–0.88 for PLSR
- **Science-informed task relation learning** (explicit cross-task connections for correlated properties) gave additional 5–10% improvement for weakly-spectrally-active properties (like nitrogen, which benefits from carbon features)

**Directly applicable to Jimini:** Creatinine and osmolality are correlated (both reflect total dissolved solute load) — the osmolality head can feed into the creatinine head. Similarly, WBC count and bacteria count are correlated clinical outcomes.

### 4.2 Multi-Output 1D-CNN ★

The simplest deep MTL architecture for spectral data: a 1D convolutional neural network with a multi-neuron output layer.

**Architecture (Mishra & Passos, 2022, NIR pear fruit):**
```
Input: NIR spectrum (n wavelengths)
  → Conv1D (filters=1, kernel adapted by Bayesian optimization)
  → Dense layers (ELU activation)
  → Output layer (n_targets neurons, linear activation)
```

**Key result:** Multi-output 1D-CNN achieved ~13% lower RMSE than PLS2 for simultaneous SSC + MC prediction in pear fruit (n=551 with augmentation). Simple 1-layer CNN matched or beat 3-layer CNN — **deep complexity is not always needed for spectral data.**

**Important caveat from Mishra & Passos:** When targets have very different prediction difficulty (different SDR), the **harder target can drag down the easier target** during joint training. Solution: normalize target variables to similar scale before training.

### 4.3 Physics-Informed Multi-Task Learning (PI-MTL) ★★★

The most relevant paper for Jimini. Liu et al. (2024, Spectrochimica Acta Part A) applied PI-MTL to simultaneous UV-Vis prediction of COD and nitrate in water under stochastic turbidity/chromaticity interference — the closest analog to the urine spectroscopy problem.

**Architecture:**
```
Input: UV-Vis absorption spectrum (200–1050 nm, normalized)
  → Physics-Informed Block (task-specific effective wavelength weights w₁, w₂, w₃, w₄)
  → Shared Convolutional Block (32→64→128 filters, kernel=20)
  → Squeeze-Excitation Block (channel-wise recalibration)
  → Fully-Connected Block → [COD, Nitrate]
```

**Physics-informed block:** Incorporates known effective wavelengths (254 nm for COD, 210 nm for nitrate) as trainable weight vectors that pre-weight the input spectrum before shared convolution. Background interference (turbidity, chromaticity) is included as additional "tasks" in the multi-task loss wrapper.

**Results under stochastic background interference (turbidity + chromaticity noise):**

| Model | COD R² | Nitrate R² | COD RMSE improvement vs PLSR |
|---|---|---|---|
| PLSR | 0.67 | 0.20 | baseline |
| RFR | 0.75 | 0.88 | — |
| CNN (single task) | 0.89 | 0.62 | — |
| **PI-MTL** | **0.941** | **0.958** | **-60.9% RMSE** |

**Why it matters for Jimini:** The turbidity/chromaticity interference in water is directly analogous to urine's matrix variability (turbidity from cells, crystals, bacteria; color from bilirubin, urobilinogen). The PI-MTL approach — treating background interference as an auxiliary task — is directly transferable.

**For Jimini, the "background tasks" could be:**
- Turbidity (optical: $A_{1070}$)  
- Dilution / osmolality (optical proxy + EIS conductivity)
- Bilirubin color (known absorber at 453 nm)

These auxiliary regressors stabilize the shared encoder and make the primary biomarker predictions more robust.

### 4.4 Science-Informed Transformer MTL (FTIRNet)

**FTIRNet** (Bachinin et al., 2025) introduces **Exclusive-Learnable-Mask & Adaptation (ELMA)** blocks with learnable per-task, per-neuron attention masks. Key innovations:

1. **Progressive exclusive capacity:** Early in training, each neuron is "owned" by one task. As training progresses, ownership gradually becomes shared. This prevents premature collapse to a generic representation.

2. **Directional task influence gates:** A trainable scalar $\gamma_{I \rightarrow L} \in (0,1)$ controls how much an "influencing" task (e.g., organic carbon) contributes to a "listener" task (e.g., nitrogen). If the influence is unhelpful, backprop drives $\gamma \rightarrow 0$ automatically.

3. **Science-guided task graph:** Task relationships are specified *a priori* based on domain knowledge (C:N ratio in soils → OC influences N), not discovered from data.

**For Jimini, the task influence graph could encode:**

```
Osmolality → Creatinine    (both measure total dissolved solutes)
RBC → WBC                  (co-occurrence in inflammatory/infection contexts)
Hemoglobin → Bilirubin     (hemoglobin degradation produces bilirubin)
PBG → TUP                  (PBG polymerizes to porphyrins)
Bacteria → Nitrites        (Gram-negative bacteria produce nitrites)
Uric acid → Protein        (both UV absorbers at 275 nm — correlated confounders)
```

### 4.5 Multi-Task 1D-CNN for Raman Spectroscopy (Oral Cancer Detection)

**RSC Analytical Methods (2024):** Multi-task deep learning for oral cancer detection from optical fiber Raman spectroscopy. Joint prediction of cancer type + grade + margin status from the same Raman spectrum. The shared encoder learned spectral features relevant to all cancer-related endpoints simultaneously, outperforming individual per-task models.

**Relevance:** Similar problem structure to Jimini — one spectrum, multiple clinical endpoints of varying difficulty and correlation.

---

## 5. Loss Functions and Gradient Balancing

### 5.1 Naive Sum of Losses

The simplest approach:
$$\mathcal{L}_{\text{total}} = \sum_{t=1}^{T} \lambda_t \mathcal{L}_t$$

**Problem:** If losses are on very different scales (e.g., binary cross-entropy for WBC vs MSE for creatinine in mmol/L), one task dominates gradient updates. Manual tuning of $\lambda_t$ is tedious and brittle.

### 5.2 Uncertainty-Weighted Loss (Kendall et al., 2018, CVPR) ★

The most widely adopted principled MTL loss weighting. Each task $t$ has a learnable **log noise variance** $\sigma_t^2$:

$$\mathcal{L}_{\text{total}} = \sum_{t=1}^{T} \frac{1}{2\sigma_t^2} \mathcal{L}_t + \log \sigma_t$$

**Key properties:**
- High uncertainty ($\sigma_t$ large) → task is downweighted automatically
- The $\log \sigma_t$ term prevents all $\sigma_t \rightarrow \infty$ collapse
- Works for regression (Gaussian likelihood) and classification (Laplacian likelihood) simultaneously
- Tasks with noisy labels or weak signal are automatically down-weighted

**For Jimini:** WBC count in urine is inherently noisy (cell lysis between collection and measurement, inter-observer variability in gold standard microscopy). The uncertainty weighting would automatically reduce WBC's weight relative to the more precisely labeled bilirubin target.

**Implementation (PyTorch):**
```python
class UncertaintyLoss(nn.Module):
    def __init__(self, n_tasks):
        super().__init__()
        self.log_vars = nn.Parameter(torch.zeros(n_tasks))
    
    def forward(self, losses):
        total = 0
        for i, loss in enumerate(losses):
            precision = torch.exp(-self.log_vars[i])
            total += precision * loss + self.log_vars[i]
        return total
```

**Caveat (IJCV, 2025):** A follow-up analysis found that uncertainty weighting's success is partly due to implicit learning rate scaling rather than principled Bayesian uncertainty. The authors propose an analytically motivated alternative. Still, uncertainty weighting is a reliable and simple starting point.

### 5.3 PI-MTL Loss Wrapper (Liu et al., 2024) ★

From the water quality UV-Vis paper: a **learnable loss weight vector** $v \in \mathbb{R}^T$:

$$\mathcal{L} = \frac{1}{T} \sum_{t=1}^{T} e^{-v_t} \cdot |\hat{y}_t - y_t| - v_t$$

The exponential term scales each task's contribution; $v_t$ is learned via backpropagation. If task $t$ has consistently large residuals, its $v_t$ is adjusted to re-weight accordingly. This dynamically adapts to stochastic interference — exactly the scenario in urine analysis.

### 5.4 Gradient Surgery — PCGrad

**Yu et al. (2020, NeurIPS):** When two tasks have conflicting gradients (cosine similarity < 0), project one gradient onto the normal plane of the other to eliminate the conflict:

$$g_t \leftarrow g_t - \frac{g_t \cdot g_{t'}}{|g_{t'}|^2} g_{t'} \quad \text{if } g_t \cdot g_{t'} < 0$$

**For Jimini:** Turbidity scatter (high $A_{1070}$) helps bacteria detection but *hurts* bilirubin quantification (turbidity baseline confounds 453 nm absorbance). PCGrad would automatically resolve this conflicting gradient — letting each task benefit from shared features without being harmed by the other.

### 5.5 EMA Loss Weighting (Lakkapragada et al., 2022, AAAI) ★

**Exponential Moving Average** loss weighting uses recent loss history to prevent any single task from dominating:

$$\lambda_t^{(\tau)} = \frac{\text{EMA}(\mathcal{L}_t^{(\tau)})}{\sum_{t'} \text{EMA}(\mathcal{L}_{t'}^{(\tau)})}$$

Tasks that are still improving get proportionally higher weight; converged tasks step back. Simpler than PCGrad, very easy to implement, mitigates negative transfer caused by task dominance.

---

## 6. Science-Informed Task Relations

The most important conceptual advance for Jimini. Instead of letting the network discover task relationships purely from data (which requires more training samples), you encode known biochemical/physical relationships directly into the architecture.

### 6.1 Formal Framework (FTIRNet approach)

Define task types:
- **Influencing task**: predicts a property with a strong spectral signature (high R² if modeled alone)
- **Listener task**: predicts a property with weak/ambiguous spectral signature (low R² alone) — benefits from influencing task features
- **Auxiliary task**: predicts a "nuisance" variable (turbidity, osmolality) to stabilize shared encoder; prediction itself may not be the goal

**For Jimini:**

| Influencing task | Listener task | Physical/biochemical reason |
|---|---|---|
| **Bilirubin** (strong at 453 nm) | **WBC** (weak, no chromophore) | Both elevated in hepatic/cholestatic conditions with inflammatory response |
| **RBC / Hemoglobin** (strong at 405 nm) | **WBC** (weak) | Hematuria + pyuria co-occur in UTI, nephritis |
| **Osmolality** (proxy via EIS + NIR) | **Creatinine** | Creatinine is a major osmolyte; corr ≈ 0.7 |
| **Uric acid** (strong at 275 nm) | **TUP** (weak overlap) | Both UV absorbers; uric acid subtraction improves TUP residual |
| **PBG** (via porphyrin fluorescence) | **TUP** | PBG → porphyrins; the two are sequential in the same pathway |
| **Bilirubin** | **Porphyrins** (TUP) | Both degradation products of heme; correlated in hepatic disease |
| **Bacteria** | **Nitrites** | Gram-negative bacteria → nitrite production |
| **Turbidity/scatter** ($A_{1070}$) | All cell targets (WBC, BAC, RBC, epiCells, Crystals) | Scatter is a shared confound for all particulate-containing samples |

### 6.2 Implementation Strategy

Use the FTIRNet-style directional influence gate:
```python
# In the listener task head:
def forward(self, shared_features, influencing_features):
    gamma = torch.sigmoid(self.gate)  # learnable, initialized at 0.5
    fused = self.fusion(
        torch.cat([shared_features, gamma * influencing_features], dim=-1)
    )
    return self.head(fused)
```

The gate $\gamma$ learns whether the influencing task's features actually help. If they don't, $\gamma \rightarrow 0$ and the listener head falls back to the shared encoder only.

---

## 7. Hierarchical and Cascade Prediction

### 7.1 Two-Stage Prediction

Some Jimini targets are much easier to predict reliably (high spectral signal-to-noise) than others. Predict the easy ones first, then use them as features for the hard ones:

**Stage 1 — Physically grounded, high-confidence targets:**
- Bilirubin (453 nm Beer-Lambert, very direct)
- Hemoglobin / RBC (405 nm Soret, strong signal)
- Porphyrins/TUP (405 nm fluorescence, specific)
- Uric acid (275 nm Beer-Lambert)
- Osmolality (EIS conductivity proxy)

**Stage 2 — Indirect/weak-signal targets, using Stage 1 as input features:**
- WBC — use {Hb, osmolality, turbidity, NADH fluorescence} as inputs
- Bacteria — use {turbidity, scatter slope, flavin fluorescence} + Stage 1 residuals
- Creatinine — use {osmolality, uric acid, EIS} as predictors
- Nitrites — use {bacteria prediction, scatter} as proxies
- epiCells — use {turbidity, scatter slope, Stage 1 residuals}

**Advantage:** Stage 2 models are more interpretable — their inputs have physical meaning. If the model uses high hemoglobin + high osmolality to predict elevated WBC, that's a physically plausible inference (inflammatory state with hematuria).

### 7.2 Regression → Classification Cascade

For binary targets (WBC ≥+, BAC positive): first build a continuous score model, then threshold. The continuous prediction at Stage 1 can be used as a soft feature for Stage 2 classifiers. This provides uncertainty estimates (prediction near the threshold = high uncertainty).

### 7.3 Evidence from Spectroscopy Literature

**Predicting anemia from NIR spectroscopy of spent dialysis fluid (Nature Sci. Rep., 2021):**
- Predicted 9 blood parameters simultaneously (RBC, Hb, Fe, TIBC, FER, Hct, MCV, MCHC, MCH)
- R values 0.91–0.96 for all 9 parameters
- Key observation: parameters that are biologically correlated (RBC, Hct, MCV — all related to red cell morphology) share spectral features and improve each other's predictions

---

## 8. Negative Transfer: When Multi-Task Hurts

Negative transfer occurs when jointly training two tasks degrades performance compared to training them independently. It is the primary risk of MTL.

### 8.1 When Negative Transfer Occurs

| Condition | Risk level | Mechanism |
|---|---|---|
| Tasks have uncorrelated labels | High | Conflicting gradient directions in shared layers |
| Tasks have very different input sensitivity | High | One task uses 275 nm features; another needs 1070 nm features |
| Tasks have very different output scales/types | Medium | Regression + classification in same loss without normalization |
| One task has much larger/smaller loss magnitude | Medium | Dominant task monopolizes gradient signal |
| Tasks require conflicting feature transformations | High | Turbidity helps scatter-based detection but hurts absorption-based quantification |

### 8.2 Detection and Mitigation

**Detect:** Monitor per-task validation loss during MTL training. Compare to single-task baselines. If any task is **worse** in MTL than single-task, negative transfer has occurred.

**Mitigation strategies (ranked by implementation effort):**

1. **Task grouping** — don't put completely unrelated tasks in the same MTL model. Group by input domain (optical targets together, EIS targets together) and by output type (classifiers together, regressors together)

2. **EMA loss weighting** — dynamically down-weight tasks that are improving poorly (prevents one dominant task from monopolizing)

3. **Gradient surgery (PCGrad)** — explicitly resolve conflicting gradients

4. **Soft parameter sharing** — tasks have separate networks but are regularized to be similar (L2 penalty on parameter differences). More flexible than hard sharing.

5. **Task-specific batch normalization** — separate BN statistics per task; prevents interference in normalization layers which are a common source of negative transfer

6. **Asymmetric MTL** — allow transfer from Task A → Task B but not necessarily B → A (directional gates as in FTIRNet)

### 8.3 Jimini-Specific Risk Assessment

| Task pair | Transfer risk | Reason |
|---|---|---|
| WBC ↔ BAC | **Low** — positive transfer likely | Both correlated with infection state and turbidity |
| Bilirubin ↔ RBC | **Low** — positive transfer likely | Both visible absorbers; Hb degradation produces bilirubin |
| Uric acid ↔ Creatinine | **Medium** — weak positive | Both UV-active solutes; creatinine barely visible at 275 nm |
| TUP ↔ Bilirubin | **Medium** | Both at 405 nm but different mechanisms; risk of spectral overlap confusion |
| Uric acid ↔ Scatter targets (WBC, BAC) | **High risk** | UV absorption (analyte signal) vs scatter (cell detection signal) are mechanistically unrelated at 275 nm |
| Nitrites ↔ Optical targets | **High risk** | Nitrites are spectrally invisible; forcing joint training with optical features adds no signal |

**Recommendation:** Do NOT include Nitrites, Sodium, Chloride in the optical-domain MTL model. These are EIS targets and should be modeled separately with EIS-specific inputs.

---

## 9. Comparison Matrix: MTL vs Single-Task

| Scenario | Best approach | Evidence |
|---|---|---|
| n > 500 per task, tasks weakly correlated | Single-task models | Mishra & Passos 2022: single DL beats multi-output DL |
| n < 300 per task, tasks correlated | **MTL with uncertainty weighting** | FTIRNet, PI-MTL both show clear gains |
| Strong spectral interference (turbidity, color) | **PI-MTL with auxiliary interference tasks** | Liu et al. 2024: 60% RMSE reduction vs PLSR |
| Some tasks have weak spectral signal | **MTL with science-informed task connections** | FTIRNet: weak S/K prediction improved significantly by including correlated C/N tasks |
| Mixed binary + continuous targets | **Hard sharing + task-specific heads** | Standard approach; uncertainty weighting handles scale mismatch |
| Need interpretability | PLS2 or SO-PLS | Loadings directly interpretable as spectral features |
| Rapid prototyping, few samples | **PLS2 baseline → MTL DL if insufficient** | PLS2 as baseline, DL for production |

---

## 10. Decision Guide for Jimini V20 Targets

### 10.1 Recommended Task Groups

Group targets that should be jointly trained together based on shared physics and positive-transfer likelihood:

**Group 1 — Optical Absorbers + Fluorophores (spectral domain)**
```
Targets: Bilirubin, RBC/Hemoglobin, TUP, PBG, Uric acid, Protein, NADH
Input:   A(275), A(365), A(405), A(455), white-LED spectrum (C12/C14)
Model:   Shared 1D-CNN encoder → task-specific heads
Notes:   Influencing chain: Hb → TUP → PBG (biochemical cascade)
```

**Group 2 — Particulate/Scatter Targets (scatter domain)**
```
Targets: WBC, BAC, RBC (cell count), epiCells, Crystals
Input:   A(1070), scatter slope (A400/A800), NADH fluorescence, autofluorescence
         + optical Group 1 predictions as auxiliary features
Model:   Shared scatter-feature encoder → task-specific binary heads
Notes:   Use Group 1 Hb prediction as influencing feature for RBC binary head
```

**Group 3 — Solute/Electrolyte Targets (EIS + NIR domain)**
```
Targets: Osmolality, Creatinine, Sodium, Chloride
Input:   EIS (multi-frequency: 100Hz–100kHz), A(1070), spectral integral
Model:   EIS-specific encoder → continuous regression heads
Notes:   Osmolality as influencing task for Creatinine
```

**NOT in any MTL group:**
- Nitrites → model as downstream of BAC binary prediction
- CKD markers (glucose, urea) → require wavelengths outside Jimini range

### 10.2 Architecture Blueprint

```python
# Pseudo-code for Jimini Group 1 MTL model

class JiminiOpticalMTL(nn.Module):
    def __init__(self):
        # Shared encoder: processes all optical features
        self.encoder = nn.Sequential(
            nn.Conv1d(1, 32, kernel_size=11, padding=5),
            nn.BatchNorm1d(32), nn.ELU(),
            nn.Conv1d(32, 64, kernel_size=7, padding=3),
            nn.BatchNorm1d(64), nn.ELU(),
            nn.AdaptiveAvgPool1d(32),
            nn.Flatten()
        )
        
        # Physics-informed pre-weighting
        # Weight the input spectrum by known effective wavelengths
        self.pi_weights = {
            'bilirubin': nn.Parameter(init_from_spectrum(453)),   # ε peak
            'hemoglobin': nn.Parameter(init_from_spectrum(415)),  # Soret peak
            'uric_acid': nn.Parameter(init_from_spectrum(293)),   # ε peak
        }
        
        # Influence gate: Hb → TUP
        self.hb_to_tup_gate = nn.Parameter(torch.tensor(0.0))  # sigmoid → 0.5 init
        
        # Task-specific heads
        self.heads = nn.ModuleDict({
            'bilirubin': nn.Linear(64*32, 1),      # regression
            'hemoglobin': nn.Linear(64*32, 1),     # regression
            'tup': nn.Linear(64*32 + 64*32, 1),   # + Hb features via gate
            'pbg': nn.Linear(64*32, 1),            # binary
            'uric_acid': nn.Linear(64*32, 1),      # regression
        })
        
        # Uncertainty weights (Kendall 2018)
        self.log_vars = nn.Parameter(torch.zeros(len(self.heads)))
    
    def forward(self, spectrum):
        features = self.encoder(spectrum)
        
        # Compute all primary task predictions
        hb_features = features  # (would use PI-weighted variant)
        hb_pred = self.heads['hemoglobin'](features)
        
        # Science-informed: Hb features → TUP via learned gate
        gate = torch.sigmoid(self.hb_to_tup_gate)
        tup_features = torch.cat([features, gate * hb_features], dim=-1)
        
        return {
            'bilirubin': self.heads['bilirubin'](features),
            'hemoglobin': hb_pred,
            'tup': self.heads['tup'](tup_features),
            'pbg': torch.sigmoid(self.heads['pbg'](features)),
            'uric_acid': self.heads['uric_acid'](features),
        }
```

### 10.3 Data Requirements

| Target | Minimum n for MTL | Minimum n for single-task |
|---|---|---|
| WBC, BAC, RBC (binary) | ~200/class | ~300/class |
| Bilirubin (regression) | ~150 | ~200 |
| TUP, PBG (binary, rare condition) | ~100/class (but rare!) | ~200/class |
| Creatinine (regression) | ~200 | ~300 |
| Osmolality (regression) | ~150 | ~200 |

For rare-positive targets (TUP, PBG) in the ~5–15% prevalence range, **data augmentation** (spectral noise addition, concentration jitter via Beer-Lambert simulation) is essential before MTL.

---

## 11. Practical Implementation Notes

### 11.1 Target Normalization

Before joint training of regressors:
- Standardize continuous targets to zero mean, unit variance
- Or use min-max normalization to [0,1] range
- This prevents high-magnitude targets (osmolality: 50–1200 mOsm/kg) from dominating the loss over low-magnitude targets (creatinine: 0.5–25 mmol/L)

### 11.2 Binary + Regression Mix

For mixed classification/regression MTL (e.g., WBC binary + osmolality regression):
- Use **binary cross-entropy** for classifiers + **MSE or Huber** for regressors
- Apply uncertainty weighting to handle the different loss scales
- Consider a **Huber loss** (smooth L1) for regressors to reduce sensitivity to concentration outliers

### 11.3 Class Imbalance

WBC, BAC, TUP are binary with positive-class prevalence ~10–40%. Use:
- Weighted binary cross-entropy: `pos_weight = n_negative / n_positive`
- Focal loss: down-weights easy negatives, focuses on hard positives
- Never use plain BCE with imbalanced classes in a MTL setting — the imbalanced task will get over-optimized

### 11.4 Starting Point: PLS2 Baseline

Before building any DL MTL model, always first run:
```python
from sklearn.cross_decomposition import PLSRegression

# Stack all regression targets
Y = np.column_stack([bilirubin, hemoglobin, uric_acid, creatinine, osmolality])
pls2 = PLSRegression(n_components=10)
pls2.fit(X_train_spectra, Y_train)
Y_pred = pls2.predict(X_test_spectra)
```

PLS2 provides:
1. A fast, interpretable baseline to beat
2. Loading vectors that identify physically meaningful wavelength combinations
3. Score plots that reveal task correlations (which targets cluster together in spectral space = positive transfer candidates)

### 11.5 Evaluation Protocol for MTL

Always compare MTL against single-task baselines:
```
For each target t:
  STL(t) = train single-task model on target t
  MTL(t) = train joint MTL model, extract per-task performance for t
  
  Transfer gain: Δ(t) = STL_RMSE(t) - MTL_RMSE(t)
  
  Positive transfer if Δ(t) > 0
  Negative transfer if Δ(t) < 0
```

Report per-task Δ alongside aggregate metrics. Publishing only average MTL performance can hide negative transfer on individual tasks.

---

## 12. Gaps & Open Questions

1. **No published study predicts the Jimini V20 target set jointly.** The closest analogs are the water UV-Vis work (Liu et al., 2024 — 2 targets) and the NIR dialysate work (Nature, 2021 — 9 blood parameters). The combination of binary classifiers + continuous regressors + mixed optical/EIS inputs for 10+ urine biomarkers simultaneously has not been published.

2. **Optimal task grouping is empirical.** The transfer gain matrix (which tasks help/hurt each other) can only be measured on Jimini data. Theory gives guidance but actual grouping requires ablation studies.

3. **Effect of sample size on MTL advantage.** The literature shows consistent MTL advantage at n < 500 and neutral/negative at n > 1000. Jimini's clinical dataset size per target will determine whether MTL or ensemble of single-task models is better.

4. **EIS + optical fusion.** No published paper jointly trains on UV-Vis spectra + multi-frequency EIS for multi-biomarker prediction. The MB-PLS / SO-PLS framework is the natural chemometric approach; for DL, a dual-encoder architecture (one for spectra, one for EIS impedance features) with a shared fusion layer is the natural design.

5. **Temporal dynamics.** If sequential measurements of the same urine sample are possible (e.g., watching PBG darken over time), time-series MTL models could extract richer information than single-shot predictions.

---

## 13. Sources

### Key Papers

| Paper | Year | Key contribution |
|---|---|---|
| Liu et al., "Physics-informed multi-task learning for COD and nitrate in UV-Vis water spectroscopy" | 2024 | PI-MTL: 60% RMSE reduction vs PLSR under turbidity interference; directly analogous to urine matrix |
| Bachinin et al., "FTIRNet: Science-Informed Multitask Transformer for Soil FTIR" | 2025 | Shared Transformer encoder + directional task gates; science-informed relations; R² > 0.98 for 7 properties |
| Mishra & Passos, "Multi-output 1D-CNNs for NIR fruit trait prediction" | 2022 | Multi-output DL beats PLS2 by 13%; single-task slightly beats multi-output when tasks less correlated |
| Kendall, Gal & Cipolla, "Multi-Task Learning Using Uncertainty to Weigh Losses" | 2018 CVPR | Homoscedastic uncertainty weighting — the standard MTL loss approach |
| Lakkapragada et al., "Mitigating Negative Transfer with EMA Loss Weighting" | 2022 AAAI | EMA-based dynamic loss weighting to prevent negative transfer |
| "Predicting anemia from NIR dialysate spectroscopy" | 2021 Nat. Sci. Rep. | 9 blood parameters simultaneously from NIR; R ≈ 0.91–0.96 |
| Mishra et al. (Agronomy), "UV-NIR for Hydroponic Macronutrients: Single vs. Multi-Task" | 2024 | Direct single-task vs multi-task comparison on UV-NIR spectroscopy |
| Ng et al. (2019, Geoderma), "1D-CNNs for simultaneous soil properties" | 2019 | Multi-output CNN for soil VIS/NIR/MIR; foundational spectral multi-task reference |
| "Joint multi-task learning improves biomarker prediction in computational pathology" | 2024 MICCAI | MTL for histopathology biomarkers; positive transfer from easy to hard targets |
| Asymmetric Multi-task Learning (AMTL) | 2016 ICML | Sparse directional regularization graph for task relatedness |
| Yu et al. (2020), PCGrad: gradient surgery for conflicting gradients | 2020 NeurIPS | Eliminates conflicting gradient updates between tasks |

### Web & Review Sources

| Source | URL |
|---|---|
| Liu et al. PI-MTL (Spectrochimica Acta A) | [doi.org/10.1016/j.saa.2024.124857](https://doi.org/10.1016/j.saa.2024.124857) |
| FTIRNet paper (Colorado State) | [cs.colostate.edu/~shrideep/papers/2025/FTIR_eScience25.pdf](https://www.cs.colostate.edu/~shrideep/papers/2025/FTIR_eScience25.pdf) |
| Mishra & Passos multi-output NIR | [doi.org/10.1016/j.postharvbio.2021.111741](https://doi.org/10.1016/j.postharvbio.2021.111741) |
| Kendall et al. uncertainty weighting (CVPR 2018) | [openaccess.thecvf.com](https://openaccess.thecvf.com/content_cvpr_2018/html/Kendall_Multi-Task_Learning_Using_CVPR_2018_paper.html) |
| Uncertainty weighting analysis (IJCV 2025) | [link.springer.com](https://link.springer.com/article/10.1007/s11263-025-02625-x) |
| Mitigating negative transfer (AAAI 2022) | [arxiv.org/abs/2211.12999](https://arxiv.org/abs/2211.12999) |
| Anemia from NIR dialysate (Nature 2021) | [nature.com/articles/s41598-021-88821-4](https://www.nature.com/articles/s41598-021-88821-4) |
| UV-NIR hydroponic multi-task (MDPI 2024) | [mdpi.com/2073-4395/14/9/1974](https://www.mdpi.com/2073-4395/14/9/1974) |
| Multi-task grain NIR (J Near Infrared Spectrosc, 2020) | [opg.optica.org/jnirs-28-5-275](https://opg.optica.org/abstract.cfm?uri=jnirs-28-5-275) |
| MGMT framework for complex mixtures (Analytica Chimica Acta, 2026) | [sciencedirect.com](https://www.sciencedirect.com/science/article/abs/pii/S0003267025014448) |
| Asymmetric MTL (ICML 2016) | [proceedings.mlr.press/v48/leeb16.html](https://proceedings.mlr.press/v48/leeb16.html) |
| Joint MTL for biomarkers in pathology (MICCAI 2024) | [arxiv.org/abs/2403.03891](https://arxiv.org/abs/2403.03891) |
| Raman oral cancer multi-task (RSC Analytical Methods, 2024) | [pubs.rsc.org/en/content/articlelanding/2024/ay/d3ay02250a](https://pubs.rsc.org/en/content/articlelanding/2024/ay/d3ay02250a) |
| Negative transfer analysis (AAAI chemistry case study) | [ojs.aaai.org/AAAI/article/5125](https://ojs.aaai.org/index.php/AAAI/article/download/5125/4998) |
