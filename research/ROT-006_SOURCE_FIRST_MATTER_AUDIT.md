# ROT-006 — Source-First Matter Audit: Scalar-Field and Perfect-Fluid Obstructions

**Monolithic Research · 2026-11-17**  
**Target:** The **fixed** stably causal, expanding, rotating Korotkii–Obukhov spacetime verified in [ROT-005](ROT-005_KOROTKII_OBUKHOV_BRIDGE.md).  
**Disposition:** **PASS** (reproducible *restricted* mathematical no-go); **FAIL** (specified minimal matter-source candidates); **UNRESOLVED** (coupled scalar–vector sources, three or more independent scalars, nonminimal gravitational couplings, full EFMW field action, observed universal rotation).

> **No new cosmic rotation or particle species was observed.** An obstruction to one matter model on one chosen metric is **not** a no-go theorem for every rotating spacetime, every scalar theory, or every physically viable EFMW proposal.

## 1. Why this test was necessary

ROT-005 chose a published rotating, expanding spacetime with an exact Einstein tensor `G_ab`, then defined `T_eff=G_ab/κ`. This establishes that the **geometry** admits a conserved effective source satisfying a specified weak-energy condition (WEC). It does **not** establish that a known field action or a physically justified fluid provides that source.

ROT-006 reverses the inference: begin with a **specific matter model** and ask whether its stress tensor could equal the fixed Einstein tensor. The simplest candidate corresponding to the scalar aspect of Monolithic 102 is an ordinary minimally coupled real or complex scalar field. We also test perfect-fluid and pure standard electromagnetic sources.

The result is a **negative mathematical selection test**: these standalone minimal theories do not supply the exact tensor required by the frozen ROT-005 spacetime.

### Frozen geometry and source

The tested metric, coordinate domain and congruence are exactly those in [ROT-005](ROT-005_KOROTKII_OBUKHOV_BRIDGE.md):

```text
a(t)=1+t/2,  t>-2
ds²=-(dt + a exp(x/2) dy/10)²
    +a² dx² + (101/100) a² exp(x) dy² +a² dz²
u^a=(1,0,0,0);  κ=8πG=1; Λ=0;  signature (-+++).
```

Our [exact-metric recomputation](rot005_ko_sympy.py) returns the effective covariant orthonormal source `T_(hat a,hat b)`. Multiply by `a²` to remove its overall time dependence:

```text
a² T_hat = [
  [ 807/1616,         1/404,      -sqrt(101)/202,    0 ],
  [ 1/404,          -399/1616,    -sqrt(101)/404,    0 ],
  [-sqrt(101)/202,  -sqrt(101)/404, -391/1616,       0 ],
  [ 0,                 0,              0,          3/1616 ]
].
```

We compare **mixed tensor eigenvalues** `T^a_b`, which are invariant under a change of local orthonormal frame (similarity transformation), rather than merely pointing to a visually anisotropic `T_hat` matrix. That prevents a tilted-fluid or observer-coordinate choice from evading the test.

## 2. The exact eigenvalue obstruction

Let `M = 1616 a² T^a_b`. SymPy reconstructs `M` from the recomputed ROT-005 Einstein tensor, without fitting source parameters. Its **exact** characteristic polynomial is

```text
det(z I − M)
  = (z − 3) [z³ + 1597 z² + 798403 z + 127206399].
```

A positive, exact discriminant and `gcd(p,p')=1` establish **four distinct algebraic eigenvalues**. Their illustrative numerical values are

```text
z ≈ −790.7884267154, −443.5292558399,
    −362.6823174446, +3.0000000000.
```

The numeric approximations are **not** the proof; the source code checks the exact polynomial and square-free property. Scaling by positive `a²` preserves multiplicities for every spacetime point with `t>-2`.

This simple-spectrum fact is a necessary **coordinate-independent** source-selection test.

## 3. First predefined action: one canonical real scalar

Start with a minimally coupled scalar matter action, using only the first derivatives of the scalar and a potential:

```text
S_phi = ∫ d⁴x sqrt(-g)
        [−(1/2) g^ab (∂_a phi)(∂_b phi) − V(phi)].
```

Its independently derived stress tensor is

```text
T_ab = (∂_a phi)(∂_b phi)
       − g_ab[(1/2)(∇phi)² + V(phi)].
```

For its **mixed** tensor, write `v^a=∇^a phi` and `L=−(∇phi)²/2−V`:

