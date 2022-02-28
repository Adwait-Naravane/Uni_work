import numpy as np
from scipy import integrate

#l is the limit of integration, integrals are from 0 to l. 
l = np.pi

#The value of 'a' is fixed at below. It is obtained by normalising p(y) from 0 to l.
a = np.exp(l)/(np.exp(l)- 1)

def f(x):
  return 1/(x**2 + np.cos(x)**2)

def w(x,a = a):
  return a*np.exp(-x)

def inv(x,a = a):
  #inverse of the cdf
  return np.log(np.abs(a/(a-x)))

N = 1000000

#As x is the cdf, it can only be between 0 to 1
x = np.random.uniform(0,1, N)

p = inv(x)

q = f(p)/w(p)
#Value of integral
print("Integral = ", np.mean(q))

#Actual value below
print("Integral actual = {}, Variance = {}".format(integrate.quad(f, 0, l)[0],integrate.quad(f, 0, l)[1]))