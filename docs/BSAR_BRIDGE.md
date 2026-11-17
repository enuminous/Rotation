# A possible Wright–Duguay mathematical bridge — research proposal, not joint endorsement

This note connects **Monolithic 102's Cartesian fluid/vorticity work** with the open obligations in Christopher "Topher" Duguay's BSA-R Navier–Stokes study. **No joint proof, agreement, endorsement or commissioned audit is claimed.**

## Different starting points

| Wright / Monolithic | Duguay / BSA-R |
|---|---|
| ME-055 curl definition; ME-077–082 fluid relations; mathematical 3-D Cartesian specializations | Incompressible 3-D Navier–Stokes with fixed positive viscosity on a periodic torus |
| Lean formalizations of standard vector calculus, strain, viscosity and continuity | Lean conditional integer algebra and computational interval certificates |
| ME-056 proposed cosmological rotation parameter; not a GR rotating metric | Step 7 analyzes vorticity direction ξ=ω/|ω| and a conditional cone criterion |
| No proven global continuation | No independent proof of the open S2-CONE-INTEGRABILITY lemma |

## Exact overlap

The incompressible constant-ρ, constant-η, unforced specialization of the Monolithic Cartesian residual yields

```text
∂_t u + (u·∇)u = −∇(P/ρ_*) + (η/ρ_*) Δu.
```

The curl identities then point to the conventional vorticity evolution equation (for sufficiently smooth divergence-free flow):

```text
∂_t ω + (u·∇)ω = (ω·∇)u + νΔω.
```

This second equation should be fully formally established in the shared 3-D function-space setting; it is **not** a newly verified Lean theorem from this atlas.

Topher's open mathematical step is an unconditional a priori estimate on the *direction* of ω. His [Round 6 collaborator document](https://github.com/VivienSweetbrier/bsa-r/blob/main/navier_stokes/ROUND6_COLLABORATOR_SPEC.md) calls this `S2-CONE-INTEGRABILITY`: integrated control of a high-vorticity C^{1/2} direction-cone parameter. A conditional integer inequality with the cone bound already assumed cannot deliver that missing estimate.

## Proposed scoped work plan

1. Fix the exact smoothness, torus domain, viscosity, density, forcing and norm conventions.
2. Prove the momentum → vorticity identity in Lean or reproduce it in a separate independently reviewed PDE formalization.
3. Identify which Step 7 premises are physical PDE estimates and which are algebraic hypotheses.
4. Try to derive a **closed** upper bound on the required cone quantity for all eligible solutions, or construct a counterexample to any proposed intermediate inequality.
5. Record any unproved step as `UNRESOLVED` and publish negative controls.

### Recommended independent verification artifact

| Deliverable | PASS | FAIL | UNRESOLVED |
|---|---|---|---|
| Source-to-equation crosswalk | Same function spaces and equations from assumptions | Normalization/sign mismatch with a counterexample | Missing formalized definitions |
| Vorticity equation theorem | Kernel checked, no gap, explicit regularity | Concrete counterexample to claimed theorem | Build/assumption not closed |
| Cone criterion bridge | Independently derived all-solution estimate | Inequality refuted by valid flow | Estimate remains an explicit hypothesis |

No payment, customer, or agreement is presumed. A bounded Monolithic technical audit requires mutual written scope and compensation terms separately.

## Sources

- [Monolithic analysis/Fluids.lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/Fluids.lean)
- [Monolithic analysis/Vorticity.lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/Vorticity.lean)
- [BSA-R Round 6 source](https://github.com/VivienSweetbrier/bsa-r/blob/main/navier_stokes/ROUND6_COLLABORATOR_SPEC.md)
- [Existing independent Zoo source-audit mirror](https://github.com/enuminous/bsa-r/tree/main/audits/2026-11-17-monolithic-zoo)
