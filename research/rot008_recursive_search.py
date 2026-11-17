"""ROT-008 — predictive, recursive, finite proof search for frozen phi=c*t+d*x.

This is a deterministic exact proof tree, not a cosmological discovery and
not an autonomous search over arbitrary physical theories.

Inputs frozen in ROT-008_PROTOCOL.md and ROT-008_PREDICTIONS_AND_STOP.md:
  KO metric from ROT-005, t>-2, a(t)=1+t/2, κ=1, Λ=V=0
  real scalar phi=c*t+d*x, c,d real constants
  standard source-free Maxwell potential A=E(t)*exp(x/2)dy+B(t)dz.

The two independent branches check wave -> Einstein trace and
Einstein trace -> wave; recursion terminates at an exact contradiction.
Other scalar profiles and sources are NOT part of the search space.
"""
from __future__ import annotations

import json
import sympy as sp
from rot005_ko_sympy import calculate as verify_ko_metric


def compute() -> dict[str, object]:
    prior = verify_ko_metric()
    assert all(prior["checks"].values()), "KO exact GR metric must be verified first"

    t, x, y, z = sp.symbols("t x y z", real=True)
    c, d = sp.symbols("c d", real=True)
    coords = (t, x, y, z)
    a = 1 + t/sp.Integer(2)
    expx = sp.exp(x/2)
    q = sp.Rational(1,10)
    metric = sp.Matrix([
        [-1,0,-q*a*expx,0],
        [0,a*a,0,0],
        [-q*a*expx,0,a*a*expx**2,0],
        [0,0,0,a*a]
    ])
    inv = metric.inv().applyfunc(sp.simplify)
    sqrt_minus_det = sp.sqrt(101)/10*a**3*expx
    assert sp.simplify(-metric.det()-sqrt_minus_det**2)==0
    assert sp.simplify(inv[0,0]+sp.Rational(100,101))==0
    assert sp.simplify(inv[1,1]-1/a**2)==0
    assert sp.simplify(inv[0,1])==0

    phi = c*t+d*x
    gradient = sp.Matrix([sp.diff(phi,v) for v in coords])
    raised = inv*gradient
    grad_sq = sp.factor((gradient.T*raised)[0])
    box_phi = sp.factor(sum(
        sp.diff(sqrt_minus_det*raised[i], coords[i])
        for i in range(4))/sqrt_minus_det)
    expected_box = (101*d-300*c*a)/(202*a*a)
    assert sp.simplify(box_phi-expected_box)==0

    # Independent target Einstein trace: reconstruct from frozen KO tetrad,
    # not by declaring a desired arbitrary matter source.
    T0 = sp.Matrix([[sp.sympify(s) for s in row]
                    for row in prior["orthonormal_T_eff_times_a2"]])
    coframe=sp.Matrix([
        [1,0,q*a*expx,0],
        [0,a,0,0],
        [0,0,sp.sqrt(101)*a*expx/10,0],
        [0,0,0,a]
    ])
    assert (coframe.T*sp.diag(-1,1,1,1)*coframe-metric).applyfunc(sp.simplify)==sp.zeros(4)
    Gcov=(coframe.T*T0*coframe/a**2).applyfunc(sp.simplify)
    Einstein_trace=sp.factor((inv*Gcov).trace())
    assert sp.simplify(Einstein_trace+sp.Rational(797,808)/a**2)==0

    # Matter stress: fixed minimal real scalar + arbitrary source-free
    # Maxwell field. Both are derived from the action, not chosen afterward.
    scalar_cov=(gradient*gradient.T
                -sp.Rational(1,2)*metric*grad_sq).applyfunc(sp.simplify)
    scalar_trace=sp.factor((inv*scalar_cov).trace())
    assert sp.simplify(scalar_trace+grad_sq)==0
    E=sp.Function("E")(t)
    B=sp.Function("B")(t)
    A=sp.Matrix([0,0,E*expx,B])
    F=sp.Matrix(4,4,lambda i,j:sp.diff(A[j],coords[i])-
                                     sp.diff(A[i],coords[j]))
    Fup=(inv*F*inv.T).applyfunc(sp.simplify)
    F2=sp.factor(sum(F[i,j]*Fup[i,j] for i in range(4)
                     for j in range(4)))
    em_cov=(F*inv*F.T-sp.Rational(1,4)*metric*F2).applyfunc(sp.simplify)
    em_trace=sp.simplify((inv*em_cov).trace())
    assert em_trace==0
    bianchi=[sp.simplify(
        sp.diff(F[i,j],coords[k])+sp.diff(F[j,k],coords[i])
        +sp.diff(F[k,i],coords[j]))
        for i in range(4) for j in range(i+1,4) for k in range(j+1,4)]
    assert all(value==0 for value in bianchi)

    trace_residual=sp.factor(Einstein_trace-scalar_trace-em_trace)
    expected_trace=(d*d-sp.Rational(797,808)
                    -sp.Rational(100,101)*c*c*a*a)/(a*a)
    assert sp.simplify(trace_residual-expected_trace)==0

    # Two proof orders prune independently. These are identities for all
    # t>-2, never finite sampling substitutions masquerading as a theorem.
    wave_polynomial=sp.factor(202*a*a*box_phi)
    trace_polynomial=sp.factor(a*a*trace_residual)
    assert sp.expand(wave_polynomial-(101*d-300*c*a))==0
    assert sp.simplify(sp.diff(wave_polynomial,t)+150*c)==0
    assert sp.simplify(trace_polynomial-(
        d*d-sp.Rational(797,808)-sp.Rational(100,101)*c*c*a*a))==0
    assert sp.simplify(sp.diff(trace_polynomial,t)+
        sp.Rational(100,101)*c*c*a)==0

    proof_tree = []
    MAX_DEPTH = 6

    def prune(branch:str,depth:int,assignments:dict[str,sp.Expr]):
        if depth>MAX_DEPTH:
            raise AssertionError("Unjustified recursive depth")
        if branch=="wave-first" and depth==0:
            derivative=sp.diff(wave_polynomial,t) # -150*c identically
            assert sp.solveset(derivative,c,domain=sp.S.Reals)==sp.FiniteSet(0)
            proof_tree.append({"branch":branch,"depth":depth,
                "test":"d/dt[(202*a^2)*Box(phi)]=0 on interval",
                "deduction":"c=0","status":"PRUNED_TO_SUBBRANCH"})
            return prune(branch,1,{"c":sp.Integer(0)})
        if branch=="wave-first" and depth==1:
            assert assignments["c"]==0
            remainder=sp.factor(wave_polynomial.subs(c,0))
            assert remainder==101*d
            assert sp.solveset(remainder,d,domain=sp.S.Reals)==sp.FiniteSet(0)
            proof_tree.append({"branch":branch,"depth":depth,
                "test":"Box(phi)=0 after c=0",
                "deduction":"d=0","status":"PRUNED_TO_SUBBRANCH"})
            return prune(branch,2,{"c":sp.Integer(0),"d":sp.Integer(0)})
        if branch=="wave-first" and depth==2:
            residual=sp.factor(trace_polynomial.subs({c:0,d:0}))
            assert residual==-sp.Rational(797,808)
            proof_tree.append({"branch":branch,"depth":depth,
                "test":"Einstein trace at c=d=0",
                "contradiction":"-797/808 != 0 for all a>0",
                "status":"TERMINAL_FAIL"})
            return True

        if branch=="trace-first" and depth==0:
            # The derivative is -(100/101)*c^2*a for all a>0;
            # evaluating the identity at t=0 yields c=0.
            derivative=sp.factor(sp.diff(trace_polynomial,t))
            assert sp.factor(derivative.subs(t,0))==-sp.Rational(100,101)*c*c
            assert sp.solveset(derivative.subs(t,0),c,domain=sp.S.Reals)==sp.FiniteSet(0)
            proof_tree.append({"branch":branch,"depth":depth,
                "test":"d/dt[a^2*(G_trace-T_trace)]=0 on interval",
                "deduction":"c=0","status":"PRUNED_TO_SUBBRANCH"})
            return prune(branch,1,{"c":sp.Integer(0)})
        if branch=="trace-first" and depth==1:
            rem=sp.factor(trace_polynomial.subs(c,0))
            assert sp.simplify(rem-(d*d-sp.Rational(797,808)))==0
            sols=sp.solveset(rem,d,domain=sp.S.Reals)
            assert sols==sp.FiniteSet(-sp.sqrt(sp.Rational(797,808)),
                                      sp.sqrt(sp.Rational(797,808)))
            proof_tree.append({"branch":branch,"depth":depth,
                "test":"Einstein trace after c=0",
                "deduction":"d=+-sqrt(797/808), so d != 0",
                "status":"PRUNED_TO_SUBBRANCH"})
            return prune(branch,2,{"c":sp.Integer(0)})
        if branch=="trace-first" and depth==2:
            # Wave equation at c=0 requires d=0, impossible with trace.
            rem=sp.factor(wave_polynomial.subs(c,0))
            assert rem==101*d
            assert sp.Rational(797,808)>0
            proof_tree.append({"branch":branch,"depth":depth,
                "test":"Box(phi)=0 after c=0 and d^2=797/808",
                "contradiction":"wave demands d=0 but trace demands d^2=797/808>0",
                "status":"TERMINAL_FAIL"})
            return True
        raise AssertionError("Unexpected branch/depth; search cannot continue silently")

    terminal_wave=prune("wave-first",0,{})
    terminal_trace=prune("trace-first",0,{})
    assert terminal_wave and terminal_trace
    assert len(proof_tree)==6
    assert len([step for step in proof_tree if step["status"]=="TERMINAL_FAIL"])==2

    # Positive/negative controls: single gate passing does not close theory.
    wave_null=sp.factor(box_phi.subs({c:0,d:0}))
    trace_null=sp.factor(trace_residual.subs({c:0,d:0}))
    assert wave_null==0 and trace_null==-sp.Rational(797,808)/a**2
    d_control=sp.sqrt(sp.Rational(797,808))
    assert sp.simplify(trace_residual.subs({c:0,d:d_control}))==0
    assert sp.simplify(box_phi.subs({c:0,d:d_control}))!=0
    # A pointwise wave condition at t=0 is insufficient for all spacetime.
    assert sp.simplify(box_phi.subs({c:101,d:300,t:0}))==0
    assert sp.simplify(box_phi.subs({c:101,d:300,t:2}))!=0

    return {
        "experiment":"ROT-008",
        "status":"PASS_FINITE_RECURSIVE_NO_GO_VERIFICATION",
        "candidate_verdict":"FAIL_FROZEN_ACTION_AND_LINEAR_REAL_SCALAR_ANSATZ",
        "predictions_file":"research/ROT-008_PREDICTIONS_AND_STOP.md",
        "physical_domain":"t>-2; a(t)=1+t/2>0; real constants c,d",
        "wave_equation":str(box_phi),
        "wave_polynomial_202_a2":str(wave_polynomial),
        "required_Einstein_trace":str(Einstein_trace),
        "scalar_trace":str(scalar_trace),
        "Maxwell_trace":str(em_trace),
        "Einstein_trace_residual":str(trace_residual),
        "trace_polynomial_a2":str(trace_polynomial),
        "proof_strategy":"deterministic recursive branch-prune, independent wave-first and trace-first",
        "max_allowed_depth":MAX_DEPTH,
        "branches_evaluated":2,
        "nodes_evaluated":len(proof_tree),
        "terminal_contradictions":2,
        "branch_ledger":proof_tree,
        "controls":{
            "zero_scalar_wave_equation":"PASS",
            "zero_scalar_Einstein_trace":"FAIL",
            "trace_only_nonzero_spatial_scalar":"PASS_TRACE_BUT_FAIL_WAVE",
            "single_time_wave_solution":"PASS_AT_ONE_TIME_BUT_FAIL_GLOBAL"
        },
        "Maxwell_dF_zero_checked":True,
        "remaining_Maxwell_equations":"NOT_SOLVED: not needed after necessary Einstein+wave contradictions",
        "termination":"PROVEN_EXACT_UNSAT_FOR_FROZEN_DOMAIN_AND_ANSATZ",
        "limits":"Cannot infer impossibility for general phi(t,x), phi=F(t)+d*x, new potentials, nonminimal scalar/vector theory, other metrics or observed universal rotation."
    }


if __name__=="__main__":
    print(json.dumps(compute(),indent=2))
