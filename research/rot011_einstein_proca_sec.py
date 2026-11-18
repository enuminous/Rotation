"""ROT-011 — exact strong-energy-condition no-go for canonical Proca sources.

Predeclared inputs: ROT-011_PROTOCOL.md; frozen ROT-005 metric, t>-2,
Λ=0, κ=8πG=1, signature (-,+,+,+), plus any finite sum of
positive-kinetic real ordinary Proca (μ²>=0), Maxwell and real
massless minimally coupled scalar fields. No potentials or extra matter.

An explicit timelike vector violates the GR strong-energy condition:
  (a²) Ricci_hat_ab v^a v^b = (703 - 80*sqrt(101))/80800 < 0,
  eta(v,v)=-99/100, v=(1,0,1/10,0).
But each permitted matter sector has NONNEGATIVE trace-reversed
stress on every timelike vector. The contradiction excludes the entire
frozen canonical source class for this one metric. This is not a
no-go for other rotating metrics or more general physical actions.

The test also independently validates the generic six-component Maxwell
energy as a sum of squares in a boosted orthonormal frame and the
canonical Proca+scalar trace reversal identity.

Sources: Maeda & Martinez (2020) DOI 10.1093/ptep/ptaa009;
ROT-005 exact GR metric code.
"""
from __future__ import annotations

import json
import sympy as sp
from rot005_ko_sympy import calculate as verify_ko


def zeros(matrix):
    return all(sp.simplify(x)==0 for x in matrix)


