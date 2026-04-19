---
title: Multi-Task & Multi-Output Prediction for Spectroscopic Biomarker Analysis
aliases:
  - multi-task learning
  - MTL
  - multi-output prediction
tags:
  - topic/ml
  - topic/spectroscopy
  - topic/chemometrics
  - type/concept
  - status/complete
  - device/jimini
date: 2026-04-19
status: complete
type: concept
author: Usense Healthcare
---

# Multi-Task & Multi-Output Prediction for Spectroscopic Biomarker Analysis

When and how multiple urine biomarkers should be predicted jointly from the same spectral/EIS input. Covers architectures (hard/soft sharing, cross-stitch, modality-specific encoders, PI-MTL), loss functions (Kendall uncertainty weighting, GradNorm, PCGrad, CAGrad), and task-grouping strategies for Jimini's 16-target panel. See [[datascience/spectroscopy-biomarkers]] for per-analyte spectral properties, [[signal-processing]] for the preprocessing pipeline, and [[physics-grounded-ml]] for physics-informed constraints applicable to MTL architectures.

**Inputs:** LED signals at 275/365/405/455 nm + broadband visible (C12: 340–850 nm) + 1070 nm NIR (C14: 640–1050 nm) + multi-frequency EIS (10 Hz – 100 kHz). **Targets:** WBC, BAC, RBC, epiCells, Crystals, Creatinine, Osmolality, TUP, PBG, Sodium, Chloride, Nitrites, Uric acid, Bilirubin, Protein, NADH — a mix of binary classifiers and continuous regressors.

---

## 1. The Core Question: Joint vs Independent?

The fundamental decision in multi-output modeling: train one shared model for all targets, or train independent models per target?

### When joint training wins

1. **Correlated targets sharing spectral features:** If bilirubin and RBC both depend on signal at 405 nm, sharing a spectral encoder avoids learning the same feature extraction twice and can improve both if data is limited.
2. **Small dataset, many features:** With n < 500 samples and 300+ spectral channels, single-task models overfit. MTL acts as regularization by forcing the encoder to represent features useful for N tasks simultaneously — reducing the effective overfitting risk by ~N times (Caruana, 1998).
3. **Auxiliary tasks as regularizers:** Even if WBC prediction is the primary goal, training jointly with strongly-predictable analytes (bilirubin, osmolality) helps the shared encoder learn physically meaningful spectral representations rather than noise.
4. **Data augmentation effect:** Different tasks have different noise patterns. Jointly training tasks averages these noise patterns, producing a more robust shared representation.

### When independent models win

1. **Tasks with conflicting spectral features:** If bilirubin and uric acid both use the 275–455 nm region but in conflicting ways, forcing a shared representation degrades both — this is **negative transfer** (Section 11).
2. **Wildly different measurement modalities:** Chemical analytes (optical) vs ionic species (EIS-only) should likely use separate encoders with feature fusion, not fully shared representations.
3. **Large imbalanced label distributions:** If one task is extremely rare (e.g., porphyria), the shared encoder will be dominated by the common tasks and ignore the rare task's relevant features.
4. **Tasks at very different difficulty levels:** If bilirubin prediction reaches R² = 0.97 while creatinine remains at R² = 0.35, joint training may stall at a loss compromise that hurts the easy task without helping the hard one.

### Decision heuristic for Jimini

```text
For each pair of tasks (A, B):
  IF corr(y_A, y_B) > 0.4  →  likely beneficial to share
  IF same λ region drives both  →  share encoder, separate heads
  IF task A uses optical only AND task B uses EIS only  →  separate encoders, shared head only
  IF one task has >3x more data  →  be cautious about fully shared model
```

### Key empirical result (across all spectroscopy literature)

MTL consistently outperforms single-task models when:
1. Training data is limited (n < 500 per task)
2. Tasks share the same input space
3. Some tasks provide strong gradient signal that benefits weaker tasks

---

## 2. Why Multi-Task Learning Works

Multi-task learning (MTL) trains a single model to predict multiple targets simultaneously by sharing intermediate representations. The theoretical justification is **inductive transfer**: by learning correlated tasks jointly, the model receives additional gradient signal that regularizes the shared representation and can generalize better than N independent single-task models.

### The core argument for urine spectroscopy

| Phenomenon | Why it favors MTL |
|---|---|
| **Same physical input** | All biomarkers come from the same spectrum; shared feature extraction is natural |
| **Chemical correlations** | Osmolality correlates with creatinine; hematuria correlates with WBC count; porphyrins correlate with PBG |
| **Scarce labeled data** | n < 500 per target is common in clinical pilots; joint training effectively multiplies useful signal |
| **Shared confounders** | Turbidity, pH, and concentration all affect multiple targets simultaneously — a shared encoder can learn to factor these out once |
| **Mixed task types** | Binary classifiers (WBC, BAC) and regressors (creatinine, osmolality) can share a spectral encoder while having task-specific output heads |

### Mechanisms (Ruder 2017, Caruana 1998)

**Implicit data augmentation.** Different tasks have different label noise patterns. Joint training averages noise, producing a more general encoder. For Jimini: bilirubin ground-truth (spectrophotometric assay) has different measurement noise than WBC (manual microscopy). Training jointly helps the spectral encoder learn the signal, not the noise of any single reference method.

**Attention focusing.** In high-dimensional spectral data (300+ channels), MTL helps distinguish relevant from irrelevant wavelengths. If 12 tasks all use signal at 405 nm, the model learns that 405 nm is important. If only one task spuriously correlates with a noisy region, the other tasks suppress that spurious feature.

**Eavesdropping.** Some features are easy to learn for task B but hard for task A. If the osmolality model easily captures the NIR water band at 970 nm, this representation becomes available to the creatinine model, which depends on total dissolved solids in a correlated way.

**Representation bias.** MTL biases the encoder toward representations that generalize across tasks — exactly what you want for a device that must be robust to new patients, different urine matrices, and device drift.

**Regularization effect.** Overfitting the shared parameters is ~N× harder than overfitting task-specific parameters. With N=12 tasks and n=500 samples, this is significant.

---

## 3. Taxonomy of Approaches

```text
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
  MT-LASSO      MoE             for hard
  MO-RF         Science-MTL
                PI-MTL (physics)
```

---

## 4. Architecture Patterns for Spectral Data

### Hard Parameter Sharing (default starting point)

The standard MTL architecture. A single **shared encoder** processes the raw spectrum (or feature vector); **task-specific heads** produce outputs for each target.

```text
Input: A(275), A(365), A(405), A(455), A(white@λ), A(1070), EIS features
           │
    ┌──────┴──────┐
    │  Shared      │
    │  Encoder     │  ← 1D-CNN or Transformer layers
    │  (spectral   │    learning domain-general features
    │   features)  │
    └──────┬──────┘
           │  shared representation z ∈ ℝᵈ
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

**Pros:** Simplest; easiest to train; strong regularization; N× harder to overfit shared layers.
**Cons:** All tasks must agree on the shared representation; negative transfer possible if tasks conflict.
**When to use:** Default first attempt; especially effective when n < 500.

**Key design parameters:**
- Depth and width of shared encoder
- How many layers to share vs keep task-specific
- Dropout rate in shared layers (apply to all tasks simultaneously)
- The more correlated the tasks, the more sharing is beneficial

**Evidence from FTIRNet (Bachinin et al., 2025, Colorado State):** Shared Transformer encoder → task-specific Transformer heads for 7 soil properties from FTIR spectra. R² > 0.98 for all 5 primary targets vs R² 0.86–0.88 for PLSR. **Science-informed task relation learning** (explicit cross-task connections for correlated properties) gave additional 5–10% improvement for weakly-spectrally-active properties (like nitrogen, which benefits from carbon features).

### Multi-Output 1D-CNN (Mishra & Passos, 2022)

The simplest deep MTL architecture for spectral data: a 1D convolutional neural network with a multi-neuron output layer.

```text
Input: NIR spectrum (n wavelengths)
  → Conv1D (filters=1, kernel adapted by Bayesian optimization)
  → Dense layers (ELU activation)
  → Output layer (n_targets neurons, linear activation)
