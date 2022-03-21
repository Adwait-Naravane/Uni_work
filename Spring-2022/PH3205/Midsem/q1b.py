import numpy as np
from scipy import integrate

def f(x):
  return (x**(-1/4))*np.exp(-x)

def w(x):
  return (1 - 1/4)*(x**(-1/4))

def inv(x):
  #inverse of the cdf
  return x**(4/3)

N = 1000000

x = np.random.uniform(0,1, N)

p = inv(x)
#sampling
q = f(p)/w(p)
#Value of integral
print("Integral = ", np.mean(q))

print("Integral actual = {}, Variance = {}".format(integrate.quad(f, 0, 1)[0],integrate.quad(f, 0, 1)[1]))