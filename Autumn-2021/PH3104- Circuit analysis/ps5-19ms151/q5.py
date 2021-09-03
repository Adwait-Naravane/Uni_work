import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(x,t):
  return (i_s/C)*(np.exp((10*(2**(0.5))*np.sin(100*np.pi*t) - x)/V_t) - 1) - x/(R*C)

i_s = 10**(-8)
R = 1000
V_t = 0.026 
C = 10**(-3)

x0 = 0
ts = np.arange(0,5,0.001)
xs = odeint(f, x0, ts)
#xs is the array of V_0 values.
plt.plot(ts,xs)
plt.title('$V_0$ curve for $R = 1k \Omega, C = 1 m F$')
plt.xlabel('time (s)')
plt.ylabel('$V_0$')
plt.savefig('q52.png')
plt.show()