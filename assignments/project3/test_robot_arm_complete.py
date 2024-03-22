import numpy as np
import sympy as sym
from urchin import URDF
from meam2110 import *
from meshcat import Visualizer
from scipy.interpolate import make_interp_spline

# Generate kinematic motion for Robot Arm
T = 20 # Duration of animation (s)

# EDIT OR ADD JOINT MOTIONS BELOW!
# 1:3 in matrix are roll, np.pitch, yaw for shoulder
# 4 is elbow 
# 5:7 are wrist roll, np.pitch, and yaw
# All joint angles in radians
q0 = np.array([np.pi/2,0,0,0,0,0,0])
q1 = np.array([-np.pi/2,0,0,0,0,0,0])
q2 = np.array([0,0,0,-np.pi/2,0,0,0])
q3 = np.array([0,0,0,-np.pi/2,np.pi,np.pi,np.pi])
q4 = np.array([0,np.pi/4,0,-np.pi/4,0,0,0])
q5 = np.array([np.pi/8,np.pi/4,0,-np.pi/4,np.pi/4,0,0])
q6 = np.array([-np.pi/8,np.pi/4,0,-np.pi/4,-np.pi/4,0,0])
q7 = np.array([0,0,0,0,0,0,0])

# Make sure to add/remove qs to this matrix if you want them animated
q_samples = np.vstack([q0,q1,q2,q3,q4,q5,q6,q7])

t_samples = np.linspace(0, T, len(q_samples))
q_spline = make_interp_spline(t_samples, q_samples)
qdot_spline = q_spline.derivative()
qddot_spline = q_spline.derivative(2)

t = np.linspace(0, T, T*30)
q_t = q_spline(t).T
qdot_t = qdot_spline(t).T
qddot_t = qddot_spline(t).T

sys = RigidBodySystem()
visual_options = VisualOptions(visualize_frame=False)
sys.ParseURDF('models/panda_arm.urdf', visual_options=visual_options)

# Draw the position, velocity, and acceleration of the hand (link8)
B = sys.bodies['panda_link8']
position_annotation = TracePositionAnnotation(B, np.array([0, 0, 0]), color=0xff0000)
velocity_annotation = VelocityAnnotation(B, np.zeros(3), radius=.01, scale=.5, color=0x00ff00)
acceleration_annotation = AccelerationAnnotation(B, np.zeros(3), radius=.01, scale=.5, color=0x0000ff)
annotations = [position_annotation, velocity_annotation, acceleration_annotation]

sys.visualizer.open()
sys.Animate(t, q_t, qd = qdot_t, qdd=qddot_t, callbacks = annotations)
