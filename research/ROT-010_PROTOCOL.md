# ROT-010 — General Maxwell-field Rainich screen of the frozen logarithmic scalar source

**Exploratory protocol, 18 November 2026.** This test follows ROT-009 and a preliminary exact-algebra screen. **Not a sealed or blinded preregistration**; do not misstate it as one. The document freezes the exact follow-up target before committing the dedicated new reproducer.

## Scientific question

ROT-009 showed that the **specific potential** A=E(t) exp(x/2)dy+B(t)dz cannot provide the necessary negative directional stress. Could **some other ordinary real Maxwell 2-form**, with *all six independent local components unrestricted*, source the same metric **alongside the same frozen real logarithmic scalar**?

## Frozen geometric and physical inputs

Use the already published ROT-005 Korotkii–Obukhov metric, signature (-+++), units κ=8πG=1, c=1, Λ=0, region t>−2:

```text
a(t)=1+t/2>0
ds²=−(dt+a exp(x/2)dy/10)² +a²dx² +(101/100)a²exp(x)dy²+a²dz²
```

Keep the ordinary source-first Einstein + massless canonical real scalar + Maxwell **action**, no scalar potential or nonminimal couplings. The exact scalar from ROT-009 is

```text
phi(t,x)=(101*d/100)*ln(a(t)) + d*x
d² = 39850/30199; both real signs allowed
```

Do **not** restrict the Maxwell potential or prescribe its spacetime dependence. Instead allow **every algebraic real antisymmetric Maxwell 2-form F_ab at a point**. This strictly enlarges the ROT-009 electromagnetic search class without changing the scalar or metric. If the target stress is impossible even pointwise, no globally defined Maxwell potential or dynamical field can rescue it.

## Algebraic Rainich screen (classical necessary identity)

From the exact computed Einstein tensor G_ab and the **action-derived canonical scalar stress T_phi_ab** form a target Maxwell stress S_ab = G_ab − T_phi_ab. Use the normalized physical orthonormal tetrad and its Lorentz metric η=diag(−1,1,1,1). Let M^a_b = η^{ac} S_cb.

Every ordinary four-dimensional Maxwell field obeys

```text
tr(M)=0
M^a_c M^c_b = 1/4 * δ^a_b * tr(M²).
```

This identity, part of the classical Rainich algebraic conditions, is **necessary** even for null Maxwell fields. If the tensor Q=M²−I tr(M²)/4 is nonzero anywhere, the fixed scalar+Maxwell candidate is **algebraically impossible**, before imposing dF=0 or ∇_a F^{ab}=0. An all-zero Q is **not** enough by itself for a physical Maxwell solution; positivity and differential Rainich constraints would remain.

Historical reference: Bergqvist & Höglund (2002), [Algebraic Rainich theory](https://doi.org/10.1088/0264-9381/19/12/316); [arXiv gr-qc/0202092](https://arxiv.org/abs/gr-qc/0202092).

## Required computations and controls

1. Re-run ROT-005 complete Einstein-tensor verification and reconstruct the fixed orthonormal G_ab.
2. Independently differentiate phi, construct its exact canonical scalar T_phi in the orthonormal coframe, and verify trace(G−T_phi)=0 on both signs d. Do not change metric or action.
3. Compute Q symbolically with **exact rationals** over the entire domain and establish whether any component is identically nonzero for all a>0. Prefer a sign-independent, coordinate-invariant tensor nonzero witness; include the complete Q or a selected exact component.
4. As a positive control, independently construct an **arbitrary six-component antisymmetric Maxwell 2-form** in a Lorentz orthonormal frame, derive its stress tensor from the fixed Maxwell Lagrangian, and verify trace and Q=0 as symbolic polynomial identities. Include an explicit null electromagnetic field case. This guards against a mistaken Rainich formula.
5. Test both real scalar signs. No software tolerance, arbitrary sampling or coefficient retuning may certify the no-go.
6. Terminate with **FAIL for the frozen scalar + completely unrestricted ordinary Maxwell algebraic source** if Q≠0. Mark the executed mathematical screen PASS, the original candidate FAIL, and general EFMW/global cosmic rotation UNRESOLVED.

## Adjudication and boundaries

A Q≠0 exact witness is a stronger result than ROT-009: it removes the specific Maxwell **potential** ansatz entirely, but **does not** remove the fixed scalar-gradient assumption. It is **not** a no-go theorem for arbitrary scalar fields, scalar potentials, nonminimal curvature couplings, added fluid matter, nonlinear electrodynamics, different rotating geometries, or the observed universe.

PASS for a full Einstein–matter source requires all source and Maxwell equations (and physical admissibility); a Rainich algebraic match alone would be UNRESOLVED until those checks were complete. Publish all nulls, code, CI run, and theorem limitations.
