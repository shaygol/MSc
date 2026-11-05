# Generative Models in AI

Semester A 2026/27, BGU (Moodle course 66925).

This folder holds **my own** work for the course: notes, summaries, exercises and code.
It does **not** contain the lecturer's material (slides, recordings, handouts, exam material).
That stays on Moodle. See [Content policy](#content-policy).

---

## Syllabus

Topics in lecture order:

| # | Topic | Materials | Notes |
|:---:|---|---|:---:|
| **1** | **Introduction and autoregressive models**<br>(FVSBN, NADE, MADE, RNN, PixelRNN/PixelCNN, WaveNet) | • [NADE (JMLR 2016)](https://arxiv.org/abs/1605.02226)<br>• [MADE (2015)](https://arxiv.org/abs/1502.03509)<br>• [PixelRNN / PixelCNN (2016)](https://arxiv.org/abs/1601.06759)<br>• [WaveNet (2016)](https://arxiv.org/abs/1609.03499)<br>• [Attention Is All You Need (2017)](https://arxiv.org/abs/1706.03762) |  |
| **2** | **Energy-based models and score-based models** | • [LeCun Tutorial on EBMs (2006)](http://yann.lecun.com/exdb/publis/pdf/lecun-06.pdf)<br>• [Song & Kingma: Training EBMs (2021)](https://arxiv.org/abs/2101.03288)<br>• [Sliced Score Matching (2019)](https://arxiv.org/abs/1905.07088)<br>• [Song & Ermon: Score Gradients (2019)](https://arxiv.org/abs/1907.05600) |  |
| **3** | **Diffusion models (continuous)** | • [DDPM (2020)](https://arxiv.org/abs/2006.11239)<br>• [Song et al.: SDEs (2020)](https://arxiv.org/abs/2011.13456)<br>• [DDIM (2020)](https://arxiv.org/abs/2010.02502) |  |
| **4** | **Diffusion models (discrete)** | • [D3PM: Discrete Diffusion (2021)](https://arxiv.org/abs/2107.03006)<br>• [Bit-Diffusion (2022)](https://arxiv.org/abs/2208.04202) |  |
| **5** | **Graph neural networks** | • [Graph Convolutional Networks (2016)](https://arxiv.org/abs/1609.02907)<br>• [GraphVAE (2018)](https://arxiv.org/abs/1802.03480)<br>• [DiGress: Graph Diffusion (2022)](https://arxiv.org/abs/2209.14734) |  |
| **6** | **Audio generation** | • [DiffWave (2020)](https://arxiv.org/abs/2009.09761)<br>• [Jukebox (2020)](https://arxiv.org/abs/2005.00341)<br>• [AudioLDM (2023)](https://arxiv.org/abs/2301.12503) |  |
| **7** | **Transformers for image generation** | • [Image Transformer (2018)](https://arxiv.org/abs/1802.05751)<br>• [ViT (2020)](https://arxiv.org/abs/2010.11929)<br>• [MaskGIT (2022)](https://arxiv.org/abs/2202.04200)<br>• [DiT: Diffusion Transformers (2022)](https://arxiv.org/abs/2212.09748) |  |
| **8** | **Mamba, state space models, and advanced RNNs**<br>(xLSTM, RWKV, Griffin) | • [Mamba (2023)](https://arxiv.org/abs/2312.00752)<br>• [xLSTM (2024)](https://arxiv.org/abs/2405.04517)<br>• [RWKV (2023)](https://arxiv.org/abs/2305.13048)<br>• [Griffin (2024)](https://arxiv.org/abs/2402.19427) |  |
| **9** | **AI quantum codes** | • [Neural Decoder for Topological Codes (2017)](https://arxiv.org/abs/1610.04238)<br>• [DNN Decoder for Stabilizer Codes (2017)](https://arxiv.org/abs/1705.09334)<br>• [ML Decoder for QEC (2018)](https://arxiv.org/abs/1705.07855) |  |
| **10** | **Final project presentations** | • Group project / Individual paper study (no GANs) |  |

**Assignments:** Normalizing Flows and Diffusion Models, and Transformers.  
**Final project:** A group project or an individual paper study (no GANs).

---

## General Reference Material

Foundational textbooks and courses:

- [Stanford CS236: Deep Generative Models](https://deepgenerativemodels.github.io/) — course notes and slides
- [Deep Learning Textbook (Goodfellow, Bengio, Courville)](https://www.deeplearningbook.org/) — comprehensive reference
- [RealNVP: Density Estimation using Real NVP (2016)](https://arxiv.org/abs/1605.08803) — Normalizing flows reference
- [Glow: Generative Flow with Invertible 1x1 Convolutions (2018)](https://arxiv.org/abs/1807.03039) — Normalizing flows reference

---

## Layout

- [`notes/`](notes/) — my own summaries, written in my words (one file per topic).
- [`exercises/`](exercises/) — my homework solutions and experiments, one folder per exercise.
  - [`exercises/team-project/ideas.md`](exercises/team-project/ideas.md) — final-project idea pool and triage.

---

## Content policy

- Own summaries, presentations, code and other learning material (from any source other than this lecturer) are welcome here.
- Do not copy the lecturer's original files (slides, handouts, recordings, exercises) into the repo. Keep them locally in `lecturer-material/`, which is git-ignored.
- Cite public papers by title and link.
- If AI helped with a file, say so in it.
