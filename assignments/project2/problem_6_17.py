import numpy as np
import sympy as sym
from meam2110 import *
sym.init_printing(use_unicode=False)

system = RigidBodySystem(visualize=False)

N = system.InertialFrameN()
A = Body('A')
B = Body('B')
C = Body('C')

#
# YOUR CODE HERE
#
#  Use system.addJoint() to add three joints connecting N, B, C

JNA = system.AddJoint(N, A, JointType.rotation, UnitVector.z)
JAB = system.AddJoint(A, B, JointType.rotation, UnitVector.y)
JBC = system.AddJoint(B, C, JointType.rotation, UnitVector.y)




# Joint position, velocity, and acceleration variables
q_A = sym.symbols('q_A')
q_A_dot = sym.symbols('q_A_dot')
q_A_ddot = sym.symbols('q_A_ddot')

q_B = sym.symbols('q_B')
q_B_dot = sym.symbols('q_B_dot')
q_B_ddot = sym.symbols('q_B_ddot')

q_C = sym.symbols('q_C')
q_C_dot = sym.symbols('q_C_dot')
q_C_ddot = sym.symbols('q_C_ddot')

q = np.array([q_A, -q_B, q_C])
q_dot = np.array([q_A_dot, -q_B_dot, q_C_dot])
q_ddot = np.array([q_A_ddot, -q_B_ddot, q_C_ddot])


#
# YOUR CODE BELOW
#
# Use your code from this week to calculate the angular velocity and acceleration of C in N
# 
# What coordinates are the vectors expressed in? Keep this in mind!
#
# The result of your code should be w_N_C_A and alpha_N_C_A, which should be read as:
#  w_N_C_A: the angular velocity of C in N, expressed in A's coordinates
#  alpha_N_C_A: the angular acceleration of C in N, expressed in A's coordinates

print('\n w_N_C in A\'s coordinates: \n')
w_N_C_A = ChangeCoordinates(system, q, BodyAngVelAndAccel(system, q, q_dot, C, N, q_ddot)[0], N, A)
SimplifyAndPrint(w_N_C_A)

print('\n alpha_N_C in A\'s coordinates: \n')
alpha_N_C_A = ChangeCoordinates(system, q, BodyAngVelAndAccel(system, q, q_dot, C, N, q_ddot)[1], N, A)
SimplifyAndPrint(alpha_N_C_A)
