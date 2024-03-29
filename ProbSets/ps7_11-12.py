###### FOR PROBLEM 11.12c

# %% Lecture 15 Example - modified slightly
# Lecture 15 Example - modified slightly
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

# calculate dy/dt, where y = [x, xdot]
I_1 = 1
I_2 = 3
I_3 = 10
b = 0.2
def f(t, omega):
  omega_dot = np.array([((I_2 - I_3)*omega[1]*omega[2] - b*omega[0])/I_1,
                        ((I_3 - I_1)*omega[0]*omega[2] - b*omega[1])/I_2,
                        ((I_1 - I_2)*omega[0]*omega[1] - b*omega[2])/I_3])
  return omega_dot


omega_0 = np.array([0.2, 7, 0.2])

T = 4 # final time
sol = solve_ivp(f, [0, T], omega_0, max_step=1e-3)

sol.t # a vector of times, shape (N,)
sol.y # a vector of values x(t)

plt.figure(1)
ax = plt.gca()
ax.plot(sol.t, sol.y.T)
ax.set_xlabel('Time')
ax.set_ylabel('omega')
ax.legend(['omega_x', 'omega_y', 'omega_z'])
plt.show()



# %% Find K_rotn
# Find K_rotn by components to see around which axis the box stabilizes
K = [0, 0, 0]   # K in x, y, z
I = [I_1, I_2, I_3]
for i in range(len(K)):
  K[i] = 0.5 * I[i] * sol.y.T[:, i] * sol.y.T[:, i]


plt.figure(2)
ax2 = plt.gca()
ax2.plot(sol.t, K[0])
ax2.plot(sol.t, K[1])
ax2.plot(sol.t, K[2])
ax2.set_xlabel('Time')
ax2.set_ylabel('K')
ax2.legend(['K_x', 'K_y', 'K_z'])
plt.show()

# %%
