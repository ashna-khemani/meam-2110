import numpy as np
from meam2110 import *
from scipy.integrate import solve_ivp

###
### tennis racket/ space station handle example
### This uses your method from this week, NewtonEulerBodyEquations, 
### to automatically generate equations of motion and then integrate these equations numerically
### Look at how easy it is!
###

sys = RigidBodySystem()
sys.ParseURDF('models/tennis_racket.urdf')
C = sys.bodies['body_C'] # The body we're simulating
xdot_fun = NewtonEulerBodySymbolicEquations(sys, C)

q = np.array([0, 0, 0])
# Choose your initial angular velocity
qdot = np.array([.01, .01, 2])

t_eval = np.linspace(0, 10, 1000)
sol = solve_ivp(xdot_fun, [0, 10], np.hstack((q, qdot)), t_eval = t_eval)

sys.visualizer.open()
sys.Animate(sol.t, sol.y)
