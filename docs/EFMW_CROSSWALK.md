# Canonical Monolithic 102 → rotation evidence crosswalk

**Do not change** ME-001..ME-102 numbering or upgrade a source equation's epistemic status. This atlas is a separate hypothesis and research layer.

| Source | Actual content | Relevant mathematical bridge | Not established |
|---|---|---|---|
| [ME-016](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/016.md) | ψ=ρe^{iθ} | Internal complex phase and winding | A single phase for the observed universe |
| [ME-018](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/018.md) | J^μ=ρ²∇^μθ | Real/imaginary current decomposition under conventions | Directly observed gravitational rotation |
| [ME-019](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/019.md) | ∇_μJ^μ=0 | Continuity of the chosen current | Unconditional conservation for all proposed couplings |
| [ME-020/021](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/020.md) | Madelung Hamilton–Jacobi and quantum potential | One-dimensional specialized formal identities | 3+1 universal-gravity theory |
| [ME-055](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/055.md) | Ω_U=∇×v_U | Vorticity definition for a specified velocity field | Existence or measurement of v_U for cosmic matter |
| [ME-056](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/056.md) | H²=8πGρ/3+Λ/3−k/a²+Ω_U²/a² | Analyzed positive-a scalar equation, normalization, sign and degeneracy | Derivation from covariant rotating Einstein spacetime |
| [ME-077](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/077.md) | Generalized momentum/stress | Chosen Cartesian nonrelativistic specialization | Complete relativistic, incompressible regularity theorem |
| [ME-078](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/078.md) | η(t)=η₀(1−e^{−t/τ}) | Time-varying viscosity model | Uniform η>0 at t=0 |
| [ME-080](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/080.md) | ∂_tρ+div(ρu)=0 | Standard mass-conservation equation | Cosmic rotation |
| [ME-081](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/081.md) | Suggested stress tensor | Constitutive relation to be specialized | Valid thermodynamic relativistic closure |
| [ME-082](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/082.md) | dη/dt=(η_eq−η)/τ | If η(0)=η_eq>0, constant viscosity is a solution | Proof of any all-data continuation estimate |

## Linked formal mathematics

- [Vorticity.lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/Vorticity.lean): real three-space curl/divergence, product rules, rigid rotation; actual differentiability assumptions.
- [RotationKinematics.lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/RotationKinematics.lean): 2-D complex structure, SO(3) fixed-axis action, curl=2ω; conditional limits.
- [RotatingCosmology.lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/RotatingCosmology.lean): positive-scale scalar equation, k−ω² degeneracy, sign and branch ambiguity, model solutions.
- [Fluids.lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/Fluids.lean): continuity, stress, variable-viscosity product rule, nonrelativistic specialization and explicit counterexample.
- [Madelung.lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/Madelung.lean): specialized flat wave-to-phase identities.
- [ROTATION_COSMOLOGY.md](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/ROTATION_COSMOLOGY.md): explicit status and limitations.

## Three bridges worth separately testing

### B1. Rigid local motion ↔ ME-055

Let v=(-ω y,ω x,0). Then curl v=(0,0,2ω). If the scalar ω in ME-056 means *angular speed* while |Ω_U| means *vorticity magnitude*, then ω²=|Ω_U|²/4. This is an **explicit normalization choice**. No actual cosmological matter observer field has been measured by this identity.

### B2. Scalar ME-056 term ↔ curved-space geometry

Rewrite

```text
H² = A − (k−ω²)/a²
k_effective = k−ω²
```

The scalar H² relation alone cannot distinguish k from ω²; at a fixed scale, ω and −ω are also indistinguishable. The source Lean work proves these algebraic facts. A new cosmic-rotation model must define a rotating metric, congruence uᵃ and invariant vorticity, derive the expansion relation and distinguish the parameters using additional observables.

### B3. Fluid ME-077–082 ↔ fixed-viscosity 3-D Navier–Stokes

In the **chosen nonrelativistic Cartesian specialization**, at positive constant density ρ_*, zero external forcing, divergence-free velocity and constant η>0,

```text
∂_t u+(u·∇)u = −∇p+νΔu,   p=P/ρ_*,   ν=η/ρ_* > 0
```

This is the conventional incompressible Navier–Stokes equation; it does **not** derive the nonrelativistic limit from the original relativistic ME-077. It supplies an exact consistency target for a future formal bridge to [BSA-R](BSAR_BRIDGE.md).

## Scope warning

A theorem about the formal **specialization** does not prove the original relativistic statement. A theorem about a deliberately chosen scalar expansion equation does not prove it follows from Einstein's equations. Source-level Lean hygiene and past reported builds should not be presented here as a fresh independent kernel replay.

**Suggested work product:** a small pair of Lean theorems (i) reducing ME-077's specified Cartesian residual to standard NS under explicit assumptions, and (ii) deriving the standard vorticity evolution equation with every differentiability and boundary condition visible. No claim of 3-D global regularity is attached.