```

**Key result:** Multi-output 1D-CNN achieved ~13% lower RMSE than PLS2 for simultaneous SSC + MC prediction in pear fruit (n=551 with augmentation). Simple 1-layer CNN matched or beat 3-layer CNN — **deep complexity is not always needed for spectral data.**

**Caveat:** When targets have very different prediction difficulty (different SDR), the **harder target can drag down the easier target** during joint training. Solution: normalize target variables to similar scale before training.

### Soft Parameter Sharing

Each task has its own encoder with independent parameters, but the parameter distances are regularized to encourage similarity:

$$\mathcal{L}_{\text{total}} = \sum_t \mathcal{L}_t + \lambda \sum_{t \neq t'} \| \theta_t - \theta_{t'} \|_2^2$$

**Pros:** More flexible than hard sharing; each task can specialize while remaining similar to others.
**Cons:** N× more parameters; harder to train; less regularization benefit.
**When to use:** Tasks are related but each needs somewhat different feature emphasis (e.g., UV absorbers vs scatter-based markers).

### Cross-Stitch Networks (Misra et al., 2016)

Learns linear combinations of task-specific representations at each layer:

```text
Task A encoder: h_A^{l+1} = f(α_AA · h_A^l + α_AB · h_B^l)
Task B encoder: h_B^{l+1} = f(α_BA · h_A^l + α_BB · h_B^l)
```

The cross-stitch coefficients {α} are learned — when α_AB is large, task A borrows from task B; when α_AB → 0, tasks decouple.

**Pros:** Automatically learns how much to share; gracefully handles partial task relationships.
**Cons:** More parameters; harder to train; needs careful initialization.
**Spectroscopy use case:** Let the bilirubin task borrow from the hemoglobin task (both use 405–455 nm region) while the creatinine/EIS task gradually decouples.

### Modality-Specific Encoders (best for Jimini's mixed inputs)

```text
Optical spectra [C12] → SpectralEncoder_C12 → z_vis
Optical spectra [C14] → SpectralEncoder_C14 → z_nir
EIS features          → EIS_Encoder          → z_eis

[z_vis, z_nir, z_eis] → Fusion Layer → z_fused

z_fused → Task heads (one per analyte)
```

**Pros:** Respects physical modality structure; avoids mixing optical and EIS information prematurely.
**Cons:** Three separate encoders to train.
**When to use:** Different modalities have fundamentally different information content and noise characteristics (which is true for Jimini: optical vs impedance).

### Mixture-of-Experts (MoE)

Multiple "expert" sub-networks, each specializing in a subset of tasks. A gating network decides which experts to activate per input and per task.

```text
Input → [Expert_1, Expert_2, ..., Expert_K]
       ↑
   Gating: softmax(W · input) → [w_1, ..., w_K]

Output_t = Σ w_k^t · Expert_k(input)
```

**Pros:** Naturally separates task clusters; can handle tasks with very different feature needs.
**Cons:** Complex to train; gating collapse risk (all gates route to same expert).
**When to use:** If tasks clearly cluster into groups (e.g., optical-only tasks vs EIS-dependent tasks).

### Physics-Informed Multi-Task Learning (PI-MTL)

The most relevant paper for Jimini. **Liu et al. (2024, Spectrochimica Acta Part A)** applied PI-MTL to simultaneous UV-Vis prediction of COD and nitrate in water under stochastic turbidity/chromaticity interference — the closest analog to the urine spectroscopy problem.

**Architecture:**
```text
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

> [!IMPORTANT]
> The turbidity/chromaticity interference in water is directly analogous to urine's matrix variability (turbidity from cells, crystals, bacteria; color from bilirubin, urobilinogen). PI-MTL — treating background interference as an auxiliary task — is directly transferable to Jimini. See [[matrix-correction]] for the urine-specific interference model.

**For Jimini, the "background tasks" could be:**
- Turbidity (optical: $A_{1070}$)
- Dilution / osmolality (optical proxy + EIS conductivity)
- Bilirubin color (known absorber at 453 nm)

These auxiliary regressors stabilize the shared encoder and make the primary biomarker predictions more robust.

### Science-Informed Transformer MTL (FTIRNet)

**FTIRNet** (Bachinin et al., 2025) introduces **Exclusive-Learnable-Mask & Adaptation (ELMA)** blocks with learnable per-task, per-neuron attention masks. Key innovations:

1. **Progressive exclusive capacity.** Early in training, each neuron is "owned" by one task. As training progresses, ownership gradually becomes shared. This prevents premature collapse to a generic representation.
2. **Directional task influence gates.** A trainable scalar $\gamma_{I \rightarrow L} \in (0,1)$ controls how much an "influencing" task (e.g., organic carbon) contributes to a "listener" task (e.g., nitrogen). If the influence is unhelpful, backprop drives $\gamma \rightarrow 0$ automatically.
3. **Science-guided task graph.** Task relationships are specified *a priori* based on domain knowledge (C:N ratio in soils → OC influences N), not discovered from data.

### Multi-Task 1D-CNN for Raman Spectroscopy (Oral Cancer Detection)

**RSC Analytical Methods (2024):** Multi-task deep learning for oral cancer detection from optical fiber Raman spectroscopy. Joint prediction of cancer type + grade + margin status from the same Raman spectrum. The shared encoder learned spectral features relevant to all cancer-related endpoints simultaneously, outperforming individual per-task models.

**Relevance:** Similar problem structure to Jimini — one spectrum, multiple clinical endpoints of varying difficulty and correlation.

---

## 5. Classical Chemometrics: Multi-Output PLS and Variants

For Jimini's small dataset (n < 500), classical chemometric methods remain competitive and are often preferred over neural networks in the low-data regime.

### PLS2 — The Multi-Response Baseline

**PLS2** (multi-response PLS) is the standard chemometric baseline for predicting multiple analytes from spectra simultaneously. It decomposes both X (spectra) and Y (responses) into shared latent components:

$$\mathbf{X} = \mathbf{T}\mathbf{P}^T + \mathbf{E}_X \qquad \mathbf{Y} = \mathbf{U}\mathbf{Q}^T + \mathbf{E}_Y$$

The decomposition maximizes covariance between X-scores (T) and Y-scores (U). The key property: **all response variables are explained by the same set of latent components**, which forces a shared representation. Equivalently:

$$\min \| X - TP^T \|^2 + \| Y - TQ^T \|^2$$

**Strengths:**
- Handles high collinearity in spectral data natively
- Interpretable: loading vectors show which wavelengths matter per component
- Fast to train, no GPU required
- Well-understood statistical properties

**Weaknesses:**
- Linear — cannot capture Beer-Lambert nonlinearities or pH-dependent spectral shifts
- Forces shared latent space even for unrelated targets (implicit negative transfer)
- PLS2 often performs worse than individual PLS1 models per-target when tasks are poorly correlated — see Mishra & Passos (2022)

| Metric | PLS2 (MC) | PLS2 (SSC) | DL multi-output (MC) | DL multi-output (SSC) |
|---|---|---|---|---|
| RMSE | 0.67% | 0.65% | 0.551% | 0.548% |

PLS2 baseline was beaten by multi-output DL (~13% lower RMSE). Importantly, **individual single-output DL models slightly outperformed multi-output DL** for well-conditioned problems. Multi-task DL wins most when targets are correlated and data is scarce.

**For Jimini:** Train PLS2 with all continuous targets simultaneously: creatinine, osmolality, bilirubin, uric acid. Binary targets (WBC, RBC, BAC) are better handled separately as classifiers or via PLS-DA.

### SO-PLS — Sequential Orthogonalized PLS

**SO-PLS** (Sequential Orthogonalized PLS) is designed for multi-block data (multiple sensor modalities). It sequentially orthogonalizes each new data block with respect to previous ones, then applies PLS:

$$\text{Block}_2^{\perp} = \text{Block}_2 - \mathbf{P}_1 \mathbf{P}_1^T \text{Block}_2$$

**For Jimini:** Directly applicable to the multi-modal setup (UV LEDs + visible + NIR + EIS as separate blocks). SO-PLS can naturally fuse spectra from C12 (321–870 nm), C14 (570–1078 nm), and EIS signals without re-scaling issues. The PROSAC-SO-PLS variant (KU Leuven, 2025) adds automated preprocessing selection per block.

### MB-PLS — Multiblock PLS

**MB-PLS** handles multiple input blocks (same principle as SO-PLS but uses a different deflation scheme). Both SO-PLS and MB-PLS are relevant when EIS and spectral data need to be fused — each block has very different physical units and correlation structure.

Extension for multiple input blocks (modalities):

$$X_1 \text{ (C12 spectra)} \quad X_2 \text{ (C14 spectra)} \quad X_3 \text{ (EIS features)}$$

MBPLS finds block weights for each input block and projects all blocks onto shared latent variables. Block weights indicate the relative importance of each modality for predicting each target.

