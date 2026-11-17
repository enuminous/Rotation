# The goddamn Cliffords: geometric algebra and rotation

This note separates a powerful **mathematical language** from an empirical claim that all physical fields share an observed global rotation.

## 1. Rotations through bivectors

In Euclidean geometric algebra Cl(3,0), an oriented unit bivector B spanning a rotation plane satisfies B²=-1. A rotor is

```text
R(θ) = exp(-B θ/2) = cos(θ/2) − B sin(θ/2)
v' = R v reverse(R)
```

The sign convention sets the rotation orientation. Reversing R corresponds to reversing orientation/angle conventions, not new physics.

The scalar angle θ is **not** itself the scalar field ME-016; it is a parameter of a group action. A rotor is a multivector, not an ordinary real scalar. Quaternion/Spin(3) descriptions and 3×3 matrices are alternative representations of the same standard spatial rotation.

## 2. The double cover

A 2π change of θ gives R(2π)=-R(0), while the induced vector transformation is unchanged because (-R)v reverse(-R)=Rv reverse(R). A 4π change returns the rotor itself. This is the mathematical SU(2)→SO(3) double cover, observed in spin-1/2 neutron interference [Rauch et al. 1975](https://doi.org/10.1016/0375-9601(75)90798-7).

## 3. Finite rotation and vorticity

For v=(-ωy,ωx,0), the curl is (0,0,2ω). The rotation in the transverse (x,y) plane is governed by the matrix generator J with J²=-I₂. On all of 3-space with a fixed z-axis, its square is **minus the perpendicular projection**, not -I₃. These facts have concrete theorem statements in:
- [RotationKinematics.lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/RotationKinematics.lean)
- [Vorticity.lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/main/analysis/Vorticity.lean)

## 4. Potential cross-sector program

A *nontrivial* cross-field proposal would have to specify how a rotor acts on:
- a real scalar (typically via transformed spacetime arguments; no intrinsic nontrivial SO(3) action),
- a complex scalar phase (internal U(1), generally not SO(3)),
- spinors (Spin(3)/Spin(1,3) representations),
- vector/gauge fields (base-space and internal representations),
- a gravitational metric (diffeomorphism/Lorentz and observer-congruence structure).

It must provide physically meaningful covariant couplings and at least one new prediction that does not disappear as a change of basis or gauge choice.

## 5. A hard negative control

Take a constant real scalar and a zero-velocity fluid on flat spacetime. The rotation **representation** still exists, but the physical state has no motion. Therefore the existence of Clifford rotors everywhere in mathematical descriptions does not imply measured nonzero rotation everywhere.

## 6. What the toy code checks

`python -m rotation.lab` and `python -m unittest discover -s tests -v` check:
- 2-D rotor/matrix norm and inverse,
- half-angle rotor sign after 2π and return after 4π,
- rigid vorticity at prescribed angular speed.

These are standard analytic/finite-sample demonstrations, not a Lean proof of cosmic rotation.
