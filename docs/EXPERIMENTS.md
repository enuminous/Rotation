# Rotation experimental program — freeze → predict → test → ablate → reproduce

**All proposed experiments in this document are UNRUN.** This is a protocol-design record, not a preregistration with independent custody and not a result.

## Tracks

### ROT-001: mathematics, normalization and degeneracy

**Goal:** Validate the mathematical translation between angular speed ω, Euclidean curl v and the scalar ME-056 parameter.

**What to compare:** Source Lean declarations against exact symbolic math and a separately written 2-D/3-D numerical toy. Independent implementation avoids shared bugs.

**Controls:** zero angular speed; ω versus -ω; gradient-only field with curl zero; (k,ω)=(0,0) and (1,1) at same a, A.

**PASS:** all identities match their explicit assumptions; no inference of unique cosmic parameter from a scalar H² fit. **FAIL:** counterexample to a claimed algebraic identity. This is a **mathematical** test, not an observational test.

### ROT-002: phase topology versus ordinary vorticity

**Goal:** Determine exactly which forms of scalar “rotation” survive changes of gauge, phase patch and field zero.

**Models:** ordinary smooth real scalar; ordinary complex scalar; complex scalar plus U(1) connection; vector flow.

**Controls:** ψ with n=0; ψ with n=±1 and ψ=0 at core; uniform time-only phase; pure-gauge vector potential; irrotational velocity u=∇φ.

**Primary quantities:** integer winding on nonzero loop, gauge-invariant circulation under a fully specified coupling, curl u under sufficient regularity.

**PASS:** mathematical relationships and exclusions verified; **not** evidence that all sectors share a cosmic angular velocity.

### ROT-003: cosmic vorticity versus alternatives — PROTOCOL PROPOSAL ONLY

**Target hypotheses (must be defined physically first):**
- H0: standard homogeneous-isotropic ΛCDM/FLRW, with modeled systematics.
- H1: a specified GR-consistent rotating congruence/metric with nonzero present-day invariant vorticity.
- H2: conventional Bianchi shear/rotation templates and separately specified new-physics birefringence and selection-effect alternatives.

**Model prerequisities:** explicit Einstein-compatible metric, matter content, stress-energy conservation, causal regularity domain, dimensions and absolute units for rotation parameter; observable transfer functions (CMB TT/TE/EE/BB or other physically justified data).

**Pre-register before touching holdout:** likelihood, priors, sky mask, multipole range, estimator, calibration uncertainty, nuisance parameters, axis-look-elsewhere treatment, observation selection, model comparison penalty and numerical convergence.

**Discriminants:** predicted angular/redshift pattern, distinct E/B mode effects, sign/handedness where identifiable, parallax/redshift coupling, and any extra cross-field effects that standard models cannot mimic.

**Acceptance (proposed, not frozen):** replicate on a held-out independent data split or dataset; after multiplicity and systematics, material improvement against both H0 and strongest conventional H2; no violation of existing Planck-like upper limits applicable to H1. Quantitative thresholds must be selected with a data/statistics custodian beforehand.

**Null:** H1 amplitude consistent with zero; Bayes factor/unseen likelihood does not favor H1; axis unstable under sky mask, mirrored classification or independent calibration.

**Stop:** failure to derive self-consistent equations, lack of an identifiable parameter, benchmark leaks, significant contradictory held-out data, or irreproducibility.

## Evidence handling

1. Keep original raw data and independent checksums, with source, retrieval dates, author licenses and machine environment.
2. Separate exploratory data from frozen test data; label each plot accordingly.
3. Record all evaluated seeds, models and rejected attempts, including negative outcomes.
4. Independent reviewers run source-pinned code; reported numbers include uncertainty intervals and nulls.
5. New math needs exact theorem statements; new physics needs predictions and observational discrimination. Never equate the two.

## Initial acceptance gates

| Gate | Complete? | Required artifact |
|---|---|---|
| Rotation observable physically defined | NO | Metric / congruence / units / gauge behavior |
| Existing Planck consistency | NO | Model-specific fit with priors and bounds |
| Independent astrometric or polarization test | NO | Frozen protocol and custodial holdout |
| EFMW-unique prediction | NO | Equations + conventional comparator |
| Independent source replay | NO | Public logs and audit |
| Public negative-result reporting | POLICY | Preserve all FAIL/UNRESOLVED outcomes |

See [CMB constraints](COSMOLOGY.md) and [open questions](OPEN_QUESTIONS.md).
