# ROT-004 — Covariant Bridge Audit: ME-055/056 versus Einstein gravity

**Monolithic LLC • Research artifact • 2026-11-17**  
**Scope:** Theoretical consistency, exact-metric counterexample, a priori test criteria.  
**Research status:** **PASS for the standard GR identities and the Gödel metric witness; FAIL for an unqualified universal additive interpretation of ME-056; UNRESOLVED for an EFMW-specific rotating metric or any cosmological detection.**  
**Not:** An observation of global rotation, a new GR theorem, a complete Lean formalization, a numerical CMB likelihood study, or a demonstration that *every* interpretation of ME-056 is impossible.

## 0. A decisive outcome

There is a meaningful mismatch between the **stipulated** positive quadratic rotation term in canonical ME-056 and the **actual** covariant Friedmann/Gauss scalar constraint in GR. The GR constraint contains rotation *together with* shear and projected spatial curvature. The bare vorticity-squared contribution enters the constraint with a **negative** sign under the definitions below; the rotation enters the **Raychaudhuri propagation equation** with a positive term. Confusing those two equations leads to an incorrect generalization.

More importantly, an **exact dust solution** of Einstein's equations—the historical Gödel universe—is both rotating and **non-expanding**. We reproduce its Einstein-tensor and kinematic identities directly with computer algebra. This refutes the inference "nonzero physical rotation necessarily adds a positive Hubble expansion term" without making any observational claim about our universe.

These results give an actionable correction path for the EFMW hypothesis rather than invalidating rotation research itself.

## 1. Source, conventions and exact question

