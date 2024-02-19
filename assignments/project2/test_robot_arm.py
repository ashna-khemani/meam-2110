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
data = np.load('assignments/project2/project2_robot_arm.npy', allow_pickle='TRUE').item()
t = data['t']
q = data['q']
qdot = data['qdot']

i = 1
input('Press enter to visualize, after opening (or reloading) Meschat browser window')


def DrawAngularVelocityVector(system, B, q, qdot, r_No_Bo, thickness, scale):
  w_N_B,_ = BodyAngVelAndAccel(system, q, qdot, B, system.InertialFrameN())

  cyl = Cylinder(thickness, scale*np.linalg.norm(w_N_B))
  material = MeshLambertMaterial(color=0x000000, opacity=.2)
  system.visualizer[B.name + '_angvel'].set_object(cyl, material)

  if np.linalg.norm(w_N_B) > 1e-3:
    R_N_AV = Rotation.align_vectors([w_N_B], [np.array([0, 1, 0])])[0].as_matrix()

  else:
    R_N_AV = np.eye(3)
  system.visualizer[B.name + '_angvel'].set_transform(CreateTransform(r_No_Bo, R_N_AV))


t0 = time.time()
while i > 0: # samples remain
  # configuration
  t_i = t[i]
  q_i = q[:, i]
  qdot_i = qdot[:, i]
  
  for B in sys.bodies.values():
    r_No_Bo = data[B.name]['r_No_Bo'][:,i]
    R_N_B = data[B.name]['R_N_B'][:,:,i]
    B.Draw(r_No_Bo, R_N_B)
  
    if B.name == 'panda_link8':
      DrawAngularVelocityVector(sys, B, q_i, qdot_i, r_No_Bo, .02, .2
      )
  
  time.sleep(.02)

  now = time.time() - t0
  i = np.argmax(t > now)
  