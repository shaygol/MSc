# RNG paper discussion (Unit 3: architecture)

Material for leading the class discussion of *RNG: Flat Datacenter Networks at Scale* (Bernardi et al., AWS, 2026).

## Live demo

`demo.py` compares the fat-tree generator from [`ex1`](../ex1/fattree.py) with a flat random regular graph (the abstraction behind Jellyfish and RNG).

```
pip install -r requirements.txt
python demo.py topology --k 8      # Part A, < 10 s
python demo.py routing             # Part B, n=2000 d=32, ~15 s
```

**Part A (topology and cost).** Same servers, same k-port switches. Three columns: the fat-tree, a "naive" flat graph that keeps the same ToRs and deletes the upper tiers, and a "matched" flat graph with the fewest ToRs whose all-to-all capacity bound equals the fat-tree's. The naive graph looks 60% cheaper but is about 2.5:1 oversubscribed because relayed traffic eats ToR uplinks (the catch in RNG section 2). The matched graph is about 20% cheaper and has shorter paths and more disjoint paths. The oversubscription row is a total-capacity lower bound (RNG Lemma G.2), not an LP or a simulation, so it is optimistic for both topologies.

**Part B (routing).** On a random d-regular graph, counts edge-disjoint paths (s-t min cut, Menger) in the forwarding graph of three schemes: ECMP over shortest paths, spray-then-shortest-path, and Spraypoint with one waypoint level (parameters p, h). Results are split into "far" sources and sources adjacent to the destination, which reproduces the paper's argument for waypoints: spraying alone collapses onto the s-t link for adjacent pairs when n >> d^2. The model line prints RNG Model 7.1, d(1 - e^-h).

Sample run (seed 1):

```
model 7.1 (s not adjacent to t): d(1 - e^-h) = 27.7 of max 32
    source          ECMP    spray-only    Spraypoint
       far      8.5 [ 1]     30.5 [28]     27.8 [21]
  adjacent      1.0 [ 1]     11.9 [ 5]     26.8 [20]
```

The demo was written with Claude (Anthropic) as an AI assistant.
