// Draws the shared fabric map as SVG.
(function () {
  const LABELS = { OK: "OK", MISWIRED: "Miswired", ONE_WAY: "One-way", HIGH_ERRORS: "High errors", LINK_DOWN: "Link down", PEER_SILENT: "Peer silent" };
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  function linkState(l, o) {
    const ka = l.a.s + ":" + l.a.p, kb = l.b.s + ":" + l.b.p;
    const la = o.latest[ka], lb = o.latest[kb];
    if (o.confirmed.has(ka) || o.confirmed.has(kb)) return "confirmed";
    if (o.truth && (o.truth.has(ka) || o.truth.has(kb))) return "hidden";
    if ((la && la !== "OK") || (lb && lb !== "OK")) return "suspect";
    if (la === "OK" && lb === "OK") return "verified";
    if (la === "OK" || lb === "OK") return "half";
    return "unknown";
  }

  function render(svg, o) {
    const T = window.MH_TOPO, P = T.pos;
    let h = "";
    const order = { unknown: 0, half: 1, verified: 2, hidden: 3, suspect: 4, confirmed: 5 };
    const items = T.links.map(l => ({ l, st: linkState(l, o) })).sort((x, y) => order[x.st] - order[y.st]);
    items.forEach(({ l, st }) => {
      const off = l.k === 1 ? -4 : 4;
      const [x1, y1] = P[l.a.s], [x2, y2] = P[l.b.s];
      const ya = y1 + 15, yb = y2 - (l.tier === "tor" ? 11 : 15);
      const la = o.latest[l.a.s + ":" + l.a.p], lb = o.latest[l.b.s + ":" + l.b.p];
      const tip = l.a.s + " " + l.a.p + " ↔ " + l.b.s + " " + l.b.p + "\n" + l.a.s + " says: " + (la ? LABELS[la] : "no report") + "\n" + l.b.s + " says: " + (lb ? LABELS[lb] : "no report");
      h += '<line class="lk lk-' + st + '" x1="' + (x1 + off) + '" y1="' + ya + '" x2="' + (x2 + off) + '" y2="' + yb + '"><title>' + esc(tip) + "</title></line>";
    });
    T.ALL.forEach(s => {
      const [x, y] = P[s], w = s.startsWith("T") ? 58 : 70, hh = s.startsWith("T") ? 22 : 30;
      const cls = ["nd"];
      if (o.reported && o.reported.has(s)) cls.push("nd-reported");
      if (o.me === s) cls.push("nd-me");
      h += '<g class="' + cls.join(" ") + '"><rect x="' + (x - w / 2) + '" y="' + (y - hh / 2) + '" width="' + w + '" height="' + hh + '" rx="5"/>' +
        '<text x="' + x + '" y="' + (y + 4) + '" text-anchor="middle">' + s + "</text>" +
        (o.me === s ? '<text class="you" x="' + x + '" y="' + (y + (s.startsWith("T") ? 28 : 33)) + '" text-anchor="middle">YOU</text>' : "") + "</g>";
    });
    h += '<text class="blk" x="260" y="392" text-anchor="middle">Block A</text><text class="blk" x="700" y="392" text-anchor="middle">Block B</text>';
    svg.innerHTML = h;
  }

  function fromStatus(st) {
    const latest = {}, reported = new Set(), confirmed = new Set();
    (st.ports || []).forEach(r => { latest[r.s + ":" + r.p] = r.l; reported.add(r.s); });
    (st.faults || []).forEach(f => { if (f.confirmed) (f.ports || []).forEach(p => confirmed.add(p.s + ":" + p.p)); });
    return { latest, reported, confirmed };
  }

  window.MH_MAP = { render, fromStatus, LABELS, esc };
})();
