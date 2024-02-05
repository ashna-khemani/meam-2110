import numpy as np
import sympy as sym
from meam2110 import *

'''
Let's create a dummy system to test your code
'''
system = RigidBodySystem(visualize=False)
N = system.InertialFrameN()

# Add 4 bodies/frames, A, B, C, D
A = Body('A')
B = Body('B')
C = Body('C')
D = Body('D')

'''
N -> A -> B -> C are rotations about the x, y, z axes respectively,
with no offsets (the joint origin is located at the parent origin)
'''
JNA = system.AddJoint(N, A, JointType.rotation, UnitVector.x)
JAB = system.AddJoint(A, B, JointType.rotation, UnitVector.y)
JBC = system.AddJoint(B, C, JointType.rotation, UnitVector.z)

'''
N -> D is a rotation about x with non-zero joint offsets

The joint origin is rotated with respect to the parent origin
N->D: offset in position
D->E: offset in rotation
'''
# Rotation from N to JND (the joint from N to D
# This rotation matrix corresponds to a rotation about z by 90 degrees
# This means that the rotation, about the joint-x axis, is equivalently a rotation
# about n_y
R_N_JND = np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]])
JND = system.AddJoint(N, D, JointType.rotation, UnitVector.x, R_P_J=R_N_JND)


'''
Now, let's evaluate the code on some symbolic variables

First, we'll test joint kinematics
'''

# Angle variables for each joint
q_A = sym.symbols('q_A')
q_B = sym.symbols('q_B')
q_C = sym.symbols('q_C')
q_D = sym.symbols('q_D')
q = np.array([q_A, q_B, q_C, q_D])

print('-------------------------- Testing joint kinematics -------------------------- ')
print('N -> A, rotation about n_x = a_x:\n')
_, R_N_A = JointTransformation(system, JNA, q)
SimplifyAndPrint(R_N_A)

print('\n\nA -> B, rotation about a_y = b_y:\n')
_, R_A_B = JointTransformation(system, JAB, q)
SimplifyAndPrint(R_A_B)

print('\n\nB -> C, rotation about b_z = c_z:\n')
_, R_B_C = JointTransformation(system, JBC, q)
SimplifyAndPrint(R_B_C)

print('\n\nN -> D, rotation about joint x, with rotation from N to joint (n_y = d_x):\n')
_, R_N_D = JointTransformation(system, JND, q)
SimplifyAndPrint(R_N_D)

print('-------------------------- Testing relative rotation matrix  -------------------------- ')
print('R_N_A (should match N -> A above):\n')
R_N_A = RelativeRotationMatrix(system, q, A, N)
SimplifyAndPrint(R_N_A)

print('\n\nR_A_N (should be transpose of R_N_A):\n')
R_A_N = RelativeRotationMatrix(system, q, N, A)
SimplifyAndPrint(R_A_N)

print('\n\nR_N_B (should be R_N_A * R_A_B):\n')
R_N_B = RelativeRotationMatrix(system, q, B, N)
SimplifyAndPrint(R_N_B)

'''
Add your own tests here. What about longer paths? R_N_C?
Or paths that must go 'forward' and 'backward' on the tree, like R_D_C?

What about testing ChangeCoordinates?
'''