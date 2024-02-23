import numpy as np
import sympy as sym
from meam2110 import *
sym.init_printing(use_unicode=False)
system = RigidBodySystem(visualize=False)

N = system.InertialFrameN()
A = Body('A')
B = Body('B')
C = Body('C')

# YOUR CODE HERE
#
#  Use system.addJoint() to add three joints connecting N, B, C
JNA = system.AddJoint(N, A, JointType.rotation, UnitVector.z)
JAB = system.AddJoint(A, B, JointType.rotation, UnitVector.x)
JBC = system.AddJoint(B, C, JointType.rotation, UnitVector.z)

# Joint position, velocity, and acceleration variables
theta = sym.symbols('theta')
theta_dot = sym.symbols('theta_dot')
theta_ddot = sym.symbols('theta_ddot')

phi = sym.symbols('phi')
phi_dot = sym.symbols('phi_dot')
phi_ddot = sym.symbols('phi_ddot')

q_C = sym.symbols('q_C)')
omega_C = sym.symbols('omega_C')
omega_C_dot = sym.symbols('omega_C_dot')

# 
#
# YOUR CODE BELOW
#   Assemble into q, q_dot, q_ddot vectors
#   Be sure to pay attention to the sign of the angles in the problem! Your code
#   generates rotations in the positive direction, but theta and phi represent
#   angles in the negative direction
#
# The result of your code should be w_N_B_B, w_N_C_B, and alpha_N_B_B
#  w_N_B_B: the angular velocity of B in N, expressed in B's coordinates
#  w_N_C_B: the angular velocity of C in N, expressed in B's coordinates
#  alpha_N_B_B: the angular acceleration of B in N, expressed in B's coordinates
q = np.array([-theta, -phi, q_C])
q_dot = np.array([-theta_dot, -phi_dot, omega_C])
q_ddot = np.array([-theta_ddot, -phi_ddot, omega_C_dot])


# Print results in the proper coordinates
print('\n w_N_B in B\'s coordinates: \n')
w_N_B_B = ChangeCoordinates(system, q, BodyAngVelAndAccel(system, q, q_dot, B, N, q_ddot)[0], N, B)
SimplifyAndPrint(w_N_B_B)

print('\n w_N_C in B\'s coordinates: \n')
w_N_C_B = ChangeCoordinates(system, q, BodyAngVelAndAccel(system, q, q_dot, C, N, q_ddot)[0], N, B)
SimplifyAndPrint(w_N_C_B)

print('\n alpha_N_B in B\'s coordinates: \n')
alpha_N_B_B = ChangeCoordinates(system, q, BodyAngVelAndAccel(system, q, q_dot, B, N, q_ddot)[1], N, B)
SimplifyAndPrint(alpha_N_B_B)
