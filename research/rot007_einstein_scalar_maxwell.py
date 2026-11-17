"""ROT-007: exact trace obstruction for the frozen Einstein–scalar–Maxwell ansatz.

Action (4D, signature -+++, kappa=1, Lambda=0, V=0):
    S = integral sqrt(-g) [ R/2 - (1/2)*(grad phi)^2 - (1/4)*F^2 ].
Scalar field phi=phi(t), Maxwell potential
    A = E(t)*exp(x/2) dy + B(t) dz.
Fixed KO metric, t > -2, a(t)=1+t/2:
    ds² = -(dt+a exp(x/2) dy/10)²
          + a² dx² + (101/100)*a² exp(x) dy² + a² dz².

The trace equation is a necessary consequence of all ten Einstein
components. The action and ansatz fail it for every real phi(t), E(t), B(t).
No need to solve Maxwell/trace-free Einstein equations after contradiction.

Reuses ROT-005's separately tested Einstein tensor, while independently
building the metric and both field stress tensors here.
"""
from __future__ import annotations

import json
import sympy as sp
from rot005_ko_sympy import calculate


def calculate_rot007():
    old = calculate()
    assert all(old["checks"].values()), "frozen ROT-005 must pass"

    t, x, y, z = sp.symbols("t x y z", real=True)
    coords = (t, x, y, z)
    a = 1 + t/2
    e = sp.exp(x/2)
    q = sp.Rational(1, 10)
    g = sp.Matrix([
        [-1, 0, -q*a*e, 0],
        [0, a*a, 0, 0],
        [-q*a*e, 0, a*a*e*e, 0],
        [0, 0, 0, a*a]
    ])
    gi = g.inv().applyfunc(sp.simplify)
    assert sp.simplify(gi[0, 0] + sp.Rational(100,101)) == 0

    # Orthonormal covariant source is the previously independently
    # computed G_ab expressed in the rotating matter coframe.
    Tframe = sp.Matrix([
        [sp.sympify(v) for v in row]
        for row in old["orthonormal_T_eff_times_a2"]
    ])
    coframe = sp.Matrix([
        [1, 0, q*a*e, 0],
        [0, a, 0, 0],
        [0, 0, sp.sqrt(101)*a*e/10, 0],
        [0, 0, 0, a]
    ])
    assert (coframe.T*sp.diag(-1,1,1,1)*coframe-g).applyfunc(sp.simplify) == sp.zeros(4)
    Gcov = (coframe.T*Tframe*coframe/a**2).applyfunc(sp.simplify)
    Gtrace = sp.simplify((gi*Gcov).trace())
    R = -Gtrace  # g^ab G_ab = -R in 4 spacetime dimensions.
    expected_R = sp.Rational(797,808)/a**2
    assert sp.simplify(R - expected_R) == 0
    assert sp.simplify(Gtrace + expected_R) == 0

    # Canonical scalar stress comes from L_phi=-1/2*(grad phi)^2;
    # explicit zero V is part of the FROZEN proposal.
    phi = sp.Function("phi")(t)
    dphi = sp.Matrix([sp.diff(phi, t), 0, 0, 0])
    grad_sq = sp.simplify((dphi.T*gi*dphi)[0])
    Tphi = (dphi*dphi.T - sp.Rational(1,2)*g*grad_sq).applyfunc(sp.simplify)
    trace_scalar = sp.simplify((gi*Tphi).trace())
    assert sp.simplify(trace_scalar + grad_sq) == 0
    assert sp.simplify(
        grad_sq + sp.Rational(100,101)*sp.diff(phi, t)**2
    ) == 0

    # Source-first Maxwell potential, no free stress tensor.
    E = sp.Function("E")(t)
    B = sp.Function("B")(t)
    Acov = sp.Matrix([0, 0, E*e, B])
    F = sp.Matrix(4, 4, lambda i,j:sp.diff(Acov[j],coords[i])-
                                        sp.diff(Acov[i],coords[j]))
    Fup = (gi*F*gi.T).applyfunc(sp.simplify)
    invariant = sp.simplify(sum(
        F[i,j]*Fup[i,j] for i in range(4) for j in range(4)
    ))
    Tem = (F*gi*F.T-sp.Rational(1,4)*g*invariant).applyfunc(sp.simplify)
    trace_em = sp.simplify((gi*Tem).trace())
    assert trace_em == 0

    # F=dA guarantees homogeneous Maxwell equations for any E(t),B(t).
    bianchi = [sp.simplify(
        sp.diff(F[i,j],coords[k]) +
        sp.diff(F[j,k],coords[i]) +
        sp.diff(F[k,i],coords[j]))
        for i in range(4) for j in range(i+1,4)
        for k in range(j+1,4)]
    assert all(v==0 for v in bianchi)

    # Trace of all Einstein equations, not a fitted component:
    trace_total = sp.simplify((gi*(Tphi+Tem)).trace())
    assert sp.simplify(trace_total -
        sp.Rational(100,101)*sp.diff(phi,t)**2) == 0

    # G^a_a = T^a_a is necessary for Einstein equations.
    # Since t>-2 => a>0 and real phi_dot^2 >=0, RHS>=0.
    # Target G trace is strictly negative for every a>0.
    rhs_sq = sp.simplify(Gtrace/sp.Rational(100,101))
    expected_rhs = -sp.Rational(80497,80800)/a**2
    assert sp.simplify(rhs_sq-expected_rhs) == 0
    assert expected_rhs.subs(t,0) < 0

    # Recompute representative trace at independent positive-scale values,
    # not as a replacement for the global exact algebraic obstruction.
    values = []
    for at in [sp.Rational(1,2), sp.Rational(1), sp.Rational(2),
               sp.Rational(10)]:
        tvalue = 2*(at-1)
        trace_g = sp.simplify(Gtrace.subs(t,tvalue))
        required = sp.simplify(rhs_sq.subs(t,tvalue))
        assert trace_g<0 and required<0 and tvalue>-2
        values.append({"a":str(at),"G_trace":str(trace_g),
                       "required_real_phi_dot_squared":str(required)})

    return {
        "audit":"ROT-007",
        "status":"PASS_EXACT_NO_GO_FOR_FROZEN_ACTION_AND_HOMOGENEOUS_SCALAR_ANSATZ",
        "verdict_for_candidate":"FAIL",
        "fixed_background":"ROT-005 Korotkii-Obukhov causal rotating and expanding metric",
        "action":"Einstein plus minimally coupled real massless canonical scalar plus Maxwell, V=0, Lambda=0, kappa=1",
        "scalar_ansatz":"phi(t) real",
        "maxwell_ansatz":"A=E(t)*exp(x/2) dy+B(t) dz",
        "inverse_gtt":str(gi[0,0]),
        "required_Einstein_trace_Ga_a":str(Gtrace),
        "Ricci_scalar":str(R),
        "derived_scalar_trace":str(trace_scalar),
        "derived_Maxwell_trace":str(trace_em),
        "total_candidate_trace":str(trace_total),
        "Einstein_trace_forces_phi_dot_squared":str(rhs_sq),
        "reason":"A positive scale factor makes the required phi_dot^2 strictly negative; no real homogeneous scalar can satisfy the Einstein trace; Maxwell is traceless for all F in 4D.",
        "Maxwell_dF_zero_verified":all(z==0 for z in bianchi),
        "field_equations_status":"Einstein trace contradiction is sufficient to reject the entire coupled system; no successful full field-equation solution claimed.",
        "sample_values":values,
        "boundary":"Does not rule out phi(x,t), nonzero V(phi), nonminimal or higher-derivative couplings, extra matter, or different GR metrics. No new observational cosmic rotation evidence."
    }


if __name__=="__main__":
    print(json.dumps(calculate_rot007(),indent=2))
