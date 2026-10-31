# M.Sc. in Computer Science — Academic & Research Repository

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/pytest-32%20passed-success?style=flat-square&logo=pytest&logoColor=white)](courses/data-centers-and-ai-networks/ex1/)
[![Degree](https://img.shields.io/badge/degree-M.Sc.%20Computer%20Science-blueviolet?style=flat-square)](#)
[![Field](https://img.shields.io/badge/field-Data%20Centers%20%26%20AI%20Networks-informational?style=flat-square)](#)
[![Status](https://img.shields.io/badge/status-active%20coursework%20%26%20research-brightgreen?style=flat-square)](#)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)

> Coursework, distributed systems research, topology simulations, and foundational literature analysis for my Master of Science (M.Sc.) degree in Computer Science.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Coursework](#-coursework)
  - [Data Center Networks & AI (Course 361.2.2460)](#data-center-networks--ai-course-36122460)
- [Research & References](#-research--references)
- [Pedagogical Framework: AI Sparring Partner](#-pedagogical-framework-ai-sparring-partner)
- [Repository Structure](#-repository-structure)
- [Quickstart & Reproduction](#-quickstart--reproduction)
- [Academic Integrity & AI Disclosure](#-academic-integrity--ai-disclosure)

---

## 🔭 Overview

Modern computing systems face an unprecedented shift: data center networks are evolving from general-purpose web services toward massive, ultra-low-latency, lossless fabrics tailored for distributed AI training workloads (e.g., Megatron-LM, DeepSpeed) and high-performance computing (HPC).

This repository serves as an open, reproducible hub containing:
- **Scalable Network Simulations:** Topology generation, fault injection models, and path-diversity degradation analysis.
- **Curated Research Library:** 17 foundational papers and lecture slide decks with dual-format access: original PDFs and audited Markdown transcriptions featuring embedded high-resolution figures.
- **Academic Lecture Notes:** Deep dives into network fabrics, collective communications, and AI factories.
- **Rigorous Verification:** Complete unit test suites (`pytest`), empirical CSV data, and publication-ready vector/raster plots.

---

## 🎓 Coursework

### [Data Center Networks & AI (Course 361.2.2460)](courses/data-centers-and-ai-networks/)

*Semester A, 2026* | Focus: Architecture, congestion control, load balancing, and lossless transport for hyperscale AI factories.

| Component | Path | Description | Status |
|---|---|---|---|
| **Course Hub** | [`courses/data-centers-and-ai-networks/`](courses/data-centers-and-ai-networks/) | Main syllabus, learning methodology, virtual environment setup | Active |
| **Homework 1** | [`ex1/`](courses/data-centers-and-ai-networks/ex1/) | Fat-Tree topology generator, failure model, empirical robustness experiments | [32/32 Passing](courses/data-centers-and-ai-networks/ex1/test_fattree.py) |
| **Literature Hub** | [`articles/`](courses/data-centers-and-ai-networks/articles/) | 17 papers covering Clos topologies, DCTCP, TIMELY, RoCEv2/PFC, CONGA, Alibaba HPN | Complete |
| **Lecture Notes** | [`articles/notes/`](courses/data-centers-and-ai-networks/articles/notes/) | Audio & lecture companion deep-dives (e.g., AI Factory networking) | Ongoing |

#### Key Highlights from Homework 1: Fat-Tree Robustness
- **Generator & Validator:** Pure Python & NetworkX implementation constructing parameterizable $k$-ary fat-trees ($k^3/4$ hosts, $5k^2/4$ switches, all degree $k$).
- **Failure Injection Model:** Exact-fraction link removal algorithm with deterministic, nested RNG seeds to capture smooth degradation curves.
- **Key Empirical Finding:** Switch-switch link failures degrade **bisection bandwidth and path diversity** following $(1-p)^4$ long before reaching reachability partitions—demonstrating that data centers lose capacity well before losing connectivity.

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

## 📚 Research & References

The repository maintains an audited paper library under [`courses/data-centers-and-ai-networks/articles/`](courses/data-centers-and-ai-networks/articles/):

- **Topologies & Architecture:** Clos networks, Al-Fares Fat-Tree (SIGCOMM '08), VL2 (SIGCOMM '09), Jupiter Rising (SIGCOMM '15), Random Regular Graphs (RNG).
- **Workload & Traffic Dynamics:** Kandula's data center traffic in the wild (IMC '09).
- **Lossless & Congestion Transport:** Data Center TCP / DCTCP (SIGCOMM '10), TIMELY RTT-based congestion (SIGCOMM '15), DCQCN / RDMA over Converged Ethernet (SIGCOMM '15).
- **In-Network Load Balancing:** CONGA leaf-spine load balancing (SIGCOMM '14), FlowBender (CoNEXT '14), WCMP (EuroSys '14), AI training load balancing.
- **AI Infrastructure & Large-Scale LLM Training:** Meta RoCEv2 at scale (SIGCOMM '24), Alibaba HPN (SIGCOMM '24), Megatron-LM (SC '21), Collective communications (NCCL, Ring AllReduce), and Deadlock prevention in lossless networks.

Every paper features:
1. **Original PDF** — intact academic archival copy.
2. **Audited Markdown (`.md`)** — full mathematical equations (KaTeX), properly ordered multi-column text, and high-resolution figures.
3. **One-Paragraph Executive Summary** — context, core innovation, and relevance to modern network architectures.

---

## 🥊 Pedagogical Framework: AI Sparring Partner

Graduate-level comprehension requires deep, critical engagement. Rather than using generative AI to produce shallow answers, this workspace enforces a **"Sparring Partner"** study protocol:

> [!TIP]
> **1. Formulate First:** Examine architectural diagrams, theorems, and performance graphs independently before consulting AI.
> **2. Challenge & Spar:** Present an interpretation to the model and instruct it to act as an examiner:
> *"Here is my hypothesis regarding Figure 4. Do not provide answers; identify flaws in my assumptions and ask 2 rigorous counter-questions."*
> **3. Ground Truth Verification:** Always cross-reference AI claims with original papers. When AI assertions conflict with published experimental data, **the paper always wins**.

---

## 🗂 Repository Structure

```text
MSc-GitHub/
├── README.md                                  # Root repository portal (this file)
└── courses/
    └── data-centers-and-ai-networks/          # Course 361.2.2460 (Data Center Networks & AI)
        ├── README.md                          # Course syllabus & roadmap
        ├── requirements.txt                   # Shared environment dependencies
        ├── articles/
        │   ├── README.md                      # Annotated paper index & summaries (Units 1-9)
        │   ├── *.pdf                          # 17 original research papers & slide decks
        │   ├── markdown/                      # 17 audited Markdown conversions with figures
        │   │   ├── *.md
        │   │   └── images/                    # Extracted vector & high-res figures (300+ assets)
        │   └── notes/
        │       └── topic1-podcast-ai-factory.md # Hebrew lecture companion
        └── ex1/                               # Homework 1: Fat-Tree Topology & Failure Analysis
            ├── README.md                      # Comprehensive empirical lab report & CLI guide
            ├── fattree.py                     # Core simulator, failure engine, CLI & plotting
            ├── plot_bisection.py              # Visualizer for edge-disjoint bisection bandwidth
            ├── test_fattree.py                # 32 unit tests verifying topology & metrics
            ├── figures/                       # Rendered evaluation plots
            └── results/                       # Empirical CSV datasets
```

---

## 🚀 Quickstart & Reproduction

### 1. Clone & Set Up Python Environment

```bash
git clone https://github.com/shaygol/MSc.git
cd MSc/courses/data-centers-and-ai-networks

# Create and activate virtual environment
python -m venv .venv

# Windows:
.venv\Scripts\activate
# Linux / macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Test Suite

Verify all graph generation algorithms, failure distributions, and metrics:

```bash
cd ex1
python -m pytest test_fattree.py -v
```

### 3. Reproduce Fat-Tree Experiments

Generate all empirical datasets and plots in under 30 seconds:

```bash
# Run both sanity check (Experiment 1) and failure degradation (Experiment 2)
python fattree.py --experiment all --seed 42

# Generate colored full bisection bandwidth visualization for k=4
python plot_bisection.py --k 4
```

---

## ⚖️ Academic Integrity & AI Disclosure

This repository strictly adheres to academic integrity standards:
- All external literature, algorithms, and architectures cite original authors and conferences.
- Anthropic Claude and Google Gemini were utilized as pedagogical sparring partners, editorial assistants, and code verification aids. All derived code, analytical proofs, and simulation data were independently audited and verified against empirical unit tests.

---

<p align="center">
  <sub>Maintained by <b>Shay Golan</b> • M.Sc. Computer Science • 2026</sub>
</p>
