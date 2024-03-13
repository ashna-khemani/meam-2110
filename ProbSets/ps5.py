# %% Prob 9.8 sin(t)
# Prob 9.8: xdd = sin(t)
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def fun(t, x):
    xdot = np.array(np.zeros(x.size))
    xdot[0] = x[1]  #adot = b
    xdot[1] = np.sin(t)

    return xdot

x0 = np.array([0, 0])

t = np.array([0,20])
t_graph = np.linspace(0, 20, 1000)

soln = solve_ivp(fun, t, x0, t_eval=t_graph)

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(t_graph, soln.y[0])
plt.xlabel("t")
plt.ylabel("x")
plt.show()


# %% Prob 9.8 cos(t)
# Prob 9.8: xdd = cos(t)
def fun(t, x):
    xdot = np.array(np.zeros(x.size))
    xdot[0] = x[1]  #adot = b
    xdot[1] = np.cos(t)

    return xdot

x0 = np.array([0, 0])

t = np.array([0,20])

t_graph = np.linspace(0, 20, 1000)

soln = solve_ivp(fun, t, x0, t_eval=t_graph)

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(t_graph, soln.y[0])
plt.xlabel("t")
plt.ylabel("x")
plt.show()

# %% Prob 9.25 helicopter OPT 1
# Prob 9.25 helicopter OPT 1
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def x (t,theta):    # x is the ODE/sys of ODES. t is time, y (or theta) is vector of inputs
    # a = theta, b = theta dot
    # x(a,b) = adot, bdot = b, bdot, and bdot is given ODE
    thetadot = np.array(np.zeros(theta.size))
    thetadot[0] = theta[1]  #adot = b
    thetadot[1] = ( (4*thetadot[0] - 9.81*np.sin(theta[0])) / (50-2*t))

    return thetadot

theta0 = np.array([0.01745, 0])

t = np.array([0, 24.92])
t_graph = np.linspace(0, 24.92, 1000)

soln = solve_ivp(x, t, theta0, t_eval=t_graph)

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(t_graph, soln.y[0])
plt.xlabel("t")
plt.ylabel("theta")
plt.show()

# %% Prob 9.25 helicopter OPT 2
# Prob 9.25 helicopter OPT 2
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def x (t,theta):    # x is the ODE/sys of ODES. t is time, y is vector of inputs
    # a = theta, b = theta dot
    # x(a,b) = adot, bdot = b, bdot, and bdot is given ODE
    thetadot = np.array(np.zeros(theta.size))
    thetadot[0] = theta[1]  #adot = b
    thetadot[1] = ( (2*thetadot[0] - 9.81*np.sin(theta[0])) / (50-t))

    return thetadot

theta0 = np.array([0.01745, 0])

t = np.array([0, 49.84])
t_graph = np.linspace(0, 49.84, 1000)

soln = solve_ivp(x, t, theta0, t_eval=t_graph)

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(t_graph, soln.y[0])
plt.xlabel("t")
plt.ylabel("theta")
plt.show()
# %%
