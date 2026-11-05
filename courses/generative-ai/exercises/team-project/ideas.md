# Final Project: Idea Pool

Candidate ideas for the course's final project. The project is done in teams of 3–4, and GANs are not allowed. The team has remote access to the BGU HPC cluster.

**Status:** brainstorm. No idea has been chosen yet.

Numbers in parentheses, such as (5+11), are the IDs of the original ideas. Ideas that overlapped are merged into one entry. Lecture numbers refer to the [syllabus table](../../README.md#syllabus).

Each idea also lists three fields a project proposal needs: the **problem** (why it matters), the **input/output** of the final model, and **ethical concerns**.

---

## Triage criteria

1. **Course fit**: the idea builds directly on one or more lecture topics.
2. **Measurable result**: there is a quantitative metric and a clear baseline to beat or compare against.
3. **Data**: a public dataset exists, or the data can be generated.
4. **Prior work**: we know what has already been done and what our angle is.
5. **Team split**: the work divides into 3–4 parallel tracks, so nobody waits on anyone else.
6. **Compute**: this is a minor factor because of the HPC. We still need to plan for queue time and walltime limits, which means checkpointing and the ability to resume. The GPU type and quota are still to be confirmed.

---

## Tier 1: clear metric that splits well across a team

### A. Alternatives to multi-scale noise for score-based models (21)

- **Idea:** Score matching struggles in three places: when the data lies on a low-dimensional manifold, in low-density regions, and with slow Langevin mixing between modes. NCSN fixes these with multi-scale Gaussian noise. We propose a different fix, for example noise adapted to the data's geometry, and compare it with NCSN.
- **Problem:** These failure modes hurt sample quality on real data, which lies near low-dimensional manifolds and has many modes. They also force long sampling chains. A noise scheme that fits the data could reach the same quality with fewer steps.
- **Input/output:**
  - The score network takes a noisy sample and a noise level, and returns the estimated score.
  - The sampler turns random noise into new samples: 2D points or images.
- **Lectures:** 2–3.
- **Metric:**
  - On toy 2D mixtures: mode coverage and mode weight recovery.
  - On MNIST/CIFAR-10: FID or likelihood, plus the number of sampling steps needed.
- **Prior work:**
  - [NCSN, Song & Ermon 2019](https://arxiv.org/abs/1907.05600)
  - [Score SDEs, Song et al. 2020](https://arxiv.org/abs/2011.13456)
  - [Riemannian score-based models, De Bortoli et al. 2022](https://arxiv.org/abs/2202.02763)
- **Team split:**
  - toy benchmarks and diagnostics
  - NCSN baseline
  - the alternative noise scheme
  - image-scale experiments
- **Risk:** the alternative may simply lose to NCSN. Toy experiments make even a negative result clear and easy to explain.
- **Ethics:** low. The datasets are public benchmarks, and image generation at MNIST/CIFAR scale carries little misuse potential.

### B. Generative compression: how few bits are enough? (7+18)

- **Idea:** Use a generative model as the decoder of a codec. The sender transmits a very short description, and the receiver regenerates the signal. Plot rate-distortion and rate-perception curves against classical codecs.
- **Problem:** Links with very little bandwidth, such as satellite, IoT and emergency radio, need media at bitrates where classical codecs break down. A generative decoder can fill in plausible detail, which raises the question of how few bits a listener or viewer will accept.
- **Input/output:**
  - The encoder turns an image or audio clip into a short bitstream.
  - The generative decoder turns that bitstream back into a reconstructed image or clip.
- **Lectures:** 3, 6.
- **Metric:**
  - bitrate vs PSNR/SSIM (images) or SI-SDR (audio)
  - a perceptual metric
  - a small listening or viewing test, to find the rate at which people stop noticing a difference
- **Prior work:**
  - [Lossy Compression with Gaussian Diffusion, Theis et al. 2022](https://arxiv.org/abs/2206.08889)
  - [EnCodec, Défossez et al. 2022](https://arxiv.org/abs/2210.13438)
  - [Opus codec (RFC 6716)](https://www.rfc-editor.org/rfc/rfc6716)
- **Team split:**
  - encoder and quantization
  - generative decoder
  - classical baselines
  - evaluation and listening test
- **Risk:** strong neural codecs already exist, so our contribution has to be narrow, for example the extreme low-bitrate regime.
- **Ethics:**
  - The decoder *invents* detail. A reconstruction can look or sound convincing and still differ from the original, for example a changed word or facial detail. Reports must state that this makes it unsuitable for evidence, medical or legal use.
  - The listening test needs informed consent.
  - Speech data contains real voices, so use only public datasets that were collected with consent.

### C. Synthetic network traffic: can a classifier tell it apart? (1+19+22)

- **Idea:** Train a generative model on packet or flow traces and generate traffic in the style of a given application or network condition. Compare a diffusion model with a WaveNet conditioned on network state such as load and latency. The μ-law quantization in WaveNet suits heavy-tailed size distributions. Then test whether a traffic classifier can separate real traffic from synthetic traffic.
- **Problem:** Privacy keeps realistic network traces scarce, yet they are needed to test protocols and to train traffic classifiers. Traffic that is realistic and can be generated for a chosen network condition would allow such testing without real user data.
- **Input/output:**
  - The model takes an application label and a network-state condition (load, latency), plus noise.
  - It outputs a synthetic packet or flow sequence: sizes, inter-arrival times and flags.
- **Lectures:** 1, 3, 6.
- **Metric:**
  - classifier two-sample test accuracy, where 50% is ideal
  - distribution distances on packet sizes, inter-arrival times and flow sizes
  - downstream classifier accuracy when trained on synthetic data
- **Data:**
  - [ISCX VPN-nonVPN](https://www.unb.ca/cic/datasets/vpn.html), labelled by application
  - published statistics from [Benson et al., IMC 2010](https://doi.org/10.1145/1879141.1879175)
- **Prior work:**
  - [NetShare, SIGCOMM 2022](https://doi.org/10.1145/3544216.3544251) is GAN-based. We cite it as prior work only. We do not train or run it, and we compare against it only through the numbers its paper reports.
  - [NetDiffusion, 2023](https://arxiv.org/abs/2310.08543)
- **Team split:**
  - data pipeline and features
  - diffusion model
  - conditioned WaveNet
  - classifiers and evaluation
- **Risk:** NetDiffusion already fine-tunes a controlled Stable Diffusion model to generate protocol-conforming packet traces for augmenting labelled datasets. Our angle has to be conditioning on *network state* (load, latency) rather than only on the application label, plus a direct AR vs diffusion comparison.
- **Ethics:**
  - **Dual use:** traffic that fools a classifier could help attackers evade traffic classification or intrusion detection. Frame the work as an evaluation of classifiers and report defenses.
  - **Privacy:** a model trained on real traces can memorize addresses or payload fragments. Use anonymized public datasets and header-level features only.

### D. Graph diffusion for network topologies (5+11+25)

- **Idea:** Train a discrete graph-diffusion model to generate switch-level topologies with fixed switch count and port count. Steer it toward high throughput and low cost, and compare against fat-tree and Jellyfish (random regular graphs).
- **Problem:** A data center's topology sets both its throughput and its cost. Today's designs are either hand-crafted (fat-tree) or random (Jellyfish). A generative model can search the design space for structures nobody has tried.
- **Input/output:**
  - The model takes the switch count, ports per switch, and optionally a target for throughput or cost, which guides generation.
  - It outputs the adjacency matrix of a valid topology.
- **Lectures:** 4, 5.
- **Metric:**
  - throughput, from a max-concurrent-flow LP
  - bisection bandwidth
  - average path length
  - cost (switches and links)
- **Prior work:**
  - [DiGress, Vignac et al. 2022](https://arxiv.org/abs/2209.14734)
  - [GCN, Kipf & Welling 2016](https://arxiv.org/abs/1609.02907)
  - [Fat-tree, Al-Fares et al. 2008](https://doi.org/10.1145/1402958.1402967)
  - [Jellyfish, Singla et al. 2012](https://arxiv.org/abs/1110.1687)
- **Team split:**
  - topology generators and throughput evaluator
  - graph diffusion model
  - guidance and constraints (degree, connectivity)
  - analysis of the structures we discover
- **Risk:** Jellyfish is already close to optimal for throughput at equal cost, so it may be hard to beat. A well-argued "cannot beat it, and here is why" is still a valid result.
- **Ethics:** none significant. The graphs are synthetic and involve no personal data. Results hold "on paper" only, because cabling, failures and routing are not modelled, and the report should say so.

### E. Score-prior speech restoration (17)

- **Idea:** Restore corrupted speech, such as telephone band-limiting, noise, clipping or packet loss, using a score-based model as the prior.
- **Problem:** Phone calls, hearing aids, VoIP with packet loss, and old recordings all lose intelligibility. One model that handles several corruption types at once would be useful.
- **Input/output:** a corrupted speech waveform or spectrogram goes in, and an estimate of the clean speech comes out.
- **Lectures:** 2, 3, 6.
- **Metric:** PESQ, STOI and SI-SDR, broken down by corruption type.
- **Data:** [VoiceBank-DEMAND](https://datashare.ed.ac.uk/handle/10283/2791).
- **Prior work:** [SGMSE+, Richter et al. 2022](https://arxiv.org/abs/2208.05830).
- **Team split:**
  - corruption pipeline
  - baseline (SGMSE+)
  - new corruption types or a new conditioning method
  - evaluation
- **Risk:** reproducing SGMSE+ alone is not a contribution. We need a corruption type or setting it does not handle.
- **Ethics:**
  - A generative prior can produce phonemes or words that were never spoken, which makes it dangerous for transcripts or forensic audio.
  - Voices are personal data; use the public, consented dataset.
  - The method could also be misused to clean up covert recordings.

---

## Tier 2: feasible, but needs a sharper novel angle

| Idea | Lectures | Metric | Prior work | Angle / risk |
|---|:---:|---|---|---|
| **Diffusion as an error-correction decoder** (14+27): channel noise acts as the forward process, and the score drives decoding. End-to-end learned codes vs LDPC. | 3, 9 | BER/FER vs SNR | [DDECC, Choukroun & Wolf 2022](https://arxiv.org/abs/2209.13533); [Deep Quantum Error Correction, Choukroun & Wolf 2023](https://arxiv.org/abs/2301.11930); [Neural decoder for topological codes](https://arxiv.org/abs/1610.04238) | DDECC covers classical linear codes. Deep QEC already trains end-to-end neural decoders for quantum codes, but it does not use diffusion. A diffusion or score-based quantum decoder may still be open; check for newer work before committing. |
| **Mamba vs WaveNet vs attention on raw audio and long-range memory** (16+26) | 1, 6, 8 | Receptive field, speed, NLL/quality, and the point at which synthetic recall tasks break | [SaShiMi, Goel et al. 2022](https://arxiv.org/abs/2202.09729); [Mamba](https://arxiv.org/abs/2312.00752); [Zoology](https://arxiv.org/abs/2312.04927) | Much of this is already covered. Needs a controlled, matched-parameter study. |
| **An EBM that beats AR** on data with global constraints, such as Sudoku or valid graphs (24) | 1, 2 | Constraint-satisfaction rate, sample cost | [Iterative reasoning as energy minimization](https://arxiv.org/abs/2206.15448); [IRED](https://arxiv.org/abs/2406.11179); [SATNet](https://arxiv.org/abs/1905.12149) | Langevin sampling is slow. Prior work already uses energy for reasoning, so the angle has to be the AR comparison. |
| **AR likelihood for packet anomaly and attack detection** (23) | 1 | AUROC on attack traces | [PixelDefend](https://arxiv.org/abs/1710.10766); [Nalisnick et al. 2018](https://arxiv.org/abs/1810.09136) | Likelihood is known to fail on out-of-distribution data. Diffusion also gives likelihoods through the [probability-flow ODE](https://arxiv.org/abs/2011.13456), so we must compare against it fairly. |
| **When does diffusion memorize?** (15): a memorization metric as a function of dataset size | 3 | Fraction of near-copies vs training-set size | [Carlini et al. 2023](https://arxiv.org/abs/2301.13188); [Gu et al. 2023](https://arxiv.org/abs/2310.02664) | Already studied heavily; needs a new setting such as audio or graphs. |
| **AR to diffusion: retrofit a trained WaveNet** (20) | 1, 3, 6 | Quality vs fine-tuning budget, compared with training from scratch | [DiffuLLaMA (AR→diffusion for LMs)](https://arxiv.org/abs/2410.17891) | Has only been done for text. Might not work at all for audio. |
| **EBM as a judge of LLM answers** (6) | 2 | Best-of-N accuracy vs a reward model | [Residual EBMs for text](https://arxiv.org/abs/2004.11714) | Hard to distinguish from an ordinary reward model. |
| **Unlearning, made visible** (3): delete part of the data and probe what the model still "remembers" | 3 | Leakage from the forgotten class, quality on the retained classes | [Erasing Concepts from Diffusion Models](https://arxiv.org/abs/2303.07345) | Small-scale versions are easy, but the novelty is limited. |
| **Diffusion that starts from a learned start point instead of pure noise** (13) | 3 | FID vs number of steps | [SDEdit](https://arxiv.org/abs/2108.01073); [Cold Diffusion](https://arxiv.org/abs/2208.09392) | Close to existing work. |
| **Consistent synthetic logs vs a monitoring system** (9) | 1 | Detection rate of the log anomaly detector | [Loghub](https://arxiv.org/abs/2008.06448) | Narrow topic; the detector baselines need care. |

**Problem, input/output and ethics (Tier 2):**

| Idea | Problem | Input → Output | Ethics |
|---|---|---|---|
| **Diffusion decoder for ECC** | Reliable communication and fault-tolerant quantum computing need decoders that are both accurate and fast. Classical decoders (belief propagation, matching) are either suboptimal or slow. | Noisy received codeword, or the syndrome for quantum codes → estimated codeword or error pattern | None significant: the data is synthetic. |
| **Mamba vs WaveNet vs attention** | Raw audio needs very long contexts (16k samples per second). There is no clear guidance on which architecture gives the best quality and cost at a matched size. | Past audio samples → distribution over the next sample. For recall tasks: token sequence → the recalled token | Low. Audio models can imitate voices, so prefer music or public speech datasets. |
| **EBM vs AR on global constraints** | AR models generate left to right and cannot revise earlier choices, so they often break global constraints. An EBM scores the whole object at once, at the cost of slow sampling. | Puzzle with its given cells → completed grid; or a constraint spec → valid graph | None. |
| **AR likelihood for attack detection** | Signature-based intrusion detection misses new attacks. A model of normal traffic with exact likelihood could flag unseen attacks without labelled attack data. | Packet or flow sequence → log-likelihood, used as an anomaly score | False positives can block legitimate users. Publishing failure cases also teaches evasion. Real traffic raises privacy issues, so use anonymized datasets. |
| **When does diffusion memorize?** | Diffusion models can reproduce training images, which is a privacy and copyright problem. Knowing how much data prevents this guides practice. | Models trained on different dataset sizes, plus their samples → a memorization score per sample | The topic itself is privacy. Use public datasets only, and do not run extraction on models trained on private or copyrighted data. |
| **AR → diffusion retrofit** | Training audio generators from scratch is expensive. Reusing a trained AR model could give faster, parallel sampling cheaply. | Noise, optionally with conditioning → audio clip | Voice-cloning risk if trained on speech; prefer music or public speech. |
| **EBM as LLM judge** | LLMs give several answers of uneven quality. A learned energy over (question, answer) pairs could pick the best one without a human label for each query. | Question + candidate answers → energy per answer → the selected answer | The judge can encode bias and reward answers that are confident but wrong. Relying on automatic judging can hide errors. |
| **Unlearning, made visible** | Data owners can demand removal of their data, for example under the GDPR right to erasure. Retraining is costly, and it is unclear what a model still "remembers" after unlearning. | Trained model + forget set → edited model. Probe: class or prompt → samples and a leakage score | The goal is privacy, but weak unlearning can give a false assurance that data was deleted. Report the leakage honestly. |
| **Learned start point** | Diffusion sampling is slow because it starts from pure noise and needs many steps. A better start point could cut the number of steps. | Optional condition → learned initial latent → sampler → image | Low. |
| **Consistent synthetic logs** | Organizations trust log-based anomaly detectors to catch intrusions. It is untested whether a consistent, generated fake history can fool them. | Log context + target behaviour → a sequence of consistent log lines | **High dual use**: this is an anti-forensics capability. Frame it as red-team evaluation of detectors, use public log datasets, do not release the generator, and report defenses. |

### Tier 2b: safe, but small for a team of 4

| Idea | Lectures | Metric | Data / prior work | Note |
|---|:---:|---|---|---|
| **WaveNet for ECG or seismic signals** (8): generation plus anomaly detection | 1, 6 | NLL, anomaly AUROC | [PTB-XL](https://physionet.org/content/ptb-xl/) ([paper](https://doi.org/10.1038/s41597-020-0495-6)) | Could be combined with the Mamba comparison to make a larger project. |

| Idea | Problem | Input → Output | Ethics |
|---|---|---|---|
| **WaveNet for ECG** | Arrhythmias are rare and labelled ECG data is scarce. A generative model of normal ECG can flag abnormal beats and produce data for augmentation. | ECG history → next-sample distribution, and an anomaly score per beat | Medical data: PTB-XL is de-identified, but synthetic ECG could still leak patient patterns. The model must not be presented as diagnostic, and false negatives matter. |

---

## Tier 3: evaluation unclear even with enough compute

| Idea | Why not (for now) |
|---|---|
| **Long-form structured music** (12): structure from text, kept coherent for minutes | Long-range coherence is hard to measure, and the baselines are large ([MusicGen](https://arxiv.org/abs/2306.05284), [Jukebox](https://arxiv.org/abs/2005.00341)). |
| **Audio "time machine"** (10): restyle a modern recording as 1930s audio with score guidance and no paired data | There is no objective metric. |
| **New instruments from latent space** (4) | Evaluation depends on human ratings, and it is close to [NSynth](https://arxiv.org/abs/1704.01279). |
| **Reverse-time generation** (2): generate the beginning from the end | The causality hypothesis is not sharp. See [Arrows of Time for LLMs](https://arxiv.org/abs/2401.17505). |

| Idea | Problem | Input → Output | Ethics |
|---|---|---|---|
| **Long-form structured music** | Music generators sound good for seconds but lose structure over minutes. | Text description of the structure (intro, build-up, climax) → minutes of audio | Copyright of the training music, and imitation of specific artists' styles. |
| **Audio "time machine"** | Audio style transfer without paired data, such as old and new versions of the same recording. | Modern recording → the same content in a historical style | Could fabricate fake "historical" recordings; copyright of the source recordings. |
| **New instruments** | Sound design is limited to existing timbres. A learned latent space may hold new timbres that can still be played. | Latent point, or a mix of instruments, plus pitch → audio of a note | None significant. |
| **Reverse-time generation** | Do generative models capture causal structure, or only statistics? | Ending of a text or a piece of music → a generated beginning | Low. |

---

## Next step

1. Form the team. Confirm the HPC GPU type, quota and walltime.
2. Pick 1–2 ideas from Tier 1 or 2.
3. Write a one-page proposal: research question, data, baseline, metrics, team split, milestones, compute budget.

---

## AI usage

Claude (Anthropic) helped organize the brainstorm into this triage and find the prior work. arXiv and DOI links were checked against arXiv and Crossref. The remaining links (datasets, RFC) were checked to resolve.
