import numpy as np
import meshcat.geometry
from scipy.integrate import solve_ivp

from meam2110 import *
from project5_visualization_annotations import *

###
### A planar (2D) object attached by a spring
### This uses your method from this week, NewtonEulerBodyEquations, 
### to automatically generate equations of motion and then integrate these equations numerically.
### Look at how easy it is!
###
system = RigidBodySystem(visualize=True)
N = system.InertialFrameN()
system.ParseURDF('assignments/project5/spring_pendulum_2dbody.urdf')

k = 20
L0 = .5
C = system.GetBodyByName('body_C')

# Try changing the attachment point of the spring
# spring = SpringForce('C_spring', C, np.array([0, 0, 0]), N, np.zeros(3), k=k, L0 = L0) #attached at the COM
spring = SpringForce('C_spring', C, np.array([0, .25, .25]), N, np.zeros(3), k=k, L0 = L0) #attached at a corner
system.AddForceTorque(spring)

# Add a small amount of damping to the system. Adds linear and rotational dampers. Feel free to play with the
# damping coefficient b
for joint in system.joints.keys():
  b = .002
  damper = ConstantVelocityController(joint, 0, b)
  system.AddForceTorque(damper)

# Model gravity
AddGravityToSystem(system)

# Since all objects are 3D in our code, we need constraints to keep it 2D
AddJointConstraints(system)

# Generate the equations of motion and itegrate!
xdot_fun = NewtonEulerSystemSymbolicEquations(system, C)
T = 20
t_eval = np.linspace(0, T, 1000)
q = np.array([.1, -1.5, .02]) # initial [position_y, position_z, rot_x]
qdot = np.array([0, 0, 0])
sol = solve_ivp(xdot_fun, [0, T], np.hstack((q, qdot)), t_eval = t_eval)


# Draw the solution
position_annotation = Project5TracePositionAnnotation(C, np.zeros(3), color=0xFF0000)
spring_annotation = Project5SpringAnnotation(spring, color=0x00FFFF, scale=.01)

system.visualizer.open()
system.Animate(sol.t, sol.y, callbacks = [position_annotation, spring_annotation])
