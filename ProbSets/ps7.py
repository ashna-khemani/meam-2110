# Based on Lecture 15 Example
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

# calculate dy/dt, where y = [x, xdot]
def f(t, omega):
  I_1 = 1
  I_2 = 3
  I_3 = 10
  omega_dot = np.array([(I_2 - I_3)/I_1*omega[1]*omega[2],
                        (I_3 - I_1)/I_2*omega[0]*omega[2],
                        (I_1 - I_2)/I_3*omega[0]*omega[1]])
  return omega_dot


omega_0 = np.array([.01, 1, .01])

T = 50 # final time
sol = solve_ivp(f, [0, T], omega_0, max_step=1e-3)

sol.t # a vector of times, shape (N,)
sol.y # a vector of values x(t)


ax = plt.gca()
ax.plot(sol.t, sol.y.T)
ax.set_xlabel('Time', fontsize=20)
ax.set_ylabel('omega', fontsize=20)
ax.legend(['omega_x', 'omega_y', 'omega_z'], fontsize=20)
plt.show()
