"""ROT-004: algebraic bridge between ME-056 and the 1+3 GR scalar constraint.

Standard-library arithmetic only. The GR 1+3 scalar constraint is an
ASSUMED literature identity here, not a freshly derived Einstein equation.
The independent exact-metric check lives in research/rot004_godel_sympy.py.

Signature (-+++), c=1; kappa_rho = 8*pi*G*rho;
sigma_sq = 1/2 sigma_ab sigma^ab; omega_sq=1/2 omega_ab omega^ab;
R_rest denotes the scalar of the *projected spatial connection*,
NOT necessarily a scalar curvature of an actual 3-D hypersurface.
For nonzero vorticity the orthogonal rest spaces are not integrable.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
import json
from typing import TypeAlias

Number: TypeAlias = int | float | F


@dataclass(frozen=True)
class GRKinematics:
    kappa_rho: Number
    lam: Number
    shear_sq: Number
    vorticity_sq: Number
    projected_rest_curvature: Number

    def h_squared(self) -> Number:
        """3H^2 = kappa*rho + Lambda + sigma^2 - omega^2 - R_rest/2."""
        if self.shear_sq < 0 or self.vorticity_sq < 0:
            raise ValueError("Squared shear and vorticity cannot be negative")
        return F(1, 3) * (self.kappa_rho + self.lam + self.shear_sq
                          - self.vorticity_sq - F(1, 2) * self.projected_rest_curvature)


@dataclass(frozen=True)
class ME056:
    kappa_rho: Number
    lam: Number
    curvature_k: Number
    a: Number
    omega_scalar: Number

    def h_squared(self) -> Number:
        """Stipulated ME-056, requiring positive a and an externally defined omega."""
        if self.a <= 0:
            raise ValueError("Scale factor must be positive")
        return (F(1, 3) * (self.kappa_rho + self.lam)
                + F(1) * (self.omega_scalar**2 - self.curvature_k) / (self.a**2))


def bridge_residual(gr: GRKinematics, me: ME056) -> Number:
    """3(H_ME056^2 - H_GR^2), not a dynamical field equation.

    Zero is NECESSARY for the two scalar relations to agree at a point
    when their rho, Lambda and expansion observables are identified.
    It does not ensure the existence of a metric satisfying Einstein's
    equations or the associated differential constraints.
    """
    if gr.kappa_rho != me.kappa_rho or gr.lam != me.lam:
        raise ValueError("The matter density and Lambda must be compared on the same footing")
    a2 = me.a**2
    if a2 <= 0:
        raise ValueError("Scale factor must be positive")
    return (3 * me.omega_scalar**2 / a2
            - (gr.shear_sq - gr.vorticity_sq
               - (gr.projected_rest_curvature - 6*me.curvature_k/a2)/2))


def shear_needed_for_match(
    *, omega_scalar: Number, a: Number,
    physical_vorticity_sq: Number,
    rest_curvature: Number, curvature_k: Number
) -> Number:
    """Required sigma^2 if both scalar equations agree; not a proof it is realized."""
    if a <= 0 or physical_vorticity_sq < 0:
        raise ValueError("Invalid a or physical vorticity squared")
    return (3*omega_scalar**2/a**2 + physical_vorticity_sq
            + (rest_curvature - 6*curvature_k/a**2)/2)


def raychaudhuri_theta_dot(
    *, theta: Number, shear_sq: Number, vorticity_sq: Number,
    kappa_rho: Number, kappa_p: Number, lam: Number,
    acceleration_divergence_4d: Number = 0
) -> Number:
    """Raychaudhuri for timelike u, input acceleration divergence = nabla_a A^a.

    theta_dot = -theta^2/3 - 2 sigma^2 + 2 omega^2
                - (kappa*rho+3*kappa*p)/2 + Lambda + nabla_a A^a
    This is a separate propagation equation; it is not ME-056.
    """
    if shear_sq < 0 or vorticity_sq < 0:
        raise ValueError("Squared kinematic magnitudes must be nonnegative")
    return (-theta**2/3 - 2*shear_sq + 2*vorticity_sq
            - (kappa_rho + 3*kappa_p)/2 + lam
            + acceleration_divergence_4d)


def godel_kinematic_control(m_sq: Number = F(2)) -> dict[str, object]:
    """Exact GR Gödel dust constants, with theta=0, sigma^2=0.

    This comparison is CONDITIONAL: ME-056 has no specified mapping of its
    global (a,k,Omega_U) onto Gödel's *nonintegrable* local rest spaces.
    Choosing a=1, k=0 from projected curvature R_rest=0, and setting
    Omega_scalar^2 = physical vorticity^2 exposes why the naive
    universal positive-additive interpretation cannot simply be asserted.
    """
    if m_sq <= 0:
        raise ValueError("Gödel m^2 must be positive")
    omega_sq = m_sq/2
    gr = GRKinematics(kappa_rho=m_sq, lam=-m_sq/2, shear_sq=0,
                      vorticity_sq=omega_sq, projected_rest_curvature=0)
    # omega_scalar is sqrt(m_sq/2). Select m_sq=2 for exact rational toy.
    me_h2 = (m_sq - m_sq/2)/3 + omega_sq
    return {
        "theta": 0, "shear_sq": 0, "physical_vorticity_sq": str(omega_sq),
        "Lambda": str(-m_sq/2), "kappa_rho": str(m_sq),
        "projected_rest_curvature": "0",
        "GR_H2": str(gr.h_squared()),
        "ME056_H2_under_conditional_ad_hoc_mapping": str(me_h2),
        "GR_equation_satisfied": gr.h_squared() == 0,
        "Raychaudhuri_equation_satisfied": raychaudhuri_theta_dot(
            theta=0, shear_sq=0, vorticity_sq=omega_sq,
            kappa_rho=m_sq, kappa_p=0, lam=-m_sq/2) == 0,
        "interpretation": "Gödel proves rotation need not imply expansion; "
        "the a,k,Omega mapping is not a general identification."
    }


def report() -> dict[str, object]:
    a = F(2)
    k = F(3, 2)
    R = 6*k/a**2
    gr_flrw = GRKinematics(F(3), F(1, 2), 0, 0, R)
    me_flrw = ME056(F(3), F(1, 2), k, a, 0)
    # Algebraic equality fixture: NOT asserted to be an Einstein spacetime.
    gr_algebraic = GRKinematics(F(3), 0, F(4), F(1), 0)
    me_algebraic = ME056(F(3), 0, 0, 1, 1)
    return {
        "status": "PASS_SCOPED_ALGEBRA_ONLY",
        "FLRW_zero_rotation_limit": {
            "GR_H2": str(gr_flrw.h_squared()),
            "ME056_H2": str(me_flrw.h_squared()),
            "bridge_residual": str(bridge_residual(gr_flrw, me_flrw))
        },
        "possible_scalar_equality_not_spacetime": {
            "GR_H2": str(gr_algebraic.h_squared()),
            "ME056_H2": str(me_algebraic.h_squared()),
            "bridge_residual": str(bridge_residual(gr_algebraic, me_algebraic))
        },
        "Godel_exact_GR_control_constants": godel_kinematic_control(),
        "warning": "A new rotating cosmological metric or physical ME-056 derivation is not proven."
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2))
