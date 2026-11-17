# Rotation — a cross-field evidence atlas

**Monolithic Research • enuminous/Rotation • v0.1.0 • 2026-11-17**  
**Status: OPEN RESEARCH ATLAS — NOT A DETECTION OF GLOBAL COSMIC ROTATION**

> **Question:** Rotation is found across mechanics, fluids, phases, spinors, electromagnetic polarization, rotating spacetimes, and astronomical objects. Which of those observations or mathematical structures, if any, imply an invariant, measurable rotation of the universe as a whole?

This repository gathers **positive evidence, rigorous mathematical identities, model-specific observational constraints, counterexamples, open mathematical obligations, and EFMW conjectures** in one inspectable place. The word *universal* is the research question, **not an established empirical conclusion**.

## Start here

1. [Evidence register](data/evidence.json) and [source bibliography](data/sources.json) — machine-readable, with honest evidence classes.
2. [What counts as rotation?](docs/WHAT_ROTATION_MEANS.md) — five inequivalent senses of the word.
3. [Scalar and phase fields](docs/SCALAR_FIELDS.md) — real scalars, complex phases, winding, zero sets, and gauge caveats.
4. [Rotation in every field type](docs/FIELD_ATLAS.md) — scalar, vector, spinor, tensor, connection, fluid, cosmological and computational systems.
5. [Geometric algebra / Clifford rotors](docs/CLIFFORDS.md) — the geometry, without equating representational rotors with cosmic measurement.
6. [Cosmic rotation: evidence **and** null results](docs/COSMOLOGY.md) — strong observational limitations and disputed hints.
7. [Monolithic 102 crosswalk](docs/EFMW_CROSSWALK.md) — precise ME-016–021, ME-055–056, and ME-077–082 links.
8. [BSA-R / Topher research bridge](docs/BSAR_BRIDGE.md) — shared vorticity mathematics, distinct open problems.
9. [Test program](docs/EXPERIMENTS.md) and [open obligations](docs/OPEN_QUESTIONS.md).
10. [Run the small mathematical laboratory](#reproduce-the-toy-laboratory).
11. Open [the interactive Rotation Lab and evidence explorer](index.html) using a local HTTP server or GitHub Pages.

## Interactive Rotation Lab (GitHub Pages)

The root [`index.html`](index.html), [`assets/rotation-lab.js`](assets/rotation-lab.js), and [`assets/rotation-lab.css`](assets/rotation-lab.css) form a **dependency-free browser laboratory**. Choose among six instrument modes:

| Mode | Adjustable parameters | Live mathematical outputs |
|---|---|---|
| **Vector / SO(3)** | Angular speed, circle radius | Curl = 2ω, circulation and Stokes flux |
| **Complex scalar / U(1)** | Integer winding, time-phase rate, nodal-core size | Phase winding, defect and scalar-domain caveats |
| **Real scalar null** | Quadratic x/y curvatures, offset | An explicitly curl-free gradient counterexample |
| **Clifford / Spin(3)** | Rotor start angle and speed | Half-angle rotor, 2π sign reversal, 4π restoration |
| **Vorticity & strain** | Angular speed, trace-free strain, tracer count | Divergence-free velocity, tracer motion and curl |
| **Cosmic degeneracy / ME-056** | Curvature, rotation, scale factor, expansion base | Two distinct parameter sets with identical H²(a) |

**Controls:** Play/pause, reset, step, speed, parameter sliders, 1–6 keyboard mode switching, and CSV export of analytic **toy** values. The original evidence browser remains available with search, status/domain filters, and links to the 33 source records.

Run locally:

```bash
python -m http.server 8000
# open http://localhost:8000/
```

To host it, enable GitHub Pages manually (deploy from `main` / root). The page uses relative asset/data paths, so no CDN is required. **It is not a cosmological data fit, a Navier–Stokes solver, or evidence of universal rotation.**

The [browser smoke test](tests/smoke_rotation_lab.cjs) exercises six modes, controls, CSV export and evidence filtering with a simulated DOM/canvas. GitHub Actions additionally checks JavaScript syntax and Python unit tests. A green CI run does **not** certify pixel-perfect browser rendering or physical conclusions.

## ROT-004 — Covariant GR bridge: completed bounded audit

[Full ROT-004 report](research/ROT-004_COVARIANT_BRIDGE.md) · [Exact Gödel metric control](research/ROT-004_GODEL_CONTROL.md)

The standard 1+3 Einstein scalar constraint includes shear, physical vorticity and projected rest-space curvature. An independently positive universal `Omega_U^2/a^2` term cannot be inferred from it without extra assumptions.

A reproducible SymPy computation checks the historical Gödel exact solution: real physical rotation and **zero expansion**. This is a counterexample to `rotation implies expansion`, not a cosmological detection or a disproof of all possible EFMW models. The canonical Monolithic 102 equations remain unchanged.

Next research gate **ROT-005**: select a concrete expanding rotating spacetime metric, calculate Einstein tensor and physical vorticity, and test whether ME-056 can actually be derived.

## ROT-005 — Expanding and rotating Einstein geometry

**Published:** [ROT-005 exact-metric report](research/ROT-005_KOROTKII_OBUKHOV_BRIDGE.md) · [SymPy tensor reproducibility](research/rot005_ko_sympy.py).

The published Korotkii–Obukhov family supplies a **specific expanding, rotating, stably causal metric**. For a frozen illustrative member, our exact Einstein-tensor calculation verifies expansion and vorticity, zero shear, global causal time, the Einstein 1+3 Gauss and Raychaudhuri identities, and a **strict weak-energy-condition bound** on a defined effective imperfect source. This source is *reconstructed from the metric*, not a new microphysical EFMW action or evidence of the observed universe.

**ME-056 comparison:** Under the explicitly chosen identification of its curvature and rotation with the geometric invariants, ME-056 has an exact nonzero H² mismatch; retuning its curvature parameter removes the mismatch without determining cosmic rotation. **Next (ROT-006):** independently specify a physical matter action, derive its stress tensor and test for a distinguishable prediction. The canonical 102 equations remain unchanged.

## Critical separation of claims

| Question | Status today | Evidence boundary |
|---|---|---|
| Do local fluids and superfluids rotate? | **Yes; observed** | Does **not** entail rotation of every field or of spacetime globally |
| Are phase winding, angular momentum and spinorial double covering real mathematical structures? | **Yes** | Representations are different physical observables |
| Is local relativistic frame dragging observed? | **Yes** | Earth's frame dragging is not universal rotation |
| Does a scalar field necessarily rotate? | **No** | A real scalar has no intrinsic angular direction; a complex phase *may* wind |
| Is a spinning astrophysical object evidence that all of spacetime rotates? | **No** | Object spin and cosmological vorticity are separate |
| Has global Bianchi-type cosmic rotation been detected? | **No accepted detection** | Planck's physical Bianchi VIIh analysis found no evidence and a tight **model-specific** upper limit |
| Does ME-056 derive a rotating metric from GR? | **Not yet** | The repository's equation is a stipulated scalar extension, with curvature/rotation degeneracy |
| Is the same rotational generator shared by *all* fields? | **Open hypothesis** | Requires specified dynamics, cross-sector couplings, new predictions, and independent data |

### The strongest present counterweight to global rotation

The Planck 2015 geometry/topology analysis of physically coupled **Bianchi VIIh** models found no evidence for that cosmology and reported **(ω/H)₀ < 7.6 × 10⁻¹⁰ (95% confidence)**. This is **not** a universal limit on every imaginable spacetime or every definition of rotation. [Planck Collaboration, *A&A* (2016), DOI 10.1051/0004-6361/201525829](https://doi.org/10.1051/0004-6361/201525829).

By contrast, laboratory quantized vortices in Bose–Einstein condensates are real observations ([Madison et al. 2000](https://doi.org/10.1103/PhysRevLett.84.806)), as is local frame dragging ([Everitt et al. 2011](https://doi.org/10.1103/PhysRevLett.106.221101)). Neither supports the extra *universal* inference without a connecting model and prediction.

The 2025 JADES galaxy-handedness asymmetry report is included as a **reported, contested observational pattern**, not a verified cosmological rotation detection: [Shamir 2025](https://doi.org/10.1093/mnras/staf292). Survey selection, handedness classification, sky geometry, axis and redshift dependencies, and independent replication must be addressed before inference.

## Why the scalar field matters

ME-016 writes ψ = ρ exp(iθ). In complex scalar fields the phase θ can wind around a zero of ψ, with integer winding number

n = (1 / 2π) ∮ dθ.

But **a smooth single-valued real scalar φ has curl(grad φ) = 0** on its regular domain; a constant scalar is an immediate nonrotating counterexample. A local phase gradient is not itself proof of rotating matter or an angular velocity for the whole universe. In a gauge theory, physical circulation requires a gauge-invariant combination.

See [scalar field analysis](docs/SCALAR_FIELDS.md) and [code](rotation/lab.py).

## Canonical EFMW / Monolithic bridges

- [ME-016](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/016.md) and [ME-018–021](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/018.md): phase-amplitude representation, current, conservation, Madelung decomposition.
- [ME-055](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/055.md): Ω_U = curl v_U, a **definition/model construct**.
- [ME-056](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/056.md): H² = (8πG/3)ρ + Λ/3 − k/a² + Ω_U²/a², a **working hypothesis**, not an Einstein-equation derivation.
- [RotationKinematics.lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/RotationKinematics.lean) and [RotatingCosmology.lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/RotatingCosmology.lean): conditional formal algebra and explicit identifiability limitations.
- [Vorticity.lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/Vorticity.lean), [Fluids.lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/Fluids.lean) and [Madelung.lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/Madelung.lean): standard differential identities with scoped assumptions.

**Normalization caution:** For rigid-body angular velocity ω, curl v = 2ω. Using the scalar angular-speed parameter rather than the **magnitude of vorticity** in ME-056 changes a term by a factor of four. The source Lean analysis chooses a normalization explicitly rather than deriving one from cosmology.

## Reproduce the toy laboratory

No third-party Python packages required (Python 3.10+):

```bash
python -m unittest discover -s tests -v
python -m rotation.lab
python scripts/validate_evidence.py
python -m http.server 8000
# then open http://localhost:8000
```

Tests illustrate kinematics, phase winding, spinor sign change, and parameter degeneracy. **They are not evidence of cosmic rotation, Lean proof replay, or astrophysical data fitting.**

## Evidence standards and collaboration

- Every entry in [data/evidence.json](data/evidence.json) identifies the **domain, epistemic status, claim, sources, limitation, and bearing on the cosmic hypothesis**.
- Link to primary sources where possible. A preprint, mathematical theorem, simulation, and independent observation are not interchangeable.
- Do **not** elevate data fitted after seeing outcomes into a preregistered prediction.
- [Protocol](docs/EXPERIMENTS.md) requires a named metric, competing models, systematic errors, sealed holdouts, a null model, and stop criteria.
- [Outside review](docs/OPEN_QUESTIONS.md) is required before declaring a novel universal law.
- Proposals, objections, null results, and corrections are welcome. This repo does **not** imply that Christopher Duguay/Topher or other external researchers endorse EFMW.

**Author/curator:** Matthew Chenoweth Wright — Monolithic LLC. Mathematical and research drafting assistance: OpenAI GPT-6. References to external code or papers preserve their own authorship.

## License

New original code: MIT (see [LICENSE](LICENSE)). New original documentation and authored metadata: CC BY 4.0. Linked third-party research, code, data and figures retain their own licenses; they are **not** imported or relicensed by this repository.
