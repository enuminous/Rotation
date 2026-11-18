# Rotation experimental program — freeze → predict → test → ablate → reproduce

**Updated 2026-11-18.** ROT-004 through ROT-011 are **completed bounded mathematical investigations** with source-pinned CI; **ROT-001–003 have not undergone full independent confirmatory execution**. No astronomical confirmation of EFMW universal rotation is claimed.

## Completed bounded mathematical investigations

| ID | Evidence | Status and limited result |
|---|---|---|
| ROT-004 | [Covariant GR/Gödel audit](../research/ROT-004_COVARIANT_BRIDGE.md) | PASS for exact Gödel rotating/no-expansion metric and algebra; FAIL for a universally additive standalone ME-056 term; EFMW physical metric UNRESOLVED |
| ROT-005 | [Causal expanding KO metric](../research/ROT-005_KOROTKII_OBUKHOV_BRIDGE.md) | PASS expanding+rotating+stable-causal geometry, Einstein tensor, weak-energy-condition *effective* source; FAIL for explicit natural ME-056 mapping; independent source UNRESOLVED |
| ROT-006 | [Source-first matter audit](../research/ROT-006_SOURCE_FIRST_MATTER_AUDIT.md) | PASS exact simple-spectrum test; FAIL for perfect fluid, one real/two real minimally coupled scalars, and pure Maxwell **as sole source of the fixed KO metric**; coupled field action UNRESOLVED |
| ROT-007 | [Source-first Einstein–scalar–Maxwell test](../research/ROT-007_EINSTEIN_SCALAR_MAXWELL_AUDIT.md) | PASS for exact negative mathematical witness; FAIL for the frozen real homogeneous scalar, V=Lambda=0 and Maxwell fields because the Einstein trace forces a negative real derivative square; richer actions and spatial scalar gradients UNRESOLVED |
| ROT-008 | [Two-branch recursive no-go](../research/ROT-008_RECURSIVE_TERMINAL_REPORT.md) | PASS source-pinned two independent proof orders, six nodes and two terminal contradictions; FAIL for frozen real phi=ct+dx coupled to source-free Maxwell; broader scalar profiles UNRESOLVED |
| ROT-009 | [Source-first logarithmic scalar and full-tensor audit](../research/ROT-009_FULL_TENSOR_AUDIT.md) | PASS wave and Einstein trace, full 10-component residual construction and Maxwell stress identities; FAIL for the frozen complete source because Gxx<0 while real scalar/Maxwell Txx≥0 on both sign branches; other physical matter actions UNRESOLVED |
| ROT-010 | [Unrestricted Maxwell Rainich no-go](../research/ROT-010_RAINICH_ALGEBRAIC_AUDIT.md) | PASS six-component generic and nonzero null-field Maxwell controls; FAIL for **any ordinary real Maxwell 2-form** with the same fixed logarithmic scalar, because S=G−T_scalar violates the squared-tensor Rainich identity by a nonzero exact fraction |
| ROT-011 | [Einstein–Proca strong-energy-condition audit](../research/ROT-011_EINSTEIN_PROCA_SEC_AUDIT.md) | PASS exact timelike Ricci negative witness and arbitrary Proca/Maxwell/scalar energy-condition controls; FAIL for any finite positive combination of canonical Proca, Maxwell, massless real scalars with Λ=0 as the sole source of the selected metric |

All results are scoped to their mathematical hypotheses. A full Einstein-tensor computation does not produce an observed cosmology. A source defined by \(T=G/\kappa\) is not a microphysical model. A result about one metric does not rule out all rotating spacetimes.

## ROT-009 completed: one exact spatial Einstein obstruction

ROT-009 tested the [previously frozen logarithmic scalar candidate](../research/ROT-009_PROTOCOL.md) and verified the source-free scalar wave equation and Einstein trace. The all-component tensor construction then revealed **Gxx=−399/1616<0 versus nonnegative scalar+Maxwell Txx**. Every permitted real sign branch fails with a strictly positive mismatch; see the [report](../research/ROT-009_FULL_TENSOR_AUDIT.md) and [actual CI terminal ledger](../research/ROT-009_TERMINAL_LEDGER.json). This is an *early-stop proof of impossibility* under the frozen action, not a claim that all Maxwell EOM have a simultaneously solved source.

### Next gate — a new independently justified physical source (not selected or run)

Do **not** repair the negative result by adjusting a potential or metric after seeing the obstruction. The next source must be specified in a separate protocol before calculation, with an independently motivated stress that can support the needed directional tension and flux while respecting energy conditions, causality and full matter dynamics. Observational validation remains blocked until a source and uniquely identifiable prediction exist.
## ROT-010 — algebraic termination of Maxwell freedom

ROT-009 excluded a particular Maxwell potential. [ROT-010](../research/ROT-010_RAINICH_ALGEBRAIC_AUDIT.md) tested **every** ordinary Maxwell 2-form algebraically and found a necessary Rainich tensor identity fails for the same frozen scalar and fixed geometry. The exact certificate is \(a^4 Q^{\hat0}{}_{\hat1}=-160795/326432\ne0\), for both scalar signs on the full domain. General six-component and null-Maxwell positive controls passed. The candidate **FAILS** without needing to solve Maxwell differential equations.

**Next physical-source gate (not run):** Specify a new matter action before inspecting tensor residuals, with a principled source of directional stress/flux and an independent observable, or close the frozen model and redirect effort to the already open observational identifiability obligations. Do not silently retune ROT-009/010.
## ROT-011 — SEC gate closes the canonical Proca/Maxwell/massless scalar source class

[ROT-011](../research/ROT-011_EINSTEIN_PROCA_SEC_AUDIT.md) identifies an explicit timelike direction for which the fixed KO Ricci tensor is negative, while standard real Proca with \(\mu^2\ge0\), Maxwell, and massless real scalar sources obey SEC for **all** real field profiles. Both the pure-Proca and combined canonical source possibilities terminate at the same exact contradiction, without Proca ODE fitting. The result holds only for the frozen metric, \(\Lambda=0\), and positive-kinetic matter in the named class. It does **not** exclude other spacetimes or source actions.

**Next gate (not executed):** Require independent motivation for an SEC-violating source, positive scalar potential, nonzero cosmological constant, or a different rotating spacetime. Do not retrofit matter to the old KO metric and claim a sourced cosmological theory. Any new experiment must define an observable that distinguishes rotation from curvature.
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
| Logarithmic real scalar plus the frozen Maxwell potential | **FAIL (ROT-009)** | Wave/trace PASS; negative Einstein Gxx conflicts with nonnegative Txx for both signs of d |
| Frozen logarithmic real scalar with **arbitrary ordinary Maxwell tensor** | **FAIL (ROT-010)** | Traceless candidate stress fails classical squared-tensor Rainich identity |
| Standard positive-kinetic real Proca (alone or with canonical Maxwell/massless real scalars), Λ=0 | **FAIL (ROT-011)** | Ricci(v,v)<0 for a timelike observer, but permitted source SEC(v,v)≥0 |
| Independently derived viable EFMW matter source | **UNRESOLVED** | Full field action and exact stress tensor |
| EFMW-unique identifiable rotational observable | **UNRESOLVED** | Prediction beyond curvature/ordinary models |
| Current Planck-compatible astronomical fit | **UNRESOLVED** | Reproducible likelihood and constraints |
| Sealed independent observational validation | **UNRESOLVED** | Predefined comparison and custodian |

See [cosmic evidence and constraints](COSMOLOGY.md) and [open research obligations](OPEN_QUESTIONS.md).
