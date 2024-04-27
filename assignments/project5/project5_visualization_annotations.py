import numpy as np
from scipy.spatial.transform import Rotation
from meshcat.geometry import Cylinder, Sphere, MeshLambertMaterial, Line, PointsGeometry
from meam2110 import PointKinematics, CreateTransform

def Project5TracePosition(system, B, r_Bo_P, q, color):
  '''
  Trace the position of a given point P on a body

  Args:
    system: The rigid body system
    B: the body B
    r_Bo_P: The location of P on B
    q: the current joint positions
    color: The color of the line
  '''
  r_No_P, _, _ = PointKinematics(system, q, B, system.InertialFrameN(), r_Ao_P = r_Bo_P)
  name = B.name + '_' + str(r_Bo_P)
  if not hasattr(Project5TracePosition, "line_vertices"):
    Project5TracePosition.line_vertices = dict()
  if name in Project5TracePosition.line_vertices:
    Project5TracePosition.line_vertices[name] = np.column_stack((Project5TracePosition.line_vertices[name], r_No_P))
  else:
    Project5TracePosition.line_vertices[name] = np.column_stack((r_No_P)).T
  system.visualizer[name].set_object(Line(PointsGeometry(Project5TracePosition.line_vertices[name]), MeshLambertMaterial(color)))

def Project5TracePositionAnnotation(B, r_Bo_P, color):
  '''
  Returns the annotation, for use in RigidBodySystem.Animate, that traces
   the position of a given point

  Args:
    B: the body B
    r_Bo_P: The location of P on B
    color: The color of the line
  '''
  annotation = lambda sys, q, qdot, qddot, t : Project5TracePosition(sys, B, r_Bo_P, q, color)
  return annotation


def Project5DrawSpring(system, spring, color, scale, q):
  # TODO: add documentation
  N = system.InertialFrameN()
  r_No_P, _, _ = PointKinematics(system, q, spring.C, N, r_Ao_P = spring.r_Co_G)
  r_No_Q, _, _ = PointKinematics(system, q, spring.P, N, r_Ao_P = spring.r_Po_H)
  
  r_P_Q = -r_No_P + r_No_Q

  cyl_len = np.linalg.norm(r_P_Q)
  
  radius = np.sqrt(scale/cyl_len)
  cyl = Cylinder(cyl_len, radius)
  # Set the color to be mostly transparent red.
  material = MeshLambertMaterial(color=color, opacity=.3)
  system.visualizer[spring.name + '_cyl'].set_object(cyl, material)

  # Set the location and orientation.
  R_N_Cyl = Rotation.align_vectors([r_P_Q], [np.array([0, 1, 0])])[0].as_matrix()


  # Set the location so the base of the cylinder is at the origin
  r_No_Vo = r_No_P + r_P_Q / 2
  system.visualizer[spring.name + '_cyl'].set_transform(CreateTransform(r_No_Vo, R_N_Cyl))

def Project5SpringAnnotation(spring, color, scale):
  '''
  Returns the annotation, for use in RigidBodySystem.Animate, that draws
   a spring as a cylinder

  Args:
    spring: The SpringForce object
    scale: A scaling factor applied to the cylinder, roughly corresponding with volume / pi
    color: The color
  '''
  annotation = lambda sys, q, qdot, qddot, t : Project5DrawSpring(sys, spring, color, scale, q)
  return annotation