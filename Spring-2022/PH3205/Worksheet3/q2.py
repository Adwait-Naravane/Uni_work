import numpy as np
import matplotlib.pyplot as plt

la = 1
f = lambda x: -x - la*(x**3) 

#velo verlet algo
def verlet(initial, dx, a, b):
  t = np.arange(a,b,dx)
  r = []
  r.append(initial)
  for i in range(len(t)):
    y = r[i][1] + dx*f(r[i][0])*0.5
    x = r[i][0] + dx*y
    v = y + dx*f(x)*0.5
    r.append(np.array([x,v]))
  return r

initial = np.array([1,0])

h = [0.001*i for i in range(1,4)]
for j in h:
  stuff = verlet(initial, j, 0, 10)
  position = np.array([stuff[i][0] for i in range(len(stuff))])
  velocity = np.array([stuff[i][1] for i in range(len(stuff))])
  t = np.arange(0,10+j, j)
  E = (velocity**2)/2 + (position**2)/2 + la*(position**4)/4
  plt.plot(t, E-np.mean(E), label = 'h = {}'.format(j))

plt.xlabel('time')
plt.ylabel('Error in Energy')
plt.legend()
plt.show()


#Use the code below for part b
'''
las = [0.3*i for i in range(1,4)]
for l in las:
  la = l
  stuff = verlet(initial, 0.0001, 0, 10)
  position = np.array([stuff[i][0] for i in range(len(stuff))])
  velocity = np.array([stuff[i][1] for i in range(len(stuff))])

  t = np.arange(0,10+0.0001, 0.0001)
 
  plt.plot(position, velocity, label = '$\lambda$ = {}'.format(l))
plt.xlabel('position')
plt.ylabel('velocity')
plt.legend()
'''

'''
The error increases with O(h^3) as we can see in part a
In part b, we see that the configuration space diagram moves from a circle at lambda = 0 (harmonic oscillator) to an ellipse in the anharmonic case. 
'''