**Practical advantage:** Directly interpretable — tells you which modality (optical vs EIS) drives each biomarker.

### Multi-Task LASSO and Group LASSO

For linear models with feature selection:

$$\min_{B} \| Y - XB \|_F^2 + \lambda \sum_{j} \| B_{j \cdot} \|_2$$

where $B \in \mathbb{R}^{p \times T}$ is the coefficient matrix ($p$ features, $T$ tasks), and $\| B_{j \cdot} \|_2$ is the row-wise group norm.

**Effect:** Group lasso forces entire features (wavelengths) to be zero or non-zero across ALL tasks simultaneously. This finds the minimal set of spectral wavelengths that predict all targets.

**Interpretation:** If wavelength 405 nm is in the non-zero group, it is relevant for at least one task. This is a principled way to perform wavelength selection for the full multi-analyte panel simultaneously.

### Multi-Output Random Forest

Standard Random Forest extended to multi-output by splitting nodes based on reduction in total variance across all outputs:

$$\text{gain} = \sum_t \text{Var}(y_t | \text{parent}) - \text{Var}(y_t | \text{split})$$

**Key property:** Tasks naturally cluster during tree construction — if bilirubin and RBC both improve from the same 405 nm split, they will share tree structure. Non-correlated tasks will use different branches.

**When to use:** If you want a non-parametric multi-output model without defining architecture; good baseline for mixed regression/classification panels.

---

## 6. Loss Functions and Task Weighting

### Naive Sum (Uniform Weighting)

$$\mathcal{L}_{\text{total}} = \sum_{t=1}^{T} \lambda_t \mathcal{L}_t, \quad \lambda_t = 1 \, \forall t$$

**Problem:** If losses are on very different scales (e.g., binary cross-entropy for WBC vs MSE for creatinine in mmol/L), one task dominates gradient updates. MSE for bilirubin (range 0–20 mg/dL) might be 100× larger than BCE for WBC (range 0–1). The optimizer will effectively ignore WBC. Manual tuning of $\lambda_t$ is tedious and brittle.

**When it works:** Tasks with similar scales and similar convergence speeds. Rare in practice.

### Manual Loss Scaling

$$\mathcal{L} = \sum_t w_t \mathcal{L}_t, \quad w_t \text{ chosen by grid search}$$

For Jimini, rough scales: regression losses (MSE) → divide by target variance; classification losses (BCE) → typically on 0–1 scale already. Heuristic:

$$w_t^{\text{regression}} = \frac{1}{\sigma_{y_t}^2}, \quad w_t^{\text{classification}} = 1$$

**Problem:** N tasks → exponentially large grid search space. Impractical for 12+ tasks.

### Uncertainty-Weighted Loss — Kendall et al. (2018, CVPR)

**The most principled approach for mixed regression + classification tasks.**

Derivation: assume each task output is Gaussian-distributed with task-dependent homoscedastic noise $\sigma_t$:

$$p(y_t | f^\theta(x)) = \mathcal{N}(y_t; f_t^\theta(x), \sigma_t^2)$$

For regression, the log-likelihood loss is:

$$\mathcal{L}_t^{\text{reg}} = \frac{1}{2\sigma_t^2} \| y_t - \hat{y}_t \|^2 + \log \sigma_t$$

For classification, the scaled cross-entropy is:

$$\mathcal{L}_t^{\text{cls}} = \frac{1}{\sigma_t^2} \mathcal{H}(y_t, \hat{y}_t) + \log \sigma_t$$

Total loss:

$$\mathcal{L}_{\text{total}} = \sum_{t=1}^{T} \frac{1}{2\sigma_t^2} \mathcal{L}_t + \log \sigma_t$$

where $\sigma_t$ are **learned parameters** alongside the network weights. Crucially:

- High uncertainty ($\sigma_t$ large) → task is downweighted automatically
- The $\log \sigma_t$ term prevents all $\sigma_t \rightarrow \infty$ collapse
- Works for regression (Gaussian likelihood) and classification (Laplacian/categorical likelihood) simultaneously
- Tasks with noisy labels or weak signal are automatically down-weighted
- In practice, learn $s_t = \log \sigma_t^2$ for numerical stability

**Why this is perfect for Jimini:**
- Creatinine (hard, high uncertainty) → large $\sigma$, small weight → model doesn't waste gradient on it
- Bilirubin (easy, strong signal) → small $\sigma$, large weight → model focuses here
- WBC (binary classification) → separate $\sigma$ term from regression tasks
- WBC count in urine is inherently noisy (cell lysis between collection and measurement, inter-observer variability in gold standard microscopy) — uncertainty weighting automatically reduces WBC's weight relative to the more precisely labeled bilirubin target
- Task weights adapt automatically during training — no grid search needed

**Implementation (PyTorch):**

```python
class UncertaintyWeightedLoss(nn.Module):
    def __init__(self, n_tasks):
        super().__init__()
        # Initialize log(sigma^2) = 0 for all tasks (sigma=1)
        self.log_vars = nn.Parameter(torch.zeros(n_tasks))

    def forward(self, losses):
        # losses: list of per-task losses
        total = 0
        for i, loss in enumerate(losses):
            precision = torch.exp(-self.log_vars[i])
            total += precision * loss + self.log_vars[i]
        return total
```

**Result:** Kendall et al. showed uncertainty weighting **outperforms manually-tuned static weights and often outperforms single-task models** on each task simultaneously.

**Caveat (IJCV, 2025):** A follow-up analysis found that uncertainty weighting's success is partly due to implicit learning rate scaling rather than principled Bayesian uncertainty. The authors propose an analytically motivated alternative. Still, uncertainty weighting is a reliable and simple starting point.

### Dynamic Weight Average (Liu et al., 2019)

Adjusts weights based on the rate of change of each task's loss:

$$w_t(T) = \frac{T \cdot \exp(r_t(T-1) / \tau)}{\sum_{t'} \exp(r_{t'}(T-1) / \tau)}$$

where $r_t(T) = \mathcal{L}_t(T-1) / \mathcal{L}_t(T-2)$ is the relative decrease in task $t$'s loss.

**Interpretation:** Tasks with slow loss decrease get higher weight; tasks already converging get lower weight. Like a teacher focusing attention on the student who is most behind.

### PI-MTL Loss Wrapper (Liu et al., 2024)

From the water quality UV-Vis paper: a **learnable loss weight vector** $v \in \mathbb{R}^T$:

$$\mathcal{L} = \frac{1}{T} \sum_{t=1}^{T} e^{-v_t} \cdot |\hat{y}_t - y_t| - v_t$$

The exponential term scales each task's contribution; $v_t$ is learned via backpropagation. If task $t$ has consistently large residuals, its $v_t$ is adjusted to re-weight accordingly. This dynamically adapts to stochastic interference — exactly the scenario in urine analysis.

### EMA Loss Weighting (Lakkapragada et al., 2022, AAAI)

**Exponential Moving Average** loss weighting uses recent loss history to prevent any single task from dominating:

$$\lambda_t^{(\tau)} = \frac{\text{EMA}(\mathcal{L}_t^{(\tau)})}{\sum_{t'} \text{EMA}(\mathcal{L}_{t'}^{(\tau)})}$$

Tasks that are still improving get proportionally higher weight; converged tasks step back. Simpler than PCGrad, very easy to implement, mitigates negative transfer caused by task dominance.

---

## 7. Gradient Balancing Methods

Even with proper loss weighting, different task gradients can **conflict** — pointing in opposite directions in parameter space — causing mutual interference that hurts both.

### GradNorm (Chen et al., ICML 2018)

Normalizes gradient magnitudes so all tasks contribute equally to the parameter update.

**Algorithm:**
1. Compute the gradient of each task's loss with respect to a shared layer's weights: $\nabla_\theta \mathcal{L}_t$
2. Compute the gradient norm for each task: $G_t^W = \|\nabla_\theta w_t \mathcal{L}_t\|_2$
3. Compute the mean gradient norm: $\bar{G}^W = E_t[G_t^W]$
4. Compute each task's "training rate ratio": $\tilde{L}_t = \mathcal{L}_t / \mathcal{L}_t^{(0)}$ (current loss / initial loss)
5. Target gradient norm: $G_t^W \cdot r_t^\alpha$ where $r_t = \tilde{L}_t / E_t[\tilde{L}_t]$
6. Loss on task weights: $\mathcal{L}_{\text{grad}} = \sum_t |G_t^W - \bar{G}^W r_t^\alpha|_1$
7. Update task weights $w_t$ by backpropagating through $\mathcal{L}_{\text{grad}}$

