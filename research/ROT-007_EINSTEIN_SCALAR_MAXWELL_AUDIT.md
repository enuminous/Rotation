# ROT-007 — Frozen Einstein–Scalar–Maxwell Candidate: Exact Trace No-Go

**Monolithic Research / November 17, 2026**  
**Status:** **FAIL for the source-first action and homogeneous scalar ansatz frozen in the ROT-007 protocol.**  
**Check method:** Exact four-dimensional symbolic stress-energy contraction and comparison against the independently recomputed Einstein tensor of the *fixed* ROT-005 metric.  
**Not:** An observational claim, a no-go theorem for every scalar or scalar–Maxwell theory, or a proof that the universe has no vorticity.

## 1. Question

Could the [predeclared ROT-007 action](ROT-007_PROTOCOL.md), with a massless real canonical scalar field and standard Maxwell field, support the **specific** expanding and rotating Korotkii–Obukhov spacetime already examined in [ROT-005](ROT-005_KOROTKII_OBUKHOV_BRIDGE.md)?

We did **not** add a source defined after the fact as `T_ab = G_ab`; the *matter action and the initial field ansatz were frozen first*. Nor did we change the metric or the original Monolithic 102 equations to obtain a favorable answer.

### Frozen action, conventions, and ansatz

In four-dimensional spacetime, metric signature `(-+++)`, units `8πG=1`, `c=1`, `Λ=0`:

```text
S = ∫ sqrt(-g) [ R/2 − (1/2)g^ab(∂a phi)(∂b phi)
                          − (1/4)F_ab F^ab ] d⁴x.

F = dA.
phi = phi(t)         real and single-valued
A = E(t) exp(x/2) dy + B(t) dz.
V(phi) = 0.
```

The fixed metric is

```text
a(t) = 1+t/2 > 0, t > -2
ds² = −(dt+a exp(x/2)dy/10)²
      +a² dx² +(101/100)a² exp(x)dy²+a² dz².
```

These are the exact conditions of the [public pre-run protocol](ROT-007_PROTOCOL.md). Maxwell functions `E(t),B(t)` remain arbitrary, so the negative result does not depend on selecting their parameters.

## 2. Necessary Einstein trace equation

In four spacetime dimensions, `G^a_a = −R`. The canonical stress tensors obtained by metric variation are

```text
T(phi)_ab = (∂a phi)(∂b phi) − (1/2) g_ab (∇phi)²

T(EM)_ab = F_ac F_b^c − (1/4) g_ab F_cd F^cd.
```

Their *exact traces* are

```text
T(phi)^a_a = −(∇phi)²,
T(EM)^a_a = 0.
```

The vanishing electromagnetic trace is an algebraic identity in **four dimensions**, for arbitrary electromagnetic amplitudes, not a special choice of polarization or gauge. Thus the trace of the coupled Einstein equation imposes

```text
G^a_a = −(∇phi)²,
or equivalently, R = (∇phi)².
```

This is necessary for **all ten** Einstein components to match. One contradictory trace is sufficient to refute the entire proposed source solution.

## 3. Exact geometric obstruction

The fixed metric has

```text
g^tt = −100/101,
R = 797/(808 a²) > 0,
G^a_a = −797/(808 a²) < 0,      for every t > −2.
```

The code constructs the metric and its inverse, reads the verified ROT-005 orthonormal Einstein source, transforms it back to the coordinate tensor and computes `G^a_a` directly. Its Ricci scalar agrees with `−G^a_a`. The prior ROT-005 job **independently recomputes that Einstein tensor from Christoffel symbols** on each CI run.

With the frozen homogeneous **real** scalar `phi(t)`,

```text
(∇phi)² = g^tt (dphi/dt)²
        = −(100/101) (dphi/dt)² ≤ 0.
```

The Einstein trace requires

```text
  −797/(808a²) = (100/101) (dphi/dt)².

Therefore (dphi/dt)² = −80497/(80800a²) < 0.
```

For any `a>0`, that is **impossible** for a real-valued derivative.

**ROT-007 disposition: FAIL for the frozen action and homogeneous scalar ansatz.**

This obstruction does not rely on fitting just one diagonal Einstein component, choosing a particular electromagnetic field, using a numerical tolerance, or assuming a cosmological observation. It is an **exact symbolic sign contradiction**.

## 4. Maxwell field and matter Euler–Lagrange equations

The code constructs the proposed 1-form `A=E(t)e^(x/2)dy+B(t)dz` and its field strength `F=dA`. It verifies the Bianchi identity `dF=0`, then forms `F_ac F_b^c−g_ab F²/4` and checks **directly on the rotating metric** that its trace is zero. No Maxwell `E(t),B(t)` can repair the Einstein trace.

The action would additionally demand

```text
Box(phi) = 0,
nabla_a F^ab = 0,
G_ab = T(phi)_ab + T(EM)_ab.
```

Because the **necessary** trace of the Einstein equation fails identically for real `phi(t)`, **there is no solution of the full system** in the frozen ansatz. Solving the remaining differential equations is unnecessary for this negative determination; the computation **does not falsely claim** that those extra field equations have been independently solved.

