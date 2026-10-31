# MSc — Computer Science

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/pytest-32%20passed-success?style=flat-square&logo=pytest&logoColor=white)](courses/data-centers-and-ai-networks/ex1/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)

Coursework, network simulations, and research materials for my M.Sc. in Computer Science, focusing on data center networks, distributed systems, and AI training infrastructure.

---

## Contents

- [Courses](#courses)
  - [Data Center Networks & AI (Course 361.2.2460)](#data-center-networks--ai-course-36122460)
- [Studying with AI: The Sparring Partner Method](#studying-with-ai-the-sparring-partner-method)
- [Repository Structure](#repository-structure)
- [Setup & Reproduction](#setup--reproduction)

---

## Courses

### [Data Center Networks & AI (Course 361.2.2460)](courses/data-centers-and-ai-networks/)

Semester A 2026. Covers scalable network fabrics, congestion control, lossless Ethernet, and interconnects for distributed AI training clusters.

| Resource | Path | Description | Status |
|---|---|---|---|
| **Course Hub** | [`courses/data-centers-and-ai-networks/`](courses/data-centers-and-ai-networks/) | Syllabus, environment setup, and learning notes | Active |
| **Exercise 1** | [`ex1/`](courses/data-centers-and-ai-networks/ex1/) | Fat-tree topology generator, link failure model, degradation analysis | [32/32 tests passing](courses/data-centers-and-ai-networks/ex1/test_fattree.py) |
| **Articles** | [`articles/`](courses/data-centers-and-ai-networks/articles/) | 17 papers & slides (Clos, DCTCP, TIMELY, RoCEv2, CONGA, Alibaba HPN) | Dual PDF + Markdown |
| **Notes** | [`articles/notes/`](courses/data-centers-and-ai-networks/articles/notes/) | Audio and lecture companion notes | Ongoing |

#### Exercise 1: Fat-Tree Robustness Highlights
- Pure Python and NetworkX generator for $k$-ary fat-tree topologies ($k^3/4$ hosts, $5k^2/4$ switches, all switches degree $k$).
- Exact-fraction link failure model with deterministic nested RNG seeds.
- **Empirical result:** Under switch-switch link failures, surviving shortest paths follow $(1-p)^4$ across all $k$. Networks lose bisection bandwidth and path diversity well before losing host reachability.

```
                   ┌──────────┐      ┌──────────┐
                   │  Core 1  │      │  Core 2  │  ...
                   └────┬─────┘      └─────┬────┘
                        │                  │
               ┌────────┴──────────────────┴────────┐
               │              Pod Switches           │
               │  [ Aggregation 0 ]   [ Aggregation 1 ]│
               │         │                   │       │
               │  [    Edge 0     ]   [    Edge 1    ]│
               └────────┬────────────────────┬───────┘
                        │                    │
                   ┌────┴─────┐         ┌────┴─────┐
                   │ Host S0  │         │ Host S1  │
                   └──────────┘         └──────────┘
```

---

## Research Literature

The repository maintains an audited paper library under [`courses/data-centers-and-ai-networks/articles/`](courses/data-centers-and-ai-networks/articles/) with one-paragraph summaries, original PDFs, and Markdown conversions with embedded figures:

- **Topologies:** Al-Fares Fat-Tree (SIGCOMM '08), VL2 (SIGCOMM '09), Jupiter Rising (SIGCOMM '15), Random Regular Graphs (RNG '24).
- **Traffic Patterns:** Data center traffic in the wild (IMC '09).
- **Transport & Congestion Control:** DCTCP (SIGCOMM '10), TIMELY (SIGCOMM '15), DCQCN / RoCEv2 (SIGCOMM '15).
- **Load Balancing:** FlowBender (CoNEXT '14), WCMP (EuroSys '14), CONGA (SIGCOMM '14).
- **AI Infrastructure:** Meta RoCEv2 (SIGCOMM '24), Alibaba HPN (SIGCOMM '24), Megatron-LM (SC '21), Deadlocks in lossless fabrics (SIGCOMM '21).

---

## Studying with AI: The Sparring Partner Method

Using AI for ready-made answers bypasses the learning process and creates an illusion of understanding that fails under scrutiny. Instead, use AI to challenge your own thinking:

1. **Try first:** Inspect the paper figures and architecture diagrams. Write down your own interpretation before prompting an AI tool.
2. **Ask AI to challenge you (Sparring):** Provide your interpretation and ask:
   > *"Here is my reading of Figure X: [...]. Do not give me the answer. Critique my reasoning, point out edge cases, and ask me 2 questions to test whether I truly understand it."*
3. **Verify every claim against the paper:** AI tools frequently hallucinate units, scales, or details (e.g. confusing KB with MB). **If the AI and the paper disagree, the paper wins.**

---

## Repository Structure

```text
MSc-GitHub/
├── README.md                                  # Repository overview
└── courses/
    └── data-centers-and-ai-networks/          # Course 361.2.2460
        ├── README.md                          # Syllabus & exercise directory
        ├── requirements.txt                   # Shared Python dependencies
        ├── articles/
        │   ├── README.md                      # Paper summaries (Units 1-10)
        │   ├── *.pdf                          # Original paper PDFs
        │   ├── markdown/                      # Markdown conversions with figures
        │   └── notes/                         # Hebrew lecture deep-dives
        └── ex1/                               # HW1: Fat-Tree Simulation & Robustness
            ├── README.md                      # Lab report & documentation
            ├── fattree.py                     # Generator, failure engine & CLI
            ├── plot_bisection.py              # Bisection bandwidth visualizer
            ├── test_fattree.py                # 32 unit tests
            ├── figures/                       # Plots and diagrams
            └── results/                       # Measurement CSVs
```

---

## Setup & Reproduction

```bash
git clone https://github.com/shaygol/MSc.git
cd MSc/courses/data-centers-and-ai-networks

# Virtual environment setup
python -m venv .venv
.venv\Scripts\activate          # Windows (Linux/macOS: source .venv/bin/activate)
pip install -r requirements.txt

# Run test suite
cd ex1
python -m pytest test_fattree.py -v

# Run experiments
python fattree.py --experiment all --seed 42
python plot_bisection.py --k 4
```
