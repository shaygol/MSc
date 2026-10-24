"""Live demo for the RNG paper discussion: fat-tree vs. flat random graph.

Usage:
  python demo.py topology --k 8          # Part A: fat-tree(k) vs. a flat expander of ToRs
  python demo.py routing --n 2000 --d 32  # Part B: ECMP vs. spraying vs. Spraypoint
  python demo.py all --k 8

Part A reuses build_fattree() from ex1 and compares it against a random
d-regular graph that has the same ToRs and servers but no aggregation or core
layer (each ToR keeps k/2 ports for servers and k/2 for the mesh, like an
edge switch in the fat-tree).

Part B rebuilds the core idea of RNG section 5 (Bernardi et al. 2026) on a
random regular graph: count edge-disjoint paths (= s-t min cut, Menger)
in the forwarding DAG that each routing scheme produces.
"""

import argparse
import math
import random
import sys
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ex1"))
from fattree import build_fattree  # noqa: E402


# ---------------------------------------------------------------- Part A


def fattree_switch_graph(k):
    """Fat-tree without hosts; returns the switch graph and the ToR (edge) list."""
    G = build_fattree(k)
    hosts = [v for v, layer in G.nodes(data="layer") if layer == "host"]
    G.remove_nodes_from(hosts)
    tors = [v for v, layer in G.nodes(data="layer") if layer == "edge"]
    return G, tors, len(hosts)


def flat_expander(n, d, seed):
    """Random d-regular graph on n ToRs (the Jellyfish/RNG abstraction)."""
    G = nx.random_regular_graph(d, n, seed=seed)
    while not nx.is_connected(G):
        seed += 1
        G = nx.random_regular_graph(d, n, seed=seed)
    return G


def tor_hop_histogram(G, tors):
    tor_set = set(tors)
    hist = {}
    for s in tors:
        for t, dist in nx.single_source_shortest_path_length(G, s).items():
            if t in tor_set and t != s:
                hist[dist] = hist.get(dist, 0) + 1
    total = sum(hist.values())
    return {h: c / total for h, c in sorted(hist.items())}


def mean_disjoint_paths(G, tors, pairs, rng):
    """Average number of edge-disjoint paths between random ToR pairs."""
    vals = []
    for _ in range(pairs):
        s, t = rng.sample(tors, 2)
        vals.append(nx.edge_connectivity(G, s, t))
    return sum(vals) / len(vals), min(vals)


def spectral_gap(G):
    """1 - lambda2/lambda1 of the adjacency matrix; larger = better expander."""
    import numpy as np

    eig = sorted(np.linalg.eigvalsh(nx.to_numpy_array(G)), reverse=True)
    return 1 - eig[1] / eig[0]


def uniform_oversub_bound(G, tors, servers_per_tor):
    """Lower bound on oversubscription under all-to-all ToR traffic.

    Total capacity argument (RNG Lemma G.2): each unit of ToR-to-ToR traffic
    uses `mean hops` link units and the fabric has 2|E| directed link units,
    so a ToR can send at most 2|E| / (n * mean hops). Comparing that to the
    ToR's server capacity gives the oversubscription ratio (>= 1).
    """
    hist = tor_hop_histogram(G, tors)
    mean_hops = sum(h * f for h, f in hist.items())
    per_tor = 2 * G.number_of_edges() / (len(tors) * mean_hops)
    return max(1.0, servers_per_tor / per_tor)


def matched_expander(k, servers, target, seed):
    """Fewest ToRs (k ports each) whose flat graph meets the target oversub bound."""
    for s in range(k - 1, 0, -1):  # more servers per ToR = fewer ToRs
        d = k - s
        n = math.ceil(servers / s)
        n += (n * d) % 2  # n * d must be even for a d-regular graph
        if d < 3 or d >= n:  # d < 3 is never a connected expander
            continue
        G = flat_expander(n, d, seed)
        if uniform_oversub_bound(G, list(G), s) <= target + 1e-9:
            return G, s, d
    return None, None, None


