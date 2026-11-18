# Scalar field rotation: what is possible, and what is not

The scalar sector is the easiest place to distinguish **real physical rotational evidence** from overbroad language.

## A. Ordinary smooth real scalar φ

A scalar field φ:M→ℝ assigns a number to each spacetime point. It does not transform as a spatial vector under an active SO(3) rotation. Its gradient is a vector or 1-form; its second exterior derivative vanishes:

```text
d(dφ) = 0
curl(grad φ) = 0   (in Euclidean 3-D, provided appropriate C² smoothness)
```

A constant scalar is a complete counterexample to the literal “every scalar rotates nontrivially” claim. A nonconstant φ may describe a circularly *arranged* level set without carrying material vorticity or angular momentum.

## B. Complex scalar ψ=ρe^{iθ}

ME-016 supplies ψ=ρe^{iθ}. On a loop around a defect, if ψ never vanishes on that loop, θ can wind by 2πn, n∈ℤ. For a local illustrative profile, ψ(r,φ)=f(r)e^{inφ}, with f(0)=0 for n≠0 and f(r)>0 for r>0. A punctured loop has nonzero integer winding while the field may be continuous at its zero.

Our standard-library toy computes n from phase-difference sums and checks n=0,±1,±2; it does not simulate Schrödinger/Klein–Gordon time evolution.

In ordinary (non-gauge) Madelung hydrodynamics, if a nonzero complex wave has phase θ, its current can be proportional to ρ²∇θ, subject to the physical constants and equation used. **A circulating current is not inferred from the existence of an arbitrary phase decomposition**.

## C. Gauge dependence

With a local U(1) gauge field, a transformation θ→θ+qχ, A→A+∇χ makes ∇θ−qA the gauge-invariant combination in the appropriate conventions. A bare ∇θ is not in general a directly measurable absolute rotation. Aharonov–Bohm holonomy and quantized magnetic flux are related geometric mechanisms with separate sources and hypotheses.

## D. Time-phase versus spatial winding

A homogeneous field ψ(t)=ρexp(iωt) rotates in an *internal phase plane* at frequency ω while having zero spatial vorticity. A spatial vortex ψ(x,y) can have phase winding without the entire universe rotating. Conversely, a rotating fluid can be described without an underlying scalar-phase vortex.

| Model | Winding on spatial loop | Spatial fluid vorticity | Global cosmological vorticity |
|---|---|---|---|
| φ=C, real | not applicable | not implied | not implied |
| ψ(t)=ρe^{iωt} | zero | not implied | not implied |
| ψ=f(r)e^{inφ}, n≠0 | n | model-dependent circulation | not implied |
| rigid u=(-ωy,ωx,0) | scalar phase unnecessary | 2ω z-direction | not implied |

## E. Existing EFMW formal work

- [ME-016](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/016.md) (amplitude/phase)
- [ME-018](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/018.md) (current)
- [ME-019](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/019.md) (continuity)
- [Madelung.lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/Madelung.lean) and [its scope report](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/MADELUNG.md)

Madelung formalization is specialized to flat 1+1 dimensions and explicitly tracks nonzero-amplitude assumptions where needed. It does not establish a smooth global phase reconstruction or a physical cosmological rotation.

## Open test

Construct a **gauge-invariant and observer-invariant** proposed EFMW scalar rotation observable, with a distinct prediction not already implied by conventional complex-field phase dynamics. Compare the predicted signal with a matched conventional scalar model **before** seeing the data. If no distinct prediction exists, this strand remains an explanatory analogy rather than an independently verified new physical mechanism.

## F. ROT-006: what a scalar field cannot source in the fixed rotating metric

[ROT-006](../research/ROT-006_SOURCE_FIRST_MATTER_AUDIT.md) tests the *standalone matter stress tensor*, rather than just scalar phase winding. The exact metric of ROT-005 requires a stress tensor with four distinct mixed eigenvalues. A minimally coupled first-derivative real scalar has a rank-one correction to \(L\delta^a_b\) and three repeated eigenvalues; an ordinary complex scalar has rank at most two and at least two repeated eigenvalues. Neither can equal the frozen source alone. This also excludes a perfect fluid and pure Maxwell as single sources by their eigenvalue structure.

If a physical observer velocity \(u_a\) is proportional to \(\partial_a\phi\), its vorticity vanishes by Frobenius. The ROT-005 comoving fluid has nonzero \(u\wedge du\), so that **specific** physical congruence cannot be a one-scalar gradient.

These results do **not** rule out scalar–vector couplings, nonminimal curvature terms, higher-derivative models, other rotating metrics, or genuinely multi-field source actions. They also do not claim all scalar fields intrinsically rotate.

## G. ROT-007: combined scalar + Maxwell also fails under the frozen homogeneous ansatz

[ROT-007](../research/ROT-007_EINSTEIN_SCALAR_MAXWELL_AUDIT.md) tests the complete **trace** required by the Einstein–scalar–Maxwell action with `V=Lambda=0` and real `phi(t)`. Even allowing arbitrary electromagnetic `E(t),B(t)`, the Maxwell stress trace vanishes; the scalar trace is `(100/101)*phi_dot²>=0`. The fixed rotating/expanding metric needs `G^a_a=-797/(808a²)<0`. This yields a contradiction without choosing field amplitudes. A spatial real gradient, an explicitly declared potential or a richer action may alter the necessary trace equation, so **the negative result is intentionally not universal**.

## H. ROT-008 — linear spatial scalar also fails, but the wave and trace gates do not ban every profile

[ROT-008](../research/ROT-008_RECURSIVE_TERMINAL_REPORT.md) freezes the massless action and scalar \(\phi=ct+dx\). The scalar wave equation forces \(c=d=0\), whereas the Einstein trace cannot hold for those values. This proof is exact and the two recursive proof orders terminate at contradiction.

**Boundary control:** changing the scalar to \(\phi(t,x)=(101d/100)\ln a(t)+dx\) with \(d^2=39850/30199\) satisfies these *two necessary equations*, but no other Einstein or Maxwell equation has been proven for the enlarged class. Thus the linear ansatz no-go does not establish a scalar-field no-go in general.

## I. ROT-009 — passing the scalar wave and trace is not enough

In the [ROT-009 source-first full-tensor test](../research/ROT-009_FULL_TENSOR_AUDIT.md), the frozen log-time plus linear-space scalar \(\phi=(101d/100)\ln a+dx\), \(d^2=39850/30199\), passes \(\Box\phi=0\) and the Einstein trace. But the fixed KO spacetime needs \(G_{xx}<0\), whereas the scalar gives \(T^{(\phi)}_{xx}=501d^2/800>0\) and the specified ordinary Maxwell potential adds only nonnegative squares to that component. **No source solution exists for these assumptions.** This does not ban general spatial scalars, other Maxwell field components, nonminimal actions, or new physical sources.
