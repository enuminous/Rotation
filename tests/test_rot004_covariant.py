"""ROT-004 tests: algebraic criteria, not full Einstein-equation certification."""
import unittest
from fractions import Fraction as F
from rotation.rot004_covariant import (
    GRKinematics, ME056, bridge_residual, shear_needed_for_match,
    raychaudhuri_theta_dot, godel_kinematic_control, report
)


class TestCovariantBridge(unittest.TestCase):
    def test_flrw_zero_rotation_zero_shear(self):
        for a in [F(1, 2), F(1), F(3, 2), F(4)]:
            for k in [F(-1), F(0), F(1)]:
                mu, lam = F(3), F(1, 3)
                gr = GRKinematics(mu, lam, 0, 0, 6*k/a**2)
                me = ME056(mu, lam, k, a, 0)
                self.assertEqual(gr.h_squared(), me.h_squared())
                self.assertEqual(bridge_residual(gr, me), 0)

    def test_required_correction_includes_shear_curvature(self):
        gr = GRKinematics(F(3), F(0), F(4), F(1), F(0))
        me = ME056(F(3), F(0), F(0), F(1), F(1))
        self.assertEqual(bridge_residual(gr, me), 0)
        self.assertEqual(gr.h_squared(), me.h_squared())
        self.assertEqual(shear_needed_for_match(
            omega_scalar=1, a=1, physical_vorticity_sq=1,
            rest_curvature=0, curvature_k=0), 4)

    def test_zero_shear_same_curvature_positive_vorticity_cannot_match_positive_scalar_square(self):
        gr = GRKinematics(F(3), F(1), 0, F(1), 0)
        me = ME056(F(3), F(1), 0, F(1), F(1))
        self.assertGreater(bridge_residual(gr, me), 0)
        self.assertNotEqual(gr.h_squared(), me.h_squared())

    def test_h2_difference_is_residual_over_three(self):
        for shear in [F(0), F(1, 7), F(2)]:
            gr = GRKinematics(F(9), F(1), shear, F(3, 4), F(2, 3))
            me = ME056(F(9), F(1), F(2), F(3, 2), F(1, 2))
            self.assertEqual(
                3*(me.h_squared()-gr.h_squared()), bridge_residual(gr, me))

    def test_matter_must_be_same(self):
        with self.assertRaises(ValueError):
            bridge_residual(GRKinematics(1,0,0,0,0), ME056(2,0,0,1,0))

    def test_nonpositive_a_denied(self):
        with self.assertRaises(ValueError):
            ME056(1,0,0,0,0).h_squared()
        with self.assertRaises(ValueError):
            shear_needed_for_match(
                omega_scalar=1,a=-1,physical_vorticity_sq=0,
                rest_curvature=0,curvature_k=0)

    def test_squared_kinematics_nonnegative(self):
        with self.assertRaises(ValueError):
            GRKinematics(0,0,-1,0,0).h_squared()
        with self.assertRaises(ValueError):
            raychaudhuri_theta_dot(theta=0,shear_sq=0,vorticity_sq=-1,
                                   kappa_rho=0,kappa_p=0,lam=0)

    def test_godel_exact_kinematic_control(self):
        for m2 in [F(1),F(2),F(3,2),F(9)]:
            x=godel_kinematic_control(m2)
            self.assertTrue(x["GR_equation_satisfied"])
            self.assertTrue(x["Raychaudhuri_equation_satisfied"])
            self.assertEqual(x["GR_H2"],"0")
            self.assertNotEqual(x["GR_H2"],
                                x["ME056_H2_under_conditional_ad_hoc_mapping"])

    def test_report_scoped(self):
        r=report()
        self.assertEqual(r["status"],"PASS_SCOPED_ALGEBRA_ONLY")
        self.assertIn("not",r["warning"].lower())


if __name__ == "__main__":
    unittest.main()
