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



'''
N -> A -> B are rotations about the z and x axes respectively
The A -> B joint is offset 10 cm in the a_x direction
'''
r_Ao_Bo = np.array([.1, 0, 0])

# Add 2 bodies/frames, A, B
A = Body('A', mass=.1, I_B_Bcm=0.1*np.diag([.0001, .0006, .0006]), r_Bo_Bcm=np.array([.05, 0, 0]))
B = Body('B', mass=.3, I_B_Bcm=0.3*np.diag([.001, .001, .0001]), r_Bo_Bcm=np.array([0, 0, .075]))

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

print('\n-------------------------- Testing center of mass  -------------------------- ')
# The correct answer is:
#
# [0.05625*sin(q_A)*sin(q_B) + 0.0875*cos(q_A)]
# [                                           ]
# [0.0875*sin(q_A) - 0.05625*sin(q_B)*cos(q_A)]
# [                                           ]
# [             0.05625*cos(q_B)              ]
r_No_Scm = SystemCOM(system, q, N)
SimplifyAndPrint(r_No_Scm)

print('\n-------------------------- Testing change inertia origin  -------------------------- ')
# The correct answer is:
#
# [0.10001    0.1       0   ]
# [                         ]
# [  0.1    0.10006     0   ]
# [                         ]
# [   0        0     0.20006]
I_A_P = ChangeInertiaOrigin(system, A, r_Bcm_P=np.array([1, -1, 0]))
SimplifyAndPrint(I_A_P)

print('\n-------------------------- Testing change inertia coordinates  -------------------------- ')
# Write the inertia of A about Acm in N's coordinates
# The correct answer is:
#
# [          2                                                 ]
# [5.0e-5*sin (q_A) + 1.0e-5     -2.5e-5*sin(2*q_A)        0   ]
# [                                                            ]
# [                                              2             ]
# [   -2.5e-5*sin(2*q_A)      6.0e-5 - 5.0e-5*sin (q_A)    0   ]
# [                                                            ]
# [            0                          0              6.0e-5]
I_A_Acm_N = ChangeInertiaCoordinates(system, q, A.I_B_Bcm, A, N)
SimplifyAndPrint(I_A_Acm_N)


print('\n-------------------------- Testing linear momentum of the first link (e.g. a pendulum)  -------------------------- ')
# Remember, since we're only looking at body A, this is just a pendulum.
# It's length is 5cm, and mass  is 0.1. The linear momentum is therefore
#
# [-0.005*q_A_dot*sin(q_A)]
# [                       ]
# [0.005*q_A_dot*cos(q_A) ]
# [                       ]
# [           0           ]
L_A_N = BodyLinearMomentum(system, q, q_dot, A, N)
SimplifyAndPrint(L_A_N)

print('\n-------------------------- Testing linear momentum of the second link  -------------------------- ')
# The second link is far less intuitive, since both joints can move it. Its linear momentum is
#
# [-0.03*q_A_dot*sin(q_A) + 0.0225*q_A_dot*sin(q_B)*cos(q_A) + 0.0225*q_B_dot*sin(q_A)*cos(q_B)]
# [                                                                                            ]
# [0.0225*q_A_dot*sin(q_A)*sin(q_B) + 0.03*q_A_dot*cos(q_A) - 0.0225*q_B_dot*cos(q_A)*cos(q_B) ]
# [                                                                                            ]
# [                                  -0.0225*q_B_dot*sin(q_B)                                  ]
L_B_N = BodyLinearMomentum(system, q, q_dot, B, N)
SimplifyAndPrint(L_B_N)


print('\n-------------------------- Testing angular momentum of the first link about No (e.g. a pendulum)  -------------------------- ')
# Remember, since we're only looking at body A, this is just a pendulum.
# Accounting for its mass, and inertia about the center of mass, the angular momentum is
# purely in the nz=az direction.
#
# [       0       ]
# [               ]
# [       0       ]
# [               ]
# [0.00056*q_A_dot]
H_A_No_N = BodyAngularMomentum(system, q, q_dot, A, N, -A.r_Bo_Bcm)
SimplifyAndPrint(H_A_No_N)

print('\n-------------------------- Testing angular momentum of the second link about Bo (e.g. a pendulum)  -------------------------- ')
# Here, we'll calculate the angular momentum of B about Bo in N, but then express it in B coordinates
# It's far more readable in B coordinates than in N coordinates!
# 
# [-0.0045*q_A_dot*cos(q_B) + 0.003675*q_B_dot]
# [                                           ]
# [         0.003675*q_A_dot*sin(q_B)         ]
# [                                           ]
# [   2.99999999999996e-5*q_A_dot*cos(q_B)    ]
H_B_Bo_N = BodyAngularMomentum(system, q, q_dot, B, N, -B.r_Bo_Bcm)
H_B_Bo_N_B = ChangeCoordinates(system, q, H_B_Bo_N, N, B)
SimplifyAndPrint(H_B_Bo_N_B)

print('\n-------------------------- Testing change momentum origin ------------------------- ')
# Use the angular momentum H_A_No_N (the angular momentum of A about No in N) to
# be about some alternate point P
# The correct answer is:
#
# [     -0.005*q_A_dot*cos(q_A)      ]
# [                                  ]
# [     -0.005*q_A_dot*sin(q_A)      ]
# [                                  ]
# [q_A_dot*(0.00056 - 0.005*sin(q_A))]
r_No_P = np.array([0, 1, -1])
H_A_P_N = ChangeMomentumOrigin(system, q, q_dot, A, N, H_A_No_N, r_No_P)
SimplifyAndPrint(H_A_P_N)
