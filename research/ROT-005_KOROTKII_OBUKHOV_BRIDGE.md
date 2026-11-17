# ROT-005 — Expanding, Rotating, Causal General Relativity: An Exact-Metric Test of ME-056

**Monolithic Research · 2026-11-17 · Source-pinned symbolic replication**  
**Status:** **PASS** (explicit causal expanding/rotating GR geometry with a weak-energy-condition effective source); **FAIL** (ME-056 under a specified direct curvature/vorticity identification); **UNRESOLVED** (EFMW-specific matter action, uniquely identifiable cosmic rotation and astronomical confirmation).

> This is **not a new solution of Einstein's equations** or a measurement of the rotation of the observed universe. The family of metrics was published by Korotkii & Obukhov. We contributed a reproducible exact tensor computation for a chosen family member, a global algebraic energy-condition bound, and an adversarial comparison with Wright's historical proposed equation.

## 1. Scientific question and sources

**ROT-005:** Can a definite, physically meaningful expanding and rotating spacetime satisfy Einstein's equations while avoiding the causality defect of the classic Gödel spacetime? If it can, does the scalar expansion law obtained from that geometry establish the separately positive rotation term in canonical Monolithic ME-056?

**Original literature:**

- **Korotkii and Obukhov (1991),** [*Kinematic analysis of cosmological models with rotation*, Soviet Physics JETP 72(1):11–15, Eq. (4.1) and (4.2)](https://jetp.ras.ru/cgi-bin/dn/e_072_01_0011.pdf). They introduce this class of expanding, shear-free, rotating, causally well-behaved spatially homogeneous metrics, including its vorticity formula.
- **Korotky, Masár and Obukhov (2020),** [*In the Quest for Cosmic Rotation*, Universe 6(1):14, Eq. (7)](https://doi.org/10.3390/universe6010014). The review restates the metric family and discusses its physical interpretation; the authors' proposed observations should **not** be read as a consensus empirical detection.
- [ROT-004](ROT-004_COVARIANT_BRIDGE.md), our preceding 1+3 Einstein constraint and Gödel negative control.
- [Canonical ME-055](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/055.md) and [ME-056](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/056.md), **preserved unchanged**.

The original sources use `(+---)` metric signature; our script uses `(-+++)` **and reverses the coordinate orientation `y→−y`**, which changes the sign of the mixed `dt dy` term while leaving all scalar invariants unchanged. We also use `c=1`, `8πG=1`, and `Λ=0` for a deliberately normalized mathematical model. The **Korotkii–Obukhov coefficient `k_KO=1` is NOT the Friedmann/ME-056 curvature parameter `k_ME`**.

## 2. An explicitly testable geometry

Choose `t>-2`, spatial topology `R^3`, and parameters

```text
a(t) = 1 + t/2 > 0,   m = 1/2,
sqrt(sigma) = 1/10,   k_KO = 1.
```

The exact metric is

```text
ds² = -(dt + a(t) exp(x/2) dy / 10)²
      + a(t)² dx²
      + (101/100) a(t)² exp(x) dy²
      + a(t)² dz².
```

It is a fixed representative of the cited Gödel-type **Bianchi III** family, not a novel geometry. The selected matter observers have normalized four-velocity `u^a=(1,0,0,0)`. This vector is timelike: `g_ab u^a u^b=-1`.

**Causality:** The inverse metric has `g^{tt}=-100/101<0` throughout `t>-2`. Thus `t` is a global time function with timelike gradient; closed future-directed causal curves cannot exist in this domain. Each `t=constant` slice has positive-definite induced metric. This establishes stable causality, **not** timelike or null geodesic completeness (the example ends at `t=-2`).

## 3. Derived kinematics — definite nonzero rotation and expansion

The [standalone SymPy code](rot005_ko_sympy.py) differentiates the metric to compute the Christoffel symbols, Ricci tensor, Einstein tensor, and four-velocity gradient. No formula for the Einstein tensor is supplied as input. With `H=Theta/3`:

```text
Theta = 3/(2a),          H = 1/(2a) > 0
sigma_ab = 0,           sigma² = 0
omega² = (1/2) omega_ab omega^ab = 1/(1616 a²) > 0
R_rest = -203/(404 a²)
g^tt = -100/101
```

Physical rotation here is **the covariant vorticity of the defined matter-observer congruence**, not merely an angular coordinate or Clifford rotor. The model has nonzero four-acceleration and is **not** the shear-free, geodesic dust case prohibited from simultaneous expansion and rotation.

The vorticity follows the Korotkii–Obukhov published kinematic formula for this metric family:

```text
|omega| = m/(2a) sqrt(sigma/(k_KO+sigma))
        = 1/(4 sqrt(101) a).
```

The illustrative dimensionless ratio is `|omega|/H = 1/(2 sqrt(101)) ≈ 0.04975`. **These parameters were chosen for an exact rational test, not fitted to astronomical measurements**. Do not compare this number directly with Planck's model-specific Bianchi VIIh bound or portray it as an observational estimate.

## 4. Einstein equations and the matter-source limitation

Define an **effective** source by `kappa*T_eff_ab = G_ab`, with `kappa=1` and `Lambda=0`. This construction automatically satisfies the algebraic Einstein equation, but its scientific content lies in the independent tensor reconstruction, its directly checked conservation and its physically constrained energy condition. It does **not** identify a known microscopic fluid Lagrangian or show that ordinary pressureless dust generates the metric.

The code directly recomputes:

```text
nabla^a G_ab = 0 for all b,             PASS
3H² = rho + sigma² - omega² - R_rest/2, PASS
Raychaudhuri propagation residual = 0, PASS
```

The source as measured in the orthonormal observer frame has

```text
kappa*T_eff^(hat a hat b) = (1/a²) *
[[ 807/1616,          1/404,       -sqrt(101)/202,     0       ],
 [ 1/404,            -399/1616,    -sqrt(101)/404,     0       ],
 [ -sqrt(101)/202,   -sqrt(101)/404,-391/1616,          0       ],
 [ 0,                 0,           0,                   3/1616  ]].
```

Here `T_eff` means **orthonormal covariant components**, not a coordinate `T^{ab}`; the matrix is symmetric and has a nonzero observer-frame energy flux and anisotropic spatial stresses. It is therefore **not comoving perfect-fluid matter** in this observer frame.

### Positive-energy test: WEC holds throughout the chosen domain

For any local causal vector `v^(hat a)=gamma(1,beta_i)` with `|beta|<=1`, we have

```text
T_eff_ab v^a v^b / gamma²
 = rho + 2 T_(hat0,hati) beta_i
       + P_ij beta_i beta_j.
```

Bound the linear term by the sum of absolute fluxes and the spatial quadratic form using the Gershgorin lower eigenvalue bound. The exact symbolic matrices yield the **strict positive** lower bound

```text
T_eff_ab v^a v^b / gamma²
>= (400 - 20 sqrt(101))/(1616 a²) > 0.
```

Because the same orthonormal tensor scales as `1/a²` everywhere, this supplies an **analytic weak energy condition (WEC) verification for the defined effective source over all `t>-2` and all spatial coordinates**, not just a random finite sample of observer directions.

This does **not** establish the dominant energy condition, a microphysically consistent equation of state, thermodynamic stability, a particle/field source action, or observational plausibility. It does rule out the simplest allegation that this exact metric could only be realized by **negative observed energy density** in the specified effective-source interpretation.

## 5. Critical result: compare the *derived* expansion to ME-056

For this metric, the full 1+3 scalar constraint gives:

```text
3H² = kappa*rho + sigma² - omega² - R_rest/2.
```

The term with `-omega²` cannot be independently replaced with a universal **positive** `+Omega_U²/a²` without accounting for curvature, shear and model-specific identifications.

For a deliberately stated "natural" but **extra** mapping, choose

```text
k_ME = a² R_rest/6             = -203/2424
Omega_ME² = a² omega_physical² = 1/1616.
```

The stipulated ME-056 formula then gives an exact mismatch:

```text
H²_ME056 - H²_derived_GR = 1/(1212 a²) > 0.
```

**FAIL for that explicit mapping**. We have supplied a self-consistent *expanding*, *rotating*, *causal* metric where the independent-positive-additive assignment fails. The earlier Gödel model was non-expanding; this result eliminates that specific escape from the counterexample.

**But the scalar relation can be made to fit.** With the same `Omega_ME²`, redefining `k_ME=-67/808` exactly matches the scalar `H²(a)` curve:

```text
H²_ME056 - H²_derived_GR = 0       (retuned curvature)
```

This is **not new evidence for rotation**. It exposes the existing `k−Omega²` parameter degeneracy. A scalar expansion curve that admits a curvature retuning cannot uniquely recover a physical rotational parameter by itself.

**The mathematical interpretation is deliberately limited:** The source `k_ME` is not defined in a rotating metric, and `Omega_U` is a proposed vector rather than a fully specified covariant scalar. These comparisons assess explicitly named parameter mappings, not every conceivable reinterpretation of canonical ME-056.

## 6. Reproducibility and independent checks

The new script [`research/rot005_ko_sympy.py`](rot005_ko_sympy.py) recomputes the full tensor and reports JSON with 15 exact PASS/FAIL booleans, including:

- Lorentzian orthonormal coframe and stable-causal global time;
- unit material-observer congruence, strictly positive expansion and nonzero covariant vorticity;
- zero shear and nonzero acceleration;
- Einstein tensor, exact source conservation, Gauss and Raychaudhuri identities;
- constant-in-space orthonormal effective source and global positive WEC lower bound;
- mismatched natural ME-056 parameter mapping and exactly retuned degenerate scalar comparison.

The CI job **ROT-005 expanding causal rotating Einstein spacetime** runs pinned `sympy==1.14.0` independently of the Gödel test and the normal Python laboratory. Check the commit and workflow run, not just the fact that a source file exists.

To reproduce:

```bash
python -m pip install sympy==1.14.0
python research/rot005_ko_sympy.py
```

Expected top-level result: `PASS_FIXED_CAUSAL_EXPANDING_ROTATING_EINSTEIN_METRIC_WITH_WEC_EFFECTIVE_MATTER`. Test outputs are *mathematical*, and the mode contains no observational data or hidden parameter fitting.

## 7. Zoo-style ledger

| Finding | Assessment | Evidence boundary |
|---|---|---|
| ROT005-GR-01 Published causally admissible expanding rotating metric family | **PASS / known literature** | Not new research discovery |
| ROT005-GR-02 Explicit fixed metric is Lorentzian and admits a global time function | **PASS / exact algebra** | Not geodesically complete |
| ROT005-GR-03 Covariant `Theta>0`, `omega²>0`, `sigma²=0` | **PASS / exact tensor calculation** | Specific observer congruence |
| ROT005-GR-04 Einstein equation with `T_eff=G/kappa` and covariant conservation | **PASS / exact geometry** | Source is *defined* from G, not independently derived |
| ROT005-MAT-01 WEC holds for that imperfect effective source | **PASS / strict analytic bound** | No DEC, field action or stability certification |
| ROT005-EFMW-01 ME-056 direct curvature/vorticity mapping | **FAIL / explicit counterexample** | Mapping is a conditional choice, not canonical |
| ROT005-EFMW-02 Retuning ME-056 curvature matches scalar H² exactly | **PASS algebra; FAIL identifiability** | Fit is degenerate and has no observational support |
| ROT005-EFMW-03 Derive a novel EFMW Lagrangian yielding this source | **UNRESOLVED** | No source action or equations supplied |
| ROT005-OBS-01 Distinctive prediction from cosmic vorticity compatible with real data | **UNRESOLVED** | No CMB or galaxy-data fitting performed |

## 8. What we should do next — ROT-006

**Do not announce a discovery of universal rotation.** Mathematically, expanding, rotating and causal GR geometries have been available for decades. Our added value is a reproducible model-to-claim audit.

The next test must **stop defining matter from the metric afterward**:

1. Start with a **predefined physical matter action / stress tensor**, e.g. a well-specified imperfect fluid, Einstein–Maxwell–scalar, or a rigorously specified EFMW field action; do not tune it to reproduce the desired Einstein tensor.
2. Independently derive `T_ab` from that matter model and compare to the tensor required by this metric, including energy flux and anisotropic stress.
3. Check `nabla^a T_ab=0`, hyperbolicity/stability, energy conditions, causal behavior, and the no-rotation FLRW limit.
4. Require at least one **new identifiable prediction** not absorbed by redefining curvature or ordinary matter.
5. Freeze the numerical observational likelihood and a null model **before** opening held-out data; then compare with established rotating cosmology models and standard `Lambda`CDM.

**Stop:** If no physically defensible matter source or uniquely measurable rotational parameter exists, label the EFMW-specific physical bridge UNRESOLVED and revise the model—not the data.

## Conclusion

**ROT-005 succeeded at constructing and independently checking a concrete admissible geometrical example of rotation plus expansion**, but **did not derive ME-056 as a universal GR equation**. Under the directly specified geometrical mapping, the proposed term fails; under an adjustable curvature parameter, it fits without identifying rotation. The decisive outstanding question is **a physical source theory and a distinct observable**, not the existence of rotating mathematical spacetimes.

*Original source equations and publications retain their attribution. This report is an independent mathematics/reproducibility audit prepared for Matthew Chenoweth Wright / Monolithic LLC; no author of the cited work or Topher has endorsed it.*
