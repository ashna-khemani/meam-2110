import numpy as np
import sympy as sym
from meam2110 import *

sym.init_printing(use_unicode=False)

# The problem has four bodies of interest: N, A, B, C
# N is special, as our system always has an inertial frame
system = RigidBodySystem(visualize=False)

# constants
m = sym.symbols('m')
r = sym.symbols('r')
L = sym.symbols('L')

mass_C = m

#
# YOUR CODE BELOW !!!!! READ THIS!!
#
# Determine the inertia of C about Ccm, and the position of the center of mass in C's coordinates
I_C_Ccm = np.array([[1, 0, 0],
                   [0, 1, 0],
                   [0, 0, 1]]) # fix me

r_Co_Ccm = np.array([0, 0, 0]) # Fix me

N = system.InertialFrameN()
A = Body('A')
B = Body('B')
C = Body('C', mass=mass_C, I_B_Bcm=I_C_Ccm, r_Bo_Bcm=r_Co_Ccm)

# Joint position, velocity
theta = sym.symbols('theta')
theta_dot = sym.symbols('theta_dot')
phi = sym.symbols('phi')
phi_dot = sym.symbols('phi_dot')
q_C = sym.symbols('q_c') # the textbook only defines omega_C, but our code always needs a position variable too
omega_C = sym.symbols('omega_C')

# 
#
# YOUR CODE BELOW
#   Assemble into q, q_dot
#   Be sure to pay attention to the sign of the angles in the problem! Your code
#   generates rotations in the positive direction, but theta and phi represent
#   angles in the negative direction
# 
# Add the appropriate joints to the system
#
#  Use your code from this week to calculate
#  L_C_N_B: the linear momentum of C in N, expressed in B's coordinates
#  H_C_No_N_B: the angular momentum of C about No, in N, expressed in B's coordinates
q = np.zeros(3) # REPLACE ME!
q_dot = np.zeros(3) # REPLACE ME!
q_ddot = np.zeros(3) # REPLACE ME!


# Since C is the only body that hass any mass, we only need to compute momentum of C
print('\n*** L_C_N expressed in B coordinates ***')
L_C_N_B = np.zeros(3)
SimplifyAndPrint(L_C_N_B)
                        
print('\n*** H_C_No_N expressed in B coordinates ***')
H_C_No_N_B = np.zeros(3)
SimplifyAndPrint(H_C_No_N_B)

# Optional (ungraded): compute the kinetic energy K_C_N
# Suggestion: use your kinematics methods from previous weeks, in combination with the momentum results above!
# If you choose to do this, you'll need the updated util.py from Canvas for SimplifyAndPrint to work properly
