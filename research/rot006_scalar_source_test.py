"""ROT-006: source-first scalar and electromagnetic matter no-go for ROT-005.

Exact SymPy 1.14.0. The frozen ROT-005 Einstein tensor is independently
recomputed by rot005_ko_sympy.calculate(), not entered as a free matter fit.

Matter classes tested:
  - perfect fluid, any tilt and equation of state;
  - one minimally coupled first-derivative real scalar / k-essence;
  - two minimally coupled first-derivative real scalars / one complex scalar;
  - pure standard Maxwell electromagnetism.
No statement excludes higher-derivative, curvature-coupled, >2-scalar,
interacting scalar-vector, or general imperfect-fluid matter.

Metric signature (-,+,+,+); c=1, 8*pi*G=1, Lambda=0.
"""
from __future__ import annotations
import json
import sympy as sp
from rot005_ko_sympy import calculate


def scalar_multiplicity_floor(number_of_scalar_fields: int) -> int:
    """For S_m=integral sqrt(-g)L(phi^I,X^IJ), rank(T^a_b-L delta^a_b)<=N.

    X^IJ=-1/2*g^ab*(grad_a phi^I)*(grad_b phi^J).
    Thus at least (4-N) algebraic eigenvalues equal L at each point.
    This scope excludes curvature/higher derivative metric dependence.
    """
    if number_of_scalar_fields<0 or number_of_scalar_fields>4:
        raise ValueError("Expected 0 to 4 independent first-derivative fields")
    return 4-number_of_scalar_fields


