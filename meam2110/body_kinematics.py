import numpy as np
from . import FindPath, JointTransformation, JointChildVelocity, JointChildAcceleration

def RelativeRotationMatrix(system, q, A, B):
  '''
  Compute \(^B R^A\), the rotation matrix expressing B in A.
  This requires determining the path from B to A, then successively computing
  the rotation matrix expressing B in various vector bases along the path.

  Args:
    system: The RigidBodySystem object
    q: The vector of joint positions
    A: The Body A object
    B: The Body B object

  Returns:
    R_B_A: the rotation matrix expressing B in A, \(^B R^A\)
  '''

  path, directions = FindPath(B, A)

  # Call `C` the current child body along the path. Traversing the path, update
  # R_B_C until C is A

  # Initialize C = B
  R_B_C = np.eye(3)

  for i, direction_i in enumerate(directions):
    # Set the new parent to be the old child
    R_B_P = R_B_C

    # Find joint, joint parent, and joint child
    if direction_i > 0:
      JP = path[i]
      JC = path[i+1]
    else:
      JP = path[i+1]
      JC = path[i]
    joint = JC.parent_joint

    # Use other code you've written to:
    # 1) calculate R_JP_JC
    # 2) determine R_P_C, using direction_i
    # 3) calculate R_B_C
    # YOUR CODE HERE
    R_JP_JC = np.eye(3) # replace me!
    R_P_C = np.eye(3) # replace me!
    R_B_C = np.eye(3) # replace me!
    
  # A is the last child
  R_B_A = R_B_C

  return R_B_A


def ChangeCoordinates(system, q, x_A, A, B):
  '''
  Express the vector x in B's coordinates, given an expression in A's
  coordinates. Note that x_A and x_B represent the same vector, just in
  different coordinates.

  Args:
    system: The RigidBodySystem object
    q: The vector of joint positions
    x_A: A representation of x in A's coordinates
    A: Body A object
    B: Body B object

  Returns:
    x_B: The representation of x in B's coordinates
  '''

  # YOUR CODE GOES HERE
  x_B = np.zeros(3) # replace me!

  return x_B

def BodyAngVelAndAccel(system, q, qdot, A, B, qddot = None):
  '''
  Compute angular velocity and acceleration of body A in body B, in B coordinates
  Specifically, returns \( ^B \\vec \omega ^A \) and \( ^B \\vec \\alpha ^A \)

  Args:
    system: The RigidBodySystem object
    q: vector of joint positions
    qdot: vector of joint velocities
    qddot: vector of joint accelerations
    A: The Body A object
    B: The Body B object

  Returns:
    w_B_A: The angular velocity \( ^B \\vec \omega ^A \)
    alpha_B_A: The angular acceleration \( ^B \\vec \\alpha ^A \)
  '''

  if qddot is None:
    qddot = qdot * 0

  path, directions = FindPath(B, A)

  # Call `C` the current child body along the path. Traversing the path, update
  # w_B_C until C is A

  # Initialize C = B

  C = B
  w_B_C = np.zeros(3)
  alpha_B_C = np.zeros(3)

  for i, direction_i in enumerate(directions):
    # Set the new parent to be the old child
    w_B_P = w_B_C
    alpha_B_P = alpha_B_C
    P = C
    C = path[i+1]

    # Find joint, joint parent, and joint child
    if direction_i > 0:
      JP = path[i]
      JC = path[i+1]
    else:
      JP = path[i+1]
      JC = path[i]
    joint = JC.parent_joint

    # Use other code you've written to:
    # 1) calculate w_JP_JC and alpha_JP_JC
    # 2) determine w_P_C and alpha_P_C
    # 3) calculate w_B_C and alpha_B_C
    # Be sure to carefully track what coordinates every vector is expressed in, and change
    # coordinates if necessary!
    #
    # YOUR CODE HERE
    w_B_C = np.zeros(3)
    alpha_B_C = np.zeros(3)

  # The last child is A
  w_B_A = w_B_C
  alpha_B_A = alpha_B_C

  return w_B_A, alpha_B_A