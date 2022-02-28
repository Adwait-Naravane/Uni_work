'''
Here I just present how a = e^l/(e^l - 1) maximises the accuracy 

'''
import numpy as np
from scipy import integrate

#l is the limit of integration, integrals are from 0 to l. 
#l = np.pi

#The value of 'a' is fixed at below. It is obtained by normalising p(y) from 0 to l.
#a = np.exp(l)/(np.exp(l)- 1)

def f(x):
  return 1/(x**2 + np.cos(x)**2)

def w(x,a):
  return a*np.exp(-x)

def inv(x,a):
  #inverse of the cdf
  return np.log(np.abs(a/(a-x)))

N = 1000000
x = np.random.uniform(0,1, N)

def q(x,a):
  
  
  p = inv(x,a)
  q = f(p)/w(p,a)
  return q 

a_s = np.arange(0.1, 4, 0.05)
ints = []
for a in a_s:
  ints.append(np.abs((np.mean(q(x,a)) - integrate.quad(f, 0, np.pi)[0])))

import matplotlib.pyplot as plt
plt.plot(a_s, ints)
plt.xlabel('Value of a')
plt.ylabel('Error in integral value')
plt.show()

'''
As we can see, a = 1.04 minimises the error which is the same as a = e^pi/(e^pi - 1) = 1.045
'''