def run():
    previous=verify_ko()
    assert all(previous["checks"].values()), "ROT-005 source metric must pass"

    eta=sp.diag(-1,1,1,1)
    a=sp.symbols("a",positive=True,real=True) # physical a=1+t/2>0
    G0=sp.Matrix([[sp.sympify(item) for item in row]
                  for row in previous["orthonormal_T_eff_times_a2"]])
    G=G0/a**2
    trG=sp.simplify((eta*G).trace())
    assert sp.simplify(trG+sp.Rational(797,808)/a**2)==0
    Ricci=(G-sp.Rational(1,2)*trG*eta).applyfunc(sp.simplify)
    Ricci0=(a*a*Ricci).applyfunc(sp.simplify)
    expected=sp.Matrix([
        [sp.Rational(5,808),sp.Rational(1,404),-sp.sqrt(101)/202,0],
        [sp.Rational(1,404),sp.Rational(199,808),-sp.sqrt(101)/404,0],
        [-sp.sqrt(101)/202,-sp.sqrt(101)/404,sp.Rational(203,808),0],
        [0,0,0,sp.Rational(50,101)]
    ])
    assert zeros(Ricci0-expected)

    beta=sp.Rational(1,10)
    v=sp.Matrix([1,0,beta,0])
    norm=sp.simplify((v.T*eta*v)[0])
    assert norm==-sp.Rational(99,100)
    scaled_ricci_contraction=sp.simplify((v.T*Ricci0*v)[0])
    witness=(sp.Integer(703)-80*sp.sqrt(101))/sp.Integer(80800)
    assert sp.simplify(scaled_ricci_contraction-witness)==0
    assert 703**2 < 80**2*101 # strict exact comparison
    assert witness<0
    assert sp.simplify((v.T*Ricci*v)[0]-witness/a**2)==0

    # Unrestricted algebraic Maxwell 2-form with six independent
    # arbitrary REAL entries, no coordinate/gauge restriction.
    f01,f02,f03,f12,f13,f23=sp.symbols(
        "f01 f02 f03 f12 f13 f23",real=True)
    entries=(f01,f02,f03,f12,f13,f23)
    F=sp.zeros(4)
    for value,(i,j) in zip(entries,
                           ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))):
        F[i,j]=value
        F[j,i]=-value
    Fup=eta*F*eta
    F2=sp.expand(sum(F[i,j]*Fup[i,j]
                for i in range(4) for j in range(4)))
    T_EM=(F*eta*F.T-sp.Rational(1,4)*eta*F2).applyfunc(sp.expand)
    assert sp.expand((eta*T_EM).trace())==0

    A=sp.Matrix(sp.symbols("A0:4",real=True))
    p=sp.Matrix(sp.symbols("p0:4",real=True))
    mu2=sp.symbols("mu_squared",nonnegative=True,real=True)
    A2=sp.expand((A.T*eta*A)[0])
    p2=sp.expand((p.T*eta*p)[0])

    # Action-derived Proca with positive kinetic sign and μ²>=0.
    T_mass=mu2*(A*A.T-sp.Rational(1,2)*eta*A2)
    T_proca=(T_EM+T_mass).applyfunc(sp.expand)
    T_scalar=(p*p.T-sp.Rational(1,2)*eta*p2).applyfunc(sp.expand)
    T_total=(T_proca+T_scalar).applyfunc(sp.expand)
    trace=sp.expand((eta*T_total).trace())
    sec_tensor=(T_total-sp.Rational(1,2)*trace*eta).applyfunc(sp.expand)

    # Trace-reversal is an exact identity for all components and arbitrary
    # 6 Maxwell + 4 Proca + 4 gradient variables:
    #   SEC tensor = T_EM + mu² A_a A_b + p_a p_b.
    identity=(T_EM+mu2*A*A.T+p*p.T).applyfunc(sp.expand)
    assert zeros(sec_tensor-identity)

    # Show Maxwell positivity using an orthonormal Lorentz boost
    # (time, y) that sends the new timelike basis to v/sqrt(-v²).
    gamma=1/sp.sqrt(1-beta**2)
    L=sp.Matrix([[gamma,0,beta*gamma,0],
                 [0,1,0,0],
                 [beta*gamma,0,gamma,0],
                 [0,0,0,1]])
    assert zeros(L.T*eta*L-eta)
    assert zeros(L[:,0]-v/sp.sqrt(-norm))
    Fprime=(L.T*F*L).applyfunc(sp.simplify)
    Eprime_sq=sp.expand(sum(Fprime[0,i]**2 for i in (1,2,3)))
    Bprime_sq=sp.expand(sum(Fprime[i,j]**2
                      for i,j in ((1,2),(1,3),(2,3))))
    squares=sp.simplify(-norm*sp.Rational(1,2)*(Eprime_sq+Bprime_sq))
    Maxwell_contraction=sp.simplify((v.T*T_EM*v)[0])
    assert sp.simplify(Maxwell_contraction-squares)==0

    contraction=sp.factor((v.T*sec_tensor*v)[0])
    expression=(squares+mu2*(v.T*A)[0]**2+(v.T*p)[0]**2)
    assert sp.simplify(contraction-expression)==0
    assert sp.simplify(
        Maxwell_contraction-
        (101*f01**2-40*f01*f12+99*f02**2+101*f03**2
          +40*f03*f23+101*f12**2+99*f13**2+101*f23**2)/200
    )==0

    # Additional controls ensure the positivity calculation is not
    # identically zero or relying on the desired sign.
    z={sym:0 for sym in (*entries,*A,*p)}
    z[mu2]=sp.Integer(0)
    assert sp.simplify(contraction.subs(z))==0
    electric=dict(z);electric[f01]=1
    assert sp.simplify(contraction.subs(electric))>0
    only_proca=dict(z);only_proca[A[0]]=1;only_proca[mu2]=1
    assert sp.simplify(contraction.subs(only_proca))==1
    only_scalar=dict(z);only_scalar[p[0]]=1
    assert sp.simplify(contraction.subs(only_scalar))==1
    massless=dict(z);massless[f23]=1
    assert sp.simplify(contraction.subs(massless))>0

    # Einstein with Λ=0 demands Ricci(v,v)=SEC(v,v), but their signs
    # are strictly opposite for this fixed metric and every allowed source.
    branches=[
        {"source_class":"ordinary real Proca fields (mu²>=0, positive kinetic)",
         "verdict":"TERMINAL_FAIL_SEC"},
        {"source_class":"any finite sum of ordinary Maxwell and massless real scalar fields, plus real Proca",
         "verdict":"TERMINAL_FAIL_SEC"},
    ]
    return {
        "experiment":"ROT-011",
        "verification_status":"PASS_EXACT_SEC_SOURCE_NO_GO",
        "candidate_verdict":"FAIL_CANONICAL_EINSTEIN_PROCA_MAXWELL_MASSLESS_SCALAR_SOURCE_CLASS",
        "metric":"ROT-005 exact causal expanding/rotating Korotkii-Obukhov",
        "Lambda":"0","kappa":"1","physical_domain":"t>-2, a(t)=1+t/2>0",
        "matter_action":"standard positive kinetic Maxwell, real Proca with mu²>=0, massless real canonical scalar, any finite nonnegative sums",
        "observer_orthonormal_components":["1","0","1/10","0"],
        "observer_norm_squared":str(norm),
        "Ricci_orthonormal_times_a2":[[str(Ricci0[i,j]) for j in range(4)] for i in range(4)],
        "Ricci_observer_contraction":str(witness/a**2),
        "Ricci_observer_a2_coefficient":str(witness),
        "strict_negative_witness":"703^2=494209 < 80^2*101=646400; (703-80sqrt(101))/(80800 a^2)<0",
        "Maxwell_six_component_positive_control":"PASS EXACT SUM OF SIX SQUARES IN BOOSTED ORTHONORMAL FRAME",
        "Proca_trace_reverse_identity":"PASS: T_proca - 1/2 T_proca_trace eta = T_Maxwell + mu² A_a A_b",
        "scalar_trace_reverse_identity":"PASS: massless scalar contributes (grad_a phi)(grad_b phi)",
        "SEC_source_observer":"nonnegative for every real F, A, grad(phi) and mu²>=0",
        "source_branches":branches,
        "terminal_fail_branches":len(branches),
        "termination":"INVARIANT_STRONG_ENERGY_CONDITION_CONTRADICTION",
        "limits":"Exact no-go for this KO metric and only standard SEC-satisfying matter with Λ=0. Positive Λ, scalar potentials, nonminimal/higher-derivative source, exotic fluids or other metrics can violate SEC. Cosmic rotation observations and EFMW-specific predictions remain unresolved."
    }


if __name__=="__main__":
    print(json.dumps(run(),indent=2))
