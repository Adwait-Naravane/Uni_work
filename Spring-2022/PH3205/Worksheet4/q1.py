import numpy as np
import matplotlib.pyplot as plt 
rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0

def f(state):
    #first derivative
    x, y, z = state  
    return np.array([sigma * (y - x), x * (rho - z) - y, x * y - beta * z]) 

def rk4(initial, f, a, b ,dx):
    
  t = np.arange(a, b, dx) 
  lis = []
  lis.append(initial)
  for i in range(len(t) - 1):
    k1 = f(lis[i])
    k2 = f(lis[i] + k1*dx/2)
    k3 = f(lis[i] + k2*dx/2) 
    k4 = f(lis[i] + k3*dx)
    lis.append(lis[i] + dx*(k1 + 2*k2 + 2*k3 + k4)/6)
  return np.array(lis)

state0 = np.array([0, 1, 0])
t = np.arange(0.0, 40.0, 0.001)
states = rk4(state0, f, 0, 40, 0.01)
t = np.arange(0, 40, 0.01)


#part 1
fig, ax = plt.subplots()
ax.plot(t, states.T[1])
ax.set_xlabel('t')
ax.set_ylabel('y')
plt.show()


#part 2
plt.plot(states.T[0], states.T[2])
plt.xlabel('x')
plt.ylabel('z')
plt.show()