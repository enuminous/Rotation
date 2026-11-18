"""ROT-010 — unrestricted Maxwell-field algebraic screen (Rainich identity).

This is a deterministic, exact 4D source-first matter test. It retains
ROT-005's fixed expanding/rotating metric and ROT-009's *exact same*
massless scalar. It replaces ROT-009's restricted Maxwell potential with
an ARBITRARY real 2-form at each point, with all 6 components unrestricted.

Necessary classical 4D Maxwell identity, signature (-+++):
  for mixed stress M^a_b = g^{ac}T_cb,
  tr(M)=0 and M^2 = I * tr(M^2)/4.
Failure of this algebraic identity for S_ab=G_ab-T_scalar_ab disproves
any ordinary Maxwell 2-form source for this fixed geometry+scalar, even
before dF=0 or div F=0 are applied. Not a theorem about every scalar theory.

SymPy pinned by CI to 1.14.0.
"""
from __future__ import annotations

import json
import sympy as sp
from rot005_ko_sympy import calculate as recompute_ko


def exact_zero_matrix(m):
    return all(sp.simplify(v) == 0 for v in m)


def action_maxwell_in_orthonormal_frame(f):
    """Derive ordinary Maxwell stress from 6 independent 2-form entries."""
    eta = sp.diag(-1,1,1,1)
    assert f.shape == (4,4)
    assert f.T == -f
    Fup = eta*f*eta
    f2 = sp.expand(sum(f[i,j]*Fup[i,j] for i in range(4) for j in range(4)))
    Tcov = (f*eta*f.T - sp.Rational(1,4)*eta*f2).applyfunc(sp.expand)
    M = (eta*Tcov).applyfunc(sp.expand)
    rainich = (M*M - sp.eye(4)*sp.trace(M*M)/4).applyfunc(sp.expand)
    return {"T":Tcov,"mixed":M,"F2":f2,"Rainich":rainich}


