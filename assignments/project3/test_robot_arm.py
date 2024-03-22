import numpy as np
import time
from meam2110 import *
from project3_visualization_annotations import Project3TracePosition, Project3DrawVelocity, Project3DrawAcceleration

'''
This file tests your `RelativeRotationMatrix` by visualizing a 7 degree of freedom robot arm

For this homework only, it uses pre-calculated positions and orientations to DRAW the robot
arm, but then uses student code to draw a frame for the arm. Each joint of the arm will
move through a 90 degree rotation. If your code is working, each drawn frame will stay rigidly
attached to the arm.

'''


# visualize system
sys = RigidBodySystem(visualize=True)
visual_options = VisualOptions()
visual_options.visualize_frame = False
sys.ParseURDF(urdf='models/panda_arm.urdf', visual_options=visual_options)

# load data
data = np.load('assignments/project3/project3_robot_arm.npy', allow_pickle='TRUE').item()
t = data['t']
q = data['q']
qdot = data['qdot']
qddot = data['qddot']

i = 1

sys.visualizer.open()

t0 = time.time()
while i > 0: # samples remain
  # configuration
  t_i = t[i]
  q_i = q[:, i]
  qdot_i = qdot[:, i]
  qddot_i = qddot[:, i]
  
  for B in sys.bodies.values():
    r_No_Bo = data[B.name]['r_No_Bo'][:,i]
    R_N_B = data[B.name]['R_N_B'][:,:,i]
    B.Draw(r_No_Bo, R_N_B)
  
    if B.name == 'panda_link8':
      Project3TracePosition(sys, B, np.zeros(3), q_i, color=0xff0000)
      Project3DrawVelocity(sys, B, np.zeros(3),  radius=.01, scale=.5, color=0x00ff00, q=q_i, qdot=qdot_i)
      Project3DrawAcceleration(sys, B, np.zeros(3), radius=.01, scale=.5, color=0x0000ff, q=q_i, qdot=qdot_i, qddot=qddot_i)

  time.sleep(.02)

  now = time.time() - t0
  i = np.argmax(t > now)
 