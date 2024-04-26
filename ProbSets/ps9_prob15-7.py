# 15.7
from sympy.solvers import solve
from sympy import Symbol, sin, cos

theta = Symbol('theta')
m_Q = 1
m_B = 4
g = 9.8
h = 0.25
k = 120
L_n = 0.5
y = m_Q*g*cos(theta)/k + L_n

sum_mmt0 = -1*m_Q*g*y*sin(theta) + m_B*g*h*sin(theta)
print(solve(sum_mmt0, theta))