def run():
    prior = recompute_ko()
    assert all(prior["checks"].values()), "Independent ROT-005 metric recomputation must pass"
    t,x,y,z = sp.symbols("t x y z",real=True)
    a = 1+t/2
    e = sp.exp(x/2)
    eta = sp.diag(-1,1,1,1)
    q = sp.Rational(1,10)
    C = sp.Matrix([[1,0,q*a*e,0],
                   [0,a,0,0],
                   [0,0,sp.sqrt(101)*a*e/10,0],
                   [0,0,0,a]])
    g = sp.Matrix([[-1,0,-q*a*e,0],
                   [0,a*a,0,0],
                   [-q*a*e,0,a*a*e*e,0],
                   [0,0,0,a*a]])
    assert exact_zero_matrix(C.T*eta*C-g)

    # Metric's exact G_ab already reconstructed in ROT-005 from Christoffel,
    # Ricci and Einstein tensor; here use its orthonormal coframe result.
    G0 = sp.Matrix([[sp.sympify(v) for v in row]
                    for row in prior["orthonormal_T_eff_times_a2"]])
    Ghat = G0/a**2

    dsquared=sp.Rational(39850,30199)
    allowed_d=(sp.sqrt(dsquared),-sp.sqrt(dsquared))
    branches=[]
    witnesses=[]
    for sign,d in zip(("positive","negative"),allowed_d):
        # Fixed logarithmic real scalar:
        # phi=(101*d/100)*log(a) + d*x.
        # Physical covector dphi transforms from coordinates to the
        # orthonormal coframe via C^{-T}; no Maxwell ansatz is used.
        gradient=sp.Matrix([sp.Rational(101,200)*d/a,d,0,0])
        phi_hat=(C.inv().T*gradient).applyfunc(sp.simplify)
        grad_sq=sp.simplify((phi_hat.T*eta*phi_hat)[0])
        assert sp.simplify(grad_sq-sp.Rational(797,808)/a**2)==0
        Tphi=(phi_hat*phi_hat.T-sp.Rational(1,2)*eta*grad_sq).applyfunc(sp.simplify)
        residual=(Ghat-Tphi).applyfunc(sp.simplify)
        M=(eta*residual).applyfunc(sp.simplify)
        assert sp.simplify(sp.trace(M))==0, "Einstein trace should pass"

        # Compute tensor Rainich obstruction, scaled by a^4 for a rational
        # certificate independent of position in the physical domain.
        N=(a*a*M).applyfunc(sp.simplify)
        Q=(N*N-sp.eye(4)*sp.trace(N*N)/4).applyfunc(sp.simplify)
        exact_certificate=-sp.Rational(160795,326432)
        assert sp.simplify(Q[0,1]-exact_certificate)==0
        assert exact_certificate!=0
        witnesses.append(sp.simplify(Q[0,1]))
        branches.append({
            "d_sign":sign,
            "d":str(d),
            "scalar_gradient_squared":str(grad_sq),
            "candidate_Maxwell_trace":"0",
            "Rainich_a4_Q_0_1":str(Q[0,1]),
            "Rainich_Q_0_1":str(sp.factor(Q[0,1]/a**4)),
            "result":"TERMINAL_FAIL_NO_MAXWELL_2_FORM"
        })
    assert len(branches)==2 and witnesses[0]==witnesses[1]

    # UNIVERSAL symbolic positive control with six independent real
    # antisymmetric field components: catches sign/index convention bugs.
    f=sp.symbols("f01 f02 f03 f12 f13 f23",real=True)
    F=sp.zeros(4)
    for value,(i,j) in zip(f,((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))):
        F[i,j]=value
        F[j,i]=-value
    generic=action_maxwell_in_orthonormal_frame(F)
    assert sp.expand(sp.trace(generic["mixed"]))==0
    assert exact_zero_matrix(generic["Rainich"])

    # Independent null Maxwell control: F=(dt-dz) wedge dx; nonzero
    # physical stress yet both algebraic Rainich conditions hold.
    nullF=sp.zeros(4)
    nullF[0,1]=1
    nullF[1,0]=-1
    nullF[1,3]=1
    nullF[3,1]=-1
    null=action_maxwell_in_orthonormal_frame(nullF)
    assert null["F2"]==0 and null["T"]!=sp.zeros(4)
    assert exact_zero_matrix(null["Rainich"])

    return {
        "experiment":"ROT-010",
        "source":"research/ROT-010_PROTOCOL.md",
        "verification_status":"PASS_EXACT_RAINICH_TENSOR_NO_GO",
        "candidate_verdict":"FAIL_LOG_SCALAR_WITH_ARBITRARY_ORDINARY_REAL_MAXWELL_2_FORM",
        "metric":"fixed ROT-005 Korotkii-Obukhov",
        "physical_domain":"t>-2, a(t)=1+t/2>0",
        "scalar":"phi=(101d/100)*ln(a)+d*x; d^2=39850/30199",
        "Maxwell_scope":"ALL six real algebraic components, no restrictive potential/coordinate ansatz",
        "source_tensor":"S_ab=G_ab-T_canonical_scalar_ab",
        "source_trace":"0",
        "Rainich_needed":"(g^{-1}S)^2 - I*tr((g^{-1}S)^2)/4 = 0",
        "exact_nonzero_certificate":"a^4 * Q^0_1 = -160795/326432",
        "real_scalar_sign_branches":branches,
        "null_Maxwell_positive_control":"PASS",
        "six_independent_Maxwell_components_symbolic_identity":"PASS",
        "termination":"TWO_SCALAR_SIGNS_EXHAUSTED_NO_ALGEBRAIC_MAXWELL_STRESS",
        "Maxwell_field_equations":"NOT REQUIRED: algebraic necessary condition fails before differential equations",
        "scope":"Only this frozen scalar + standard massless linear Maxwell action on fixed geometry. Other scalars, nonlinear EM, nonminimal source, fluids, potentials, metrics or observed cosmic rotation UNRESOLVED."
    }


if __name__=="__main__":
    print(json.dumps(run(),indent=2))
