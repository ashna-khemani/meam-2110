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
system.AddJoint(N, A, JointType.rotation, UnitVector.z)
system.AddJoint(A, B, JointType.rotation, UnitVector.x, r_Po_Jo=r_Ao_Bo)

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

# Define a point at the end of the pendulum
r_Bo_P = np.array([0, 0, .1])

r_No_P, v_N_P, a_N_P = PointKinematics(system, q, B, N, qdot=q_dot, qddot=q_ddot, r_Ao_P=r_Bo_P)

print('\n-------------------------- Testing position: r_No_P -------------------------- ')
# The correct answer is:
#
# [0.1*sin(q_A)*sin(q_B) + 0.1*cos(q_A)]
# [                                    ]
# [0.1*sin(q_A) - 0.1*sin(q_B)*cos(q_A)]
# [                                    ]
# [            0.1*cos(q_B)            ]
SimplifyAndPrint(r_No_P)

print('\n-------------------------- Testing velocity: v_N_P -------------------------- ')
# The correct answer is:
#
# [-0.1*q_A_dot*sin(q_A) + 0.1*q_A_dot*sin(q_B)*cos(q_A) + 0.1*q_B_dot*sin(q_A)*cos(q_B)]
# [                                                                                     ]
# [0.1*q_A_dot*sin(q_A)*sin(q_B) + 0.1*q_A_dot*cos(q_A) - 0.1*q_B_dot*cos(q_A)*cos(q_B) ]
# [                                                                                     ]
# [                                -0.1*q_B_dot*sin(q_B)                                ]
SimplifyAndPrint(v_N_P)

print('\n-------------------------- Testing acceleration: a_N_P -------------------------- ')
# The correct answer is (very long!)
SimplifyAndPrint(a_N_P)