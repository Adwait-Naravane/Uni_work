import numpy as np
import matplotlib.pyplot as plt

dx = 0.01
dt = 0.01
pos = np.arange(-2,2,dx)
time = np.arange(1, 20, dt)

def rk4(initial, f, a, b ,dx):
    #same as the last one
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

'''
def euler(initial, f, a, b, dx):
    t = np.arange(a,b,dx)
    lis = []
    lis.append(initial)
    for i in range(len(t) - 1):
        lis.append(lis[i] + dx*f(lis[i]))
    return np.array(lis)

 #Uncomment it to use   

'''

def rho(x, t):
  D = (dx**2)/(2* dt)
  sigma = (2*t*D)**0.5 
  return (1/(2*np.pi*(sigma**2))**(0.5))*np.exp(-x**2/(2*(sigma**2)))

def g(state):
    #double derivative of distribution
  D = (dx**2)/(2* dt)
  # we have to calculate p(i+1) + p(i-1) - 2p(i), instead I shall use the gradient function in numpy which does the exact same job.
  return D*np.gradient(np.gradient(state)/np.gradient(pos))/np.gradient(pos)


state0 = rho(pos, 1)
states = rk4(state0, g, 1, 20, dt)
#states = euler(state0, g, 1, 20, dt)


plt.plot(pos, states[0], color = 'black', label = 't = 1s')
plt.plot(pos, states[1800], color = 'r', label = 't = 19s')
plt.plot(pos, states[800], color = 'b', label = 't = 9s')
plt.xlabel('x')
plt.ylabel('distribution')
plt.legend()
plt.show()