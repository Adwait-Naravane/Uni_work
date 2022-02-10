from numba import jit
import numpy as np
import matplotlib.pyplot as plt
@jit(nopython=True, nogil=True)

def rand_walk(N,a):
  x = 0 
  for i in range(N):
    x = x + ((-1)**(np.random.randint(0,2)))*a
  return x


N = 1000
a = 1
M = 1000
turns = lambda M,N: np.array([rand_walk(N,a) for j in range(M)])
sigma = []

for i in range(1,100):
  sigma.append(np.std(turns(M, N*i)))

'''
#2.B
'''

plt.scatter(range(1,100), sigma)
plt.plot(range(1,100), 32*np.array(range(1,100))**0.5, color = 'r')
plt.xlabel('N')
plt.ylabel('$\sigma$')
#here we can see, that sigma is prop to square root of N
plt.show()

'''
#2.A
plt.hist(turns(100000,1000),bins = 200)
plt.xlabel('distance from origin')
plt.ylabel('freq')
plt.show()
'''