The hyperparameter $\alpha \in [0.1, 2.0]$ controls asymmetry between tasks. Chen et al. showed GradNorm **matches or surpasses exhaustive grid search** across multiple architectures and task types.

**Key result:** GradNorm improved over single-task models on both regression and classification tasks, demonstrating that proper gradient balancing can make MTL consistently better than independent models.

### PCGrad — Gradient Surgery (Yu et al., NeurIPS 2020)

**Insight:** Conflicting gradients (negative cosine similarity) are the root cause of multi-task failure.

**Algorithm:** For each pair of conflicting task gradients $(g_i, g_j)$ where $\cos(g_i, g_j) < 0$, project $g_i$ onto the normal plane of $g_j$:

$$g_i^{\text{PC}} = g_i - \frac{g_i \cdot g_j}{\|g_j\|^2} g_j \quad \text{if } g_i \cdot g_j < 0$$

This removes the conflicting component from $g_i$, preventing $g_j$ from being canceled out. Tasks that don't conflict are left unchanged.

**For Jimini:** Turbidity scatter (high $A_{1070}$) helps bacteria detection but *hurts* bilirubin quantification (turbidity baseline confounds 453 nm absorbance). PCGrad would automatically resolve this conflicting gradient — letting each task benefit from shared features without being harmed by the other. If the bilirubin gradient and the creatinine gradient point in opposite directions (because creatinine has no spectral signal and the model is learning nonsense for it), PCGrad prevents the creatinine gradient from destroying the bilirubin representation.

### CAGrad — Conflict-Averse Gradient Descent (Liu et al., NeurIPS 2021)

Minimizes the average loss while ensuring the update is the worst-case improvement across all tasks is maximized:

$$\min_{d: \|d-\bar{g}\| \leq c\|\bar{g}\|} \max_t \langle -d, g_t \rangle$$

**Advantage over PCGrad:** Comes with convergence guarantees (converges to a minimum of the average loss); PCGrad has no formal convergence proof.

### Gradient Similarity Weighting (Du et al., 2018)

Uses cosine similarity between auxiliary task gradients and the main task gradient as adaptive weights:

$$w_t^{(k)} = \cos(g_{\text{main}}^{(k)}, g_t^{(k)})$$

Tasks whose gradients align with the main task get higher weight; conflicting tasks get downweighted or excluded. Converges to the main task's critical points, unlike simple gradient averaging.

**For Jimini:** Designate WBC as the "main task" (primary clinical objective). All other tasks get weighted by how much their gradients agree with WBC optimization. Bilirubin and hemoglobin (strong spectral features) will naturally align; creatinine (indirect) will be downweighted.

### GradDrop (Chen et al., 2020)

Probabilistic masking of gradient components based on consistency across tasks:

- At each activation layer, mask gradient components where tasks disagree
- Probability of keeping a gradient component ∝ its consistency across tasks
- Result: naturally sparse, conflict-free gradient updates

**Best combined with:** GradNorm for magnitude balancing + GradDrop for direction conflict resolution.

---

## 8. Science-Informed Task Relations

The most important conceptual advance for Jimini. Instead of letting the network discover task relationships purely from data (which requires more training samples), you encode known biochemical/physical relationships directly into the architecture.

### Formal Framework (FTIRNet approach)

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

### Implementation Strategy

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

## 9. Task Relationship Learning

Instead of pre-defining which tasks share parameters, learn the task relationships from data.

### Task Clustering

Cluster tasks by similarity of their optimal model parameters or their gradient behavior. Tasks in the same cluster share parameters; tasks in different clusters use separate encoders.

**For Jimini, initial task clustering hypothesis:**

```text
Cluster A (optical absorbers):
  bilirubin, hemoglobin/RBC, uric acid, protein, porphyrins/TUP, PBG
  → share UV-Vis spectral encoder

Cluster B (scatter/cellular):
  WBC, bacteria, crystals, epithelial cells
  → share scatter feature extractor (A1070, scatter slope, autofluorescence)

Cluster C (EIS-dependent):
  creatinine, osmolality, sodium, chloride
  → share EIS encoder

Cluster D (multi-modal):
  Merge Cluster A and B representations with some interaction
  for targets that depend on both (nitrites = proxy from BAC ∈ B)
```

### Task Affinity Matrices

Compute pairwise task affinity (after training independent models):

- $\text{Affinity}(t_1, t_2) = \cos(\theta_{t_1}^*, \theta_{t_2}^*)$ where $\theta_t^*$ is the optimal parameter vector for task t
- High affinity → good candidates for parameter sharing
- Near-zero or negative affinity → should be kept separate

### Cross-Stitch Coefficients as Task Relationship Indicators

After training a cross-stitch network, the learned $\alpha_{t_1 t_2}$ coefficients directly quantify how much task $t_2$'s representation helps task $t_1$. This is a data-driven measurement of task affinity.

---

## 10. Hierarchical and Cascaded Prediction

Hierarchical prediction uses outputs from easy tasks as inputs (features) for harder tasks. This is physically motivated for Jimini: some analytes are easier to measure optically and their values constrain or predict others.

### Two-Stage Prediction

Some Jimini targets are much easier to predict reliably (high spectral signal-to-noise) than others. Predict the easy ones first, then use them as features for the hard ones.

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

### Physical Hierarchy for Jimini (3 levels)

```text
Level 1 — Direct Beer-Lambert (easiest, highest confidence):
  bilirubin → A455, A455/A600
  uric acid → A275, A275/A320
  hemoglobin/RBC → A405, A405/A455, Q-band doublet
  porphyrins/TUP → fluorescence ex405/em620

Level 2 — Scatter + matrix (medium):
  osmolality → EIS conductivity + A1070
  crystals → A800/A400 scatter slope
  WBC → scatter + NADH autofluorescence + EIS

Level 3 — Indirect / correlated (hardest):
  creatinine → EIS + spectral residual + osmolality (L1)
  bacteria → turbidity + scatter slope + Level 1 residuals
  sodium, chloride → EIS only
  nitrites → proxy from BAC model
```

### Cascade Architecture (code)

```python
# Stage 1: predict strongly-anchored analytes
stage1_features = spectral_encoder(x)
bili_hat = bilirubin_head(stage1_features)   # high confidence
hb_hat = hemoglobin_head(stage1_features)    # high confidence
ua_hat = uricacid_head(stage1_features)      # high confidence
porphyrin_hat = porphyrin_head(stage1_features)

# Stage 2: augment features with Stage 1 predictions
augmented = torch.cat([stage1_features, bili_hat, hb_hat, ua_hat, porphyrin_hat], dim=-1)
osm_hat = osmolality_head(augmented)         # medium confidence
wbc_hat = wbc_head(augmented)                # benefits from hb_hat, osm_hat
rbc_hat = rbc_head(augmented)                # benefits from hb_hat

# Stage 3: use all prior predictions
full_features = torch.cat([augmented, osm_hat, wbc_hat], dim=-1)
creat_hat = creatinine_head(full_features)   # uses osmolality as proxy
bac_hat = bacteria_head(full_features)       # uses turbidity + WBC context
```

**Caution:** Cascaded errors propagate. If Stage 1 is wrong, Stage 2 inherits the error. Use prediction intervals or soft predictions (logits/probabilities, not hard labels) as inputs to subsequent stages.

### Regression → Classification Cascade

For binary targets (WBC ≥+, BAC positive): first build a continuous score model, then threshold. The continuous prediction at Stage 1 can be used as a soft feature for Stage 2 classifiers. This provides uncertainty estimates (prediction near the threshold = high uncertainty).

### "Hints" as Auxiliary Tasks (Caruana, 1998)

Instead of cascading at inference time, use intermediate targets as **auxiliary training objectives** at intermediate network layers:

- Add a supervision signal for bilirubin at layer 3 of the encoder
- Force the network to represent bilirubin-relevant features early in the processing hierarchy
- The bilirubin feature then naturally propagates to deeper layers used by WBC, RBC, and bacterial detection

**Joint Many-Task model (Hashimoto et al., 2016):** This is the NLP analog — lower-level tasks (part-of-speech tagging) supervised at lower layers; higher-level tasks (semantic analysis) supervised at higher layers. For Jimini, the analogy is: Beer-Lambert absorbers at lower layers, scatter-based cellular markers at higher layers.

### Evidence from Spectroscopy Literature

