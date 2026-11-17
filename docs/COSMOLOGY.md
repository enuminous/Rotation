# Cosmological rotation — evidence, caveats, and hard nulls

**Question:** Is there a covariant nonzero large-scale vorticity field of cosmological matter observers that the data require, rather than merely permit?

## Measured local rotational physics is not a global detection

- Gravity Probe B measured Earth's local frame dragging; its frame-dragging drift was **−37.2 ± 7.2 mas/year**, compared with GR prediction **−39.2 mas/year** in the published experiment. [Everitt et al. 2011](https://doi.org/10.1103/PhysRevLett.106.221101).
- LIGO's GW150914 data support a spinning final black-hole remnant within waveform modeling. Component spin in that initial event was poorly determined. [GWOSC](https://gwosc.org/events/GW150914/) and [LIGO summary](https://ligo.org/science-summaries/GW150914/).
- These observations validate rotation within GR, not nonzero rotation of the **background universe**.

## Planck constraints on Bianchi VIIh

[Planck 2015 results XVIII](https://doi.org/10.1051/0004-6361/201525829) tested anisotropic Bianchi VIIh geometry. Temperature data in a **decoupled/unphysical** template can favor a Bianchi-like contribution, but its implied background parameters conflict with the standard cosmology; the corresponding polarization template is inconsistent with the physical expectation. In the self-consistently fitted physical Bianchi VIIh model, Planck reported **no evidence** for rotation and a present-day bound:

```text
(ω/H)₀ < 7.6 × 10⁻¹⁰    (95% confidence, Bianchi VIIh model family)
```

It is inappropriate either to call the decoupled fit a global rotation discovery **or** to apply this upper bound automatically to every possible rotating metric. Later or different cosmologies require their own likelihoods.

## Galaxy handedness: interesting but not a cosmic-vorticity measurement

[Shamir, MNRAS 2025](https://doi.org/10.1093/mnras/staf292) reports an imbalance in apparent spin handedness of JADES galaxies. A reported projected-count asymmetry depends on direction-classification methods, image parity, field geometry, resolution/redshift selection, optical and observer effects, and whether blind independent analysts recover the pattern. The presence of an asymmetry in *one survey or method* is not the same as detecting an invariant cosmological vorticity 2-form.

A decisive program must predefine the selected sky areas, matched artificial mirror images, magnitude/morphology cuts, axis search penalties, classifier blindness, and holdout sky patches.

## Cosmic birefringence is a different rotation

[LONAPPAN et al. Phys Rev D 2025](https://doi.org/10.1103/yxmh-rh9z) constrain **anisotropic cosmic birefringence**, a polarization angle phenomenon. Its amplitude is consistent with zero within approximately 2σ in that analysis. Even an eventual nonzero birefringence signal would not directly measure the rotation of a cosmological matter congruence; parity-violating couplings, calibration, plasma and other mechanisms are alternatives.

## ME-056: identifiability and metric gap

The Monolithic 102 scalar extension is:

```text
H² = (8πG/3)ρ + Λ/3 − k/a² + Ω²/a².
```

This has at least three issues independent of whether it generates useful toy fits:

1. **Curvature/rotation degeneracy:** the scalar equation depends only on k−Ω² when Ω is treated as an independent scalar. Changing (k,Ω) while preserving k−Ω² keeps H² unchanged; a fit to H alone cannot identify cosmic Ω.
2. **Sign degeneracy:** Ω and −Ω give the same H², so it cannot determine handedness.
3. **Physical identification gap:** a full rotating metric and matter congruence must yield the term from Einstein's equations, and definitions and units for k, a, Ω must be stated. Writing it as a Friedmann-like extension does not derive a rotating universe.

[RotatingCosmology.lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/RotatingCosmology.lean) formalizes exact algebraic consequences of the chosen formula and **explicitly does not claim** a rotating metric, cosmological observation or GR derivation. Its [status report](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/ROTATION_COSMOLOGY.md) describes remaining obligations.

## ROT-005: exact causal rotating expansion — mathematical evidence only

The independently calculated [ROT-005 Korotkii–Obukhov example](../research/ROT-005_KOROTKII_OBUKHOV_BRIDGE.md) has a global time function, simultaneous physical vorticity and expansion, zero shear and a weak-energy-condition effective imperfect source. It shows that rotation and expansion **can** coexist mathematically in Einstein gravity (already known from the cited 1991 and 2020 literature), but does not show that the observed universe rotates.

The example's source is **defined** from its Einstein tensor, not derived from a matter-field action; its rotation-to-expansion ratio is illustrative, not observational. A geometrically motivated ME-056 parameter identification fails, while another curvature parameter fits the same H²(a) curve exactly. Consequently ME-056 remains nonidentifying from scalar expansion alone.

## ROT-006: source-first matter obstruction (not a cosmic measurement)

The [ROT-006 source audit](../research/ROT-006_SOURCE_FIRST_MATTER_AUDIT.md) finds that the exact stress required by the chosen ROT-005 metric cannot arise from a standalone ordinary real scalar, ordinary complex scalar, perfect fluid or pure Maxwell model. This is proved by the invariant eigenvalue multiplicities of their respective stress tensors. More general matter models can remain physically viable; no new cosmological observation follows.
## Zero-rotation comparator

The conventional isotropic and homogeneous FLRW comoving congruence has vanishing vorticity. It is an indispensable null model. A genuinely preferred rotation should outperform a well-calibrated ΛCDM/FLRW baseline **after** accounting for other CMB/systematic anisotropy and cosmic variance. Standard local vortices do not falsify FLRW.

## Proposed falsifiable routes

- Derive a proper covariant rotating metric, stress-energy and congruence and compute CMB temperature and polarization transfer functions; compare against published likelihoods and Bianchi alternatives on held-out multipoles or sky splits.
- Specify independent signatures separating cosmic vorticity from ordinary curvature, shear, weak lensing, cosmic birefringence and galactic rotation catalog selection.
- Abandon/unfreeze the model if it cannot satisfy existing cosmological constraints or cannot make a prediction distinguishable from ΛCDM once nuisance parameters are admitted.

**Current verdict:** Rotating cosmologies are mathematically possible as models; local rotation is abundantly observed; a distinctive EFMW cosmic rotation signal has **not** been independently established.
