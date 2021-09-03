import numpy as np
import matplotlib.pyplot as plt

V_s = np.linspace(0, 3, 1000)

# print(V_s)
r = []
def I_D(x):
  return pow(10, 8) * x + 1 - np.exp((v_s - 1000 * x) / (26 * pow(10, -3)))


def I_D_prime(x):
  return pow(10, 8) + (1000 / (26 * pow(10, -3))) * np.exp((v_s - 1000 * x) / (26 * pow(10, -3)))


def new_rap(f, df, x0, tol):
       
  if abs(f(x0)) < tol:
    return x0
  else:
    return new_rap(f, df, x0 - f(x0) / df(x0), tol)

for v_s in V_s:
    roots = new_rap(I_D, I_D_prime, 1, 1e-6)
    r.append(roots)

r = 1000 * np.array(r)  
# print(r)
V_D = V_s - 1000 * (r / 1000)
# print(V_D)
plt.plot(V_s, r)
plt.title('Static V-I characteristics')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.savefig('q4-1.png')
plt.show()
plt.clf()
plt.plot(V_D, r)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.title('Dynamic V-I characteristics')
plt.savefig('q4-2.png')
plt.show()