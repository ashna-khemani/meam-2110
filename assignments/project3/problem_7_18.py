import numpy as np
import sympy as sym
from meam2110 import *

# The problem has three bodies of interest: N, A, B, C
# N is special, as our system always has an inertial frame
system = RigidBodySystem(visualize=False)

N = system.InertialFrameN()
A = Body('A')
B = Body('B')
C = Body('C')

# Lengths
L_A = sym.symbols('L_A')
L_B = sym.symbols('L_B')
L_C = sym.symbols('L_C')

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

# q_B is in the -a_y direction
q = np.array([q_A, -q_B, q_C])
qdot = np.array([q_A_dot, -q_B_dot, q_C_dot])
qddot = np.array([q_A_ddot, -q_B_ddot, q_C_ddot])

# Define all the fixed position vectors 
# YOUR CODE BELOW
r_No_Ao_N = np.zeros(3) # FIX ME!
r_Ao_Bo_A = np.zeros(3) # FIX ME!
r_Bo_Co_B = np.zeros(3) # FIX ME!
r_Co_Q_C = np.zeros(3) # FIX ME!

# Add three joints connecting N, A, B, C. How are q_A_, q_B, q_C defined in the problem?
# Be sure to add them in the same order: q_A, q_B, q_C.
# For this problem, r_Po_Jo (the location of the joint on the parent) is needed!
# THE DEFINITIONS BELOW ARE WRONG!

# system.AddJoint(N, A, JointType.rotation, UnitVector.?, r_Po_Jo=np.zeros(3))
# system.AddJoint(A, B, JointType.rotation, UnitVector.?, r_Po_Jo=np.zeros(3))
# system.AddJoint(B, C, JointType.rotation, UnitVector.?, r_Po_Jo=np.zeros(3))

# Use your code to calculate the velocity and acceleration of Q in A, expressed in C:
#     v_A_Q_C and a_A_Q_C
# You'll need to use PointKinematics from this week, and change the coordinates

print('\n*** v_A_Q expressed in C coordinates ***')
v_A_Q_C = np.zeros(3) # FIX ME!
SimplifyAndPrint(v_A_Q_C)

print('\n*** a_A_Q expressed in C coordinates ***')
a_A_Q_C = np.zeros(3) # FIX ME!
SimplifyAndPrint(a_A_Q_C)
