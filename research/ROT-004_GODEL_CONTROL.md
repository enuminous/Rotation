# ROT-004 symbolic witness — classic Gödel rotating dust spacetime

This exact GR case is a strong negative control for the assertion that
**rotation necessarily causes a positive Hubble expansion term**. It is not
evidence that the observed universe globally rotates.

## What the code actually computes

`research/rot004_godel_sympy.py` independently constructs a four-dimensional
metric and calculates all 64 Levi-Civita Christoffel coefficients, the
Ricci tensor, scalar curvature and Einstein tensor. It checks the **matrix
identity** (G_{ab}+Lambda g_{ab}=kappaho u_a u_b), rather than trusting
a literature claim or a manually typed Ricci tensor.

Using coordinates ((t,x,y,z)), (m>0), signature ((-+++)):

```text
ds² = -(dt + exp(mx)dy)² + dx² + (exp(2mx)/2)dy² + dz²
u^a = (1,0,0,0)
8πGρ = m²,    Λ = -m²/2
```

For this congruence, the computer algebra derives:

- normalized timelike dust flow (u_a u^a=-1);
- expansion (Theta=0);
- shear and four-acceleration zero;
- nonzero (omega^2=	frac12omega_{ab}omega^{ab}=m^2/2);
- projected-rest-space scalar (mathcal R=0) under the 1+3 definition;
- exact Einstein dust equation with negative cosmological constant.

The computed (mathcal R=0) is **not** the Ricci scalar of a globally
integrable fluid-orthogonal spatial hypersurface; no such hypersurface exists
where the chosen flow has nonzero vorticity.

### Scope of the conditional ME-056 comparison

A purely illustrative attempt to put this rotating solution into the
`ME-056` format by setting (a=1), (k=0) from (mathcal R=0), and
(Omega_U^2=omega^2=m^2/2), predicts:

```text
ME-056: H² = (m²+Λ)/3 + Omega_U² = 2 m²/3  > 0
Gödel:  H² = (Theta/3)² = 0
```

This shows that the **naive** identification is wrong. It does **not**
prove every restricted or modified ME-056 interpretation mathematically
inconsistent, because the original equation does not define how its global
scale factor and curvature labels relate to a vortical, non-hypersurface-
orthogonal metric.

More fundamentally, the Gödel GR solution itself demonstrates
**rotation without expansion**, and therefore disproves any claim that
physical vorticity *alone* universally implies nonzero expansion.

### Run

```sh
python -m pip install sympy==1.14.0
python research/rot004_godel_sympy.py
```

`PASS_EXACT_GODEL_EINSTEIN_METRIC_COMPUTATION` certifies the listed
symbolic equalities only. The repository's core standard-library Python lab
remains dependency-free.

**Sources:** [Zhao, Modesto, Bambi (2026), Sec. 2](https://doi.org/10.1140/epjc/s10052-026-15963-y)
historically quotes Gödel's exact metric and constants; [1+3 covariant
Friedmann discussion](https://www.mdpi.com/2218-1997/8/6/318).
