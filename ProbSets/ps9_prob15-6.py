# 15.6
from sympy.solvers import solve
from sympy import Symbol
from sympy import sin, cos, tan, sqrt, asin

theta = Symbol('theta')
R = 0.4
h = 1
g = 9.8
m_B = 4.8
L_B = 1
m_Q = 1
y = 2*R*cos(theta)
k = 120
L_n0 = 0.1
L_n1 = 0.3
L_1 = sqrt( (L_B*sin(theta))*(L_B*sin(theta)) + ((h+R)-L_B*cos(theta))*((h+R)-L_B*cos(theta)))
F_Ncirc = 1/cos(theta) * (m_B*g*cos(theta) + k*(y-L_n0))

moment_sum0 = -g*(0.5*m_B*L_B*sin(theta) + m_Q*y*sin(theta)) + L_B*k*(L_1-L_n1)*(R+h)*sin(theta)/L_1 - y*F_Ncirc*sin(2*theta)

solve(moment_sum0, theta)


