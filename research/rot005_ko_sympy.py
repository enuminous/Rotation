"""ROT-005: an expanding, rotating, stably causal GR spacetime.

A fixed Korotkii-Obukhov type-III metric, checked from Christoffel symbols
through the Einstein tensor. All quantities exact in SymPy; c=1, kappa=1,
Lambda=0, signature (-,+,+,+).

R(t)=1+t/2>0, m=1/2, sqrt(sigma)=1/10, KO k=1.
ds^2=-(dt+R*exp(x/2)/10 dy)^2 + R^2 dx^2
     +(101/100)*R^2*exp(x) dy^2 +R^2 dz^2.

Physical observer candidate u^a=delta^a_t is unit timelike.
T_effective=G_ab is defined by the exact metric (not a separately derived
microphysical fluid model or EFMW action).

Sources:
Korotkii & Obukhov (1991), Eq. 4.1,
https://jetp.ras.ru/cgi-bin/dn/e_072_01_0011.pdf
Korotky, Masar & Obukhov (2020), Eq. 7,
https://doi.org/10.3390/universe6010014

This is a mathematical counterexample/research control, NOT observational
evidence of globally rotating cosmos or proof of canonical ME-056.
"""
from __future__ import annotations

import json
import sympy as sp


def zero(m):
    return all(sp.simplify(z) == 0 for z in m)


