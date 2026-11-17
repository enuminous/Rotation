# Field atlas — rotation by mathematical and physical sector

This is **broad, not exhaustive**. “All fields” in the title of a research question means *test as many field classes as are relevant*, not assert a universal law before their observables agree. The evidence register tracks explicit limitations and primary-source anchors.

| Sector | Appropriate rotational quantity | Demonstrated fact | What it does **not** mean |
|---|---|---|---|
| Smooth real scalar | dφ and Hessian; SO(3) acts by pullback on arguments | d²φ=0; constant scalar is a null | An intrinsic nonzero angular velocity |
| Complex scalar | Phase arg ψ, U(1) winding n | Integer winding on loops avoiding zero | Cosmic spacetime vorticity |
| Classical vector | SO(3) action, curl u, circulation | Rigid-body curl=2ω | Every vector field has curl |
| Rank-2 tensor | Symmetric strain, antisymmetric part, rotated basis | Tensor transformations under spatial rotations | All tensor components co-rotate physically |
| Spinor | Spin(3) / SU(2), double cover | 4π spinor response in interferometry | Global frame dragging |
| Gauge connection | Curvature F=dA+A∧A; Wilson-loop holonomy | Nontrivial local/gauge-invariant holonomy | Single absolute gauge-independent phase angle |
| Classical fluid | Vorticity ω=∇×u | Eddies, vortices, rigid kinematic solutions | Uniform nonzero cosmic vorticity |
| Quantum fluid | Winding / vortex lines / flux circulation | Quantized BEC vortices observed | All scalar fields are superfluids |
| Electromagnetism | Circular polarization, Faraday rotation, optical OAM | Polarization angle evolves in media | Cosmic metric itself rotates |
| Relativistic matter | Vorticity 2-form of uᵃ congruence | Defined covariantly after choosing uᵃ | Every foliation has same vorticity |
| Gravity around a body | Frame dragging / Kerr spin | Earth dragging and rotating BH models/data | Rotation of the universe |
| Cosmological geometry | Bianchi shear/vorticity and null-geodesic imprint | Planck puts strong constraints on selected rotating models | Detection of nonzero cosmic rotation |
| Galaxy observations | Projected apparent spiral handedness | Galaxies often have spin; 2025 reported sample imbalance | Invariant cosmic congruence rotation |
| Pure Clifford algebra | Bivectors, rotors, Spin↔SO map | Exact math, not contingent on an experiment | Universal shared physical rotation |

## Important separations

### Spin versus orbit versus vorticity

Quantum spin is a representation of spacetime rotational symmetry, not a little sphere necessarily spinning on an axis. Orbital angular momentum of stars/galaxies is not by itself spacetime congruence rotation. Vorticity is a differential property of a velocity field, not a property every field has.

### Polarization rotation versus angular rotation

A Faraday angle rotates electromagnetic **polarization** as light propagates through plasma. The observed azimuthal EHT polarization pattern near M87* probes local fields and matter, not a universal fluid-vorticity measurement: [EHT 2021](https://doi.org/10.3847/2041-8213/abe4de).

### Tensor strain versus material spin

The velocity gradient decomposes into symmetric stretching/strain and an antisymmetric local rotation. Neither one equals angular momentum without geometry, material definition and boundary conditions. This distinction is central to [Fluids.lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/Fluids.lean).

### No single global axis is required for every definition

Local vorticity can be nonzero without a shared axis throughout a curved spacetime. Conversely a visual preferred axis in galaxy counts could be observational selection, not a covariant cosmic vorticity. A proposal must state which coordinate-free observable it predicts.

## Evidence by category

Use [data/evidence.json](../data/evidence.json) and [data/sources.json](../data/sources.json). The registry distinguishes:
- mathematically true statements and model-formalized conditional theorems,
- measured local effects,
- cosmology model constraints,
- contested candidate patterns,
- EFMW and other untested theoretical models,
- concrete nulls and missing derivations.

A proposal to make “universal rotation” a law must replace **cross-field analogy** with actual **field equations and jointly predicted observables**.
