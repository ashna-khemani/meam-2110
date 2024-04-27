import numpy as np
import sympy as sym

from meam2110 import *

sym.init_printing(use_unicode=False)

'''
Let's test your spring force on a planar body attached to a spring
'''

system = RigidBodySystem(visualize=False)
N = system.InertialFrameN()
system.ParseURDF('assignments/project5/spring_pendulum_2dbody.urdf')

k = 20
L0 = .5
C = system.GetBodyByName('body_C')

# Try changing the attachment point of the spring
spring_com = SpringForce('C_spring', C, np.array([0, 0, 0]), N, np.zeros(3), k=k, L0 = L0) #attached at the COM
spring_corner = SpringForce('C_spring', C, np.array([0, 0.25, 0.25]), N, np.zeros(3), k=k, L0 = L0) #attached at a corner


# Joint position, velocity, and acceleration variables
q_y = sym.symbols('q_y')
q_y_dot = sym.symbols('q_y_dot')
q_y_ddot = sym.symbols('q_y_ddot')

q_z = sym.symbols('q_z')
q_z_dot = sym.symbols('q_z_dot')
q_z_ddot = sym.symbols('q_z_ddot')

theta = sym.symbols('theta')
theta_dot = sym.symbols('theta_dot')
theta_ddot = sym.symbols('theta_ddot')


q = np.array([q_y, q_z, theta])
q_dot = np.array([q_y_dot, q_z_dot, theta_dot])
q_ddot = np.array([q_y_ddot, q_z_ddot, theta_ddot])


print('\n-------------------------- Testing force from a spring attached to the CoM  -------------------------- ')
# The correct answer is:
#
# [             0              ]
# [                            ]
# [                10.0*q_y    ]
# [-20.0*q_y + ----------------]
# [               _____________]
# [              /    2      2 ]
# [            \/  q_y  + q_z  ]
# [                            ]
# [                10.0*q_z    ]
# [-20.0*q_z + ----------------]
# [               _____________]
# [              /    2      2 ]
# [            \/  q_y  + q_z  ]

F_C_N, T_C_N = spring_com.ComputeForceAndTorque(system, q, q_dot)
SimplifyAndPrint(F_C_N)

print('\n-------------------------- Testing moment from a spring attached to the CoM  -------------------------- ')
# This should be zero!
SimplifyAndPrint(T_C_N)

print('\n-------------------------- Testing ComputeAppliedForcesAndMoments from a spring  -------------------------- ')
# This should look the same as above, when you use spring_com
system.AddForceTorque(spring_com)
# READ ME! Try changing this to use "spring_corner", the spring attached to the corner of the cube. 
# Your answer should change dramatically, and get pretty messy! Good luck doing this math by hand.
F_C_N, M_Ccm_N = ComputeAppliedForcesAndMoments(system, q, q_dot, C)

SimplifyAndPrint(F_C_N)

SimplifyAndPrint(M_Ccm_N)


print('\n-------------------------- Testing equations of motion  -------------------------- ')
# Let's calculate the N-E equations for this body
# Since it's a 2D body, but we treat everything as 3D, we'll have some extra zeros in here for 
# th3 out-of-plane motion
# 
# Assuming that, above, you're using spring_com, the equations below.
#
# You're encouraged to inspect! Remember, these expressons are all equal to 0
# Since we attached the spring to the COM, there's no net moment, and so theta_ddot = 0 (third equation)
# 
# The other two equations describe the y and z linear spring dynamics, plus gravity (g=10)
#
# [                     0                     ]
# [                                           ]
# [                10.0*q_y                   ]
# [-20.0*q_y + ---------------- - 2.0*q_y_ddot]
# [               _____________               ]
# [              /    2      2                ]
# [            \/  q_y  + q_z                 ]
# [                                           ]
# [                10.0*q_z                   ]
# [-20.0*q_z + ---------------- - 2.0*q_z_ddot]
# [               _____________               ]
# [              /    2      2                ]
# [            \/  q_y  + q_z                 ]
# [                                           ]
# [             -0.01*theta_ddot              ]
# [                                           ]
# [                     0                     ]
# [                                           ]
# [                     0                     ]
eom = NewtonEulerBodyEquations(system, q, q_dot, q_ddot, C)

SimplifyAndPrint(eom)