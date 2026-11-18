# ROT-011 — Source-first Einstein–Proca strong-energy-condition screen

**Exploratory hypothesis and acceptance policy. Date: 18 November 2026.** This follows ROT-010. A preliminary algebraic check of the fixed metric's Ricci tensor was made before this protocol was committed. **Not** a blind independent preregistration. The dedicated executable and results are to be committed *after* this protocol.

## Scientific motivation

Ordinary Maxwell fields proved insufficient for the frozen logarithmic scalar source in ROT-010. A physically recognized alternative is **massive Proca matter**, whose mass term adds directional stress without introducing an arbitrary reconstructed matter tensor. This is a distinct action, not a retroactive repair of ROT-009/010.

The physical question: **can the existing exact causal expanding rotating Korotkii–Obukhov metric be sourced solely by a finite collection of ordinary positive-kinetic real Proca fields (possibly accompanied by standard Maxwell fields and massless canonical real scalar fields), with Λ=0 and κ=8πG=1?**

Instead of inventing a vector-potential ansatz and fitting it, first test the **strong energy condition** (SEC) that all of those source sectors obey when their kinetic signs and squared masses are nonnegative. A pointwise violation of that necessary condition for the specified metric excludes the whole named matter class and renders Proca ODE fitting unnecessary.

## Frozen metric and material action

Use the already published exact ROT-005 metric on t>−2, a(t)=1+t/2>0, signature (−+++):

```text
ds²=−(dt + a exp(x/2)dy/10)²
      +a² dx² +(101/100)a² exp(x)dy² +a² dz².

u^a = δ^a_t; coframe:
theta^0=dt+a exp(x/2)dy/10
theta^1=a dx
theta^2=sqrt(101) a exp(x/2)dy/10
theta^3=a dz.
```

Einstein gravity with Λ=0, κ=1. The predeclared conventional matter sectors (any finite numbers of fields, including none) are:

```text
L_m = − Σ_I [1/4 F^(I)_ab F^(I)ab + 1/2 μ_I² A^(I)_a A^(I)a]
      − Σ_J 1/4 H^(J)_ab H^(J)ab
      − Σ_K 1/2 (∇φ_K)²,

F^(I)=dA^(I), H^(J)=dB^(J),
each μ_I² >= 0; all kinetic coefficients positive.
```

An optional positive overall coefficient on each sector preserves the argument. **No scalar potential, cosmological constant, higher derivatives, nonminimal curvature coupling, phantom/negative kinetic signs, extra imperfect fluid, or other invented correction stress.** The Proca fields can have arbitrary local real 1-form potentials and arbitrary real 2-form derivatives; do not impose symmetry or coordinate ansätze.

Einstein's equations and matter stress normalization use G_ab=T_ab with the chosen κ=1.

## Exact SEC necessary condition

For any normalized physical timelike vector n^a, the SEC of matter requires

```text
(T_ab − 1/2 T g_ab) n^a n^b >= 0.
```

Einstein equations with Λ=0 imply R_ab n^a n^b >=0.

The canonical Proca source's trace-reversed stress obeys (in 4D):

```text
T^(Proca)_ab − 1/2 T^(Proca) g_ab
   = T^(Maxwell)_ab + μ² A_a A_b.
```

Massless real scalar similarly contributes (∂aφ)(∂bφ) to the trace-reversed source, and pure Maxwell is traceless with nonnegative local energy density for any timelike observer. Therefore **any finite sum of the allowed sectors obeys SEC** in any observer frame, even if the fields vary arbitrarily in spacetime. The argument holds without solving any differential source field equations.

For the exact KO geometry in the observer-adapted orthonormal coframe, a preselected, unnormalized timelike vector is `v^hat = (1,0,1/10,0)`. The coframe Minkowski metric gives v·v=−99/100<0, and its norm is irrelevant to the sign. The preliminary predicted Ricci contraction is

```text
a² R_hat_ab v^hat a v^hat b = (703−80 sqrt(101))/80800 < 0,
because 703²=494209 < 80²*101=646400.
```

**Predicted contradiction:** The fixed spacetime violates SEC for this concrete timelike vector, ruling out a source consisting **only** of the specified ordinary canonical matter classes. A positive cosmological constant or positive scalar potential could alter SEC and is not included.

## Required executable controls and decisions

1. Independently rerun the exact ROT-005 tensor verification from its frozen source and reconstruct its orthonormal Einstein and Ricci tensors.
2. Derive and check Ricci contraction with the specified vector and verify strict negativity with exact radicals/rationals, not a numerical tolerance or finite sampling.
3. Independently construct an **arbitrary six-component Maxwell field**, four arbitrary Proca vector components, and an arbitrary canonical massless scalar gradient in a local Lorentz orthonormal frame. Derive all stress tensors from the frozen standard actions and verify the trace-reversed SEC identity.
4. Show the Maxwell term is a nonnegative sum of squares in a **boosted orthonormal frame** adapted to the selected timelike vector, rather than assuming positivity without a control. Include massless Proca limit and zero-field null controls.
5. Stop if a necessary SEC inequality is contradicted, with **FAIL** for the frozen action and background, **PASS** for the exact computation and controls, **UNRESOLVED** for general scalar potentials, positive Λ, nonminimal interactions and observed cosmic rotation. Preserve both negative and positive results.

## Attribution and scope

Canonical Proca stress and its classical energy conditions: Maeda and Martínez, *Energy conditions in arbitrary dimensions*, **PTEP** 2020, 043E02, [DOI 10.1093/ptep/ptaa009](https://doi.org/10.1093/ptep/ptaa009). Einstein–Proca systems appear in established rotating Gödel-type matter literature, but those spacetimes and actions are not novel to this project. The outcome must not be represented as proof that rotating spacetimes or standard Proca fields are unphysical generally: it concerns the *single ROT-005 exact geometry* under the fixed **Λ=0** and matter-sector restrictions above.

No source-by-metric inversion T=G is allowed as a physical derivation.
