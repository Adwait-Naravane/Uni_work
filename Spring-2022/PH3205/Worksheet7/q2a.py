import numpy as np
import matplotlib.pyplot as plt
from numba import jit

num_sims = 500
N = 100000
Y_0 = 0
t_0 = 0
T = 10
k1 = 10
k2 = 1
@jit(nopython = True, nogil = True)
def BirthDeath(N,num_sims, T):
  dt = (T - t_0) / N
  t = np.arange(t_0, T, dt) 

  dW = np.zeros(N)
  dW[0] = 0

  X = np.zeros(N) 
  X[0] = 0

  Y = np.zeros(N)
  Y[0] = 0

  SX = np.zeros(N)
  SY = np.zeros(N)
  for n in range(num_sims):
    for i in range(1, t.size): 
      dW[i] = np.random.normal(loc = 0.0, scale = np.sqrt((k1+k2*Y[i-1])*dt))

      X[i] = (k1/k2)*(1-np.exp(-k2*t[i]))
      SX[i] = SX[i] + X[i]/num_sims

      Y[i] = Y[i-1] + k1*dt - k2*dt*Y[i-1] + dW[i] 
      SY[i] = SY[i] + Y[i]/num_sims
  return t, SX, SY

t, SX, SY = BirthDeath(N, num_sims, T)

plt.plot(t, SX, label = 'actual')
plt.plot(t, SY, label = 'predicted')
plt.xlabel('t')
plt.ylabel('Population')
plt.legend()
plt.show()