"""Source-level mathematical checks; NOT astrophysical data validation."""
import math
import unittest

from rotation import lab


class TestRotationToyMath(unittest.TestCase):
    def test_curl_twice_angular_speed(self):
        for w in (-4.0, -1.0, 0.0, 0.5, 13.0):
            self.assertEqual(lab.rigid_curl(w), (0.0, 0.0, 2*w))
            self.assertEqual(lab.rigid_divergence(w), 0.0)

    def test_rigid_velocity(self):
        self.assertEqual(lab.rigid_velocity(2.0, 3.0, 4.0), (-12.0, 8.0, 0.0))

    def test_stokes_circulation_and_flux(self):
        for omega in (-3.0, 0.0, 2.0):
            for radius in (0.1, 1.0, 3.5):
                self.assertAlmostEqual(lab.rigid_circulation(omega, radius),
                                       lab.rigid_vorticity_flux(omega, radius), places=12)

    def test_circulation_requires_positive_radius(self):
        with self.assertRaises(ValueError):
            lab.rigid_circulation(1.0, 0.0)

    def test_so3_axis_rotation_preserves_norm(self):
        v = (1.2, -2.4, 9.0)
        for theta in (0.0, 1.3, math.pi/2, 2*math.pi):
            rv = lab.rotate_about_z(v, theta)
            self.assertAlmostEqual(lab.squared_norm(v), lab.squared_norm(rv), places=11)
            self.assertAlmostEqual(rv[2], v[2])

    def test_so3_inverse(self):
        v = (-1.1, 2.4, 6.0)
        rv = lab.rotate_about_z(lab.rotate_about_z(v, 2.4), -2.4)
        for a,b in zip(v,rv):
            self.assertAlmostEqual(a,b, places=12)

    def test_spinor_half_angle(self):
        zero=lab.spinor_rotor_components(0.0)
        two=lab.spinor_rotor_components(math.tau)
        four=lab.spinor_rotor_components(2*math.tau)
        for x,y in zip(zero,two):
            self.assertAlmostEqual(x,-y, places=12)
        for x,y in zip(zero,four):
            self.assertAlmostEqual(x,y, places=12)

    def test_phase_winding_positive_negative_zero(self):
        for n in range(-4,5):
            self.assertEqual(lab.phase_winding(n, 512), n)

    def test_phase_winding_rejects_alias(self):
        with self.assertRaises(ValueError):
            lab.phase_winding(8, 16)
        with self.assertRaises(ValueError):
            lab.phase_winding(1, 4)

    def test_real_scalar_no_vorticity(self):
        self.assertEqual(lab.real_scalar_quadratic_gradient(2,3,4), (4,6,8))
        self.assertEqual(lab.real_scalar_quadratic_curl_of_gradient(), (0.0,0.0,0.0))

    def test_gauge_invariant_combination(self):
        theta=(4.0,7.0)
        A=(1.0,-2.0)
        q=2.0
        shift=(0.5,-1.3)
        old=lab.gauge_covariant_phase_gradient(theta,A,q)
        new=lab.gauge_covariant_phase_gradient(
            [v+q*s for v,s in zip(theta,shift)],
            [v+s for v,s in zip(A,shift)],q)
        self.assertEqual(old,new)

    def test_gauge_vector_length_guard(self):
        with self.assertRaises(ValueError):
            lab.gauge_covariant_phase_gradient([1.0], [0.0,1.0], 1.0)

    def test_cosmology_sign_degeneracy(self):
        for w in (-4.0,-0.1,0.0,2.0):
            a=lab.expansion_rate_squared(1.3,0.2,3.0,w)
            b=lab.expansion_rate_squared(1.3,0.2,3.0,-w)
            self.assertEqual(a,b)

    def test_curvature_rotation_degeneracy(self):
        self.assertTrue(lab.scalar_curvature_degeneracy()["equal"])
        self.assertEqual(lab.expansion_rate_squared(1.0,0.0,2.0,0.0),
                         lab.expansion_rate_squared(1.0,1.0,2.0,1.0))

    def test_cosmology_nonpositive_scale(self):
        for a in (0.0,-1.0):
            with self.assertRaises(ValueError):
                lab.expansion_rate_squared(1.0,1.0,a,1.0)

    def test_report_explicit_toy_label(self):
        r=lab.report()
        self.assertEqual(r["classification"],"ANALYTIC_TOY_NOT_EMPIRICAL_COSMIC_EVIDENCE")
        self.assertEqual(r["status"],"PASS_TOY_IDENTITIES_ONLY")


if __name__ == "__main__":
    unittest.main()