**Predicting anemia from NIR spectroscopy of spent dialysis fluid (Nature Sci. Rep., 2021):**
- Predicted 9 blood parameters simultaneously (RBC, Hb, Fe, TIBC, FER, Hct, MCV, MCHC, MCH)
- R values 0.91–0.96 for all 9 parameters
- Key observation: parameters that are biologically correlated (RBC, Hct, MCV — all related to red cell morphology) share spectral features and improve each other's predictions

---

## 11. Negative Transfer: When Multi-Task Hurts

Negative transfer occurs when jointly training two tasks degrades performance compared to training them independently. It is the primary risk of MTL.

### When Negative Transfer Occurs

| Condition | Risk level | Mechanism |
|---|---|---|
| Tasks have uncorrelated labels | High | Conflicting gradient directions in shared layers |
| Tasks have very different input sensitivity | High | One task uses 275 nm features; another needs 1070 nm features |
| Tasks have very different output scales/types | Medium | Regression + classification in same loss without normalization |
| One task has much larger/smaller loss magnitude | Medium | Dominant task monopolizes gradient signal |
| Tasks require conflicting feature transformations | High | Turbidity helps scatter-based detection but hurts absorption-based quantification |

### Causes (detailed)

| Cause | Description | Jimini example |
|---|---|---|
| **Gradient conflict** | Task gradients point in opposite directions; one task's update undoes another's | Creatinine (EIS-dependent) gradient conflicts with bilirubin (optical) gradient |
| **Task asymmetry** | One task dominates the loss magnitude; others are suppressed | Regression MSE for osmolality >> binary CE for WBC → WBC effectively not trained |
| **Spurious correlations** | Task B shares a spurious feature with task A in training data but not at test time | If WBC correlates with pH in training data but pH-independent bilirubin is jointly trained, the encoder may over-fit to pH |
| **Representation bottleneck** | Shared representation too narrow to capture all task-relevant features | Shared z ∈ ℝ⁸ cannot represent both spectral shape features AND EIS impedance profile |
| **Unrelated task** | Task B has genuinely different spectral basis from task A | Nitrites (spectrally transparent) and bilirubin (optical) should NOT share a spectral encoder |

### Detection

**Method 1 — Performance comparison.** Compare MTL model performance vs single-task baseline per task. If MTL is worse for task t, negative transfer has occurred for task t.

