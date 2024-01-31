import numpy as np
import sympy as sym

def rot_x(theta):   # NEEDS TO BE CHECKED!!
  '''
  Calculate R_A_B the rotation matrix that expresses the 'a' vector basis in terms of the 'b' basis.
  The a's are found by rotating the b's about b_x by angle theta

  Args:
    theta: The angle of rotation

  Returns:
    R_A_B
  '''
  # Use the sympy or math libraries for trig functions, depending on if the input is a floating point
  # number or a symbolic variable
  if isinstance(theta, sym.Expr):
    from sympy import sin, cos
  else:
    from math import sin, cos

  R_A_B = np.array([
    [1, 0, 0],
    [0, cos(theta), -sin(theta)],
    [0, sin(theta), cos(theta)]
  ])
  
  return R_A_B

def rot_y(theta):
  '''
  Calculate R_A_B the rotation matrix that expresses the 'a' vector basis in terms of the 'b' basis.
  The a's are found by rotating the b's about b_y by angle theta

  Args:
    theta: The angle of rotation

  Returns:
    R_A_B
  '''
  # Use the sympy or math libraries for trig functions, depending on if the input is a floating point
  # number or a symbolic variable
  if isinstance(theta, sym.Expr):
    from sympy import sin, cos
  else:
    from math import sin, cos
  
  R_A_B = np.eye(3) # REPLACE ME!
  return R_A_B

# Create symbolic variables q_1 and q_2
q_1 = sym.symbols('q_1')
q_2 = sym.symbols('q_2')

# Test rot_x
R_A_B = rot_x(q_1)
print('-----R_A_B, a rotation about the x-axis by angle q_1-----')
print(R_A_B)

# Test rot_y
R_B_C = rot_y(q_2)
print('-----R_B_C, a rotation about the y-axis by angle q_2-----')
print(R_A_B)

# Calculate and test R_A_C with symbolic inputs above
print('-----R_A_C with symbolic inputs-----')
# USE YOUR CODE HERE

# Calculate R_A_C where q_1 = 0.1 radians and q_2 = -.5
print('-----R_A_C with numeric inputs-----')
# USE YOUR CODE HERE