- **Canonical ME-055**: [`Ω_U = ∇×v_U`](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/055.md) is a Cartesian curl-type definition, with a *proposed* universal velocity field.
- **Canonical ME-056**: [`H² = 8πGρ/3 + Λ/3 − k/a² + Ω_U²/a²`](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/056.md) is labelled a **working hypothesis** and does not supply a rotating metric.
- **Primary GR comparison:** Ashkbiz Danehkar, [*Covariant Evolution of Gravitoelectromagnetism*](https://doi.org/10.3390/universe8060318), *Universe* 8(6):318 (2022), especially Eq. (46), with the cosmological constant restored.
- **Foundational framework:** Ellis & van Elst, [*Cosmological Models*](https://arxiv.org/abs/gr-qc/9812046), 1+3 covariant cosmology.
- **Exact rotating metric:** Gödel's historical solution in the conventional metric form quoted in [Zhao, Modesto & Bambi, *EPJ C* 86, 713 (2026), Sec. 2](https://doi.org/10.1140/epjc/s10052-026-15963-y). Their discussion of nonlocal gravity is **not** used as a premise here; the reproduced metric is an exact solution of ordinary Einstein gravity with dust and negative Λ.
- **Shear-free restrictions:** Senovilla, Sopuerta & Szekeres (1998), [*Theorems on Shear-free Perfect Fluids with their Newtonian Analogues*](https://doi.org/10.1023/A:1018854608416).

Use spacetime signature ((-+++)), (c=1), (kappa=8πG), normalized physical timelike congruence (u^a u_a=-1), and:

```text
h_ab = g_ab + u_a u_b
Theta = nabla_a u^a     ;   H = Theta/3
sigma^2 = (1/2) sigma_ab sigma^ab  >= 0
omega^2 = (1/2) omega_ab omega^ab  >= 0
R_rest = scalar of the 1+3 projected spatial connection
```

Here **physical** `omega^2` is a local covariant scalar. It must not be silently equated with the `Ω_U²` in ME-056, whose vector-to-scalar normalization is not yet specified. In ordinary rigid three-space `|curl v| = 2 |angular velocity|`, but this is **not** automatically the cosmological 1+3 identification.

## 2. The GR covariant constraint: a direct algebraic comparison

The full 1+3 Gauss scalar relation (with Λ restored) is:

```text
R_rest = 2 (kappa*rho + Lambda - Theta²/3 + sigma² - omega²)
```

Equivalent form, with (H=Theta/3):

```text
3 H² = kappa*rho + Lambda + sigma² - omega² - R_rest/2
H² = (kappa*rho+Lambda)/3 + (sigma²-omega²)/3 - R_rest/6.
```

**Critical geometric caution:** When `omega != 0`, the 3D local rest spaces are **not hypersurface-orthogonal** (Frobenius condition). Then `R_rest` is not automatically the scalar curvature of a global spatial slice and **cannot in general be replaced by** `6k/a²`. The FRW substitution `R_rest=6k/a²` is valid under the appropriate FLRW spatial-slicing assumptions, not automatically for rotating models.

In the standard FLRW case `sigma=omega=0`, `R_rest=6k/a²`, this returns:

```text
H² = (kappa*rho + Lambda)/3 - k/a²,
```

matching the zero-rotation limit of ME-056. **PASS: zero-rotation limit.**

### Exact necessary condition for agreement with ME-056

ME-056 posits:

```text
3 H² = kappa*rho + Lambda - 3k/a² + 3*Omega_U²/a² .
```

For *both scalar equations* to agree at a given event with matched matter density, Λ and measured expansion, one must have:

```text
   3*Omega_U²/a²
 = sigma² - omega² - (R_rest - 6k/a²)/2.      (BRIDGE CONDITION)
```

This is a **necessary algebraic compatibility condition**, not a sufficient Einstein-equation solution. The condition can hold for specially selected parameters, but the geometry and the matter evolution must *independently* realize them. The right side need not be positive.

Equivalently, the shear magnitude required by that identification would be:

```text
sigma²_required
 = 3*Omega_U²/a² + omega² + (R_rest - 6k/a²)/2 .
```

This shows why neither the positive additive term nor a matching coefficient can be declared universal by looking only at the scalar expansion equation.

### Conditional sign obstruction

If one *additionally* imposed `sigma=0` and `R_rest=6k/a²` in a rotating case, the bridge condition would become:

```text
3*Omega_U²/a² = -omega² .
```

For real positive `a` and nonzero physical vorticity that cannot hold with real `Omega_U`. **This invalidates the naive simultaneous assumptions.** It is *not* a general no-go theorem for rotating GR cosmologies, because a genuinely rotating spacetime need not obey those irrotational curvature/hypersurface conditions. A further restriction exists for geodesic shear-free dust: it cannot both expand and rotate (Ellis' dust theorem); do not generalize that theorem to arbitrary imperfect fluids.

## 3. Do not confuse the constraint with Raychaudhuri propagation

For a timelike congruence, with four-acceleration `A^a=u^b nabla_b u^a`, the propagation equation is:

```text
dot(Theta) =
 -Theta²/3 -2*sigma² +2*omega²
 -(kappa/2)*(rho+3p) + Lambda + nabla_a A^a.
```

Here rotation's `+2*omega²` term can oppose focusing **in the expansion derivative**. It does *not* imply an independently positive `Omega_U²/a²` term in the algebraic Friedmann constraint. Integrating Raychaudhuri requires consistent energy and vorticity evolution equations, shear, acceleration and constraints; assumptions about their scaling matter.

The [standard-library checks](../rotation/rot004_covariant.py) implement both formulas as separate functions so that they cannot be interchanged inadvertently. The script does not independently derive them from Christoffel symbols for a generic metric.

## 4. Exact GR control: rotating Gödel dust with zero expansion

Use the historical metric:

```text
ds² = -(dt + exp(mx) dy)² + dx² + (exp(2mx)/2) dy² + dz²
m > 0, u^a=(1,0,0,0), in (t,x,y,z) coordinates.
```

The [independent SymPy computation](rot004_godel_sympy.py) calculates the metric inverse, all connection coefficients, the Ricci tensor, the Ricci scalar, the Einstein tensor, and the dust congruence's covariant derivatives. With `kappa*rho=m²` and `Lambda=-m²/2`, it directly checks:

```text
G_ab + Lambda*g_ab = m²*u_a*u_b       exact
u_a u^a                  = -1        exact
Theta                     = 0         exact
sigma_ab                  = 0         exact
acceleration A_a          = 0         exact
omega²                    = m²/2      nonzero
R_rest (1+3 projected)    = 0         exact
H=Theta/3                 = 0
```

The apparent paradox of nonzero rotation and zero expansion disappears in the full GR constraint:

```text
3 H² = m² - m²/2 + 0 - m²/2 - 0 = 0.
```

Raychaudhuri also closes:

```text
dot(Theta) = +2*(m²/2) - m²/2 - m²/2 = 0.
```

### The useful FAIL

Under the **naive, extra** identification `a=1, k=0, Omega_U²=omega²`, ME-056 predicts `H² = 2m²/3 > 0`, while the exact spacetime has `H=0`. This *conditional mapping fails*.

**Do not misreport the scope:** Gödel's model contains closed timelike curves and is not an acceptable observational cosmology; it also has no global hypersurface orthogonal to the rotating dust congruence. There is no general meaning of the ME-056 FLRW `k` and global `a` in that metric without a new identification. Thus the exact-metric result is an **adversarial test of an overly broad inference**, not a completed falsification of every possible restricted EFMW rotation theory.

## 5. Dimensional and geometric obligations

1. **Metric first:** Identify (g_{ab}), matter (T_{ab}), normalized (u^a), physical (omega_{ab}), shear and acceleration.
2. **Units:** (H), physical vorticity and ordinary angular speed have inverse-time units. If `a` is a dimensionless scale factor, the dimensions of `Omega_U²/a²` can be correct when Ω has inverse-time units. Then the curvature parameter `k` needs corresponding units under the chosen normalization. If `a` carries length units, the interpretation changes. No canonical physical normalization is presently supplied.
3. **Geometry:** In rotating flow do **not** identify the projected rest curvature (mathcal R) with a global slice curvature without a proof.
4. **Matter:** Require Einstein equations, conservation (
abla^a T_{ab}=0), and all remaining shear/vorticity evolution constraints.
5. **Scalar identification:** Choose whether Ω_U means an angular speed, a vorticity *vector* (
abla	imes v), a vorticity 2-form norm, or some genuinely new EFMW field. These are not interchangeable.
6. **Causality:** Gödel is a negative-control geometry, not a template for a physically admissible expanding universe.

## 6. Zoo-style findings

| ID | Finding | Status | Exact interpretation |
|---|---|---|---|
| ROT004-GR-01 | Covariant Gauss scalar identity and FLRW zero-rotation limit | **PASS (sourced + algebraically checked)** | Full GR identity is cited, but not generic-metric kernel formalized |
| ROT004-GR-02 | Matching ME-056 requires shear and projected-curvature bridge | **PASS (necessary algebraic condition)** | Not sufficient for a metric |
| ROT004-GR-03 | Claim that positive Ω²/a² is a universal independent GR correction | **FAIL (unqualified inference)** | Not implied by standard 1+3 equations |
| ROT004-GR-04 | Gödel exact GR rotating, nonexpanding solution | **PASS (SymPy tensor witness after CI)** | Historical GR counterexample, not a cosmological observation |
| ROT004-GR-05 | Direct ME-056 identification with Gödel under k=0, a=1 and Ω²=ω² | **FAIL (conditional mapping)** | Mapping is extra and is not proven general |
| ROT004-GR-06 | A new self-consistent expanding rotating EFMW metric reproducing ME-056 | **UNRESOLVED** | No metric or Einstein-equation closure supplied |
| ROT004-GR-07 | An identifiable new EFMW cosmic observable, compared to Planck-like models | **UNRESOLVED** | No observational likelihood or independent prediction |
| ROT004-GR-08 | A shared scalar/vector/spinor/metric physical generator | **UNRESOLVED** | Clifford representation alone supplies no dynamics |

## 7. Minimal reproduction

Core algebra and necessary-condition checks need only the Python standard library:

```bash
python -m unittest discover -s tests -v
python -m rotation.rot004_covariant
```

Independent four-dimensional exact-metric GR computation:

```bash
python -m pip install sympy==1.14.0
python research/rot004_godel_sympy.py
```

See [Gödel control details](ROT-004_GODEL_CONTROL.md). `PASS_EXACT_GODEL_EINSTEIN_METRIC_COMPUTATION` means the prescribed standard metric passes its GR/dust identities, not that ME-056 has been derived.

The GitHub CI workflow separately runs Python 3.10/3.12 core tests and a pinned SymPy job. Results must be tied to the exact commit when reporting a PASS.

## 8. Next bounded scientific step: ROT-005

**Do not fit an arbitrary `Omega_U` coefficient to cosmological observations yet.**

- Specify an **explicit covariant ansatz** for a rotating, expanding, causally admissible spacetime (or choose a known rotating Bianchi family).
- Compute (G_{ab}), choose a physically motivated (T_{ab}), and verify the off-diagonal Einstein equations, momentum constraints, and matter conservation.
- Calculate the physical observer congruence, shear, vorticity, acceleration, and projected spatial curvature.
- Derive the scalar expansion identity from that metric. If it differs from ME-056, **retain ME-056 as canonical source history** and publish a separately numbered corrected research model.
- Only after a valid metric and identifiable parameter exist, specify an astronomical signature that the standard ΛCDM/FLRW and conventional rotating Bianchi models cannot mimic.
- Commission independent GR and observational review before any detection claim.

**Proposed stop rule:** If every admissible ansatz either requires (omega=0), yields a different sign/scaling, violates GR matter constraints, or cannot distinguish Ω from conventional parameters, record FAIL/UNRESOLVED without forcing the desired formula.

## Final determination

**ROT-004 provides a substantial falsification-oriented result, not a proof of universal rotation.** The canonical proposed quadratic scalar addition cannot be taken as a general consequence of Einstein gravity. Its next legitimate role is to motivate a carefully specified rotating metric or an explicitly non-GR alternative, with predictions and nulls published in advance.

**Attribution:** Original scientific sources credited above. Curated for Matthew Chenoweth Wright / Monolithic LLC with OpenAI assistance. No endorsement from Topher or any cited external author is asserted.
