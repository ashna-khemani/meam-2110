import numpy as np
import sympy as sym

from meam2110 import *

sym.init_printing(use_unicode=False)

'''
Let's create a dummy system to test your code
'''
system = RigidBodySystem(visualize=False)
N = system.InertialFrameN()


# We'll use what's called a "Furuta pendulum" https://en.wikipedia.org/wiki/Furuta_pendulum
# to test simple rotations

# Add 2 bodies/frames, A, B
A = Body('A')
B = Body('B')

'''
N -> A -> B are rotations about the z and x axes respectively
The A -> B joint is offset 10 cm in the a_x direction
'''
r_Ao_Bo = np.array([.1, 0, 0])
JNA = system.AddJoint(N, A, JointType.rotation, UnitVector.z)
JAB = system.AddJoint(A, B, JointType.rotation, UnitVector.x, r_Po_Jo=r_Ao_Bo)

'''
Now, let's evaluate the code on some symbolic variables

First, we'll test joint kinematics
'''

# Joint position, velocity, and acceleration variables
q_A = sym.symbols('q_A')
q_A_dot = sym.symbols('q_A_dot')
q_A_ddot = sym.symbols('q_A_ddot')

q_B = sym.symbols('q_B')
q_B_dot = sym.symbols('q_B_dot')
q_B_ddot = sym.symbols('q_B_ddot')

q = np.array([q_A, q_B])
q_dot = np.array([q_A_dot, q_B_dot])
q_ddot = np.array([q_A_ddot, q_B_ddot])

print('-------------------------- Testing joint velocity -------------------------- ')
print('N -> A, rotation about n_z = a_z:\n')
v_Po_Co, w_P_C = JointChildVelocity(system, JNA, q_dot)
print('Linear velocity: ')
SimplifyAndPrint(v_Po_Co)
print('Angular velocity: ')
SimplifyAndPrint(w_P_C)

print('A -> B, rotation about n_x = a_x:\n')
v_Po_Co, w_P_C = JointChildVelocity(system, JAB, q_dot)
print('Linear velocity: ')
SimplifyAndPrint(v_Po_Co)
print('Angular velocity: ')
SimplifyAndPrint(w_P_C)

print('-------------------------- Testing joint acceleration -------------------------- ')
print('N -> A, rotation about n_z = a_z:\n')
a_Po_Co, alpha_P_C = JointChildAcceleration(system, JNA, q_ddot)
print('Linear acceleration: ')
SimplifyAndPrint(a_Po_Co)
print('Angular acceleration: ')
SimplifyAndPrint(alpha_P_C)

print('A -> B, rotation about n_x = a_x:\n')
a_Po_Co, alpha_P_C = JointChildAcceleration(system, JAB, q_ddot)
print('Linear acceleration: ')
SimplifyAndPrint(a_Po_Co)
print('Angular acceleration: ')
SimplifyAndPrint(alpha_P_C)

print('-------------------------- Testing body velocity/acceleration -------------------------- ')
w_N_B, alpha_N_B = BodyAngVelAndAccel(system, q, q_dot, B, N, qddot=q_ddot)
print('Angular velocity of B in N, w_N_B, expressed in N coordinates')
SimplifyAndPrint(w_N_B)
print('Angular acceleration of B in N, w_N_B, expressed in N coordinates')
SimplifyAndPrint(alpha_N_B)

'''
Add your own tests here. What other cases might be considered? Feel free to change the system definition
# as you like.
'''