import numpy as np
from. import PointKinematics, RelativeRotationMatrix

def SystemMass(system):
  '''
  Compute the total mass of the system m_S

  Args:
    system: The RigidBodySystem object

  Returns:
    m_S: The total mass of the system
  '''

  m_S = 0
  for body in system.bodies.values():
    m_S += body.mass
  return m_S

def SystemCOM(system, q, B):
  '''
  Compute the center of mass of the system from point Bo, expressed in B's coordinates

  Args:
    system: The RigidBodySystem oject
    q: The current system configuration
    B: Frame B

  Returns:
    r_Bo_Scm: Center of mass of the system from point Bo, \(^{B_o}\\vec r^{S_{cm}} \) expressed in  B's coordinates
  '''
  # YOUR CODE HERE
  # Calculate the position of the center of mass
  # You may find for loop in SystemMass(system), above, to be helpful as a starting point
  r_Bo_Scm = np.zeros(3) # replace me!

  return r_Bo_Scm

def ChangeInertiaOrigin(system, B, r_Bcm_P):
  '''
  I_B_P = ChangeInertiaOrigin(system, B, r_Bcm_P)

  Changes origin of inertia of body B from Bcm to arbitrary point P

  system: A RigidBodySystem object
  B: The body described by the inertia tensor
  r_Bcm_P" Vector from Bcm to point P, in B coordinates
  I_B_P: Inertia of B about point P, in B coordinates
  '''
  
  # YOUR CODE HERE
  I_B_P = np.eye(3)

  return I_B_P


def ChangeInertiaCoordinates(system, q, I_S_P_A, A, B):
  '''
  I_S_P_B = ChangeInertiaCoordinates(system, q, I_S_P_A, A, B)
  Changes the inertia matrix for system S from A's coordinates to B's
  coordinates.

  system: The RigidBodySystem object
  q: The current system configuration
  I_S_P_A: Inertia of S around point P in A's coordinates
  A: The body whose coordinates are used to express I_S_P_A
  B: The body whose coordinates will be used to express I_S_P_B

  I_S_P_B: The inertia of S around P in B coordinates
  '''

  # YOUR CODE HERE
  I_S_P_B = np.eye(3)

  return I_S_P_B