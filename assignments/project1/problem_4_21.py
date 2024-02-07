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

# Position variables, arranged as a vector
q_A = sym.symbols('q_A')
q_B = sym.symbols('q_B')
q_C = sym.symbols('q_C')
q = np.array([q_A, q_B, q_C])

# Add three joints connecting N, A, B, C. How are q_A_, q_B, q_C defined in the problem?
# Be sure to add them in the same order: q_A, q_B, q_C.
# YOUR CODE GOES HERE
system.AddJoint(N, A, JointType.rotation, UnitVector.z)
system.AddJoint(A, B, JointType.rotation, UnitVector.z)
system.AddJoint(B, C, JointType.rotation, UnitVector.z)

L_A = 1
L_B = 2
L_C = 2
L_N = 1

from sympy import sin, cos

# In A coordinates, r_Ao_Bo is easy to define
r_Ao_Bo_A = np.array([L_A, 0, 0])
r_Ao_Bo_N = np.array([L_A*cos(q_A), L_A*sin(q_A), 0])

r_Bo_Bc_N = np.array([L_B*cos(q_B), L_B*sin(q_B), 0])

r_Bc_Co_N = np.array([-L_C*cos(q_C), -L_C*sin(q_C), 0])

r_Co_Ao_N = np.array([0, -L_N, 0])

# The loop, r_Ao_Ao_N (starting at A_o and returning back to the same point) can be calculated as below
# Your challenge will be to determine the four vectors below.
# Remember, the last "_N" at the end is to convert all four vectors into N coordinates!
loop = r_Ao_Bo_N + r_Bo_Bc_N + r_Bc_Co_N + r_Co_Ao_N

SimplifyAndPrint(loop)

# We'll substitute in q_A = pi/6 (30 degrees), and then solve for q_B and q_C
equations_to_solve = (loop[0].subs(q_A, np.pi/6), loop[1].subs(q_A, np.pi/6))
solutions = sym.solve(equations_to_solve, (q_B, q_C))

print('Solutions to (q_B, q_C) in degrees:')
for solution in solutions:
  print(np.array(solution) * 180 / np.pi)

