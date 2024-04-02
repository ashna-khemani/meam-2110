import numpy as np
from scipy.spatial.transform import Rotation
from meshcat.geometry import Cylinder, Sphere, MeshLambertMaterial, Line, PointsGeometry
from meam2110 import  DrawArrow, SystemCOM, BodyLinearMomentum, BodyAngularMomentum

def Project4TraceCoMPosition(system, q, color):
  '''
  Trace the position of the center of mass of the systrem

  Args:
    system: The rigid body system
    B: the body B
    r_Bo_P: The location of P on B
    q: the current joint positions
    color: The color of the line
  '''
  N = system.InertialFrameN()
  r_No_Scm = SystemCOM(system, q, N)
  name = 'System_CoM'
  if not hasattr(Project4TraceCoMPosition, "line_vertices"):
    Project4TraceCoMPosition.line_vertices = dict()
  if name in Project4TraceCoMPosition.line_vertices:
    Project4TraceCoMPosition.line_vertices[name] = np.column_stack((Project4TraceCoMPosition.line_vertices[name], r_No_Scm))
  else:
    Project4TraceCoMPosition.line_vertices[name] = np.column_stack((r_No_Scm)).T
  system.visualizer[name].set_object(Line(PointsGeometry(Project4TraceCoMPosition.line_vertices[name]), MeshLambertMaterial(color)))

def Project4TraceCoMPositionAnnotation(color):
  '''
  Returns the annotation, for use in RigidBodySystem.Animate, that traces
   the center of mass of the system

  Args:
    color: The color of the line
  '''
  annotation = lambda sys, q, qdot, qddot, t : Project4TraceCoMPosition(sys, q, color)
  return annotation


def Project4DrawLinearMomentum(system, radius, scale, color, q, qdot):
  '''
  Draw an arrow for the linear momentum of the system, originating at the center of mass

  Args:
    sys : RigidBodySystem object
    radius: The radius for the body of the arrow
    scale: A scaling factor applied to the arrow size
    color: The arrow color
    q: System positions
    qdot: System velocities
  '''
  N = system.InertialFrameN()
  r_No_Scm = SystemCOM(system, q, N)
  L_S_N = np.zeros(3)
  for body in system.bodies.values():
    L_S_N = L_S_N + BodyLinearMomentum(system, q, qdot, body, N)

  name = 'L_S_N'
  DrawArrow(system.visualizer, name, r_No_Scm, scale * L_S_N, radius, color, 0.2)

def Project4DrawLinearMomentumAnnotation(radius, scale, color):
  '''
  Returns the annotation, for use in RigidBodySystem.Animate, that draws
   the linear momentum of the system as an arrow

  Args:
    B: the body B
    r_Bo_P: The location of P on B
    radius: The radius for the body of the arrow
    scale: A scaling factor applied to the arrow size
    color: The arrow color
  '''
  annotation = lambda sys, q, qdot, qddot, t : Project4DrawLinearMomentum(sys, radius, scale, color, q, qdot)
  return annotation



def Project4DrawAngularMomentum(system, radius, scale, color, q, qdot):
  '''
  Draw an arrow for the angular momentum of the system, about the center of mass

  Args:
    sys : RigidBodySystem object
    radius: The radius for the body of the arrow
    scale: A scaling factor applied to the arrow size
    color: The arrow color
    q: System positions
    qdot: System velocities
  '''
  N = system.InertialFrameN()
  r_No_Scm = SystemCOM(system, q, N)
  H_S_Scm_N = np.zeros(3)
  for body in system.bodies.values():
    H_S_Scm_N = H_S_Scm_N + BodyAngularMomentum(system, q, qdot, body, N, r_No_Scm)

  name = 'H_S_Scm_N'
  DrawArrow(system.visualizer, name, r_No_Scm, scale * H_S_Scm_N, radius, color, 0.2)

def Project4DrawAngularMomentumAnnotation(radius, scale, color):
  '''
  Returns the annotation, for use in RigidBodySystem.Animate, that draws
   the angular momentum of the system as an arrow

  Args:
    radius: The radius for the body of the arrow
    scale: A scaling factor applied to the arrow size
    color: The arrow color
  '''
  annotation = lambda sys, q, qdot, qddot, t : Project4DrawAngularMomentum(sys, radius, scale, color, q, qdot)
  return annotation
