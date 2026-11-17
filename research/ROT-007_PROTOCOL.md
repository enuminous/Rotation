# ROT-007 — Candidate minimally coupled Einstein–scalar–Maxwell source test

**PROPOSED / UNRUN (2026-11-17)**. This is an **exploratory protocol written after seeing the fixed ROT-005 metric**, not a sealed preregistration and not evidence of a sourced cosmology.

## Frozen question

Can ordinary canonical scalar matter **plus** an independently dynamical Maxwell field supply the full Einstein stress required by ROT-005, while satisfying *both* matter field equations?

The restricted no-go in [ROT-006](ROT-006_SOURCE_FIRST_MATTER_AUDIT.md) excludes each component **by itself**; it does **not** exclude their sum. Coupled sources can have richer stress spectra, but that is only a possibility.

## Fixed action, no adjustable extra anisotropic stress

Use units \(c=1\), \(\kappa=8\pi G=1\), \(\Lambda=0\), signature \((-+++)\):

```text
S[g,phi,A] = ∫ sqrt(-g) [
    R/2 - (1/2) g^ab ∂a phi ∂b phi
        - (1/4) F_ab F^ab
] d^4x,    F_ab = ∂a A_b − ∂b A_a.
```

No scalar potential, hidden fluid, metric-dependent counterterm, hand-selected stress tensor, or post hoc coupling coefficient is permitted for this first exploratory candidate.

Metric variation implies:

```text
G_ab = T(phi)_ab + T(EM)_ab
T(phi)_ab = ∂a phi ∂b phi − (1/2) g_ab (∇phi)^2
T(EM)_ab = F_ac F_b^c − (1/4)g_ab F_cd F^cd.
```

Field equations:

```text
Box phi = 0
nabla_a F^ab = 0
dF = 0 (since F=dA).
```

## Initial restricted symmetry-compatible ansatz

On the fixed [KO metric](ROT-005_KOROTKII_OBUKHOV_BRIDGE.md), take:

```text
phi=phi(t)
A = E(t) exp(x/2) dy + B(t) dz.
```

Here \(E(t),B(t),\phi(t)\) are unknown functions subject to the equations, **not** adjustable parameters that may be hand-tuned to match only a subset of Einstein components. Restriction to this ansatz is a deliberate scope choice: its failure does not exclude every scalar–Maxwell field configuration.

## Verification order

1. Derive stress and field equations from the fixed action; independently verify covariance, index signs and metric variation.
2. Recompute all 10 symmetric Einstein components for the existing metric.
3. Substitute the ansatz, derive and solve/obstruct every Einstein component including off-diagonal entries.
4. Independently check scalar wave and Maxwell equations, Bianchi identities, conservation and boundary/domain conditions.
5. If exact matching is possible, evaluate weak/dominant energy conditions, hyperbolicity, perturbative modes and any divergences at \(t=-2\).
6. Repeat with a freely selected observer to ensure no result depends on a coordinate basis artifact.
7. If a complete solution is found, test its no-rotation limit and explicitly derive the expansion relation; no assumption of ME-056 allowed.
8. Only if a unique physical rotation parameter survives these constraints, design a separate sealed observational test.

## Disposition

- **PASS:** an exact scalar–Maxwell solution satisfying the **entire** coupled system on the frozen geometry, with source constants fixed as above. This would be a mathematical source construction, not a detection.
- **FAIL:** an explicit contradiction for the frozen action and ansatz, with a source-pinned algebraic witness.
- **UNRESOLVED:** partial equations, untested numerical fits or omitted components.

**No source-by-metric substitution:** Defining \(T=G\) and then calling the matrix a 'scalar–Maxwell fluid' fails this protocol.

## References

- [ROT-005 exact metric and source](ROT-005_KOROTKII_OBUKHOV_BRIDGE.md)
- [ROT-006 source exclusion](ROT-006_SOURCE_FIRST_MATTER_AUDIT.md)
- [Scalar-source conditions](../docs/SCALAR_FIELDS.md)

Any attempt to expand beyond this action must be declared in a **separate versioned** candidate, not silently retuned after seeing a failure.
