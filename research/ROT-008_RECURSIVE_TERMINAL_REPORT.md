# ROT-008 — Predictive Recursive Proof Search to Exact Termination

**Monolithic Research · 2026-11-17**  
**Disposition:** **PASS** for reproducible finite recursive proof of unsatisfiability; **FAIL** for the *frozen* minimally coupled Einstein–scalar–Maxwell candidate with real linear scalar `phi(t,x)=ct+dx`; **UNRESOLVED** for richer scalar profiles and theories, and for observed global rotation.

**Frozen prediction file (published before the search code):** [ROT-008_PREDICTIONS_AND_STOP.md](ROT-008_PREDICTIONS_AND_STOP.md).  
**Source implementation:** [rot008_recursive_search.py](rot008_recursive_search.py).  
**Actual executed CI stdout, preserved as a JSON ledger:** [ROT-008_TERMINAL_LEDGER.json](ROT-008_TERMINAL_LEDGER.json).  
**Successful pinned execution:** [GitHub Actions run 44173109860](https://github.com/enuminous/Rotation/actions/runs/44173109860), source revision `e727c93f35cf2d107483081a1020ece8938aa028`.

> **Interpretation:** *Termination* means all allowed branches of the **specific** parameter search are excluded by exact identities. This is not a proof that the universe does not rotate, a solution of all possible scalar field actions, or proof that some other ansatz would be impossible.

## 1. Frozen physical/mathematical system

We did not change the metric or source action after the earlier ROT-007 failure.

The fixed causally admissible Korotkii–Obukhov metric from [ROT-005](ROT-005_KOROTKII_OBUKHOV_BRIDGE.md) is

```text
a(t) = 1+t/2 > 0,  t > -2,
ds² = -(dt + a exp(x/2) dy/10)²
      + a² dx² + (101/100)a² exp(x)dy² + a² dz².
```

The previously declared [ROT-008 protocol](ROT-008_PROTOCOL.md) fixes `κ=8πG=1`, `Λ=0`, signature `(-+++)`, no scalar potential, and the canonical action

```text
S = ∫ sqrt(-g)[R/2 − (1/2)g^ab ∂_a phi ∂_b phi − (1/4)F_ab F^ab] d⁴x
F=dA,   phi = c*t + d*x,   c,d real constants,
A = E(t)exp(x/2)dy + B(t)dz.
```

The allowed adjustable values are the **two real constants `c,d`** and the arbitrary functions `E(t),B(t)` subject to the action's field equations. Allowing a different `phi`, `V(phi)`, `Λ`, additional fields or retuned metric is **a new hypothesis**, not a branch of ROT-008.

## 2. Predictive claim P08-01 — scalar wave equation

The script reconstructs the metric, inverse and volume factor

```text
g^tt=-100/101, g^xx=1/a², g^tx=0,
sqrt(-g)=(sqrt(101)/10) a³ exp(x/2).
```

With `phi=ct+dx`, the canonical scalar Euler–Lagrange equation `Box(phi)=0` gives

```text
Box(phi)
  = 1/sqrt(-g) ∂_a[sqrt(-g) g^ab ∂_b phi]
  = [101*d − 300*c*a(t)]/[202*a(t)²].
```

Since the equation is required for every `t>-2` and `a(t)=1+t/2` changes with time,

```text
101*d − 300*c*a(t) = 0          for all t,
d/dt of the identity: -150*c = 0
thus c=0, and then 101*d=0 -> d=0.
```

**Wave-equation gate:** Its only allowed constant-parameter solution is `c=d=0`. This inference is global over the domain, not a numerically sampled single-time fit.

## 3. Predictive claim P08-02 — Einstein trace

The source-free four-dimensional Maxwell tensor is traceless for all `E,B`:

```text
T^a_a[Maxwell] = 0.
```

The canonical real scalar stress obeys `T^a_a[phi]=-(∇phi)²`. The fixed metric's *independently verified* Einstein trace is

```text
G^a_a = -797/[808*a(t)²].
```

For the linear real scalar,

```text
(∇phi)² = -(100/101)c² + d²/a²,
T^a_a[phi] = (100/101)c² − d²/a².
```

Consequently, a necessary Einstein equation is

```text
G^a_a − T^a_a[phi] − T^a_a[Maxwell] = 0

<=> d² − (100/101)c²*a(t)² = 797/808.
```

The wave equation forces `c=d=0`, but then its left side vanishes while the right side is strictly positive. Therefore **no solution of the full Einstein–scalar–Maxwell field equations exists with the frozen action and real linear scalar ansatz**, regardless of Maxwell amplitudes.

## 4. The recursive proof tree

To reduce the risk of a one-sided algebraic reasoning mistake, the executable checks **both orders of necessary conditions**:

| Branch | Depth | Pruning condition | Deduction |
|---|---:|---|---|
| Wave-first | 0 | Differentiate global wave polynomial | `c=0` |
| Wave-first | 1 | Substitute `c=0` into wave equation | `d=0` |
| Wave-first | 2 | Test Einstein trace at `c=d=0` | **TERMINAL FAIL:** `−797/808 ≠0` after multiplication by `a²` |
| Trace-first | 0 | Differentiate global trace polynomial | `c=0` |
| Trace-first | 1 | Substitute `c=0` into trace equation | `d²=797/808`, so `d≠0` |
| Trace-first | 2 | Test wave equation with that constraint | **TERMINAL FAIL:** wave demands `d=0` |

Machine-executed closure results:

```text
branches_evaluated:       2
nodes_evaluated:          6
terminal_contradictions:  2
maximum_allowed_depth:    6
actual terminal depth:    2 per branch
candidate_verdict: FAIL_FROZEN_ACTION_AND_LINEAR_REAL_SCALAR_ANSATZ
termination: PROVEN_EXACT_UNSAT_FOR_FROZEN_DOMAIN_AND_ANSATZ
```

This is **deterministic symbolic recursion and pruning**, not learning, stochastic evolutionary search, hidden reparameterization, or exploration of all possible field theories. Each branch terminates because it is mathematically unsatisfiable, not because an arbitrary iteration budget was exhausted.

## 5. Controls and prediction adjudication

| Prediction | Result | Interpretation |
|---|---|---|
| P08-01: Global `Box phi=0` requires `c=d=0` | **CONFIRMED** | No nontrivial fixed linear `t,x` scalar wave |
| P08-02: Einstein trace conflicts with `c=d=0` | **CONFIRMED** | Scalar and Maxwell stresses cannot source this metric |
| P08-03: Trace-first instead requires `d²=797/808` | **CONFIRMED** | Incompatible with the wave equation |
| P08-04: `c=d=0` passes wave but fails Einstein; `c=0,d²=797/808` passes Einstein trace but fails wave | **CONFIRMED** | Passing one necessary equation is not enough |
| P08-04: `c=101,d=300` passes wave at `t=0` but fails elsewhere | **CONFIRMED** | Pointwise matching does not prove a spacetime solution |
| P08-05: Both branches terminate at exact contradictions | **CONFIRMED** | Full finite proof-tree closure for the frozen class |

The code also explicitly derives `F=dA`, forms the canonical Maxwell stress from all four coordinates, verifies its zero trace and `dF=0`. The remaining Maxwell equations `∇_aF^{ab}=0` were **not solved**, because the scalar wave equation plus one necessary Einstein equation already make the entire coupled system impossible.

## 6. Engineering provenance: CI iteration without moving the scientific goalposts

The initially published Python proof engine had two narrow **test-harness** defects: `assert expression_a == expression_b` compared structurally different SymPy expressions that are mathematically equivalent. Both were corrected with `sympy.simplify(expression_a-expression_b)==0`. The fixed equations, predictive claims, domain, physical action and source ansatz **never changed**.

- Executed green source revision: `e727c93f35cf2d107483081a1020ece8938aa028`.
- Successful GitHub Actions run: [44173109860](https://github.com/enuminous/Rotation/actions/runs/44173109860).
- The complete computational stdout has been captured in the [machine-readable terminal ledger](ROT-008_TERMINAL_LEDGER.json), including both branches, all six nodes and the negative-control results.
- This verification is a reproducible computation, **not** a proof-assistant kernel theorem or independent PDE/cosmology peer review.

## 7. Essential scope boundary: a broader scalar need not fail these *same two* gates

An important exploratory counter-control demonstrates why ROT-008 is **not a universal scalar no-go**.

If a **separately defined next hypothesis** permits `phi=F(t)+d x`, where `F(t)` is no longer constrained to be linear, then the scalar wave and Einstein trace equations *alone* can be satisfied by

```text
a(t)=1+t/2,
d² = 39850/30199 > 0,
F(t) = (101*d/100) log(a(t)) + C.
```

The wave condition follows from `F'(t)=101*d/(200*a(t))`; substituting this and `d²=39850/30199` into the exact trace relation gives `G^a_a=T^a_a`. This is a direct algebraic counterexample to the **incorrect generalization** “no time-dependent scalar with a spatial gradient can ever pass the trace and wave gates.”

**It is NOT a full Einstein–Maxwell–scalar solution.** None of the other nine independent Einstein component equations or inhomogeneous Maxwell dynamics has been shown to hold for this broader profile. It is not a valid rescue of the frozen ROT-008 test; it must enter a separately labeled later proposal with source and acceptance criteria fixed before execution.

The more general possibility of a compatible matter source and a distinctive observed cosmic rotation signature remains **UNRESOLVED**.

## 8. Zoo summary and next research gate

| ID | Assessment | Scope |
|---|---|---|
| ROT008-PRED-01 | **PASS** | Predictions committed before the new executable |
| ROT008-GR-01 | **PASS** | Fixed KO Einstein trace independently cross-checked |
| ROT008-SCALAR-01 | **PASS** | Exact wave equation of the frozen linear real scalar |
| ROT008-EM-01 | **PASS** | Generic Maxwell stress is trace-free and `dF=0` |
| ROT008-RECURSE-01 | **PASS** | Two independent orders, six steps, terminal contradictions |
| ROT008-SOURCE-01 | **FAIL** | No coupled field-equation solution with `phi=c t+d x`, real constants, frozen action |
| ROT008-MAT-02 | **UNRESOLVED** | Broader `phi=F(t)+d x` satisfying only wave and trace; full Einstein+Maxwell remains open |
| ROT008-OBS-01 | **UNRESOLVED** | No cosmological observation or EFMW-specific prediction |

**Suggested ROT-009:** Freeze `phi(t,x)=F(t)+d x` with the exact logarithmic candidate above as one explicit input, preserve the same canonical scalar–Maxwell action and the same KO metric, then test **all** Einstein components, `\Box\phi=0`, `\nabla_aF^{ab}=0` and `dF=0` with one independently written consistency checker. No arbitrary extra stress tensor, field potential or cosmological parameter retuning permitted. Report mathematical PASS/FAIL/UNRESOLVED without confusing it with astrophysical validation.

## Final determination

**ROT-008 completed its entire frozen recursive search and terminated at a mathematically exact no-go.** The existing canonical Monolithic 102 remains untouched. The broader scientific question is still open; progress consists of replacing a vague scalar-rotation expectation with a sharp, reproducible obstruction and an explicitly delimited next hypothesis.

*Prepared for Matthew Chenoweth Wright / Monolithic LLC with computational assistance. External source authors and Topher have not endorsed these findings. Corrections, counterexamples and independent replay are welcome.*
