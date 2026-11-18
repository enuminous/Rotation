# ROT-011 — A Strong-Energy-Condition No-Go for Canonical Einstein–Proca Matter in a Fixed Rotating Cosmology

**Monolithic LLC · 18 November 2026**  
**Status:** **PASS** for exact symbolic GR and canonical-matter identities; **FAIL** for the frozen positive-kinetic Proca/Maxwell/massless-real-scalar source class on the selected KO metric; **UNRESOLVED** for alternative matter, different metrics and any observed universal rotation.

**Original protocol:** [ROT-011_PROTOCOL.md](ROT-011_PROTOCOL.md) · **Reproducer:** [rot011_einstein_proca_sec.py](rot011_einstein_proca_sec.py) · **Executed machine ledger:** [ROT-011_TERMINAL_LEDGER.json](ROT-011_TERMINAL_LEDGER.json) · **Green source-pinned CI:** [run 44334458697](https://github.com/enuminous/Rotation/actions/runs/44334458697), commit `0e8e78af8d1f30291e19cf4e5138b49c437c1db5`.

## Abstract

Following the exact Maxwell-stress Rainich no-go in ROT-010, ROT-011 considers a conventional **massive real Proca vector** with a positive kinetic term and nonnegative mass squared, a physically familiar matter source capable of stresses unavailable from a purely massless Maxwell tensor. Using an exact known expanding/rotating causal Korotkii–Obukhov spacetime (the fixed ROT-005 geometry), we derive a stronger obstruction than a failed potential ansatz. The metric's Ricci tensor violates the **strong energy condition (SEC)** along one explicitly constructed timelike observer, while every ordinary real Proca sector with \(\mu^2\ge0\), standard Maxwell sector and canonical massless real scalar sector has nonnegative trace-reversed stress for all timelike observers. In the specified orthonormal frame, \(a^2R_{\hat a\hat b}v^{\hat a}v^{\hat b}=(703-80\sqrt{101})/80800<0\), where \(v=(1,0,1/10,0)\) and \(v^2=-99/100\). Positive control checks verify exact Maxwell energy positivity using **all six independent electromagnetic 2-form components** and a Lorentz boost, and verify Proca and scalar trace reversal for arbitrary components. The metric therefore cannot be sourced *solely* by any finite sum of the frozen standard positive-kinetic Proca, Maxwell and massless-real-scalar fields with \(\Lambda=0\). This is a **conditional, reproducible source-class no-go**, not a prohibition on Proca fields or rotating GR generally, and not a detection of universal cosmic rotation.

## 1. Why ROT-011 tests a different physical source

The ROT-006–010 sequence progressively excluded particular minimal matter sources and the fixed logarithmic-scalar plus *any* standard Maxwell 2-form from sourcing one chosen metric. The next meaningful alternative is to change the **physical source action**, rather than disguise another a posteriori correction as a derived stress tensor. Standard Proca theory is Einstein gravity coupled to a real massive spin-1 vector. Its nonnegative mass term changes its stress and trace, so it is a distinct legitimate candidate.

ROT-011 is **exploratory**, informed by earlier no-go results and a preliminary Ricci check before freezing the protocol; it is not a blind independent preregistration. The protocol preserves \(\kappa=1,\Lambda=0\), the previous metric and positive physical kinetic signs.

## 2. Fixed geometry and invariant witness

The known Korotkii–Obukhov metric (ROT-005) on \(t>-2\) is

\[
a(t)=1+\frac t2>0,\qquad
ds^2=-\Big(dt+\frac{ae^{x/2}}{10}dy\Big)^2+
a^2dx^2+\frac{101}{100}a^2e^xdy^2+a^2dz^2. \tag{1}
\]

Use signature \((-+++)\), the orthonormal coframe

\[
\vartheta^{\hat0}=dt+\frac{ae^{x/2}}{10}dy,\quad
\vartheta^{\hat1}=a\,dx,\quad
\vartheta^{\hat2}=\frac{\sqrt{101}}{10}ae^{x/2}dy,\quad
\vartheta^{\hat3}=a\,dz, \tag{2}
\]

and \(\eta_{\hat a\hat b}=\mathrm{diag}(-1,1,1,1)\).

Starting from the independently computed Einstein tensor of ROT-005, use \(R_{ab}=G_{ab}-\frac12G^c{}_c g_{ab}\) in four dimensions. The exact orthonormal Ricci tensor is

\[
a^2R_{\hat a\hat b}=
\begin{pmatrix}
5/808&1/404&-\sqrt{101}/202&0\\
1/404&199/808&-\sqrt{101}/404&0\\
-\sqrt{101}/202&-\sqrt{101}/404&203/808&0\\
0&0&0&50/101
\end{pmatrix}. \tag{3}
\]

For \(v^{\hat a}=(1,0,1/10,0)\), \(v^av_a=-99/100<0\); it is a physically timelike direction. Direct exact contraction gives

\[
\boxed{
a^2 R_{\hat a\hat b}v^{\hat a}v^{\hat b}
=\frac{703-80\sqrt{101}}{80800}<0.
}\tag{4}
\]

This inequality is certified without floating-point tolerance, since \(703^2=494209<646400=80^2(101)\). The vector is deliberately not unit-normalized, but multiplying by a positive normalization factor cannot change the sign.

**This metric violates SEC for the chosen timelike direction**, even though its ROT-005 *effective* source previously passed a weak-energy-condition (WEC) lower bound. WEC does **not** imply SEC; the two findings are compatible.

## 3. Standard Proca, Maxwell and massless scalar sectors obey SEC

The frozen admissible matter action is any finite positive-coefficient sum of

\[
\mathcal L_{\mathrm{Proca}}=
-\tfrac14F_{ab}F^{ab}-\tfrac12\mu^2A_aA^a,\qquad
F=dA,\quad \mu^2\ge0, \tag{5}
\]

standard Maxwell sectors, and canonical massless real scalar sectors \(-(\nabla\phi)^2/2\). No positive scalar potential, positive cosmological constant, negative kinetic sign, added imperfect fluid, nonlinear electromagnetism or nonminimal curvature interaction is allowed in this frozen hypothesis.

In four-dimensional Lorentz geometry the Proca action gives

\[
T^{(P)}_{ab}=T^{(EM)}_{ab}
+\mu^2\left(A_aA_b-\tfrac12g_{ab}A^2\right).
\tag{6}
\]

Since \(T^{(EM)a}{}_a=0\) and the Proca mass contribution has trace \(-\mu^2A^2\),

\[
\boxed{
T^{(P)}_{ab}-\tfrac12T^{(P)}g_{ab}
=T^{(EM)}_{ab}+\mu^2 A_aA_b.
}\tag{7}
\]

For every timelike vector \(v\), the corresponding contraction is

\[
T^{(EM)}_{ab}v^av^b+\mu^2(A_av^a)^2\ge0.
\tag{8}
\]

The ordinary Maxwell contribution is a sum of nonnegative electric/magnetic squares in the normalized observer frame. For the massless real canonical scalar, trace reversal yields exactly \(\nabla_a\phi\nabla_b\phi\), contributing \((v\cdot\nabla\phi)^2\ge0\). Thus **every finite positive combination of the listed source fields satisfies SEC**.

The reproducer independently constructs a **general real six-component Maxwell 2-form**, all four real Proca potential components and all four real scalar-gradient components. It verifies the exact trace-reversal identities and performs an orthonormal boost to the timelike direction of (4), confirming

\[
T^{(EM)}_{ab}v^av^b=
\frac{-v^2}{2}\sum_{i=1}^3(E_i'^2+B_i'^2)\ge0
\tag{9}
\]

as a symbolic identity over all six electromagnetic variables. Zero-field, Maxwell-only, pure-Proca-mass and scalar-only controls were also checked.

## 4. The contradiction and exact stopping rule

Einstein's equation with \(\Lambda=0\) and \(\kappa=1\) demands

\[
R_{ab}=T_{ab}-\tfrac12Tg_{ab}.
\tag{10}
\]

The **left** side contracted with the explicit timelike vector is **strictly negative**, from (4). Every permitted **right** side is **nonnegative**, from (7)–(9). Therefore no matter fields within the frozen canonical source family can satisfy Einstein's equations for the selected metric.

This is a stronger kind of statement than a failed symmetry-restricted vector potential: it applies to **arbitrary** real Proca 1-form configurations, any vector mass squared \(\mu^2\ge0\), arbitrary real Maxwell 2-forms and any number of massless real canonical scalar gradients, with positive kinetic coefficients, because the inequality is source-class-wide. There is no need to solve Proca's differential equation once a necessary algebraic Einstein/energy-condition requirement is impossible.

The constraint is limited to the stated **metric, \(\Lambda=0\), and SEC-satisfying matter family**. It is not a general no-go for massive vector fields in other GR spacetimes or for modified/interaction-rich actions.

## 5. Verification and decision ledger

| Gate | Exact result |
|---|---|
| Frozen KO exact Einstein tensor independently replayed | **PASS** |
| Orthonormal Ricci tensor reconstructed | **PASS** |
| Explicit timelike observer with \(v^2=-99/100\) | **PASS** |
| Negative Ricci contraction with exact radical certificate | **PASS** |
| Six Maxwell component positivity identity in boosted frame | **PASS** |
| Canonical Proca mass and scalar trace-reversal identities | **PASS** |
| Only positive-kinetic Einstein–Proca sources on this metric | **FAIL** |
| Any finite sum with Maxwell and massless canonical scalars | **FAIL** |
| New physical source, alternative metric or positive \(\Lambda\) | **UNRESOLVED** |
| Observed universal cosmic rotation and EFMW-specific observable | **UNRESOLVED** |

Machine output was taken directly from the successful [run 44334458697](https://github.com/enuminous/Rotation/actions/runs/44334458697), executed at commit `0e8e78af8d1f30291e19cf4e5138b49c437c1db5`, and archived in [ROT-011_TERMINAL_LEDGER.json](ROT-011_TERMINAL_LEDGER.json). The status `PASS_EXACT_SEC_SOURCE_NO_GO` means the **mathematical negative test passed**, not that a Proca cosmological source passed. The experiment's source verdict is `FAIL_CANONICAL_EINSTEIN_PROCA_MAXWELL_MASSLESS_SCALAR_SOURCE_CLASS`.

For reproduction:

```bash
git clone https://github.com/enuminous/Rotation.git
cd Rotation
python -m pip install sympy==1.14.0
python research/rot005_ko_sympy.py
python research/rot011_einstein_proca_sec.py
```

A green CI run verifies the scripts' exact symbolic outputs; it does not certify a new universal field law, independent expert review or astrophysical observations.

## 6. Scientific boundary and next research decision

The physical consequence is a **selection gate**: an Einstein source for this specific metric cannot consist solely of SEC-satisfying standard massless scalars, ordinary Maxwell fields and healthy real Proca fields with \(\Lambda=0\). Successful source theories could instead include a **physically motivated sector violating SEC**, such as an appropriately specified positive scalar potential or cosmological constant, or they could choose a different rotating geometry. Those are distinct hypotheses requiring independent motivations, parameter definitions and full field equations—not silent retunings of ROT-011.

In particular, a positive cosmological constant changes the timelike Ricci focusing relation. This has **not** been tested here. Likewise, the result does not invalidate all rotating universes or establish that *our* universe rotates.

**Next appropriate action:** Select and publish a new source-first matter action only if there is independent physical motivation, or change the research objective from fitting this one metric to extracting an observable that distinguishes plausible already known rotating cosmologies from the conventional isotropic baseline. Do not continue an unbounded search for arbitrary corrective stress tensors.

## 7. Conclusion

ROT-011 terminates with an exact **strong-energy-condition obstruction**: the fixed expanding/rotating spacetime has a demonstrably negative Ricci contraction along one timelike direction, while the specified positive-kinetic Einstein–Proca/Maxwell/massless-scalar source class requires it to be nonnegative. The result excludes the whole named canonical class for this one metric and zero cosmological constant, rather than a single potential pattern.

It advances the mathematical audit without confirming or disproving universal cosmic rotation.

## References and disclosure

1. H. Maeda and C. Martínez, *Energy Conditions in Arbitrary Dimensions*, **Progress of Theoretical and Experimental Physics** (2020), 043E02, [DOI 10.1093/ptep/ptaa009](https://doi.org/10.1093/ptep/ptaa009).
2. V. A. Korotkii and Yu. N. Obukhov, *Kinematic Analysis of Cosmological Models with Rotation*, **Soviet Physics JETP** 72, 11–15 (1991), [original article](https://jetp.ras.ru/cgi-bin/dn/e_072_01_0011.pdf).
3. M. C. Wright / Monolithic LLC, [ROT-005 exact metric](ROT-005_KOROTKII_OBUKHOV_BRIDGE.md), [ROT-010 Maxwell Rainich audit](ROT-010_RAINICH_ALGEBRAIC_AUDIT.md), and [ROT-011 executed ledger](ROT-011_TERMINAL_LEDGER.json).

**Disclosure:** Matthew Chenoweth Wright / Monolithic LLC research record, prepared with OpenAI GPT-6 computational assistance. Standard metric and source identities retain their original academic attribution. The result is **not independently peer-reviewed** and does not show an observational detection of the universe's global rotation.
