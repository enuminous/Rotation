"""ROT-009: exact full-tensor matter comparison and finite real-branch termination.

Frozen inputs: research/ROT-009_PROTOCOL.md, produced after ROT-008.
This code does not modify the action, metric, or scalar ansatz.

Geometry is the fixed ROT-005 causal expanding/rotating Korotkii-Obukhov
metric. Matter action: Einstein + canonical real massless scalar + Maxwell;
kappa=1, Lambda=0, V=0, signature (-+++).

Scalar: phi = 101*d/100*log(a(t)) + d*x, d²=39850/30199.
Maxwell potential A = E(t)*exp(x/2)dy + B(t)dz; E,B real.
The Maxwell functions and derivatives remain *arbitrary*. The exact
(xx) Einstein equation is impossible at every point and for both signs d.

A verified early-stop negative certificate: constructing 10 Einstein
component residuals and Maxwell divergences does not imply that all
Maxwell equations were solved. They need not be after the contradiction.
No cosmic observation, EFMW-specific action, or novel GR metric is claimed.
"""
from __future__ import annotations

import json
import sympy as sp
from rot005_ko_sympy import calculate as verify_frozen_geometry


def run() -> dict[str,object]:
    prior = verify_frozen_geometry()
    assert all(prior["checks"].values()), "ROT-005 metric recomputation failed"

    t,x,y,z = sp.symbols("t x y z",real=True)
    coords=(t,x,y,z)
    a=sp.Integer(1)+t/sp.Integer(2)
    ex=sp.exp(x/2)
    q=sp.Rational(1,10)
    g=sp.Matrix([[-1,0,-q*a*ex,0],
                 [0,a*a,0,0],
                 [-q*a*ex,0,a*a*ex*ex,0],
                 [0,0,0,a*a]])
    gi=g.inv().applyfunc(sp.simplify)
    C=sp.Matrix([[1,0,q*a*ex,0],[0,a,0,0],
                 [0,0,sp.sqrt(101)*a*ex/10,0],[0,0,0,a]])
    eta=sp.diag(-1,1,1,1)
    assert (C.T*eta*C-g).applyfunc(sp.simplify)==sp.zeros(4)

    # Recover the exact Einstein tensor in coordinate components from the
    # output of a separate source-pinned full Christoffel -> Ricci GR run.
    T0=sp.Matrix([[sp.sympify(s) for s in row]
                  for row in prior["orthonormal_T_eff_times_a2"]])
    Einstein=(C.T*T0*C/a**2).applyfunc(sp.simplify)
    assert sp.simplify(Einstein[1,1]+sp.Rational(399,1616))==0
    einstein_trace=sp.simplify((gi*Einstein).trace())
    assert sp.simplify(einstein_trace+sp.Rational(797,808)/a**2)==0

    d=sp.symbols("d",real=True)
    dsq=sp.Rational(39850,30199)
    phi=sp.Rational(101,100)*d*sp.log(a)+d*x
    grad=sp.Matrix([sp.diff(phi,u) for u in coords])
    grad_sq=sp.factor((grad.T*gi*grad)[0])
    assert sp.simplify(grad_sq-sp.Rational(299,400)*d*d/a**2)==0
    rootg=sp.sqrt(101)*a**3*ex/10
    assert sp.simplify(-g.det()-rootg**2)==0
    wave=sp.simplify(sum(sp.diff(rootg*(gi*grad)[i],coords[i])
                       for i in range(4))/rootg)
    assert wave==0

    # Canonical scalar matter stress from the FROZEN metric-coupled action.
    scalar=(grad*grad.T-sp.Rational(1,2)*g*grad_sq).applyfunc(sp.simplify)
    assert sp.simplify(scalar[1,1]-sp.Rational(501,800)*d*d)==0
    assert sp.simplify((gi*scalar).trace()+grad_sq)==0

    # Maxwell action and stress in 4-D, with unspecified real functions.
    E=sp.Function("E",real=True)(t)
    B=sp.Function("B",real=True)(t)
    A=sp.Matrix([0,0,E*ex,B])
    F=sp.Matrix(4,4,lambda i,j:
                sp.diff(A[j],coords[i])-sp.diff(A[i],coords[j]))
    Fup=(gi*F*gi.T).applyfunc(sp.simplify)
    F2=sp.simplify(sum(F[i,j]*Fup[i,j]
                       for i in range(4) for j in range(4)))
    maxwell=(F*gi*F.T-sp.Rational(1,4)*g*F2).applyfunc(sp.simplify)
    assert sp.simplify((gi*maxwell).trace())==0
    dF=[sp.simplify(sp.diff(F[i,j],coords[k])
                   +sp.diff(F[j,k],coords[i])
                   +sp.diff(F[k,i],coords[j]))
        for i in range(4) for j in range(i+1,4)
        for k in range(j+1,4)]
    assert len(dF)==4 and all(z==0 for z in dF)

    # Maxwell's dynamical equations are explicitly formed as four
    # covariant divergences but not solved: no complete solution exists
    # once the necessary Einstein xx condition is contradictory.
    maxwell_div=[sp.simplify(sum(sp.diff(rootg*Fup[i,j],coords[i])
                        for i in range(4))/rootg) for j in range(4)]
    assert len(maxwell_div)==4

    # Form the ENTIRE covariant Einstein residual, not only the scalar trace.
    full=(Einstein-scalar-maxwell)
    components={(i,j):sp.factor(full[i,j])
                for i in range(4) for j in range(i,4)}
    assert len(components)==10
    assert all(sp.simplify(full[i,j]-full[j,i])==0
               for i in range(4) for j in range(4))

    # Exact single-component no-go, for any allowed values of E(t),
    # E'(t), B'(t). The xx component has opposite required sign:
    #   G_xx = -399/1616
    #   T_xx = +501/800*d² +25/202*E²/a²
    #                 +50/101*(E'²+B'²).
    Eprime=sp.diff(E,t)
    Bprime=sp.diff(B,t)
    Maxwell_xx=(sp.Rational(25,202)*E**2/a**2
                +sp.Rational(50,101)*(Eprime**2+Bprime**2))
    assert sp.simplify(maxwell[1,1]-Maxwell_xx)==0
    expected_xx=(-sp.Rational(399,1616)
                 -sp.Rational(501,800)*d*d-Maxwell_xx)
    assert sp.simplify(components[1,1]-expected_xx)==0

    # Verify the two previously passing necessary gates with d² fixed.
    scalar_trace=sp.simplify((gi*scalar).trace())
    assert sp.simplify(einstein_trace-scalar_trace).subs(d*d,dsq)==0
    assert sp.simplify(grad_sq.subs(d*d,dsq)
                       -sp.Rational(797,808)/a**2)==0

    # Exact positive-definite obstruction in a real jet space.
    P,V,W=sp.symbols("P V W",real=True)
    jac=sp.factor((-expected_xx).xreplace({
        Eprime:V,Bprime:W,E:P,d*d:dsq}))
    target=(sp.Rational(399,1616)+sp.Rational(501,800)*dsq
            +sp.Rational(25,202)*P**2/a**2
            +sp.Rational(50,101)*(V**2+W**2))
    assert sp.simplify(jac-target)==0
    assert sp.Rational(399,1616)>0
    assert sp.Rational(501,800)*dsq>0
    assert all(v>0 for v in
        [sp.Rational(25,202),sp.Rational(50,101)])
    constant_lower=sp.simplify(
        sp.Rational(399,1616)+sp.Rational(501,800)*dsq)
    assert constant_lower>0

    # Finite recursive branch pruning of the *two* allowed real signs.
    # Both have the same d² and cannot affect the fixed nonnegative
    # Maxwell sum of squares. No speculative new physical branches.
    ledger=[]
    for sign in ("positive","negative"):
        value=(1 if sign=="positive" else -1)*sp.sqrt(dsq)
        branch_res=sp.factor(expected_xx.subs(d,value))
        branch_expected=sp.factor(-constant_lower-Maxwell_xx)
        assert sp.simplify(branch_res-branch_expected)==0
        ledger.append({
            "sign_of_d":sign,
            "d":str(value),
            "wave_equation":"PASS",
            "Einstein_trace":"PASS",
            "xx_Einstein_equation":"TERMINAL_FAIL",
            "exact_gap_Gxx_minus_Txx":str(branch_expected),
            "lower_bound_of_Txx_minus_Gxx":str(constant_lower),
            "proof":"Real Maxwell jets give nonnegative squares, so gap is <0 for a>0"
        })
    assert len(ledger)==2
    assert all(x["xx_Einstein_equation"]=="TERMINAL_FAIL" for x in ledger)

    # Concrete independent arithmetic controls are supplemental, not
    # substitutes for the symbolic sign bound over all t and real fields.
    controls=[]
    for scale in (sp.Rational(1,2),sp.Rational(1),sp.Rational(2)):
        for (p,v,w) in ((0,0,0),(1,0,0),(0,1,1)):
            val=sp.simplify((-branch_expected).subs(
                {a:scale,E:sp.Integer(p),Eprime:sp.Integer(v),Bprime:sp.Integer(w)}))
            # xreplace also protects against derivatives that survive subs.
            test=sp.simplify(target.subs({a:scale,P:p,V:v,W:w}))
            assert test>0
            controls.append({"a":str(scale),"E":p,"Eprime":v,"Bprime":w,
                             "positive_gap_Txx_minus_Gxx":str(test)})

    return {
        "experiment":"ROT-009",
        "candidate_verdict":"FAIL_FROZEN_LOG_SCALAR_PLUS_MAXWELL",
        "verification_status":"PASS_EXACT_FULL_TENSOR_CONSTRUCTION_AND_BOUNDED_NO_GO",
        "source_protocol":"research/ROT-009_PROTOCOL.md",
        "domain":"t>-2, a(t)=1+t/2>0; scalar real; E(t),B(t) real",
        "fixed_d_squared":str(dsq),
        "wave_equation":str(wave),
        "full_einstein_symmetric_components_constructed":len(components),
        "Einstein_trace_minus_scalar_trace_at_d_squared_fixed":"0",
        "Maxwell_stress_trace":"0",
        "Maxwell_geometric_Bianchi_dF":"0 for every independent triple",
        "Einstein_G_xx":str(Einstein[1,1]),
        "scalar_T_xx":str(scalar[1,1]),
        "Maxwell_T_xx":str(Maxwell_xx),
        "xx_residual_G_minus_T":str(expected_xx),
        "strict_lower_bound_of_Txx_minus_Gxx":str(constant_lower),
        "allowed_real_branches":len(ledger),
        "terminal_fail_branches":len(ledger),
        "branch_ledger":ledger,
        "sample_controls":controls,
        "Maxwell_dynamic_equations":{
            "derived_divergence_components":[str(z) for z in maxwell_div],
            "solved":"NO: impossible necessary Einstein xx component makes full solution nonexistent"
        },
        "termination":"PROVEN_UNSAT_FOR_TWO_FROZEN_REAL_SIGN_BRANCHES",
        "scope":"Only frozen KO metric, log scalar with fixed d², and canonical Maxwell potential. Does not exclude other matter, potentials, nonminimal couplings, scalar profiles, metrics or observed cosmic rotation."
    }


if __name__=="__main__":
    print(json.dumps(run(),indent=2))
