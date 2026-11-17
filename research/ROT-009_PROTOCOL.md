# ROT-009 — Proposed source-first logarithmic scalar continuation

**EXPLORATORY PROTOCOL; NOT RUN.** Prepared on November 17, 2026 *after* the ROT-008 exact linear-ansatz failure. This is not an independent sealed preregistration.

## Frozen candidate for the next experiment

Preserve exactly the same Einstein–massless-real-scalar–Maxwell action, zero scalar potential, zero Λ, κ=1, and fixed causally admissible ROT-005 Korotkii–Obukhov metric:

```text
a(t)=1+t/2>0, t>-2,
phi(t,x)= (101*d/100)*ln(a(t)) + d*x,
d²=39850/30199 > 0; choose and retain both real sign branches,
A=E(t)*exp(x/2)dy+B(t)dz.
```

A direct independent symbolic substitution shows **only**:

```text
Box(phi)=0,
R=(grad phi)² = 797/(808a(t)²).
```

This is already-known necessary-condition calibration, **not** a PASS of Einstein's equations or Maxwell's dynamical field equations.

## Predictive sequence and termination

1. Recompute metric and full Einstein tensor (not substitute an a posteriori matter tensor).
2. Recompute the scalar stress of the **fixed** action, then Maxwell field strength and stress with E(t),B(t) unspecified.
3. Check the *full* ten Einstein tensor equalities, including every off-diagonal component. Use exact algebraic elimination; preserve all constraints and field variables.
4. Check the scalar Euler–Lagrange equation independently of the prior calibration; check both Maxwell equations `dF=0` and `nabla_a F^{ab}=0`, as well as conservation.
5. Branch only over the two frozen signs of d and actual allowed solutions of E(t),B(t); do not change the metric, add a scalar potential, tune Λ, or invent a new source term.
6. Stop with **PASS** only for a complete real solution of *all* coupled equations; **FAIL** if every allowed branch has an exact contradictory necessary condition; otherwise report **UNRESOLVED** with the precise surviving obligations.

## Scientific limit

Even a sourced exact rotating metric is *not* proof of universal rotation in the observed universe. ME-056 has a curvature/rotation identifiability issue; any future physical claim needs a separate, independently identifiable observational prediction and calibration against standard GR cosmologies.

See [ROT-008 terminal report](ROT-008_RECURSIVE_TERMINAL_REPORT.md) and [ROT-005 fixed geometry](ROT-005_KOROTKII_OBUKHOV_BRIDGE.md).
