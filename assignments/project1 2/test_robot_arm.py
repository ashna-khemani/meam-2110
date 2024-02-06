import numpy as np
import time
from meam2110 import *

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
data = np.load('assignments/project1/project1_robot_arm.npy', allow_pickle='TRUE').item()
t = data['t']
q = data['q']

i = 1

# Create triad objects to draw body frames
for B in sys.bodies.values():
  if B.vis is not None:
    body_triad = triad(0.3)
    B.vis.vis[B.vis.name + '_triad'].set_object(body_triad)

input('Press enter to visualize, after opening (or reloading) Meschat browser window')

t0 = time.time()
while i > 0: # samples remain
  # configuration
  t_i = t[i]
  q_i = q[:, i]
  
  for B in sys.bodies.values():
    r_No_Bo = data[B.name]['r_No_Bo'][:,i]
    R_N_B = data[B.name]['R_N_B'][:,:,i]
    B.Draw(r_No_Bo, R_N_B)

    if B.vis is not None:
      R_N_B_student = RelativeRotationMatrix(sys, q_i, B, sys.InertialFrameN())

      # Draw triad at body origin, not visual origin
      T_N_B = CreateTransform(r_No_Bo, R_N_B_student)
      B.vis.vis[B.vis.name + '_triad'].set_transform(T_N_B)

  
  time.sleep(.02)

  now = time.time() - t0
  i = np.argmax(t > now)