```text
T^a_b = v^a v_b + L δ^a_b.
```

The non-isotropic part is **rank at most one**; therefore at least three algebraic eigenvalues of `T^a_b` equal `L`. The SymPy script independently verifies this as an exact symbolic characteristic-polynomial factorization:

```text
det(z I − T) = (z−L)³ (z−L−v²).
```

The fixed ROT-005 source has **four distinct** eigenvalues. Consequently:

**FAIL: No single ordinary minimally coupled canonical scalar, with any allowed gradient or potential, can by itself equal the exact required source on this fixed background.**

The same rank-one conclusion holds for first-derivative single-field k-essence `L(phi,X)` with the usual metric dependence through `X=−(∇phi)²/2`. It does **not** cover nonminimal scalar-curvature couplings, higher derivatives or scalar–vector interactions.

## 4. The stronger two-scalar / complex-scalar obstruction

For a minimally coupled Lagrangian involving `N` real scalars whose metric dependence occurs through first-derivative contractions `X^{IJ}`, the mixed stress tensor has the schematic structure

```text
T^a_b = L δ^a_b + Σ_{I,J} K_IJ (∇^a phi^I)(∇_b phi^J).
```

The gradient contribution has **rank at most `N`**, regardless of kinetic mixing. Therefore it has at least `4−N` eigenvalues `L`, counting algebraic multiplicity.

For **N=2** (including one ordinary complex scalar split into real and imaginary parts) the required repeated pair is absent from the frozen source. This excludes standalone, minimally coupled two-scalar first-derivative matter as the sole source of *this* metric:

**FAIL: A simple minimally coupled complex scalar or two first-derivative real scalars cannot by themselves reproduce ROT-005's exact stress tensor.**

Important distinction: A complex phase can have quantized winding, and the phase may still be interesting physics. The obstruction concerns **sourcing this particular Einstein metric**, not the existence of quantum vortices or every possible scalar–vector coupling.

## 5. Perfect fluid — including a tilted observer frame

A perfect fluid has

```text
T_ab = (rho+p) U_a U_b + p g_ab,  U^a U_a = −1.
```

Its mixed tensor is an isotropic `p δ^a_b` plus a **rank-one** term. It therefore has three repeated eigenvalues even after arbitrary Lorentz frame changes. The fixed source has four distinct eigenvalues.

**FAIL: No standalone perfect fluid of any equation of state or velocity tilt can exactly source this fixed KO spacetime.** An imperfect fluid with heat flux and anisotropic stresses is not excluded.

## 6. Pure Maxwell matter

The standard electromagnetic action is

```text
S_EM = −(1/4) ∫ d⁴x sqrt(-g) F_ab F^ab
T_ab = F_ac F_b^c − (1/4)g_ab F_cd F^cd.
```

For an arbitrary antisymmetric 2-form in 4-D Lorentzian geometry, `T^a_c T^c_b = c δ^a_b` for a scalar `c` determined by its electromagnetic invariants, hence

```text
det(z I − T) = (z²−c)².
```

The script uses **six independent symbolic electromagnetic field components**, constructs this stress from the Maxwell action, checks the squared-tensor identity, and checks the characteristic-polynomial factorization.

**FAIL: A pure ordinary Maxwell field cannot by itself source the fixed ROT-005 metric.** Electromagnetism **combined with other physical fields** is not excluded.

## 7. Separate geometric no-go: a single scalar cannot be the rotating comoving velocity potential

If a fluid four-velocity is a normalized timelike gradient, `u_a = alpha ∂_a phi`, then the differential one-form `u_flat=alpha dphi` obeys

```text
u_flat ∧ d(u_flat)
 = alpha dphi ∧ [d(alpha) ∧ dphi] = 0.
```

This is the Frobenius hypersurface-orthogonality condition, which means such a scalar-gradient congruence has **zero vorticity**.

For the KO metric's selected rotating observer `u^a=δ^a_t`, the independently calculated one-form is

```text
u_flat = −dt − a exp(x/2)/10 dy.
```

The explicit `(t,x,y)` component of its Frobenius 3-form is

```text
[u_flat ∧ d(u_flat)]_{txy}
    = a exp(x/2)/20 > 0,     t > −2.
```

Thus **the chosen rotating matter-observer congruence cannot be the normalized gradient of a single ordinary scalar**, irrespective of whether some *other* scalar configuration could coexist with the geometry.