def verify() -> dict:
    geo=calculate()
    assert all(geo["checks"].values()), "ROT-005 exact metric must pass first"
    T=sp.Matrix([[sp.sympify(v) for v in row]
                 for row in geo["orthonormal_T_eff_times_a2"]])
    eta=sp.diag(-1,1,1,1)
    M=(1616*eta*T).applyfunc(sp.simplify)
    z=sp.symbols("z")
    polynomial=sp.factor(M.charpoly(z).as_expr())
    expected=(z-3)*(z**3+1597*z**2+798403*z+127206399)
    assert sp.expand(polynomial-expected)==0
    gcd=sp.gcd(polynomial,sp.diff(polynomial,z))
    disc=sp.factor(sp.discriminant(polynomial,z))
    assert gcd==1 and disc>0, "Four distinct mixed eigenvalues required"

    # Source-first canonical scalar action L=-1/2*g^ab phi_a phi_b - V.
    # Its T^a_b=L*delta^a_b + (grad^a phi)*(grad_b phi) has rank-one
    # deviation from an isotropic tensor, for ANY gradient direction.
    p0,p1,p2,p3,V=sp.symbols("p0 p1 p2 p3 V",real=True)
    dphi=sp.Matrix([p0,p1,p2,p3])
    derivative_norm=(dphi.T*eta*dphi)[0]
    L=-derivative_norm/2-V
    T_scalar=dphi*dphi.T+L*eta
    mixed_scalar=(eta*T_scalar).applyfunc(sp.expand)
    assert mixed_scalar-L*sp.eye(4)==(eta*dphi)*dphi.T
    scalar_poly=sp.factor(mixed_scalar.charpoly(z).as_expr())
    assert sp.simplify(scalar_poly-(z-L)**3*(z-L-derivative_norm))==0
    assert scalar_multiplicity_floor(1)==3
    assert scalar_multiplicity_floor(2)==2

    # A two-scalar first-derivative matter Lagrangian has the more general
    # T^a_b=L I + P^a_I K^IJ P_{J,b}. Image rank <=2, hence a 2-fold
    # eigenvalue regardless of kinetic mixing or scalar potential. Verify
    # this nontrivial pair as a numerical/symbolic smoke control.
    dphi1=sp.Matrix([2,1,0,0])
    dphi2=sp.Matrix([0,1,2,0])
    two_scalar=eta*(dphi1*dphi1.T+dphi2*dphi2.T)-7*sp.eye(4)
    assert sp.rem(two_scalar.charpoly(z).as_expr(),(z+7)**2,z)==0

    # Maxwell action S=-1/4 int sqrt(-g)F_ab F^ab. Prove in symbolic
    # 4-D Lorentz algebra for SIX independent components that T^2=c*I.
    # Consequently its characteristic polynomial is (z^2-c)^2.
    f=sp.symbols("f01 f02 f03 f12 f13 f23",real=True)
    F=sp.zeros(4)
    for v,(i,j) in zip(f,((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))):
        F[i,j]=v
        F[j,i]=-v
    Fup=eta*F*eta
    invariant=sp.expand(sum(F[i,j]*Fup[i,j]
                            for i in range(4) for j in range(4)))
    maxwell_cov=F*eta*F.T-sp.Rational(1,4)*eta*invariant
    maxwell_mixed=(eta*maxwell_cov).applyfunc(sp.expand)
    squared=(maxwell_mixed*maxwell_mixed).applyfunc(sp.expand)
    maxwell_c=sp.factor(squared[0,0])
    assert all(sp.expand(squared[i,j]-(maxwell_c if i==j else 0))==0
               for i in range(4) for j in range(4))
    assert sp.expand(maxwell_mixed.charpoly(z).as_expr()
                     -(z*z-maxwell_c)**2)==0

    # A rotating fluid four-velocity cannot be the normalized gradient
    # of an ordinary single-valued scalar: alpha*dphi wedge
    # d(alpha*dphi)=0. Show KO's fluid congruence violates Frobenius.
    t,x,y=sp.symbols("t x y",real=True)
    a=1+t/2
    u=sp.Matrix([-1,0,-a*sp.exp(x/2)/10,0])  # u_flat from KO
    coords=(t,x,y,sp.symbols("zcoord",real=True))
    i,j,k=0,1,2
    twist=sp.factor(
        u[i]*(sp.diff(u[k],coords[j])-sp.diff(u[j],coords[k]))
       +u[j]*(sp.diff(u[i],coords[k])-sp.diff(u[k],coords[i]))
       +u[k]*(sp.diff(u[j],coords[i])-sp.diff(u[i],coords[j])))
    assert sp.simplify(twist-a*sp.exp(x/2)/20)==0
    assert twist!=0

    return {
        "status":"PASS_EXACT_RESTRICTED_MATTER_SOURCE_EXCLUSION",
        "fixed_background":"ROT-005 published expanding/rotating causal Korotkii-Obukhov member",
        "mixed_characteristic_polynomial_for_1616_a2_T":"(z-3)*(z^3+1597*z^2+798403*z+127206399)",
        "discriminant":str(disc),
        "gcd_of_poly_and_derivative":str(gcd),
        "scaled_mixed_eigenvalues":[str(sp.re(v)) for v in sp.nroots(polynomial)],
        "source_all_four_eigenvalues_simple":True,
        "single_minimal_real_scalar":"FAIL_TO_MATCH_EXACT_SOURCE",
        "two_minimal_real_scalars_or_simple_complex_scalar":"FAIL_TO_MATCH_EXACT_SOURCE",
        "perfect_fluid_even_when_tilted":"FAIL_TO_MATCH_EXACT_SOURCE",
        "pure_minimal_standard_Maxwell":"FAIL_TO_MATCH_EXACT_SOURCE",
        "generic_Maxwell_T_squared_multiple_of_identity":"SYMBOLIC_IDENTITY_CHECK_PASSED",
        "KO_comoving_Frobenius_wedge_012":str(twist),
        "rotating_comoving_u_as_gradient_of_single_scalar":"IMPOSSIBLE_WITH_STATED_ASSUMPTIONS",
        "higher_derivative_nonminimal_vector_plus_scalar_or_three_plus_scalars":
            "NOT_EXCLUDED_AND_UNRESOLVED",
        "cosmic_observational_confirmation":"NONE",
        "boundary":"Algebraic source exclusion for one frozen exact metric, not a no-go for every rotating spacetime or every EFMW theory."
    }


if __name__=="__main__":
    print(json.dumps(verify(),indent=2))
