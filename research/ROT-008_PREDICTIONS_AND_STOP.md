# ROT-008 — Frozen predictions, stopping policy, and branches

**Predictive commitment before execution of this version's new ROT-008 code (2026-11-17).** This is an *exploratory mathematical test*: the experimenter has inspected the fixed metric and ROT-007 result. It is not a sealed external preregistration or a blind observational experiment.

## Immutable inputs

- The [ROT-008 protocol](ROT-008_PROTOCOL.md) freezes the metric, gravity+massless-real-scalar+Maxwell action, and ansatz **phi = c*t + d*x** with real constants c,d.
- **No** scalar potential, nonminimal coupling, cosmological constant, scalar functional freedom, metric retuning or arbitrary extra stress tensor.
- Gauge potential remains A=E(t)*exp(x/2)dy+B(t)dz, with arbitrary E(t),B(t). The classical Maxwell field has exactly vanishing stress trace in four dimensions.
- Physical domain t>-2; a(t)=1+t/2>0. Exact symbolic identities are required for **all** points, not finite sampled values.

## Predictions made before running new ROT-008 executable

1. **P08-01 (scalar propagation):** For the frozen metric and scalar ansatz, Box(phi) factors to `(101*d - 300*c*a)/(202*a^2)`. It cannot vanish on the entire domain except when `c=d=0`.
2. **P08-02 (Einstein trace):** `G^a_a=−797/(808*a^2)`; ordinary Maxwell contributes `0`, and `T_scalar^a_a=(100/101)*c^2-d^2/a^2`. At `c=d=0`, the source trace is zero, contradicting Einstein's equation for all a>0.
3. **P08-03 (independent obstruction):** The trace at variable a alone gives `d^2 − (100/101)*c^2*a^2 = 797/808`; for constant c,d on a nontrivial time interval this requires `c=0`, `d^2=797/808`. This trace-only branch is incompatible with scalar propagation, which at c=0 requires d=0.
4. **P08-04 (null and positive controls):** Setting `c=d=0` solves Box(phi) but **not** the Einstein trace. At `c=0, d^2=797/808`, the Einstein trace matches but Box(phi) does **not**. A hand-selected time `t=t_0` may satisfy propagation for a nonzero `c,d`, but that is **not** an everywhere spacetime solution.
5. **P08-05 (terminal rule):** Stop as soon as **two independent exact necessary conditions exclude all parameter branches**. Do not solve Maxwell dynamics if the Einstein+scalar system is already inconsistent. Do not mutate the fixed action/metric/ansatz.

## Recursive branch/prune design

```text
root: real constants (c,d)
    |
    +-- wave equation for every t
    |       differentiate fixed relation in t: c = 0
    |       substitute: d = 0
    |       test trace: contradiction R > 0
    |
    +-- Einstein trace for every t
            differentiate fixed relation in t: c = 0
            substitute: d² = 797/808 (d nonzero)
            test wave: contradiction
```

The two branches are deliberately different orderings of independent necessary conditions, not stochastic search iterations. Their exact contradictions terminate the current protocol; there is no legitimate reason to recurse forever.

## What counts as closure

- **PASS for proof search, FAIL for candidate:** SymPy reproduces predictions P08-01–05, checks full algebraic identities, and writes a deterministic JSON terminal ledger with both pruning certificates and a non-overstated scientific status.
- **UNRESOLVED:** code fails / a stated identity does not verify; do not translate a build failure to scientific FAIL.
- **No universal no-go:** `phi=F(t)+d*x`, `phi=F(t)+G(x)`, nonminimal kinetic/curvature couplings or new matter actions are **new hypotheses**, not alternative branches within the frozen ROT-008 protocol.

Source: [ROT-005](ROT-005_KOROTKII_OBUKHOV_BRIDGE.md), [ROT-007](ROT-007_EINSTEIN_SCALAR_MAXWELL_AUDIT.md).