This is not proof that all scalar-field matter has zero possible rotation in every frame; it specifies which **observer congruence** is derived from the scalar.

Supporting literature:
- [Faraoni et al., scalar-gradient fluid vorticity and Frobenius discussion, *EPJ C* 2023](https://doi.org/10.1140/epjc/s10052-023-11712-7).
- [K-essence source types, *Universe* 2025](https://www.mdpi.com/2218-1997/11/3/100).

## 8. Actual execution and acceptance gates

Code: [`research/rot006_scalar_source_test.py`](rot006_scalar_source_test.py).

```bash
python -m pip install sympy==1.14.0
python research/rot005_ko_sympy.py
python research/rot006_scalar_source_test.py
```

The GitHub CI workflow recomputes the exact ROT-005 metric **before** testing the new source assumptions. It verifies:
- complete exact metric tensor checks and effective stress;
- exact mixed characteristic polynomial and square-free proof;
- canonical-scalar source derived from the specified action;
- rank bound for two first-derivative scalars and a nontrivial symbolic example;
- exact generic six-component Maxwell algebra;
- Frobenius obstruction for the given comoving velocity field.

Expected status: `PASS_EXACT_RESTRICTED_MATTER_SOURCE_EXCLUSION`. A green CI run is an independent **execution of the scripts**, not an independent mathematical peer review.

## 9. Findings and proposed ROT-007

| ID | Finding | Status | Precisely limited scope |
|---|---|---|---|
| ROT006-INV-01 | KO source's mixed stress has four simple eigenvalues | **PASS** | Exact fixed metric |
| ROT006-SRC-01 | Single canonical real scalar / single first-derivative k-essence | **FAIL source match** | As sole minimally coupled matter |
| ROT006-SRC-02 | Ordinary complex scalar / two first-derivative real scalars | **FAIL source match** | As sole minimally coupled matter |
| ROT006-SRC-03 | Any tilted or comoving perfect fluid | **FAIL source match** | No heat flux or anisotropic stress |
| ROT006-SRC-04 | Pure standard Maxwell electromagnetic field | **FAIL source match** | No other coupled sectors |
| ROT006-KIN-01 | Scalar-gradient 4-velocity represents rotating KO observers | **FAIL** | Only the prescribed comoving rotating congruence |
| ROT006-MAT-01 | Independently derived scalar–vector / higher-derivative / 3+-field source | **UNRESOLVED** | Not excluded by simple-spectrum test |
| ROT006-OBS-01 | Any observed physical universal rotation | **UNRESOLVED** | No observational fit |

**Next bounded experiment ROT-007:**
1. **Predefine** a concrete scalar–vector matter Lagrangian (or minimally coupled multi-scalar model) **before** inspecting any adjustable tensor equality, including couplings, kinetic signs and boundary conditions.
2. Compute `T_ab` by metric variation, including all covariant field equations.
3. Test the **full** equations `G_ab=κT_ab`, `∇^a T_ab=0` and matter Euler–Lagrange equations on ROT-005 geometry or a new explicitly selected metric.
4. Require physically admissible stress, causal/hyperbolic field equations, acceptable mode stability and a consistent zero-rotation limit.
5. Freeze at least one observational prediction that cannot be removed by reinterpreting `k−Ω²`.
6. If no source is found, publish `UNRESOLVED`/appropriate bounded `FAIL`. Do not reverse-engineer a bespoke stress tensor and call it a derived scalar theory.

A mathematically coherent scalar–vector coupling could be useful independently of universal cosmic rotation. This audit does not nominate it as the actual source of the universe.

## 10. Conclusion

ROT-006 resolves a clear matter-model question: **the fixed rotating and expanding metric from ROT-005 cannot be sourced solely by an ordinary perfect fluid, one canonical real scalar, one simple complex scalar, or pure standard Maxwell field.** The result holds at every point of the fixed spacetime because the exact stress tensor has a simple mixed spectrum.

The proposed **EFMW universal-rotation mechanism is not verified**. The path forward requires a richer, independently specified physical action and an observable that could distinguish it from conventional matter and geometry—not a broader rhetorical claim about every field spinning.

*Research prepared for Matthew Chenoweth Wright / Monolithic LLC, with computational assistance. Independent technical corrections and alternative-source counterexamples welcome. The original authors of the referenced metrics and papers have not endorsed this report.*
