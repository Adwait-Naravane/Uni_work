import numpy as np 
import matplotlib.pyplot as plt

'''
The constants below are gamma, m and omega. 
I assume m = 1 for the sake of convenience. 
'''
gamma = 25
m = 1
omega = 50
#lambda = 0.25
#Damped oscillator
f = lambda x,z: -(gamma/m)*z - (omega**2)*x

def rk4(initial, dx, a, b):
  t = np.arange(a,b, dx)
  x = []
  x.append(initial)
  for i in range(len(t)):
    k1 = x[i][1]
    l1 = f(x[i][0], x[i][1])   
    k2 = k1 + l1*dx/2
    l2 = f(x[i][0] + k1*dx/2, x[i][1] + l1*dx/2)
    k3 = k1 + l2*dx/2
    l3 = f(x[i][0] + k2*dx/2, x[i][1] + l2*dx/2)
    k4 = k1 + l3*dx
    l4 = f(x[i][0] + k3*dx, x[i][1] + l3*dx)
    y = x[i][0] + (1/6)*dx*(k1 + 2*(k2 + k3) + k4)
    z = x[i][1] + (1/6)*dx*(l1 + 2*(l2 + l3) + l4)
    x.append(np.array([y,z]))
  return x

#initial condition of particle at x = 0 with some velocity
initial = np.array([0,1])
stuff = rk4(initial, 0.0001, 0, 1)
position = [stuff[i][0] for i in range(len(stuff))]
velocity = [stuff[i][1] for i in range(len(stuff))]

t = np.arange(0,1+0.0001, 0.0001)

plt.plot(t, position)
plt.xlabel('time')
plt.ylabel('Position')
plt.show()

'''
When the value of gamma/2 > omega, we reach the overdamped region. gamma/2 = omega is the critical point 
lambda = gamma/(2*omega)
'''