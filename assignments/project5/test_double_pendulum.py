import numpy as np
from meam2110 import *
from scipy.integrate import solve_ivp


sys = RigidBodySystem()
sys.ParseURDF('models/double_pendulum.urdf')

AddJointConstraints(sys)
AddGravityToSystem(sys, 9.81)

xdot_fun = NewtonEulerSystemSymbolicEquations(sys, simplify = False)

T = 10
t_eval = np.linspace(0, T, T*60)
q = np.array([1, 0])
qdot = np.array([0, 0])


sol = solve_ivp(xdot_fun, [0, T], np.concatenate((q, qdot)), t_eval = t_eval)

sys.visualizer.open()
sys.Animate(sol.t, sol.y[:2])

