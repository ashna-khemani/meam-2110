import numpy as np
from . import PointKinematics, BodyAngVelAndAccel, ChangeInertiaOrigin, \
    ChangeInertiaCoordinates, ChangeCoordinates

def BodyLinearMomentum(system, q, qdot, A, B):
  '''
  Computes the linear momentum of Body A in body B, in B's coordinates

  Args:
    system: The RigidBodySystem object
    q: The current system joint configuration
    qdot: The current system joint velocity
    A: The A body object
    B: The B body object

  Returns:
    L_A_B: The linear momentum of Body A in frame B, expressed in B's coordinates, \( ^A \\vec L ^B \)
  '''
  
  # YOUR CODE HERE
  L_A_B = np.zeros(3)

  return L_A_B

def BodyAngularMomentum(system, q, qdot, A, B, r_Ao_P):
  '''
  Computes the angular momentum of body A about P (a point fixed in A), in
  frame B, expressed in B's coordinates

  Args:
    system: The RigidBodySystem object
    q: The current system joint configuration
    qdot: The current system joint velocity
    A: The Body that angular momentum will be found for
    B: The frame that the angular momentum will be expressed in
    r_Ao_P: The vector from the origin of body A to point P, in A coordinates, \( ^{A_o} \\vec r^P \)

  Returns:
    H_A_P_B: The angular momentum of Body A about P in B expressed in frame B, \( \left[ \\vec H^{A/P} \\right]_B \)
  '''

  # YOUR CODE HERE
  # Be careful with the coordinates used for all vectors, and the points about which inertia and momentum
  # are calculated.
  H_A_P_B = np.zeros(3)

  return H_A_P_B

def ChangeMomentumOrigin(system, q, qdot, A, B, H_A_Ao_B, r_Ao_P_B):
  '''
  Changes the origin of angular momentum of A about Ao in B (H_A_Ao_B)
  be about P (H_A_P_B)

  Args:
    system: The RigidBodySystem object
    q: The current system configuration
    qdot: The joint velocity
    A: The body associated with the angular momentum
    B: The frame that the angular momentum is in
    H_A_Ao_B: Angular momentum of A in B, about Ao, expressed in B coordinates,  \( \left[ \\vec H^{A/A_o} \\right]_B \)
    r_Ao_P_B: Position vector from Ao to P, expressed in B coordinates, \( \left[ ^{A_o} \\vec r^P \\right]_B \)

  Returns:
    H_A_P_B: Angular momentum of A in B, about P, expressed in B coordinates,  \( \left[ \\vec H^{A/P} \\right]_B \)
  '''

  H_A_P_B = H_A_Ao_B + np.cross(-r_Ao_P_B, BodyLinearMomentum(system, q, qdot, A, B))

  return H_A_P_B
