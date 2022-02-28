import numpy as np
import matplotlib.pyplot as plt
from numba import jit
num_sims = 100
N = 1000
X_0 = 1
Y_0 = 1
t_0 = 0
T = 1
r_0 = 1
sigma_0 = 1
#using numba for speed
@jit(nopython = True, nogil = True)
def BlackScholes(N, num_sims, T):
  dt = (T - t_0) / N
  t = np.arange(t_0, T, dt) 

  dW = np.zeros(N)
  dW[0] = 0

  X = np.zeros(N) 
  X[0] = 1

  Y = np.zeros(N)
  Y[0] = Y_0

  SX = np.zeros(N)
  SY = np.zeros(N)

  for n in range(num_sims):
      for i in range(1, t.size):
          dW[i] = np.random.normal(loc = 0.0, scale=np.sqrt(dt))
          X[i] = X_0 * np.exp( (r_0*t[i] - 0.5*sigma_0*sigma_0*t[i] + (float(sigma_0) * np.sum(dW[:i]))))
          SX[i] = SX[i] + X[i]/num_sims
          Y[i] = Y[i-1] + (r_0 * Y[i-1]) * dt + (sigma_0 * Y[i-1] * dW[i])
          SY[i] = SY[i] + Y[i]/num_sims
  return t, SX, SY

if __name__ == "__main__":  
    t, SX, SY = BlackScholes(N, num_sims, T)
    plt.plot(t, SX, label = 'actual')
    plt.plot(t, SY, label = 'predicted')
    plt.xlabel('t')
    plt.ylabel('x')
    plt.legend()
    plt.show()