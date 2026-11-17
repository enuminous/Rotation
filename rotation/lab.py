"""Small standard-library mathematics laboratory for cross-field rotation.

These operations implement elementary kinematics/phase topology only.
They DO NOT measure cosmic rotation, solve Navier-Stokes, or establish
a new EFMW dynamical law.
"""
from __future__ import annotations

import argparse
import cmath
import json
import math
from typing import Sequence


TAU = math.tau


def rigid_velocity(x: float, y: float, omega: float) -> tuple[float, float, float]:
    """Rigid rotation about +z, u=(-omega*y, omega*x, 0)."""
    return (-omega * y, omega * x, 0.0)


def rigid_curl(omega: float) -> tuple[float, float, float]:
    """Analytic curl of rigid_velocity (not a numerical PDE result)."""
    return (0.0, 0.0, 2.0 * omega)


def rigid_divergence(omega: float) -> float:
    """Analytic divergence of the rigid field."""
    return 0.0


def rigid_circulation(omega: float, radius: float) -> float:
    """Line integral on positively oriented x-y circle; requires radius>0."""
    if radius <= 0:
        raise ValueError("radius must be positive")
    return 2.0 * math.pi * omega * radius**2


def rigid_vorticity_flux(omega: float, radius: float) -> float:
    """Curl flux through the same disk; equals circulation by Stokes."""
    if radius <= 0:
        raise ValueError("radius must be positive")
    return rigid_curl(omega)[2] * math.pi * radius**2


def rotate_about_z(vector: Sequence[float], theta: float) -> tuple[float, float, float]:
    """A standard fixed-axis active SO(3) rotation."""
    if len(vector) != 3:
        raise ValueError("3 components required")
    x, y, z = vector
    c, s = math.cos(theta), math.sin(theta)
    return (c*x - s*y, s*x + c*y, z)


def squared_norm(vector: Sequence[float]) -> float:
    return sum(v*v for v in vector)


def spinor_rotor_components(theta: float) -> tuple[float, float]:
    """Coefficients of cos(theta/2)-B sin(theta/2), B^2=-1."""
    return (math.cos(theta/2.0), -math.sin(theta/2.0))


def phase_winding(winding: int, samples: int = 512) -> int:
    """Winding of the toy complex field exp(i*n*theta) on a nonzero loop.

    Adjacent phase increments must stay strictly below pi to avoid aliasing.
    A nonzero winding profile can be extended through the origin only by
    letting the amplitude vanish at the vortex core.
    """
    if not isinstance(winding, int):
        raise TypeError("winding must be an integer")
    if samples < 8 or samples <= 2 * abs(winding):
        raise ValueError("sampling insufficient for phase unwrapping")
    field = [cmath.exp(1j*TAU*winding*j/samples) for j in range(samples)]
    total = 0.0
    for j in range(samples):
        ratio = field[(j+1) % samples] / field[j]
        total += cmath.phase(ratio)
    estimate = total / TAU
    nearest = round(estimate)
    if abs(estimate - nearest) > 1e-7:
        raise ArithmeticError("phase winding not resolved at this precision")
    return nearest


def real_scalar_quadratic_gradient(x: float, y: float, z: float) -> tuple[float, float, float]:
    """Gradient of phi=x^2+y^2+z^2, a smooth single-valued real scalar."""
    return (2*x, 2*y, 2*z)


def real_scalar_quadratic_curl_of_gradient() -> tuple[float, float, float]:
    """Analytic curl of that gradient, identically zero."""
    return (0.0, 0.0, 0.0)


def gauge_covariant_phase_gradient(
    grad_theta: Sequence[float], potential: Sequence[float], charge: float
) -> tuple[float, ...]:
    """Conventional toy U(1) combination grad(theta)-q*A (one sign convention)."""
    if len(grad_theta) != len(potential):
        raise ValueError("mismatched vector dimensions")
    return tuple(g-charge*a for g,a in zip(grad_theta,potential))


def expansion_rate_squared(base: float, curvature: float, scale: float, omega: float) -> float:
    """ME-056 stipulated scalar toy H^2 = base + (omega^2-k)/a^2.

    This is NOT a derivation of an Einstein spacetime or a fit to cosmology.
    """
    if scale <= 0:
        raise ValueError("the scale factor must be strictly positive")
    return base + (omega*omega-curvature)/(scale*scale)


def scalar_curvature_degeneracy(
    base: float = 1.3, scale: float = 2.0
) -> dict[str, object]:
    """Counterexample to unique omega inference from scalar H^2 alone."""
    first = expansion_rate_squared(base, 0.0, scale, 0.0)
    second = expansion_rate_squared(base, 1.0, scale, 1.0)
    return {"model_A": {"k": 0.0, "omega": 0.0, "H2": first},
            "model_B": {"k": 1.0, "omega": 1.0, "H2": second},
            "equal": math.isclose(first, second, abs_tol=1e-12)}


def report(omega: float = 0.7, winding: int = 2, theta: float = 1.1) -> dict:
    position = (1.5, -0.2, 3.0)
    turned = rotate_about_z(position, theta)
    return {
        "classification": "ANALYTIC_TOY_NOT_EMPIRICAL_COSMIC_EVIDENCE",
        "rigid_rotation": {
            "omega": omega,
            "velocity_at_1_2": rigid_velocity(1.0, 2.0, omega),
            "curl": rigid_curl(omega),
            "divergence": rigid_divergence(omega),
            "unit_disk_circulation": rigid_circulation(omega, 1.0),
            "unit_disk_curl_flux": rigid_vorticity_flux(omega, 1.0)
        },
        "spatial_rotation": {
            "angle_radians": theta,
            "input": position,
            "output": turned,
            "norm2_before": squared_norm(position),
            "norm2_after": squared_norm(turned)
        },
        "complex_scalar_phase": {"requested_winding": winding,
                                 "measured_toy_winding": phase_winding(winding)},
        "spinor_double_cover": {
            "rotor_0": spinor_rotor_components(0.0),
            "rotor_2pi": spinor_rotor_components(TAU),
            "rotor_4pi": spinor_rotor_components(2*TAU)
        },
        "scalar_cosmology_identifiability": scalar_curvature_degeneracy(),
        "status": "PASS_TOY_IDENTITIES_ONLY"
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--omega", type=float, default=0.7)
    parser.add_argument("--winding", type=int, default=2)
    parser.add_argument("--angle", type=float, default=1.1, help="radians")
    a = parser.parse_args()
    print(json.dumps(report(a.omega, a.winding, a.angle), indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