def describe(name, G, tors, servers_per_tor, rng, pairs):
    hist = tor_hop_histogram(G, tors)
    dp, dp_min = mean_disjoint_paths(G, tors, pairs, rng)
    return {
        "name": name,
        "switches": G.number_of_nodes(),
        "links": G.number_of_edges(),
        "hops": sum(h * f for h, f in hist.items()),
        "max hops": max(hist),
        "disjoint": f"{dp:.1f} (min {dp_min})",
        "gap": f"{spectral_gap(G):.3f}",
        "oversub": f"{uniform_oversub_bound(G, tors, servers_per_tor):.2f}:1",
    }


def run_topology(args):
    rng = random.Random(args.seed)
    k = args.k
    ft, ft_tors, servers = fattree_switch_graph(k)
    half = k // 2

    # Naive flat graph: delete the agg and core layers, keep the same ToRs.
    naive = flat_expander(len(ft_tors), half, args.seed)
    # Cost-matched flat graph: fewest ToRs that are as good as the fat-tree.
    ft_oversub = uniform_oversub_bound(ft, ft_tors, half)
    matched, s, d = matched_expander(k, servers, ft_oversub, args.seed)

    cols = [describe(f"fat-tree k={k}", ft, ft_tors, half, rng, args.pairs),
            describe(f"flat, same ToRs (d={half})", naive, list(naive), half, rng, args.pairs)]
    if matched is not None:
        cols.append(describe(f"flat, matched (d={d})", matched, list(matched), s,
                             rng, args.pairs))

    print(f"== Part A: {servers} servers, {k}-port switches ==")
    rows = [("switches", "switches"), ("switch-switch links", "links"),
            ("mean ToR-ToR hops", "hops"), ("max ToR-ToR hops", "max hops"),
            ("edge-disjoint ToR paths", "disjoint"), ("spectral gap", "gap"),
            ("all-to-all oversub (bound)", "oversub")]
    width = 24
    print(f"{'':28}" + "".join(f"{c['name']:>{width}}" for c in cols))
    for label, key in rows:
        cells = [f"{c[key]:.2f}" if isinstance(c[key], float) else str(c[key]) for c in cols]
        print(f"{label:28}" + "".join(f"{x:>{width}}" for x in cells))
    if matched is not None:
        saving = 1 - matched.number_of_nodes() / ft.number_of_nodes()
        print(f"\nMatched flat graph: {s} servers + {d} uplinks per ToR, "
              f"{saving:.0%} fewer switches for the same bound.")
    print("Note: the oversub row is a capacity lower bound (ideal shortest-path routing),"
          " not a simulation.")


# ---------------------------------------------------------------- Part B


def ecmp_dag(G, t):
    """Shortest-path forwarding toward t: u -> v if dist(v) = dist(u) - 1."""
    dist = nx.single_source_shortest_path_length(G, t)
    D = nx.DiGraph()
    for u, v in G.edges:
        if dist[v] == dist[u] - 1:
            D.add_edge(u, v)
        elif dist[u] == dist[v] - 1:
            D.add_edge(v, u)
    return D


def spraypoint_dag(G, t, p, h, rng):
    """Pointing graph of Spraypoint with one waypoint level (l = 1).

    WP0 = neighbors of t, WP1 = p random neighbors of each WP0 node,
    IR = neighbors of WP1 not seen yet, OR = everything else.
    """
    wp0 = set(G[t])
    wp1 = set()
    for v in sorted(wp0):
        cand = [w for w in G[v] if w != t and w not in wp0 and w not in wp1]
        wp1.update(rng.sample(cand, min(p, len(cand))))
    seen = {t} | wp0 | wp1
    ir = {w for v in wp1 for w in G[v]} - seen
    out = set(G) - seen - ir

    D = nx.DiGraph()
    for v in wp0:
        D.add_edge(v, t)

    def point(u, targets):
        nbrs = [w for w in G[u] if w in targets]
        for w in rng.sample(nbrs, min(h, len(nbrs))):
            D.add_edge(u, w)

    for u in wp1:
        point(u, wp0)
    for u in ir:
        point(u, wp1)
    for u in out:
        nbrs_ir = [w for w in G[u] if w in ir]
        if nbrs_ir:
            point(u, ir)
        else:  # rare: fall back to shortest paths toward IR
            dist = nx.multi_source_dijkstra_path_length(G, ir)
            best = min(dist[w] for w in G[u])
            point(u, {w for w in G[u] if dist[w] == best})
    return D, {"WP0": len(wp0), "WP1": len(wp1), "IR": len(ir), "OR": len(out)}


