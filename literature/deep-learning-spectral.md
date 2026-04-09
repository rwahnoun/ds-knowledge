# 05 — Deep Learning for Spectral Data

1D-CNN, transformers, autoencoders, and data augmentation (WGAN, diffusion) for spectroscopic regression and classification.

## Papers

| File | Title | Year | Key Finding |
|---|---|---|---|
| `1d-cnn-vs-chemometrics-2023.pdf` | 1D-CNN vs ML for Spectral Classification | 2023 | CNN outperforms PLS/SVR/RF when n > 500. PLS competitive for n < 200. arXiv: 2301.10746 |
| `1d-cnn-review-portable-raman-2020.pdf` | 1D-CNN Review for Portable Raman | 2020 | Architecture survey for 1D spectral CNN. arXiv: 2006.10575 |
| `deep-spectral-cnn-libs-2020.pdf` | Deep Spectral CNN for LIBS | 2020 | CNN disentangles spectral signals from sensor noise. arXiv: 2012.01653 |
| `data-augmentation-spectral-cnn-2017.pdf` | Data Augmentation for Spectral CNN (Bjerrum) | 2017 | Noise injection + shifting + scaling for NIR CNN. arXiv: 1710.01927 |
| `benchmarking-dl-raman-2026.pdf` | Benchmarking DL Models for Raman | 2026 | Comprehensive comparison of DL vs chemometrics on open datasets. arXiv: 2601.16107 |

## Key Takeaway

**Model selection by dataset size**:  
- n < 100: PLS + MCCV  
- n = 100–300: SVR/RF ensemble, or PLS  
- n > 300: 1D-CNN (Conv1D→BatchNorm→ReLU→GlobalAvgPool→Dense)  
- n > 1000: Transformers (SpectraTr, SpectraViT) emerging  

**Data augmentation** is critical for clinical spectral datasets: noise injection, WGAN-GP (8–15% accuracy boost), diffusion models (state-of-the-art 2025).