This is a mathematically valid early-stop rule: every genuine solution must satisfy the trace, and none in the declared class can.

## 5. Explicit counterexamples to overgeneralizing this FAIL

The no-go **does not** extend automatically to:

- **Spatial scalar gradients:** a nonhomogeneous real scalar can have a spacelike gradient with `(∇phi)² > 0`, removing the immediate trace-sign contradiction (though all field equations may still fail).
- **Nonzero scalar potentials:** adding `V(phi)` modifies the trace to `−(∇phi)²−4V`, so a positive `V` can change the trace sign. A new potential must be specified before testing, not adjusted to fit the answer.
- **Nonminimal couplings and higher derivatives:** stress tensors receive extra curvature/derivative terms, outside this protocol.
- **Additional matter:** an imperfect fluid or further field sectors can contribute trace and off-diagonal stresses.
- **Different spacetimes:** the obstruction refers to this one KO family member with the frozen metric parameters; it is not a general theorem against expanding, rotating solutions.
- **Other field-equation conventions:** a nonzero Λ, different field kinetic sign, or alternative gravitational action would be a **new and separately labeled** hypothesis.

Even a model that avoids this trace obstruction must still satisfy **all Einstein equations and matter-field equations**, physical energy conditions, a stable evolution, and a distinct observational prediction.

## 6. Reproduction and deterministic verdict

**Code:** [`rot007_einstein_scalar_maxwell.py`](rot007_einstein_scalar_maxwell.py)

**Method:**

1. Recompute the pre-existing [ROT-005](rot005_ko_sympy.py) full metric verification.
2. Independently reconstruct the KO metric inverse and trace of its fixed Einstein tensor.
3. Derive canonical-scalar stress from the specified massless action and compute its trace.
4. Build an arbitrary source-free Maxwell potential of the frozen form, derive its field strength and stress tensor, check `dF=0` and its identically zero trace.
5. Derive the impossible negative squared real time derivative exactly.
6. Check four independent positive-scale examples as *diagnostic outputs*, not as a substitute for the analytic proof.

```bash
python -m pip install sympy==1.14.0
python research/rot005_ko_sympy.py
python research/rot007_einstein_scalar_maxwell.py
```

Expected status:

```text
PASS_EXACT_NO_GO_FOR_FROZEN_ACTION_AND_HOMOGENEOUS_SCALAR_ANSATZ
verdict_for_candidate = FAIL
```

This `PASS` describes **successful verification of a limited negative result**. It does not upgrade the failed action to a passing theory. The repository GitHub Actions workflow runs the same calculation at a pinned source revision.

## 7. Zoo disposition

| ID | Check | Verdict |
|---|---|---|
| ROT007-ACT-01 | Action, vanishing potential and ansatz predeclared and unchanged | **PASS / source custody** |
| ROT007-GR-01 | Fixed metric has positive Ricci scalar `797/(808a²)` | **PASS / exact symbolic geometry** |
| ROT007-MAT-01 | Canonical scalar trace is `−(∇phi)²` | **PASS / direct tensor calculation** |
| ROT007-MAT-02 | Maxwell trace is identically zero for the stated 4-D source | **PASS / direct tensor calculation** |
| ROT007-EIN-01 | Trace of Einstein equation is satisfiable for any real homogeneous scalar `phi(t)` | **FAIL / impossible negative derivative square** |
| ROT007-EOM-01 | Complete coupled Einstein–scalar–Maxwell solution in frozen ansatz | **FAIL / necessary Einstein condition impossible** |
| ROT007-OBS-01 | Empirically measured cosmic rotation or EFMW-specific predictive gain | **UNRESOLVED / no observational tests** |

## 8. Next research proposal — ROT-008

**First relax only one feature: allow `phi(t,x)` while preserving the massless canonical Einstein–scalar–Maxwell action `V=Λ=0` and the exact KO metric.** This permits a spacelike scalar gradient but does **not** guarantee a solution. Predefine a simple spatially covariant scalar ansatz (e.g. `phi=ct + d x`) with the same Maxwell symmetry class, then test **all** tensor equations and scalar/Maxwell Euler–Lagrange equations. Include branch and energy-condition checks; a failure of that restricted ansatz must not be generalized.

A separate later candidate could include a **fixed predeclared scalar potential** or nonminimal coupling. It should never be silently introduced into ROT-007 to make a FAIL disappear.

**No astronomical likelihood fitting** is warranted until a physical source and an independently identifiable rotation observable survive a full Einstein-equation test.

## Conclusion

**ROT-007 is an exact FAIL for the particular source-first minimal action with a real homogeneous scalar and Maxwell field.** The test has sharpened the scientific boundary around an EFMW-style scalar-driven rotating cosmology without proving or disproving universal cosmic rotation. The appropriate next move is a new source-controlled hypothesis, not reinterpretation of the old result.

*Prepared for Matthew Chenoweth Wright / Monolithic LLC with OpenAI-assisted symbolic analysis. This report is an uncommissioned independent study of an existing GR family. Original metric and literature authors are credited; no endorsement from them or Topher is claimed.*