def disjoint_paths(dag, G, s, t, spray):
    """s-t min cut of the forwarding graph; with spray, s may use every neighbor."""
    D = dag.copy()
    if spray:
        # Spraying happens only at the source, so model it as a separate node.
        src = ("spray", s)
        for w in G[s]:
            D.add_edge(src, w)
        s = src
    if s not in D:
        return 0
    nx.set_edge_attributes(D, 1, "capacity")
    return nx.maximum_flow_value(D, s, t)


def run_routing(args):
    rng = random.Random(args.seed)
    n, d, p, h = args.n, args.d or 32, args.p, args.h
    G = flat_expander(n, d, args.seed)
    print(f"\n== Part B: routing on a random {d}-regular graph with n={n} (p={p}, h={h}) ==")
    print(f"model 7.1 (s not adjacent to t): d(1 - e^-h) = {d * (1 - math.exp(-h)):.1f} of max {d}")

    nodes = list(G)
    results = {"far": {"ECMP": [], "spray-only": [], "Spraypoint": []},
               "adjacent": {"ECMP": [], "spray-only": [], "Spraypoint": []}}
    levels = None
    for _ in range(args.pairs):
        t = rng.choice(nodes)
        ecmp = ecmp_dag(G, t)
        sp, levels = spraypoint_dag(G, t, p, h, rng)
        far = rng.choice([v for v in nodes if v != t and v not in G[t]])
        adj = rng.choice(list(G[t]))
        for kind, s in (("far", far), ("adjacent", adj)):
            results[kind]["ECMP"].append(disjoint_paths(ecmp, G, s, t, spray=False))
            results[kind]["spray-only"].append(disjoint_paths(ecmp, G, s, t, spray=True))
            results[kind]["Spraypoint"].append(disjoint_paths(sp, G, s, t, spray=True))

    print(f"Spraypoint level sizes for one destination: {levels}")
    print(f"\nEdge-disjoint paths per (s, t) pair, mean [min] over {args.pairs} pairs:")
    print(f"{'source':>10}  {'ECMP':>12}  {'spray-only':>12}  {'Spraypoint':>12}")
    for kind in ("far", "adjacent"):
        cells = []
        for scheme in ("ECMP", "spray-only", "Spraypoint"):
            vals = results[kind][scheme]
            cells.append(f"{sum(vals) / len(vals):6.1f} [{min(vals):>2}]")
        print(f"{kind:>10}  " + "  ".join(f"{c:>12}" for c in cells))
    print("\nTakeaways: ECMP finds few paths in an expander; spraying fixes far pairs but "
          "collapses onto the s->t link for adjacent pairs; waypoints fix that.")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("part", choices=["topology", "routing", "all"])
    parser.add_argument("--k", type=int, default=8, help="fat-tree port count (Part A)")
    parser.add_argument("--n", type=int, default=2000, help="routers in the random graph (Part B)")
    parser.add_argument("--d", type=int, default=None,
                        help="router uplinks (default k/2 in Part A, 32 in Part B)")
    parser.add_argument("--p", type=int, default=4, help="Spraypoint waypoints per node")
    parser.add_argument("--h", type=int, default=2, help="Spraypoint next hops")
    parser.add_argument("--pairs", type=int, default=30, help="sampled (s, t) pairs")
    parser.add_argument("--seed", type=int, default=1)
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    if args.part in ("topology", "all"):
        run_topology(args)
    if args.part in ("routing", "all"):
        if args.part == "all":
            args.d = None
        run_routing(args)


if __name__ == "__main__":
    main()
