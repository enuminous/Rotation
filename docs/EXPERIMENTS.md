# Rotation experimental program — freeze → predict → test → ablate → reproduce

**Updated 2026-11-17.** ROT-004 through ROT-008 are **completed bounded mathematical investigations** with source-pinned CI; **ROT-001–003 have not undergone full independent confirmatory execution**. No astronomical confirmation of EFMW universal rotation is claimed.

## Completed bounded mathematical investigations

| ID | Evidence | Status and limited result |
|---|---|---|
| ROT-004 | [Covariant GR/Gödel audit](../research/ROT-004_COVARIANT_BRIDGE.md) | PASS for exact Gödel rotating/no-expansion metric and algebra; FAIL for a universally additive standalone ME-056 term; EFMW physical metric UNRESOLVED |
| ROT-005 | [Causal expanding KO metric](../research/ROT-005_KOROTKII_OBUKHOV_BRIDGE.md) | PASS expanding+rotating+stable-causal geometry, Einstein tensor, weak-energy-condition *effective* source; FAIL for explicit natural ME-056 mapping; independent source UNRESOLVED |
| ROT-006 | [Source-first matter audit](../research/ROT-006_SOURCE_FIRST_MATTER_AUDIT.md) | PASS exact simple-spectrum test; FAIL for perfect fluid, one real/two real minimally coupled scalars, and pure Maxwell **as sole source of the fixed KO metric**; coupled field action UNRESOLVED |
| ROT-007 | [Source-first Einstein–scalar–Maxwell test](../research/ROT-007_EINSTEIN_SCALAR_MAXWELL_AUDIT.md) | PASS for exact negative mathematical witness; FAIL for the frozen real homogeneous scalar, V=Lambda=0 and Maxwell fields because the Einstein trace forces a negative real derivative square; richer actions and spatial scalar gradients UNRESOLVED |
| ROT-008 | [Two-branch recursive no-go](../research/ROT-008_RECURSIVE_TERMINAL_REPORT.md) | PASS source-pinned two independent proof orders, six nodes and two terminal contradictions; FAIL for frozen real phi=ct+dx coupled to source-free Maxwell; broader scalar profiles UNRESOLVED |

All results are scoped to their mathematical hypotheses. A full Einstein-tensor computation does not produce an observed cosmology. A source defined by \(T=G/\kappa\) is not a microphysical model. A result about one metric does not rule out all rotating spacetimes.

## Next proposal: ROT-009 — one new scalar-profile hypothesis (UNRUN)

**ROT-008 is complete as a finite deterministic FAIL**, with [machine-captured execution ledger](../research/ROT-008_TERMINAL_LEDGER.json). Its source action and predictions were preserved during recursive search. Stop rules were triggered by exact mathematical contradictions, not exhausted iteration counts.

A new separately scoped candidate uses the same minimal massless scalar plus Maxwell action and the same fixed metric, but allows \(\phi(t,x)=(101d/100)\log a(t)+dx\) with \(d^2=39850/30199\). This passes the **two necessary wave/Einstein-trace equations** only. ROT-009 must test all remaining Einstein, scalar and Maxwell equations without adding a potential, cosmological constant, or retrofitted source tensor. [Proposed protocol](../research/ROT-009_PROTOCOL.md).

## Independent baseline tracks still open

### ROT-001 — mathematical normalization and degeneracy

Compare angular speed with curl of the rigid flow and the ME-056 scalar parameter under exact stated assumptions. Controls: \(\omega=0\), \(\omega\leftrightarrow-\omega\), gradient field with zero curl, and distinct \((k,\omega)\) pairs with the same \(k-\omega^2\). The existing Python lab and Lean sources provide partial analytic test fixtures, not an independently replayed full theorem/physics suite.

### ROT-002 — scalar phase topology versus ordinary fluid vorticity

Compare an ordinary real scalar, ordinary complex field, scalar with U(1) gauge connection, and 3-D velocity flow. Freeze zero-winding controls, nodal phase defects, pure gauge, and irrotational velocity. Record integer winding, gauge-covariant circulation, and whether nonzero material vorticity follows. Do not promote internal phase rotation into cosmic vorticity.

### ROT-003 — observational global-vorticity test (UNRUN)

**H0:** ΛCDM/FLRW with calibrated observational systematics.  
**H1:** A specific physically complete rotating Einstein metric with an independently derived matter source and a measurable vorticity parameter.  
**H2:** Conventional Bianchi/shear/curvature, polarization propagation, and selection-effect alternatives.

**Before opening a holdout:** specify CMB observables or another primary dataset, physical parameter priors, nuisance systematics, sky masks, look-elsewhere corrections, model complexity penalty, uncertainty interval and independent custody. A nonzero rotating-model parameter must add predictive value beyond both H0 and H2 and remain consistent with applicable Planck constraints.

**Null:** H1 does not outperform the baselines, inferred parameter tends to zero, or the effect disappears with a blinded sky split or calibration change.  
**Stop:** missing metric/source equations, nonidentifiability, leak or retuning, energy-condition or stability inconsistency, failure to replicate.

## Custody and publication rules

- Preserve the frozen canonical Monolithic 102, and place proposed corrections in separately versioned research artifacts.
- Record exact commits, code, dependencies, all nulls and counterexamples; source-linked data does not imply external validation.
- Distinguish mathematical identity, source feasibility, observational inference and independent replication.
- State an explicit negative result as FAIL only for the assumptions actually refuted; elsewhere use UNRESOLVED.
- A public CI PASS certifies the scripted computation, **not** empirical universal rotation.

## Gates for a novel physical theory

| Gate | Status | Evidence required |
|---|---|---|
| Specific GR geometries showing local covariant rotation | **PASS (ROT-004/005 examples)** | Reproducible Einstein tensors; examples not novel |
| One- or two-scalar *sole* source for frozen ROT-005 | **FAIL (ROT-006)** | Exact tensor spectrum; limited no-go |
| Homogeneous real scalar plus standard Maxwell under frozen minimal action | **FAIL (ROT-007)** | Einstein trace contradiction for this fixed KO metric |
| Linear real scalar in time and space plus Maxwell | **FAIL (ROT-008)** | Wave and Einstein trace cannot both hold for constants c,d |
| Independently derived viable EFMW matter source | **UNRESOLVED** | Full field action and exact stress tensor |
| EFMW-unique identifiable rotational observable | **UNRESOLVED** | Prediction beyond curvature/ordinary models |
| Current Planck-compatible astronomical fit | **UNRESOLVED** | Reproducible likelihood and constraints |
| Sealed independent observational validation | **UNRESOLVED** | Predefined comparison and custodian |

See [cosmic evidence and constraints](COSMOLOGY.md) and [open research obligations](OPEN_QUESTIONS.md).