def calculate():
    t,x,y,z = sp.symbols("t x y z",real=True)
    X=(t,x,y,z)
    n=4
    half=sp.Rational(1,2)
    a=1+t/2
    e=sp.exp(x/2)
    q=sp.Rational(1,10)
    g=sp.Matrix([[-1,0,-q*a*e,0],
                 [0,a*a,0,0],
                 [-q*a*e,0,a*a*e*e,0],
                 [0,0,0,a*a]])
    gi=g.inv().applyfunc(sp.simplify)
    dg=[[[sp.diff(g[i,j],c) for j in range(n)]
          for i in range(n)] for c in X]
    Gamma=[[[sp.simplify(half*sum(
                 gi[i,l]*(dg[j][l][k]+dg[k][l][j]-dg[l][j][k])
                 for l in range(n))) for k in range(n)]
             for j in range(n)] for i in range(n)]
    ric=sp.Matrix(n,n,lambda i,j:sp.simplify(sum(
        sp.diff(Gamma[b][i][j],X[b])
        -sp.diff(Gamma[b][i][b],X[j])
        +sum(Gamma[b][b][c]*Gamma[c][i][j]
             -Gamma[b][j][c]*Gamma[c][i][b] for c in range(n))
        for b in range(n))))
    curv=sp.simplify((gi*ric).trace())
    G=(ric-half*curv*g).applyfunc(sp.simplify)
    u=sp.Matrix([1,0,0,0])
    ud=g*u
    D=sp.Matrix(n,n,lambda i,j:sp.simplify(
        sp.diff(ud[j],X[i])
        -sum(Gamma[k][i][j]*ud[k] for k in range(n))))
    theta=sp.simplify((gi*D).trace())
    accel=sp.Matrix([sp.simplify(D[0,j]) for j in range(n)])
    h=g+ud*ud.T
    Q=(D+ud*accel.T).applyfunc(sp.simplify)
    shear=((Q+Q.T)/2-theta*h/3).applyfunc(sp.simplify)
    vortex=((Q-Q.T)/2).applyfunc(sp.simplify)

    def norm2(M):
        raised=(gi*M*gi.T).applyfunc(sp.simplify)
        return sp.simplify(half*sum(M[i,j]*raised[i,j]
                                   for i in range(n) for j in range(n)))
    sig2=norm2(shear)
    omg2=norm2(vortex)
    rho=sp.simplify(G[0,0])
    p=sp.simplify(((gi+u*u.T)*G).trace()/3)
    rest=sp.simplify(curv+2*ric[0,0]
                    -sp.Rational(2,3)*theta**2+2*sig2-2*omg2)
    H=sp.simplify(theta/3)
    gauss=sp.simplify(3*H**2-(rho+sig2-omg2-rest/2))
    Aup=(gi*accel).applyfunc(sp.simplify)
    divA=sp.simplify(sum(
        sp.diff(Aup[i],X[i])
        +sum(Gamma[i][i][j]*Aup[j] for j in range(n))
        for i in range(n)))
    ray=sp.simplify(sp.diff(theta,t)-(
        -theta**2/3-2*sig2+2*omg2-(rho+3*p)/2+divA))

    # Directly check covariant conservation, not just invoke Bianchi.
    divG=[sp.simplify(sum(gi[i,j]*(
        sp.diff(G[j,b],X[i])
        -sum(Gamma[k][i][j]*G[k,b]+Gamma[k][i][b]*G[j,k]
             for k in range(n)))
        for i in range(n) for j in range(n))) for b in range(n)]

    # Orthonormal tetrad adapted to u.
    C=sp.Matrix([[1,0,q*a*e,0],[0,a,0,0],
                 [0,0,sp.sqrt(1+q*q)*a*e,0],[0,0,0,a]])
    source=(C.inv().T*G*C.inv()).applyfunc(sp.simplify)
    source_scaled=(source*a*a).applyfunc(sp.simplify)
    T0=sp.Matrix([
        [sp.Rational(807,1616),sp.Rational(1,404),-sp.sqrt(101)/202,0],
        [sp.Rational(1,404),-sp.Rational(399,1616),-sp.sqrt(101)/404,0],
        [-sp.sqrt(101)/202,-sp.sqrt(101)/404,-sp.Rational(391,1616),0],
        [0,0,0,sp.Rational(3,1616)]
    ])
    # For any timelike/null frame vector (1,beta), |beta|<=1,
    # T_ab v^a v^b >= rho - 2 sum_i |T_0i|
    #     + min(0,min_i[P_ii-sum_{j!=i}|P_ij|]).
    flux=sum(sp.Abs(T0[0,i]) for i in range(1,4))
    gersh=[sp.simplify(T0[i,i]-sum(sp.Abs(T0[i,j])
           for j in range(1,4) if j!=i)) for i in range(1,4)]
    wec_bound=sp.simplify(T0[0,0]-2*flux+gersh[0])
    exact_bound=(400-20*sp.sqrt(101))/1616

    # The ME-056 curvature parameter is NOT KO k=1.
    # This conditional scalar mapping is an explicit extra assumption.
    k_assumed=sp.simplify(a*a*rest/6)
    O_sq=sp.simplify(a*a*omg2)
    me=sp.simplify(rho/3-k_assumed/a**2+O_sq/a**2)
    mismatch=sp.simplify(me-H**2)
    k_retuned=sp.simplify(k_assumed+sp.Rational(4,3)*O_sq)
    me_fitted=sp.simplify(rho/3-k_retuned/a**2+O_sq/a**2)

    checks={
        "metric_signature":zero(C.T*sp.diag(-1,1,1,1)*C-g),
        "stable_causal_time":sp.simplify(gi[0,0])==-sp.Rational(100,101),
        "unit_observer":sp.simplify((u.T*g*u)[0])==-1,
        "expansion":sp.simplify(H-1/(2*a))==0,
        "shear_free":zero(shear) and sig2==0,
        "vorticity":sp.simplify(omg2-1/(1616*a*a))==0,
        "accelerated":not zero(accel),
        "gauss_constraint":gauss==0,
        "raychaudhuri":ray==0,
        "stress_conservation":all(z==0 for z in divG),
        "orthonormal_stress":zero(source_scaled-T0),
        "WEC_all_causal_frame_directions":
             sp.simplify(wec_bound-exact_bound)==0 and bool(wec_bound>0),
        "effective_matter_not_comoving_perfect_fluid":T0[0,2]!=0,
        "ME056_natural_mapping_mismatch":
             sp.simplify(mismatch-1/(1212*a*a))==0 and bool(mismatch.subs(t,0)>0),
        "ME056_scalar_curvature_retuning":
             k_retuned==-sp.Rational(67,808)
             and sp.simplify(me_fitted-H**2)==0
    }
    if not all(checks.values()):
        raise AssertionError("ROT-005 failed: "+repr(checks))
    return {
        "status":"PASS_FIXED_CAUSAL_EXPANDING_ROTATING_EINSTEIN_METRIC_WITH_WEC_EFFECTIVE_MATTER",
        "case":"Korotkii-Obukhov Bianchi III with m=1/2, sqrt(sigma)=1/10, k_KO=1, a(t)=1+t/2",
        "domain":"t>-2 and spatial R^3; global t has timelike gradient",
        "physical_observer":"u^a=(1,0,0,0); kappa=1, Lambda=0",
        "H":str(H),"shear_sq":str(sig2),"physical_vorticity_sq":str(omg2),
        "projected_rest_curvature":str(rest),
        "effective_kappa_rho":str(rho),"effective_kappa_pressure":str(p),
        "orthonormal_T_eff_times_a2":[[str(T0[i,j]) for j in range(n)]
                                      for i in range(n)],
        "WEC_global_sufficient_bound_times_a2":str(wec_bound),
        "gauss_residual":str(gauss),"raychaudhuri_residual":str(ray),
        "einstein_covariant_conservation_residuals":[str(z) for z in divG],
        "ME056_natural_mapping":{
            "extra_assumption":"k_ME = a^2*R_rest/6; Omega_ME^2=a^2*omega_physical^2",
            "k_ME":str(k_assumed),"Omega_ME_squared":str(O_sq),
            "H2_ME_minus_H2_GR":str(mismatch),"result":"FAIL_UNDER_THIS_MAPPING"
        },
        "ME056_retuned_scalar_fit":{
            "k_ME_retuned":str(k_retuned),
            "H2_ME_minus_H2_GR":str(sp.simplify(me_fitted-H**2)),
            "result":"EXACT_FIT_BUT_CANNOT_IDENTIFY_ROTATION_FROM_SCALAR_EXPANSION"
        },
        "matter_caveat":"T_eff=G/kappa is a conserved imperfect effective source with WEC. No microphysical action was specified; no observed cosmic fit.",
        "checks":checks
    }


if __name__=="__main__":
    print(json.dumps(calculate(),indent=2))
