# ROT-008 — Proposed inhomogeneous scalar test (not run)

**Draft test protocol, November 17, 2026.** This proposal was written **after** the ROT-007 homogeneous scalar failure. It is not an independently sealed preregistration, a completed test, or a discovered source of cosmological rotation.

## Freeze the change

Keep the ROT-007 action and the ROT-005 metric **unchanged**:

```text
S = ∫ sqrt(-g) [R/2 - (1/2)(grad phi)^2 - (1/4)F²] d⁴x
Lambda = 0; V(phi) = 0; kappa = 1;
a(t) = 1+t/2 > 0; t > -2.
```

Change **only** the scalar ansatz from `phi=phi(t)` to the simplest explicit spacetime-dependent profile:

```text
phi(t,x) = c*t + d*x,   with real constants c,d.
A = E(t)*exp(x/2) dy + B(t) dz, as in ROT-007.
```

This gives `(grad phi)^2` a spatial component and can evade ROT-007's immediate sign obstruction. It is **not** a guarantee of full Einstein-equation solvability.

## Acceptance checks

1. Independently compute the full stress tensor from the frozen scalar and Maxwell actions.
2. Derive all ten Einstein equations on the fixed KO background; first test the trace and then the off-diagonal components.
3. Enforce `Box(phi)=0`, `nabla_a F^{ab}=0`, and `dF=0` *for the same functions*.
4. Solve or obtain an exact algebraic contradiction for the constants and field functions; do not retune the metric or add a potential.
5. If a mathematical solution exists, examine stress energy conditions and perturbative stability separately. Do not infer an EFMW physical mechanism from a model fit alone.

**PASS:** full exact coupled solution with all field equations and fixed assumptions.  
**FAIL:** a necessary Einstein or matter equation is impossible for this proposed class, with a reproducible witness.  
**UNRESOLVED:** the available implementation fails to establish either outcome.

A separate potential, nonminimal coupling, or added matter component requires a *new numbered candidate*; do not silently change this frozen proposal.

**Purpose:** narrow a physically meaningful source theory without claiming observed universal rotation.
