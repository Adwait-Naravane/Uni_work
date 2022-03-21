import numpy as np
import matplotlib.pyplot as plt 

#mass = 1
#velocity or momentum vector from hamilton's equations
f = lambda x,y: np.array([-x*(1+2*y), -y - x**2 + 1.5*(y**2)])

#velocity-verlet algorithm 
def verlet(initial, dx, a, b):
  t = np.arange(a,b,dx)
  r = []
  r.append(initial)
  for i in range(len(t)):
    y = r[i][1] + dx*f(*r[i][0])*0.5
    x = r[i][0] + dx*y
    v = y + dx*f(*x)*0.5
    r.append(np.array([x,v]))
  return r

initial = np.array([[0.2,0.2],[0.2,0.2]])

final = verlet(initial, 0.001, 0, 50)

def energy(x_val):
#energy for the system
  x, y = x_val[0]
  v_x, v_y = x_val[1]
  return (v_x**2 + v_y**2 + x**2 + y**2)/2 + y*(x**2) - y**3/2

energies = []
for coord in final:
  energies.append(energy(coord))

t = np.arange(0,50.001,0.001)
plt.plot(t, energies)
plt.xlabel('time')
plt.ylabel('Energy')
plt.show()

#print('Average energy: ', np.mean(energies)) 
#0.084000.. 
