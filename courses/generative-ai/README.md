# Generative Models in AI

Semester A 2026/27, BGU (Moodle course 66925).

This folder holds **my own** work for the course: notes, summaries, exercises and code.
It does **not** contain the lecturer's material (slides, recordings, handouts, exam material).
That stays on Moodle. See [Content policy](#content-policy).

---

## Syllabus

Topics in lecture order:

1. **Introduction and autoregressive models** (FVSBN, NADE, MADE, RNN, PixelRNN/PixelCNN, WaveNet)
2. **Energy-based models and score-based models**
3. **Diffusion models (continuous)**
4. **Diffusion models (discrete)**
5. **Graph neural networks**
6. **Audio generation**
7. **Transformers for image generation**
8. **Mamba, state space models, and advanced RNNs** (xLSTM, RWKV, Griffin)
9. **AI quantum codes**
10. **Final project presentations**

**Assignments:** Normalizing Flows and Diffusion Models, and Transformers.  
**Final project:** A group project or an individual paper study (no GANs).

---

## Background Material

Public background reading grouped by lecture topic. Links point to original sources:

| Topic | Resource | Link |
|---|---|---|
| General | Stanford CS236, Deep Generative Models (course notes and slides) | [deepgenerativemodels.github.io](https://deepgenerativemodels.github.io/) |
| General | Goodfellow, Bengio, Courville, *Deep Learning* (textbook) | [deeplearningbook.org](https://www.deeplearningbook.org/) |
| Autoregressive models | NADE, Neural Autoregressive Distribution Estimation | [arXiv:1306.0185](https://arxiv.org/abs/1306.0185) |
| Autoregressive models | MADE, Masked Autoencoder for Distribution Estimation | [arXiv:1502.03509](https://arxiv.org/abs/1502.03509) |
| Autoregressive models | PixelRNN / PixelCNN, Pixel Recurrent Neural Networks | [arXiv:1601.06759](https://arxiv.org/abs/1601.06759) |
| Autoregressive models | Attention Is All You Need (Transformer) | [arXiv:1706.03762](https://arxiv.org/abs/1706.03762) |
| WaveNet | WaveNet: A Generative Model for Raw Audio | [arXiv:1609.03499](https://arxiv.org/abs/1609.03499) |
| Energy-based models | LeCun et al., A Tutorial on Energy-Based Learning | [PDF](http://yann.lecun.com/exdb/publis/pdf/lecun-06.pdf) |
| Energy-based models | Song & Kingma, How to Train Your Energy-Based Models | [arXiv:2101.03288](https://arxiv.org/abs/2101.03288) |
| Score-based models | Sliced Score Matching | [arXiv:1905.07088](https://arxiv.org/abs/1905.07088) |
| Score-based models | Song & Ermon, Generative Modeling by Estimating Gradients of the Data Distribution | [arXiv:1907.05600](https://arxiv.org/abs/1907.05600) |
| Diffusion models | Ho et al., Denoising Diffusion Probabilistic Models (DDPM) | [arXiv:2006.11239](https://arxiv.org/abs/2006.11239) |
| Diffusion models | Song et al., Score-Based Generative Modeling through SDEs | [arXiv:2011.13456](https://arxiv.org/abs/2011.13456) |
| State space models | Gu & Dao, Mamba | [arXiv:2312.00752](https://arxiv.org/abs/2312.00752) |

---

## Layout

- [`notes/`](notes/) — my own summaries, written in my words (one file per topic).
- [`exercises/`](exercises/) — my homework solutions and experiments, one folder per exercise.

---

## Content policy

- Own summaries, presentations, code and other learning material (from any source other than this lecturer) are welcome here.
- Do not copy the lecturer's original files (slides, handouts, recordings, exercises) into the repo. Keep them locally in `lecturer-material/`, which is git-ignored.
- Cite public papers by title and link.
- If AI helped with a file, say so in it.
