# Rotation experimental program — freeze → predict → test → ablate → reproduce

**All proposed experiments in this document are UNRUN.** This is a protocol-design record, not a preregistration with independent custody and not a result.

## Tracks

### ROT-005: expanding, rotating, causal Einstein geometry — completed bounded symbolic check

[Report and exact outputs](../research/ROT-005_KOROTKII_OBUKHOV_BRIDGE.md). A frozen member of the published Korotkii–Obukhov metric family has H>0, omega²>0, shear=0, stable causality, and an exact Einstein tensor with a conserved effective source obeying the weak energy condition. The source T=G/kappa is defined **after** choosing the geometry; no field action is derived. With a stated geometric k/Omega mapping the proposed ME-056 gives a nonzero H² mismatch; retuning the scalar curvature parameter erases it and leaves rotation unidentifiable.

### ROT-006: independent physical source and observable — proposed, UNRUN

Freeze a matter Lagrangian or independently specified stress tensor **before** choosing/tuning cosmological metric coefficients; derive T_ab, then solve Einstein equations and conservation alongside nonzero expansion/vorticity. Check energy conditions, hyperbolicity, stability and a covariant no-rotation limit. Require one new measurable prediction that cannot be absorbed by reassigning curvature or ordinary fluid properties. Preserve all FAIL and UNRESOLVED results; only then proceed to blinded astronomical data.

### ROT-004: covariant GR consistency — bounded check completed

The [ROT-004 report](../research/ROT-004_COVARIANT_BRIDGE.md) compares the sourced 1+3 Einstein scalar constraint with ME-056 and independently computes the Gödel exact metric with pinned SymPy. The exact metric rotates and does not expand. **PASS:** precise GR control; **FAIL:** the unqualified positive-additive interpretation; **UNRESOLVED:** any new expanding EFMW metric. No astronomical dataset was fitted.

### ROT-005: expanding rotating metric — proposed, not run

Select a single causally admissible Einstein spacetime with expanding, physically rotating matter observers (or a justified metric ansatz). Check Einstein tensor, conservation, actual kinematics, projected rest curvature, dimensions, and the FLRW limit. Compare the **derived** scalar constraint with canonical ME-056. If it differs, preserve the historical original equation and propose a separately versioned correction. Do not fit observational data without a distinct falsifiable signal.

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
