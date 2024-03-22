import numpy as np
from scipy.spatial.transform import Rotation
from meshcat.geometry import Cylinder, Sphere, MeshLambertMaterial, Line, PointsGeometry
from meam2110 import PointKinematics, BodyAngVelAndAccel, CreateTransform, DrawArrow

def Project3TracePosition(system, B, r_Bo_P, q, color):
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
  if not hasattr(Project3TracePosition, "line_vertices"):
    Project3TracePosition.line_vertices = dict()
  if name in Project3TracePosition.line_vertices:
    Project3TracePosition.line_vertices[name] = np.column_stack((Project3TracePosition.line_vertices[name], r_No_P))
  else:
    Project3TracePosition.line_vertices[name] = np.column_stack((r_No_P)).T
  system.visualizer[name].set_object(Line(PointsGeometry(Project3TracePosition.line_vertices[name]), MeshLambertMaterial(color)))

def Project3TracePositionAnnotation(B, r_Bo_P, color):
  '''
  Returns the annotation, for use in RigidBodySystem.Animate, that traces
   the position of a given point

  Args:
    B: the body B
    r_Bo_P: The location of P on B
    color: The color of the line
  '''
  annotation = lambda sys, q, qdot, qddot, t : Project3TracePosition(sys, B, r_Bo_P, q, color)
  return annotation


def Project3DrawVelocity(system, B, r_Bo_P, radius, scale, color, q, qdot):
  '''
  Draw an arrow for the velocity of a given point.

  Args:
    sys : RigidBodySystem object
    B: the body B
    r_Bo_P: The location of P on B
    radius: The radius for the body of the arrow
    scale: A scaling factor applied to the arrow size
    color: The arrow color
    q: System positions
    qdot: System velocities
  '''
  r_No_P, v_N_P, _ = PointKinematics(system, q, B, system.InertialFrameN(), r_Ao_P = r_Bo_P, qdot = qdot)
  name = B.name + '_' + str(r_Bo_P) + '_vel'
  DrawArrow(system.visualizer, name, r_No_P, scale * v_N_P, radius, color, 0.2)

def Project3VelocityAnnotation(B, r_Bo_P, radius, scale, color):
  '''
  Returns the annotation, for use in RigidBodySystem.Animate, that draws
   the velocity of a given point as an arrow

  Args:
    B: the body B
    r_Bo_P: The location of P on B
    radius: The radius for the body of the arrow
    scale: A scaling factor applied to the arrow size
    color: The arrow color
  '''
  annotation = lambda sys, q, qdot, qddot, t : Project3DrawVelocity(sys, B, r_Bo_P, radius, scale, color, q, qdot)
  return annotation


def Project3DrawAcceleration(system, B, r_Bo_P, radius, scale, color, q, qdot, qddot):
  '''
  Draw an arrow for the acceleration of a given point.

  Args:
    sys : RigidBodySystem object
    B: the body B
    r_Bo_P: The location of P on B
    radius: The radius for the body of the arrow
    scale: A scaling factor applied to the arrow size
    color: The arrow color
    q: System positions
    qdot: System velocities
    qdot: System accelerations
  '''
  r_No_P, _, a_N_P = PointKinematics(system, q, B, system.InertialFrameN(), r_Ao_P = r_Bo_P, qdot = qdot, qddot=qddot)
  name = B.name + '_' + str(r_Bo_P) + '_accel'
  DrawArrow(system.visualizer, name, r_No_P, scale * a_N_P, radius, color, 0.2)

def Project3AccelerationAnnotation(B, r_Bo_P, radius, scale, color):
  '''
  Returns the annotation, for use in RigidBodySystem.Animate, that draws
   the acceleration of a given point as an arrow

  Args:
    B: the body B
    r_Bo_P: The location of P on B
    radius: The radius for the body of the arrow
    scale: A scaling factor applied to the arrow size
    color: The arrow color
  '''
  annotation = lambda sys, q, qdot, qddot, t : Project3DrawAcceleration(sys, B, r_Bo_P, radius, scale, color, q, qdot, qddot)
  return annotation
