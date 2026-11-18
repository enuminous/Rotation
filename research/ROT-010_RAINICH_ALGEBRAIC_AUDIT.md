# ROT-010 — An Algebraic Rainich No-Go for Arbitrary Maxwell Stress with the Frozen Logarithmic Scalar

**Monolithic Research · 18 November 2026**  
**Verdict:** **PASS** for exact tensor calculation and classical Maxwell controls; **FAIL** for the frozen Einstein–massless-real-scalar–Maxwell matter source even when its Maxwell 2-form is **completely unrestricted algebraically**; **UNRESOLVED** for different scalar profiles or interactions, alternative matter, and any observed cosmic rotation.

**Original exploratory source-defined protocol:** [ROT-010_PROTOCOL.md](ROT-010_PROTOCOL.md).  
**SymPy reproducer:** [rot010_rainich_screen.py](rot010_rainich_screen.py).  
**Literal executed CI ledger:** [ROT-010_TERMINAL_LEDGER.json](ROT-010_TERMINAL_LEDGER.json).  
**Source-pinned successful run:** [GitHub Actions 44332385490](https://github.com/enuminous/Rotation/actions/runs/44332385490), source SHA `7243426c29d6977e6ac48713c022c382b5a27151`.

> This analysis is **not** an observational measurement, an independently peer-reviewed no-go theorem, or a demonstration that Einstein–scalar–Maxwell theory cannot produce rotating cosmologies generally. It is a mathematically exact restriction for the one preselected geometry and scalar.

## Abstract

ROT-009 established an exact source incompatibility for a fixed causal, expanding and rotating Korotkii–Obukhov metric and a logarithmic real scalar combined with a particular Maxwell potential. That potential restriction left open whether another electromagnetic configuration might supply the missing anisotropic stresses. ROT-010 removes **all local algebraic restrictions on the ordinary Maxwell 2-form** while retaining the same geometry, scalar field and canonical massless Einstein–scalar–Maxwell action. The remaining stress required of the Maxwell field, \(S_{ab}=G_{ab}-T^{(\phi)}_{ab}\) (with \(\kappa=1,\Lambda=0\)), is trace-free as required, but its mixed square fails the classical Rainich identity \(S^a{}_cS^c{}_b=\tfrac14\delta^a{}_b S^c{}_dS^d{}_c\). In the fixed physical orthonormal coframe, its exact off-diagonal obstruction is \(a^4Q^{\hat0}{}_{\hat1}=-160795/326432\ne0\), independent of scalar sign and valid for every \(a(t)>0\) on \(t>-2\). An independent symbolic positive control constructs all six arbitrary Maxwell components and proves their Rainich tensor identically vanishes, including a nonzero null-field control. Accordingly, **no ordinary Maxwell field at all** can complete the source for this particular metric and scalar, regardless of potential, gauge, spacetime dependence or Maxwell evolution. Other scalar fields, matter actions, interactions and metrics remain untested. The study supplies a stronger bounded negative conclusion, not a cosmic rotation discovery.

## 1. The exact extension beyond ROT-009

The [ROT-009 audit](ROT-009_FULL_TENSOR_AUDIT.md) ruled out the Maxwell potential

```text
A=E(t)*exp(x/2)dy+B(t)dz
```

because the required \(G_{xx}\) was negative and the candidate \(T_{xx}\) nonnegative.

**ROT-010 removes this potential ansatz altogether.** We now allow **any ordinary real antisymmetric Maxwell 2-form \(F_{ab}\)** at every point. That is strictly broader than the previous source class. We do **not** remove the chosen scalar profile or change the matter action.

If the required tensor fails a necessary **pointwise algebraic identity** of every standard Maxwell stress, no electromagnetic potential or field equations can reproduce it. This avoids an unjustified open-ended sweep over functions \(E(t),B(t)\) or coordinate representations.

## 2. The frozen source

Use the already verified ROT-005 geometry, signature \((-+++)\), units \(c=\kappa=1\), \(\Lambda=0\), and region \(t>-2\), with \(a(t)=1+t/2>0\):

\[
ds^2=-\left(dt+\frac{a(t)e^{x/2}}{10}dy\right)^2
+a(t)^2dx^2+\frac{101}{100}a(t)^2e^xdy^2+a(t)^2dz^2.
\tag{1}
\]

The selected physical observer congruence has both expansion and covariant vorticity, already established as properties of this *known GR metric* in [ROT-005](ROT-005_KOROTKII_OBUKHOV_BRIDGE.md). It does not establish the observed universe has this geometry.

The matter action is unchanged:

\[
S=\int d^4x\sqrt{-g}
\left[\frac{R}{2}
-\frac12 g^{ab}\partial_a\phi\partial_b\phi
-\frac14F_{ab}F^{ab}\right].
\tag{2}
\]

The frozen **real** scalar is

\[
\phi(t,x)=\frac{101d}{100}\ln a(t)+d\,x,\qquad
d^2=\frac{39850}{30199},\quad
d=\pm\sqrt{\frac{39850}{30199}}.
\tag{3}
\]

Here \(F_{ab}\) is **any** real Maxwell 2-form, with six independent local components in four dimensions. We do not assume \(F=dA\) during the *algebraic* screen, nor do we impose a symmetry or potential pattern. Every ordinary physical Maxwell field is included among these algebraic possibilities.

Define the target electromagnetic tensor by

\[
S_{ab}:=G_{ab}-T^{(\phi)}_{ab}.
\tag{4}
\]

A completed source would require \(S_{ab}=T^{(\mathrm{EM})}_{ab}\), together with the matter field equations.

## 3. The classical Rainich necessary conditions

For a standard Maxwell field in a four-dimensional Lorentzian spacetime, with stress tensor from \(-F_{ab}F^{ab}/4\), its mixed tensor \(M^a{}_b=g^{ac}T_{cb}\) obeys

\[
\operatorname{tr}M=0,\qquad
M^a{}_cM^c{}_b=
\frac14\delta^a{}_b\,\operatorname{tr}(M^2).
\tag{5}
\]

This is a standard algebraic part of the Rainich characterizations of Einstein–Maxwell matter [Bergqvist and Höglund 2002]. The full characterization also involves energy/sign and differential conditions. **We use only the necessary algebraic identity**: failure of any component suffices, for ordinary null as well as non-null Maxwell fields.

Set

\[
Q^a{}_b:=M^a{}_cM^c{}_b
-\frac14\delta^a{}_b\operatorname{tr}(M^2).
\tag{6}
\]

Every standard Maxwell stress tensor satisfies \(Q=0\), regardless of orientation, polarization, spacetime dependence, or source-free Maxwell dynamics.

The target \(S=G-T^{(\phi)}\) is geometrically defined independent of any trial electromagnetic field. We use a normalized orthonormal coframe \(\vartheta^{\hat a}=C^{\hat a}{}_b dx^b\), with

\[
\vartheta^{\hat0}=dt+\frac{ae^{x/2}}{10}dy,\quad
\vartheta^{\hat1}=a\,dx,\quad
\vartheta^{\hat2}=\frac{\sqrt{101}}{10}ae^{x/2}dy,\quad
\vartheta^{\hat3}=a\,dz.
\tag{7}
\]

This gives \(g=\eta_{\hat a\hat b}\vartheta^{\hat a}\vartheta^{\hat b}\), \(\eta=\operatorname{diag}(-1,1,1,1)\). Passing to an orthonormal frame does **not** discard any Maxwell field freedom: a tensor equality or the Rainich tensor equation must hold in every frame if it holds in one.

## 4. The decisive exact result

The script independently reruns the full ROT-005 Einstein-tensor calculation, constructs the source's orthonormal \(G_{\hat a\hat b}\), differentiates (3), and derives

\[
T^{(\phi)}_{\hat a\hat b}
=\partial_{\hat a}\phi\,\partial_{\hat b}\phi
-\frac12\eta_{\hat a\hat b}(\nabla\phi)^2.
\tag{8}
\]

The target \(S_{\hat a\hat b}=G_{\hat a\hat b}-T^{(\phi)}_{\hat a\hat b}\) is **trace-free**, matching one necessary Maxwell condition. But the **second** condition (5) fails:

\[
\boxed{
a(t)^4 Q^{\hat0}{}_{\hat1}=
-\frac{160795}{326432}\ne0
\quad \forall\,t>-2.
}
\tag{9}
\]

The exact fraction is independent of \(x,y,z\), independent of the scalar sign, and cannot vanish at any finite point with \(a(t)>0\). It is not a floating-point small residual. The nonzero **tensor** \(Q\) cannot be transformed to zero by choosing another local observer frame or coordinate system.

Consequently:

> **Bounded ROT-010 no-go.** The fixed metric (1), canonical massless real scalar action and specified logarithmic scalar (3) admit no remaining ordinary Maxwell stress tensor \(S_{ab}\) at any point of the domain, regardless of the six local electromagnetic components. Therefore there is no solution of the complete Einstein–scalar–Maxwell system with these fixed geometric and scalar fields.

**Proof:** Every Maxwell stress obeys \(Q=0\) in (6), whereas the required stress has the nonzero component (9) in a valid orthonormal frame; a necessary algebraic identity fails. This is impossible for either sign of \(d\). \(\square\)

That proof is **strictly stronger than ROT-009's restricted potential no-go**, but it is not a no-go for arbitrary scalar profiles, alternative matter interactions or the existence of rotating spacetimes.

## 5. Positive controls: independently constructing six-component Maxwell matter

A new no-go test must first demonstrate that its exclusion criterion is correct for genuine positive examples.

The reproducer separately constructs a **generic** antisymmetric real 2-form with all six independent components,

\[
F_{\hat0\hat1},F_{\hat0\hat2},F_{\hat0\hat3},
F_{\hat1\hat2},F_{\hat1\hat3},F_{\hat2\hat3},
\]

and derives the standard Maxwell stress from the action, not from an assumed Rainich identity. SymPy verifies \(\operatorname{tr}M=0\) and **all sixteen components of \(Q\) vanish as polynomial identities** in these six unknowns. This validates the algebraic criterion for unrestricted electromagnetic field values.

A separate **nonzero null electromagnetic field** \(F=(dt-dz)\wedge dx\) in a local Minkowski orthonormal frame has \(F_{ab}F^{ab}=0\), nonzero stress and **the same exact \(Q=0\)** result. The proof does not silently exclude null electromagnetic radiation.

For the failed fixed scalar target, the machine computes both allowed real scalar signs and obtains the same nonzero certificate (9) in each.

## 6. Machine provenance and reproducibility

The source is [rot010_rainich_screen.py](rot010_rainich_screen.py), and the successful GitHub Actions job at **source revision `7243426c29d6977e6ac48713c022c382b5a27151`** is [run 44332385490](https://github.com/enuminous/Rotation/actions/runs/44332385490). Actual stdout was extracted and preserved in [ROT-010_TERMINAL_LEDGER.json](ROT-010_TERMINAL_LEDGER.json).

The recorded machine verdict is:

| Gate | Result |
|---|---|
| Recompute ROT-005 exact Einstein geometry | **PASS** |
| Target Maxwell source trace | **PASS**, zero |
| Target Maxwell Rainich squared identity | **FAIL**, exact nonzero certificate (9) |
| All six independent standard Maxwell 2-form components as positive control | **PASS** |
| Nonzero null Maxwell field as positive control | **PASS** |
| Frozen scalar sign \(d>0\) | **TERMINAL FAIL** |
| Frozen scalar sign \(d<0\) | **TERMINAL FAIL** |
| Differential Maxwell equations | **NOT NEEDED** after algebraic impossibility |
| Observed universal cosmic rotation | **UNRESOLVED** |

For a clean local replay:

```bash
git clone https://github.com/enuminous/Rotation.git
cd Rotation
python -m pip install sympy==1.14.0
python research/rot005_ko_sympy.py
python research/rot010_rainich_screen.py
```

A green CI run verifies execution of this exact symbolic calculation; it is neither expert peer review nor a Lean-kernel GR theorem. The protocol was **exploratory and informed by prior ROT-009 findings**, not a blinded independent preregistration.

## 7. Limits and source-first next step

The previous failure in ROT-009 raised a legitimate question: might a different electromagnetic field rescue the model? **ROT-010 answers that precise question negatively** under the same scalar profile, without restricting the Maxwell form.

This does **not** establish that no ordinary scalar-plus-Maxwell solution can support any rotating spacetime, that no **other scalar gradient** can make \(G-T_\phi\) a Maxwell stress, or that standard Maxwell fields are physically inadmissible. The nonzero Rainich tensor is a fixed-source result.

A scientifically justified next step must begin with a **new, independently motivated matter source or scalar action**, specifying its symmetries and observable physical scale before using the metric's required stress as a fitting target. The theory must then satisfy all Einstein and matter equations, energy conditions and dynamics. If no such predeclared model survives, the broader EFMW cosmic-rotation mechanism remains UNRESOLVED. Fitting \(H^2(a)\) alone cannot identify the physical vorticity parameter because of the curvature–rotation degeneracy established in ROT-004/005.

## Conclusion

**ROT-010 terminates in an exact bounded negative result that removes the Maxwell-potential restriction from ROT-009**: given the frozen metric and real logarithmic scalar, **no standard real Maxwell 2-form can complete the stress tensor**, because the Rainich squared-tensor identity fails by a fixed nonzero rational amount. Both scalar branches close under a successful source-pinned symbolic replay, and independent generic/nullable Maxwell controls pass.

The progress is a sharpened mathematical exclusion and a transparent scientific boundary—not evidence for universal cosmic rotation.

## References

1. G. Bergqvist and A. Höglund, *Algebraic Rainich Theory and Antisymmetrization in Higher Dimensions*, **Classical and Quantum Gravity** 19, 3341 (2002). [DOI 10.1088/0264-9381/19/12/316](https://doi.org/10.1088/0264-9381/19/12/316); [arXiv gr-qc/0202092](https://arxiv.org/abs/gr-qc/0202092).
2. V. A. Korotkii and Yu. N. Obukhov, *Kinematic Analysis of Cosmological Models with Rotation*, **Soviet Physics JETP** 72, 11–15 (1991). [Original text](https://jetp.ras.ru/cgi-bin/dn/e_072_01_0011.pdf).
3. M. C. Wright, [*Beyond the Trace: ROT-009*](https://github.com/enuminous/papers/blob/main/Beyond-the-Trace-ROT-009-Exact-Einstein-Source-Obstruction-2026-11-17.md) (2026).
4. M. C. Wright / Monolithic LLC, [ROT-005 source geometry](ROT-005_KOROTKII_OBUKHOV_BRIDGE.md), [ROT-009 log-scalar source audit](ROT-009_FULL_TENSOR_AUDIT.md), and [ROT-010 executed proof ledger](ROT-010_TERMINAL_LEDGER.json) (2026).

**Disclosure:** Computational research curated for Matthew Chenoweth Wright / Monolithic LLC with OpenAI GPT-6 assistance. This is a self-published research audit, not independently peer-reviewed or a measurement of the observed universe. Original published metrics and mathematical identities retain their own authorship.
