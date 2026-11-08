# M.Sc. Electrical Engineering

Coursework, research projects, and academic materials for my Master of Science (M.Sc.) degree in Electrical Engineering.

---

## Directory Overview

- **[`courses/`](courses/)** — Course materials, assignments, and lecture notes.
  - **[`data-centers-and-ai-networks/`](courses/data-centers-and-ai-networks/)** — Data Center Networks & AI (Course 361.2.2460, Semester A 2026).
  - **[`generative-ai/`](courses/generative-ai/)** — Generative Models in AI (Course 66925, Semester A 2026/27).
- **[`research/`](research/)** — Thesis work, literature reviews, and research experiments.
- **[`resources/`](resources/)** — General reference materials, academic papers, and tools.

---

## Courses

Each course is maintained as an independent repository linked to this parent repo as a Git submodule.

| Course | Code | Term | Description | Repository |
|---|---|---|---|---|
| [Data Center Networks & AI](courses/data-centers-and-ai-networks/) | 361.2.2460 | Semester A 2026 | Datacenter Clos topologies, lossless RDMA transports, congestion control, and network fabrics for distributed AI clusters. | [`shaygol/data-centers-and-ai-networks`](https://github.com/shaygol/data-centers-and-ai-networks) |
| [Generative Models in AI](courses/generative-ai/) | 66925 | Semester A 2026/27 | Autoregressive, score-based and energy-based generative models (own notes only). | [`shaygol/generative-ai`](https://github.com/shaygol/generative-ai) |

---

### Working with Submodules

To clone this repository including all course submodules:

```bash
git clone --recurse-submodules git@github.com:shaygol/MSc.git
```

If you have already cloned without `--recurse-submodules`, initialize and fetch submodules with:

```bash
git submodule update --init --recursive
```

To update all submodules to their latest remote commits:

```bash
git submodule update --remote --merge
```
