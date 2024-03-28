###### FOR PROBLEM 11.9

# %% Lecture 15 Example
# Lecture 15 Example
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

# calculate dy/dt, where y = [x, xdot]
I_1 = 1
I_2 = 3
I_3 = 10
def f(t, omega):
  omega_dot = np.array([(I_2 - I_3)/I_1*omega[1]*omega[2],
                        (I_3 - I_1)/I_2*omega[0]*omega[2],
                        (I_1 - I_2)/I_3*omega[0]*omega[1]])
  return omega_dot


omega_0 = np.array([7, 0.2, 0.2])

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


# %% Find H vect (Hx, Hy, Hz)
# Find H vect (Hx, Hy, Hz)
H = [0, 0, 0]
H[0] = I_1*sol.y.T[:,0]
H[1] = I_2*sol.y.T[:,1]
H[2] = I_3*sol.y.T[:,2]

plt.figure(2)
ax2 = plt.gca()
ax2.plot(sol.t, H[0])
ax2.plot(sol.t, H[1])
ax2.plot(sol.t, H[2])
ax2.set_xlabel('Time')
ax2.set_ylabel('H')
ax2.legend(['H_x', 'H_y', 'H_z'])
plt.show()


# %% Find magnitude of H
# Find magnitude of H
H_array = np.array(H)
H_mags = []
for i in range(len(sol.t)):
  H_mags.append(np.linalg.norm(H_array[:, i]))

plt.figure(3)
plt.plot(sol.t, H_mags)
plt.xlabel("Time")
plt.ylabel("Magnitude of H")
plt.show()


# %% Find K (rotational)
# Find K (rotational)
K = []
for i in range(len(sol.t)):
  curr_K = 0.5 * (I_1*sol.y.T[i][0]**2 + I_2*sol.y.T[i][1]**2 + I_3*sol.y.T[i][2]**2)
  K.append(curr_K)

plt.figure(4)
plt.plot(sol.t, K)
plt.xlabel("Time")
plt.ylabel("K")
plt.show()

# %%