**Method 2 — Gradient cosine similarity.** Monitor $\cos(g_t, g_{t'})$ during training. Consistently negative cosine similarity between tasks t and t' signals conflict.

**Method 3 — Probing experiments.** Freeze the shared encoder and train task-specific heads from scratch. If WBC head performance drops significantly when the shared encoder is trained with creatinine vs without, creatinine is causing negative transfer for WBC.

### Mitigation (ranked by implementation effort)

1. **Task grouping** — don't put completely unrelated tasks in the same MTL model. Group by input domain (optical targets together, EIS targets together) and by output type (classifiers together, regressors together).
2. **EMA loss weighting** — dynamically down-weight tasks that are improving poorly (prevents one dominant task from monopolizing).
3. **Gradient surgery (PCGrad / CAGrad / GradDrop)** — explicitly resolve conflicting gradients.
4. **Soft parameter sharing** — tasks have separate networks but are regularized to be similar (L2 penalty on parameter differences). More flexible than hard sharing.
5. **Task-specific batch normalization** — separate BN statistics per task; prevents interference in normalization layers which are a common source of negative transfer.
6. **Asymmetric MTL** — allow transfer from Task A → Task B but not necessarily B → A (directional gates as in FTIRNet).
7. **Adversarial task regularization** — add a discriminator that makes the shared representation task-invariant for some task pairs.
8. **Sluice Networks (Ruder et al., 2019)** — learn which layers and subspaces to share between each task pair; allows partial sharing instead of hard all-or-nothing decisions.
9. **Auxiliary task exclusion** — remove tasks that consistently show negative cosine similarity with primary tasks.

### Jimini-Specific Risk Assessment

| Task pair | Transfer risk | Reason |
|---|---|---|
| WBC ↔ BAC | **Low** — positive transfer likely | Both correlated with infection state and turbidity |
| Bilirubin ↔ RBC | **Low** — positive transfer likely | Both visible absorbers; Hb degradation produces bilirubin |
| Uric acid ↔ Creatinine | **Medium** — weak positive | Both UV-active solutes; creatinine barely visible at 275 nm |
| TUP ↔ Bilirubin | **Medium** | Both at 405 nm but different mechanisms; risk of spectral overlap confusion |
| Uric acid ↔ Scatter targets (WBC, BAC) | **High risk** | UV absorption (analyte signal) vs scatter (cell detection signal) are mechanistically unrelated at 275 nm |
| Nitrites ↔ Optical targets | **High risk** | Nitrites are spectrally invisible; forcing joint training with optical features adds no signal |

> [!NOTE]
> Do NOT include Nitrites, Sodium, Chloride in the optical-domain MTL model. These are EIS targets and should be modeled separately with EIS-specific inputs.

---

## 12. Spectroscopy-Specific Applications

### LUMIR: Multi-Task Infrared Spectroscopy (2025)

**Paper:** "LUMIR: an LLM-Driven Unified Agent Framework for Multi-task Infrared Spectroscopy Reasoning" (arXiv:2507.21471, Xie et al., 2025).

LUMIR handles three spectroscopy tasks simultaneously on the same spectra: classification, regression, and anomaly detection. Key approach: LLM-based framework mines literature for validated preprocessing and feature derivation strategies, then applies few-shot prompting for multi-task inference.

**Datasets:** Milk NIR, Chinese medicinal herbs, wastewater COD, Tecator meat, Corn grain. All involve predicting multiple properties from the same spectrum.

**Key finding:** Multi-task LLM-guided approach achieved performance comparable to or surpassing dedicated ML models, particularly in low-data settings. Demonstrates that multi-task spectral analysis is feasible even with very few labeled samples.

### Raman Spectral Unmixing (Multi-Component Simultaneous Estimation)

**Paper:** "Hyperspectral unmixing for Raman spectroscopy via physics-constrained autoencoders" (arXiv:2403.04526, Imperial College / Oxford, 2024).

The autoencoder architecture simultaneously estimates abundances of multiple molecular species:

- **Encoder (shared):** spectrum → component abundances (multi-output vector)
- **Decoder:** abundances → reconstructed spectrum

This is exactly multi-task regression: one shared encoder predicting multiple abundances simultaneously, where the physical constraint (sum-to-one, non-negativity) provides an additional multi-task regularizer.

**Result:** Better than MCR-ALS for complex mixtures; outperforms single-component estimation by leveraging cross-component constraints.

### Brain Tissue Molecular Composition (Multi-Component diffuse spectroscopy)

**Paper:** "Learnable real-time inference of molecular composition from diffuse spectroscopy" (arXiv:2309.16735, Imperial College/CNRS, 2023).

Simultaneously predicts 4 molecular concentrations (HbO₂, HHb, oxCCO, redCCO) from broadband NIR spectra. Shared encoder + 4 regression heads (one per molecule). Training on Beer-Lambert-simulated spectra with known multi-component mixtures.

**Key finding:** MTL approach is 1000× faster than sequential optimization of each species independently. The shared encoder naturally learns the spectral unmixing basis functions.

**Direct analogy to Jimini:** Predict uric acid + bilirubin + hemoglobin + porphyrins simultaneously as a spectral unmixing problem with known extinction coefficients as physics-based constraints.

### Drug Sensitivity Prediction (Multi-Task + Spectral-like data)

**Paper:** PaccMann (Manica et al., 2019) — multi-modal attention-based neural networks for predicting cancer drug sensitivity.

Multi-task learning across 100+ drugs simultaneously from gene expression profiles (analogous to spectral profiles). Attention mechanism identifies which "spectral" features (genes) matter most per drug.

**Relevance:** The attention-based multi-task approach directly transfers to Jimini's multi-analyte prediction, where each "spectral gene" is a wavelength channel.

### Anemia prediction from NIR dialysate (Nature Sci. Rep., 2021)

Predicts 9 blood parameters simultaneously (RBC, Hb, Fe, TIBC, FER, Hct, MCV, MCHC, MCH) from NIR spectra of dialysate fluid; R = 0.91–0.96. Parameters that are biologically correlated (red-cell morphology cluster) share spectral features and mutually improve predictions — direct empirical demonstration of positive transfer in spectroscopic MTL.

---

## 13. Comparison Matrix

### Scenario → Best approach

| Scenario | Best approach | Evidence |
|---|---|---|
| n > 500 per task, tasks weakly correlated | Single-task models | Mishra & Passos 2022: single DL beats multi-output DL |
| n < 300 per task, tasks correlated | **MTL with uncertainty weighting** | FTIRNet, PI-MTL both show clear gains |
| Strong spectral interference (turbidity, color) | **PI-MTL with auxiliary interference tasks** | Liu et al. 2024: 60% RMSE reduction vs PLSR |
| Some tasks have weak spectral signal | **MTL with science-informed task connections** | FTIRNet: weak S/K prediction improved significantly by including correlated C/N tasks |
| Mixed binary + continuous targets | **Hard sharing + task-specific heads** | Standard approach; uncertainty weighting handles scale mismatch |
| Need interpretability | PLS2 or SO-PLS | Loadings directly interpretable as spectral features |
| Rapid prototyping, few samples | **PLS2 baseline → MTL DL if insufficient** | PLS2 as baseline, DL for production |

### Method-by-method comparison (for Jimini)

| Method | Data size | Task types | Negative transfer | Interpretability | Implementation | Best for Jimini target |
|---|---|---|---|---|---|---|
| **Multi-output PLS2** | Small (n<500) | Regression only | Low risk | High (loadings) | Trivial (sklearn) | Creatinine, osmolality, bilirubin, uric acid |
| **Multi-target RF** | Small-medium | Mixed | Low | Medium | Easy | WBC, RBC (binary); creatinine (regression) — mixed panel |
| **Hard sharing + Kendall loss** | Medium (n>200) | Mixed | Medium | Low-Medium | Moderate | Full panel if n sufficient |
| **Hard sharing + GradNorm** | Medium-Large | Mixed | Low-Medium | Low | Moderate | Full panel; better gradient control |
| **Hard sharing + PCGrad** | Medium-Large | Mixed | Low | Low | Moderate | When gradient conflicts detected |
| **Hierarchical cascade** | Any | Mixed | Low (decoupled) | High | Moderate | Jimini: Stage1 optical → Stage2 scatter/EIS |
| **Cross-stitch network** | Medium | Mixed | Very low | Medium | High | Bilirubin/TUP pair (high affinity); WBC/BAC pair |
| **Modality-specific encoders** | Medium | Mixed | Low | High | Moderate | Recommended for Jimini (optical vs EIS split) |
| **Multi-output LASSO** | Small | Regression | Low | Very high | Easy | Wavelength selection for all regression targets |
| **GradNorm + Kendall** | Medium | Mixed | Low | Low | High | Full panel with proper gradient control |
| **PI-MTL (physics-informed)** | Medium | Mixed | Low | Medium | High | Turbidity/color-interfered targets |

---

## 14. Decision Guide for Jimini V20 Targets

### Task Classification

| Task | Type | Direct spectral? | Primary signal | Recommended group |
|---|---|---|---|---|
| **Bilirubin** | Regression | ★★★★★ | A455, Beer-Lambert | A (optical absorbers) |
| **RBC (hemoglobin)** | Classification | ★★★★★ | A405 Soret | A (optical absorbers) |
| **Uric acid** | Regression | ★★★★★ | A275, Beer-Lambert | A (optical absorbers) |
| **TUP (porphyrins)** | Classification | ★★★★ | ex405/em620 fluorescence | A (optical absorbers) |
| **PBG** | Classification | ★★★ | A405 (converted form) | A (optical absorbers) |
| **Protein** | Regression | ★★★★ | A275 (Trp), fluorescence | A (optical absorbers) |
| **NADH** | Regression | ★★★ | ex365/em460 fluorescence | A (optical absorbers) |
| **WBC** | Classification | ★★ | Scatter + fluorescence | B (scatter/cellular) |
| **Bacteria (BAC)** | Classification | ★★ | Scatter + UV + fluorescence | B (scatter/cellular) |
| **Crystals** | Classification | ★ | Scatter slope | B (scatter/cellular) |
| **epiCells** | Classification | ★ | Scatter | B (scatter/cellular) |
| **Osmolality** | Regression | ★★ | EIS + NIR water band | C (EIS/colligative) |
| **Creatinine** | Regression | ★ | EIS conductivity | C (EIS/colligative) |
| **Sodium** | Regression | ☆ | EIS only | C (EIS/colligative) |
| **Chloride** | Regression | ☆ | EIS only | C (EIS/colligative) |
| **Nitrites** | Classification | ☆ | Proxy: BAC model | B proxy |

### Recommended Task Groups

**Group 1 — Optical Absorbers + Fluorophores (spectral domain)**

```text
Targets: Bilirubin, RBC/Hemoglobin, TUP, PBG, Uric acid, Protein, NADH
Input:   A(275), A(365), A(405), A(455), white-LED spectrum (C12/C14)
Model:   Shared 1D-CNN encoder → task-specific heads
Notes:   Influencing chain: Hb → TUP → PBG (biochemical cascade)
```

**Group 2 — Particulate/Scatter Targets (scatter domain)**

```text
Targets: WBC, BAC, RBC (cell count), epiCells, Crystals
Input:   A(1070), scatter slope (A400/A800), NADH fluorescence, autofluorescence
         + optical Group 1 predictions as auxiliary features
Model:   Shared scatter-feature encoder → task-specific binary heads
Notes:   Use Group 1 Hb prediction as influencing feature for RBC binary head
```

**Group 3 — Solute/Electrolyte Targets (EIS + NIR domain)**

```text
Targets: Osmolality, Creatinine, Sodium, Chloride
Input:   EIS (multi-frequency: 100Hz–100kHz), A(1070), spectral integral
Model:   EIS-specific encoder → continuous regression heads
Notes:   Osmolality as influencing task for Creatinine
```

**NOT in any MTL group:**
- Nitrites → model as downstream of BAC binary prediction
- CKD markers (glucose, urea) → require wavelengths outside Jimini range

### Recommended Full Architecture (modality-specific + hierarchical)

```text
┌─────────────────────────────────────────────────────────────────┐
│                    INPUT FEATURES                                │
├──────────────────┬──────────────────┬───────────────────────────┤
│ C12 spectrum     │ C14 spectrum     │ EIS features               │
│ [288 channels]   │ [multi-px NIR]   │ [k frequency points]       │
│ 340–850 nm       │ 640–1050 nm      │ 10 Hz – 100 kHz            │
└──────────┬───────┴──────────┬───────┴──────────────┬────────────┘
           │                  │                       │
    ┌──────▼──────┐   ┌───────▼──────┐   ┌───────────▼────────┐
    │ UV-Vis      │   │ NIR Encoder  │   │ EIS Encoder        │
    │ Encoder     │   │ Conv1D layers│   │ MLP + attention    │
    │ Conv1D +    │   │ z_nir ∈ R^32 │   │ z_eis ∈ R^16       │
    │ attention   │   │              │   │                    │
    │ z_vis∈R^64  │   └──────┬───────┘   └──────────┬─────────┘
    └──────┬──────┘          │                       │
           │                 │                       │
    ┌──────▼─────────────────▼──────────────────────▼─────────┐
    │                 FUSION LAYER                              │
    │           z_fused = MLP([z_vis, z_nir, z_eis])            │
    │           z_fused ∈ R^128                                 │
    └──────┬────────────────────────────────────────────────── ┘
           │
    ┌──────▼──────────────────────────────────────────────────┐
    │  STAGE 1 HEADS (optical absorbers, high confidence)     │
    ├─────────────────────────────────────────────────────────┤
    │  bili_hat = Linear(z_vis) → [bilirubin] mg/dL           │
    │  hb_hat = Sigmoid(Linear(z_vis)) → P(RBC ≥ 5/µL)        │
    │  ua_hat = Linear(z_vis) → [uric acid] mmol/L            │
    │  porph_hat = Sigmoid(Linear(z_vis)) → P(TUP elevated)   │
    └──────┬──────────────────────────────────────────────────┘
           │  augment z_fused with Stage 1 predictions
    ┌──────▼──────────────────────────────────────────────────┐
    │  STAGE 2 HEADS (scatter/cellular + EIS)                 │
    ├─────────────────────────────────────────────────────────┤
    │  wbc_hat = Sigmoid(MLP([z_fused, hb_hat, osm_hat]))     │
    │  bac_hat = Sigmoid(MLP([z_fused, wbc_hat]))             │
    │  osm_hat = Linear(z_eis + z_nir)                        │
    └──────┬──────────────────────────────────────────────────┘
           │
    ┌──────▼──────────────────────────────────────────────────┐
    │  STAGE 3 HEADS (indirect/EIS-only)                      │
    ├─────────────────────────────────────────────────────────┤
    │  creat_hat = Linear([z_eis, osm_hat])                   │
    │  na_cl_hat = Linear(z_eis)                              │
    └─────────────────────────────────────────────────────────┘

Loss: Uncertainty-weighted sum (Kendall et al.)
      + PCGrad or CAGrad for conflicting gradients
```

### Architecture Blueprint — Physics-Informed Optical MTL (Group 1)

```python
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

        # Physics-informed pre-weighting: weight input spectrum by known effective wavelengths
        self.pi_weights = {
            'bilirubin': nn.Parameter(init_from_spectrum(453)),   # ε peak
            'hemoglobin': nn.Parameter(init_from_spectrum(415)),  # Soret peak
            'uric_acid': nn.Parameter(init_from_spectrum(293)),   # ε peak
        }

        # Influence gate: Hb → TUP
        self.hb_to_tup_gate = nn.Parameter(torch.tensor(0.0))  # sigmoid → 0.5 init

        # Task-specific heads
        self.heads = nn.ModuleDict({
            'bilirubin':  nn.Linear(64*32, 1),           # regression
            'hemoglobin': nn.Linear(64*32, 1),           # regression
            'tup':        nn.Linear(64*32 + 64*32, 1),   # + Hb features via gate
            'pbg':        nn.Linear(64*32, 1),           # binary
            'uric_acid':  nn.Linear(64*32, 1),           # regression
        })

        # Uncertainty weights (Kendall 2018)
        self.log_vars = nn.Parameter(torch.zeros(len(self.heads)))

    def forward(self, spectrum):
        features = self.encoder(spectrum)
        hb_features = features  # (would use PI-weighted variant)
        hb_pred = self.heads['hemoglobin'](features)

        # Science-informed: Hb features → TUP via learned gate
        gate = torch.sigmoid(self.hb_to_tup_gate)
        tup_features = torch.cat([features, gate * hb_features], dim=-1)

        return {
            'bilirubin':  self.heads['bilirubin'](features),
            'hemoglobin': hb_pred,
            'tup':        self.heads['tup'](tup_features),
            'pbg':        torch.sigmoid(self.heads['pbg'](features)),
            'uric_acid':  self.heads['uric_acid'](features),
        }
```

### Task Correlation Matrix (Prior Estimates)

Based on physical relationships:

| | Bili | RBC/Hb | UricA | TUP | WBC | BAC | Creat | Osm |
|--|--|--|--|--|--|--|--|--|
| **Bili** | — | 0.3 | 0.2 | 0.6 | 0.1 | 0.1 | 0.0 | 0.1 |
| **RBC/Hb** | 0.3 | — | 0.1 | 0.3 | 0.2 | 0.1 | 0.1 | 0.1 |
| **TUP** | **0.6** | 0.3 | 0.3 | — | 0.1 | 0.1 | 0.0 | 0.0 |
| **WBC** | 0.1 | 0.2 | 0.0 | 0.0 | — | **0.7** | 0.2 | 0.2 |
| **BAC** | 0.1 | 0.1 | 0.0 | 0.0 | **0.7** | — | 0.1 | 0.1 |
| **Creat** | 0.0 | 0.1 | 0.2 | 0.0 | 0.2 | 0.1 | — | **0.8** |
| **Osm** | 0.1 | 0.1 | 0.2 | 0.0 | 0.2 | 0.1 | **0.8** | — |

> High values (≥ 0.4) suggest beneficial joint training. Very low values (≤ 0.1) across all pairs suggest independent training may be safer. These are physics-based priors — validate empirically.

### Data Requirements

| Target | Minimum n for MTL | Minimum n for single-task |
|---|---|---|
| WBC, BAC, RBC (binary) | ~200/class | ~300/class |
| Bilirubin (regression) | ~150 | ~200 |
| TUP, PBG (binary, rare condition) | ~100/class (but rare!) | ~200/class |
| Creatinine (regression) | ~200 | ~300 |
| Osmolality (regression) | ~150 | ~200 |

For rare-positive targets (TUP, PBG) in the ~5–15% prevalence range, **data augmentation** (spectral noise addition, concentration jitter via Beer-Lambert simulation) is essential before MTL.

---

## 15. Practical Implementation Notes

### Baseline Protocol

1. **Step 1:** Train independent single-task models (PLS for regression, LR/RF for classification) per analyte. This is your baseline.
2. **Step 2:** Train multi-output PLS2 on all regression targets simultaneously. Compare vs Step 1 per target.
3. **Step 3:** Train hard-sharing MTL neural network with uncertainty-weighted loss (Kendall). Compare vs Step 1 and 2.
4. **Step 4:** Apply GradNorm or PCGrad. Check if gradient conflicts are present using cosine similarity diagnostics.
5. **Step 5:** If negative transfer detected for specific tasks (MTL worse than Step 1), try:
   - Task grouping (separate models for optical vs EIS targets)
   - Cross-stitch network for the conflicting pair
   - Remove the offending task from the joint model

### Hyperparameters

| Hyperparameter | Range | Note |
|---|---|---|
| Shared encoder depth | 2–4 layers | More layers → more sharing; start shallow |
| Shared encoder width | 64–256 | Scale with number of tasks |
| Task-specific head depth | 1–2 layers | Keep simple to regularize |
| Uncertainty init | log_var = 0 (σ = 1) | Allows all tasks equal initial weight |
| GradNorm α | 0.1–1.5 | α = 1.5 for similar tasks; α = 0.2 for very different |
| Dropout in shared layers | 0.1–0.3 | Apply consistently across all tasks |
| Learning rate | 1e-3 (Adam) | Separate LR for task weights (1e-2 often works) |

### Target Normalization

Before joint training of regressors:
- Standardize continuous targets to zero mean, unit variance
- Or use min-max normalization to [0,1] range
- This prevents high-magnitude targets (osmolality: 50–1200 mOsm/kg) from dominating the loss over low-magnitude targets (creatinine: 0.5–25 mmol/L)

### Binary + Regression Mix

For mixed classification/regression MTL (e.g., WBC binary + osmolality regression):
- Use **binary cross-entropy** for classifiers + **MSE or Huber** for regressors
- Apply uncertainty weighting to handle the different loss scales
- Consider a **Huber loss** (smooth L1) for regressors to reduce sensitivity to concentration outliers

### Class Imbalance

WBC, BAC, TUP are binary with positive-class prevalence ~10–40%. Use:
- Weighted binary cross-entropy: `pos_weight = n_negative / n_positive`
- Focal loss: down-weights easy negatives, focuses on hard positives
- Never use plain BCE with imbalanced classes in a MTL setting — the imbalanced task will get over-optimized

### Starting Point: PLS2 Baseline

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

### Evaluation Protocol for MTL

Always compare MTL against single-task baselines:

```text
For each target t:
  STL(t) = train single-task model on target t
  MTL(t) = train joint MTL model, extract per-task performance for t

  Transfer gain: Δ(t) = STL_RMSE(t) - MTL_RMSE(t)

  Positive transfer if Δ(t) > 0
  Negative transfer if Δ(t) < 0
```

Report per-task Δ alongside aggregate metrics. Publishing only average MTL performance can hide negative transfer on individual tasks.

### Diagnostic Checklist

Before deploying a multi-task model:
- [ ] Per-task performance vs independent single-task baseline (MTL should not be worse)
- [ ] Task weight distribution (Kendall σ values) — check no task collapsed to zero weight
- [ ] Gradient cosine similarity matrix — flag consistently negative pairs
- [ ] Confusion matrix for classification tasks — multi-task should not create new error modes
- [ ] SHAP values per task — verify feature attributions are physically sensible

---

## Gaps

1. **No published study predicts the Jimini V20 target set jointly.** The closest analogs are the water UV-Vis work (Liu et al., 2024 — 2 targets) and the NIR dialysate work (Nature, 2021 — 9 blood parameters). The combination of binary classifiers + continuous regressors + mixed optical/EIS inputs for 10+ urine biomarkers simultaneously has not been published.
2. **Optimal task grouping is empirical.** The transfer gain matrix (which tasks help/hurt each other) can only be measured on Jimini data. Theory gives guidance but actual grouping requires ablation studies.
3. **Effect of sample size on MTL advantage.** The literature shows consistent MTL advantage at n < 500 and neutral/negative at n > 1000. Jimini's clinical dataset size per target will determine whether MTL or ensemble of single-task models is better.
4. **EIS + optical fusion.** No published paper jointly trains on UV-Vis spectra + multi-frequency EIS for multi-biomarker prediction. The MB-PLS / SO-PLS framework is the natural chemometric approach; for DL, a dual-encoder architecture (one for spectra, one for EIS impedance features) with a shared fusion layer is the natural design.
5. **Temporal dynamics.** If sequential measurements of the same urine sample are possible (e.g., watching PBG darken over time), time-series MTL models could extract richer information than single-shot predictions.

---

## Sources

| Paper | Year | arXiv / DOI | Contribution |
|---|---|---|---|
| Caruana, R. "Multi-task learning" | 1997 | — | Original MTL framework; mechanisms; "hints" auxiliary-task idea |
| Misra, I. et al. "Cross-stitch networks for multi-task learning" | 2016 | — | Learned linear combinations of task-specific features |
| Asymmetric Multi-task Learning (AMTL) | 2016 | [proceedings.mlr.press/v48/leeb16.html](https://proceedings.mlr.press/v48/leeb16.html) | Sparse directional regularization graph for task relatedness |
| Hashimoto, K. et al. "Joint many-task model" | 2017 | — | Hierarchical multi-task for NLP; layer-task pairing |
| Ruder, S. "An overview of multi-task learning in DNNs" | 2017 | [1706.05098](https://arxiv.org/abs/1706.05098) | Comprehensive survey; hard vs soft sharing |
| Kendall, A., Gal, Y., Cipolla, R. "Multi-Task Learning Using Uncertainty to Weigh Losses" | 2018 | [1705.07115](https://arxiv.org/abs/1705.07115) | Homoscedastic uncertainty weighting — the standard MTL loss approach |
| Chen, Z. et al. "GradNorm" | 2018 | [proceedings.mlr.press/v80/chen18a.html](https://proceedings.mlr.press/v80/chen18a.html) | Gradient normalization for balanced MTL |
| Du, Y. et al. "Adapting auxiliary losses with gradient similarity" | 2018 | [1812.02224](https://arxiv.org/abs/1812.02224) | Cosine similarity weighting for auxiliary tasks |
| Liu, S. et al. "Dynamic Weight Average" | 2019 | — | Loss-rate-based dynamic weighting |
| Ruder, S. et al. "Sluice networks" | 2019 | — | Learned partial layer/subspace sharing |
| Ng, W. et al. "1D-CNNs for simultaneous soil properties" | 2019 | — | Multi-output CNN for soil VIS/NIR/MIR; foundational spectral multi-task reference |
| Manica, M. et al. "PaccMann" | 2019 | — | Multi-task attention for drug sensitivity; 100+ drugs jointly |
| Yu, T. et al. "Gradient surgery for MTL (PCGrad)" | 2020 | [2001.06782](https://arxiv.org/abs/2001.06782) | Eliminates conflicting gradient updates between tasks |
| Chen, Z. et al. "GradDrop" | 2020 | [2010.06808](https://arxiv.org/abs/2010.06808) | Gradient sign consistency masking |
| Crawshaw, M. "Multi-task learning with DNNs: a survey" | 2020 | [2009.09796](https://arxiv.org/abs/2009.09796) | Survey of architectures, optimization, task relationships |
| Multi-task grain NIR (J Near Infrared Spectrosc) | 2020 | [opg.optica.org/jnirs-28-5-275](https://opg.optica.org/abstract.cfm?uri=jnirs-28-5-275) | Multi-task NIR for cereal quality |
| Liu, B. et al. "CAGrad" | 2021 | [2110.14048](https://arxiv.org/abs/2110.14048) | Conflict-averse gradient descent; convergence guarantee |
| "Predicting anemia from NIR dialysate spectroscopy" | 2021 | [10.1038/s41598-021-88821-4](https://www.nature.com/articles/s41598-021-88821-4) | 9 blood parameters simultaneously from NIR; R ≈ 0.91–0.96 |
| Mishra, P. & Passos, D. "Multi-output 1D-CNNs for NIR fruit trait prediction" | 2022 | [10.1016/j.postharvbio.2021.111741](https://doi.org/10.1016/j.postharvbio.2021.111741) | Multi-output DL beats PLS2 by 13%; single-task slightly beats multi-output when tasks less correlated |
| Lakkapragada, A. et al. "Mitigating Negative Transfer with EMA Loss Weighting" | 2022 | [2211.12999](https://arxiv.org/abs/2211.12999) | EMA-based dynamic loss weighting to prevent negative transfer |
| Goodwin, C. et al. "Learnable BLL for brain tissue" | 2023 | [2309.16735](https://arxiv.org/abs/2309.16735) | MTL for simultaneous 4-chromophore estimation from NIR spectra |
| Georgiev, D. et al. "Physics-constrained AE for Raman unmixing" | 2024 | [2403.04526](https://arxiv.org/abs/2403.04526) | Multi-output spectral unmixing; simultaneous component estimation |
| Mishra et al. (Agronomy) "UV-NIR for Hydroponic Macronutrients: Single vs. Multi-Task" | 2024 | [mdpi.com/2073-4395/14/9/1974](https://www.mdpi.com/2073-4395/14/9/1974) | Direct single-task vs multi-task comparison on UV-NIR spectroscopy |
| Raman oral cancer multi-task (RSC Analytical Methods) | 2024 | [pubs.rsc.org/d3ay02250a](https://pubs.rsc.org/en/content/articlelanding/2024/ay/d3ay02250a) | Cancer type + grade + margin from fiber-optic Raman; MTL beats per-task |
| Joint MTL for biomarkers in pathology (MICCAI) | 2024 | [2403.03891](https://arxiv.org/abs/2403.03891) | MTL for histopathology biomarkers; positive transfer from easy to hard targets |
| Liu et al. "Physics-informed multi-task learning for COD and nitrate in UV-Vis water spectroscopy" | 2024 | [10.1016/j.saa.2024.124857](https://doi.org/10.1016/j.saa.2024.124857) | PI-MTL: 60% RMSE reduction vs PLSR under turbidity interference; directly analogous to urine matrix |
| Bachinin et al. "FTIRNet: Science-Informed Multitask Transformer for Soil FTIR" | 2025 | [cs.colostate.edu/FTIR_eScience25.pdf](https://www.cs.colostate.edu/~shrideep/papers/2025/FTIR_eScience25.pdf) | Shared Transformer encoder + directional task gates; science-informed relations; R² > 0.98 for 7 properties |
| Uncertainty weighting analysis (IJCV 2025) | 2025 | [10.1007/s11263-025-02625-x](https://link.springer.com/article/10.1007/s11263-025-02625-x) | Critique of Kendall 2018: benefit largely from implicit LR scaling; proposes analytically motivated alternative |
| Xie, Z. et al. "LUMIR: LLM multi-task IR spectroscopy" | 2025 | [2507.21471](https://arxiv.org/abs/2507.21471) | Multi-task classification + regression + anomaly on spectral data |
| PROSAC-SO-PLS (KU Leuven) | 2025 | — | Automated preprocessing selection per block in multi-block SO-PLS |
| MGMT framework for complex mixtures (Analytica Chimica Acta) | 2026 | [sciencedirect.com](https://www.sciencedirect.com/science/article/abs/pii/S0003267025014448) | Multi-group multi-task framework for complex chemical mixtures |
| Negative transfer analysis (AAAI chemistry case study) | — | [ojs.aaai.org/AAAI/article/5125](https://ojs.aaai.org/index.php/AAAI/article/download/5125/4998) | Empirical negative-transfer study in chemistry MTL |

**Web Resources:**

| Resource | URL |
|---|---|
| Ruder blog: "An Overview of Multi-Task Learning in DNNs" | [ruder.io/multi-task](https://ruder.io/multi-task/) |
| GradNorm ICML 2018 proceedings | [proceedings.mlr.press/v80/chen18a.html](https://proceedings.mlr.press/v80/chen18a.html) |
| arXiv MTL survey (Crawshaw 2020) | [arxiv.org/abs/2009.09796](https://arxiv.org/abs/2009.09796) |
| PCGrad (Gradient Surgery) | [arxiv.org/abs/2001.06782](https://arxiv.org/abs/2001.06782) |
| CAGrad | [arxiv.org/abs/2110.14048](https://arxiv.org/abs/2110.14048) |
| Kendall uncertainty weighting | [arxiv.org/abs/1705.07115](https://arxiv.org/abs/1705.07115) |
