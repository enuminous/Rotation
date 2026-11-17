"""ROT-004 exact Einstein-metric verification of the classical Gödel dust solution.

Independent symbolic witness for the general-relativistic 1+3 comparison.
Optional dependency: sympy==1.14.0 (not required by the core Rotation Lab).

Metric coordinates (t,x,y,z), signature (-,+,+,+), c=1:
  ds² = -[dt + exp(m*x) dy]²
        + dx² + exp(2m*x)/2 dy² + dz².

Unit dust 4-velocity u^a = (1,0,0,0).
  8 pi G rho = m²,  Lambda = -m²/2,
  omega² = (1/2) omega_ab omega^ab = m²/2,
  expansion theta=0, shear=0, acceleration=0.
These parameter relations describe a *classical exact GR solution* with
closed timelike curves. They do NOT make it a realistic observed cosmos.

Source: https://doi.org/10.1140/epjc/s10052-026-15963-y (Sec. 2,
which presents the historical Gödel metric and its GR matter parameters).
"""
from __future__ import annotations
import json
import sympy as sp


def zero_matrix(M: sp.MatrixBase) -> bool:
    return all(sp.simplify(v) == 0 for v in M)


def evaluate() -> dict[str, object]:
    t, x, y, z = sp.symbols("t x y z", real=True)
    m = sp.symbols("m", positive=True, real=True)
    coords = (t,x,y,z)
    N = len(coords)
    E = sp.exp(m*x)
    metric = sp.Matrix([
        [-1, 0, -E, 0],
        [0, 1, 0, 0],
        [-E, 0, -E**2/sp.Integer(2), 0],
        [0, 0, 0, 1]
    ])
    inv = metric.inv()
    half = sp.Rational(1,2)
    gamma = [
        [
            [
                sp.simplify(half*sum(inv[i,l] * (
                    sp.diff(metric[l,j],coords[k])
                    +sp.diff(metric[l,k],coords[j])
                    -sp.diff(metric[j,k],coords[l])
                ) for l in range(N)))
                for k in range(N)
            ] for j in range(N)
        ] for i in range(N)
    ]
    Ric = sp.Matrix(N,N,lambda i,j:sp.simplify(sum(
        sp.diff(gamma[a][i][j],coords[a])
        -sp.diff(gamma[a][i][a],coords[j])
        +sum(
            gamma[a][a][b]*gamma[b][i][j]
            -gamma[a][j][b]*gamma[b][i][a]
            for b in range(N)
        ) for a in range(N)
    )))
    scalar=sp.simplify((inv*Ric).trace())
    Einstein=(Ric-half*scalar*metric).applyfunc(sp.simplify)
    u_up=sp.Matrix([1,0,0,0])
    u_down=metric*u_up
    # D_ab = covariant derivative nabla_a u_b.
    D=sp.Matrix(N,N,lambda a,b:sp.simplify(
        sp.diff(u_down[b],coords[a])
        -sum(gamma[c][a][b]*u_down[c] for c in range(N))
    ))
    expansion=sp.simplify((inv*D).trace())
    acceleration=sp.Matrix([sp.simplify(sum(u_up[a]*D[a,b] for a in range(N)))
                            for b in range(N)])
    symmetric=(D+D.T).applyfunc(lambda v:sp.simplify(v*half))
    antisymmetric=(D-D.T).applyfunc(lambda v:sp.simplify(v*half))
    omega_up=(inv*antisymmetric*inv.T).applyfunc(sp.simplify)
    omega_sq=sp.simplify(half*sum(antisymmetric[i,j]*omega_up[i,j]
                                  for i in range(N) for j in range(N)))
    shear_zero=zero_matrix(symmetric) and expansion==0
    rho_kappa=m*m
    Lambda=-m*m/2
    source=rho_kappa*(u_down*u_down.T)
    einstein_residual=(Einstein+Lambda*metric-source).applyfunc(sp.simplify)
    projected_curvature=sp.simplify(scalar+2*(u_up.T*Ric*u_up)[0]
                                    -sp.Rational(2,3)*expansion**2
                                    -2*omega_sq)
    gr_rhs=sp.simplify(2*(rho_kappa+Lambda-sp.Rational(1,3)*expansion**2
                        -omega_sq))  # shear=0
    checked={
        "signature_det_negative": sp.simplify(metric.det()) == -E**2/2,
        "dust_unit_timelike": sp.simplify((u_up.T*metric*u_up)[0])==-1,
        "einstein_equations":zero_matrix(einstein_residual),
        "expansion_zero":expansion==0,
        "shear_zero":shear_zero,
        "acceleration_zero":zero_matrix(acceleration),
        "rotation_nonzero_and_normalized":sp.simplify(omega_sq-m*m/2)==0,
        "projected_curvature_zero":projected_curvature==0,
        "gauss_scalar_identity":sp.simplify(projected_curvature-gr_rhs)==0
    }
    if not all(checked.values()):
        raise AssertionError("Symbolic Gödel check failed: "+repr(checked))
    return {
        "status":"PASS_EXACT_GODEL_EINSTEIN_METRIC_COMPUTATION",
        "source":"historical classical Gödel metric; not a newly discovered solution",
        "metric_signature":"(-,+,+,+)",
        "Ricci_scalar":str(scalar),
        "kappa_rho":str(rho_kappa),
        "Lambda":str(Lambda),
        "expansion_theta":str(expansion),
        "shear_sq":"0",
        "physical_vorticity_sq":str(omega_sq),
        "projected_rest_space_scalar":str(projected_curvature),
        "einstein_tensor_residual":"zero",
        "checks":checked,
        "boundary":"Does not derive ME-056, construct a globally foliatable rotating FLRW model,"
                   " prove universal cosmic rotation, or fit observations."
    }


if __name__=="__main__":
    print(json.dumps(evaluate(),indent=2))
