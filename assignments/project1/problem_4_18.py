import numpy as np
import sympy as sym
from meam2110 import *

# Create a new, and currently empty system
# We won't be visualizing anything here, so we can set that flag to False
system = RigidBodySystem(visualize=False)

# The problem has three bodies of interest: N, A, B, C
# N is special, as our system always has an inertial frame
N = system.InertialFrameN()
A = Body('A')
B = Body('B')
C = Body('C')

# N to A is a translation in the n_x direction
system.AddJoint(N, A, JointType.translation, UnitVector.x)

# A to B is a rotation about a_z = b_z
system.AddJoint(A, B, JointType.rotation, UnitVector.z)

# N to C is a rotation about #a_z = c_z
system.AddJoint(N, C, JointType.rotation, UnitVector.z)


# Declare symbolic variables for the positions, x, theta_b, and theta_C
# arrange them into a single vector, q, with the same ordering as the joint declarations above
x = sym.symbols('x')
theta_B = sym.symbols('theta_B')
theta_C = sym.symbols('theta_C')
q = np.array([x, theta_B, theta_C])

from sympy import sin, cos

# Use the methods from this weak to calculate all of the rotation matrices that the problem asks for
# you can skip the part of the textbook problem that asks for angular velocities
print('\n  R_B_N:')
R_B_N = np.array([
    [cos(theta_B), sin(theta_B), 0],
    [-sin(theta_B), cos(theta_B), 0],
    [0, 0, 1]
])
SimplifyAndPrint(R_B_N)

print('\n  R_N_B:')
R_N_B = R_B_N.T     # inverse is transpose for rotation matrix
SimplifyAndPrint(R_N_B)

print('\n  R_C_N:')
R_C_N = np.array([
    [cos(theta_C), sin(theta_C), 0],
    [-sin(theta_C), cos(theta_C), 0],
    [0, 0, 1]
])
SimplifyAndPrint(R_C_N)

print('\n  R_B_C:')
R_B_C = (R_C_N @ R_N_B).T
SimplifyAndPrint(R_B_C)
