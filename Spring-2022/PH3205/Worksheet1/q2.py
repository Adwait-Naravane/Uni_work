import numpy as np
import matplotlib.pyplot as plt


f = lambda x,a,b: a + b*(x**2)

X = np.arange(0, 11, 1)
def derivative(f, a, b, h):
  g = lambda x, m, a, b : (m(x+h, a , b)-m(x, a, b))/h   
  return np.array([g(x,f, a, b) for x in X])

''' df/ dx = 2x ''' 
#take a, b = 1

derivs = [derivative(f, 1, 1, 0.000001*i) for i in range(20)]
deriv_exact = derivative(f, 1, 1, 0.0000001)
#differences
hs = [0.000001*i for i in range(20)]
#error
errors = [np.abs(np.mean((d - deriv_exact)/deriv_exact)) for d in derivs]
'''
plt.plot(hs, errors)
plt.xlabel("difference (h)")
plt.ylabel("Error")
'''
#Q2
def derivative_3(f, a, b , h): 
  g = lambda x, m, a, b : (m(x+h, a , b)-m(x-h, a, b))/(2*h)   
  return np.array([g(x,f, a, b) for x in X])

derivs_3 = [derivative_3(f, 1, 1, 0.00001*i) for i in range(20)]
deriv_exact_3 = derivative_3(f, 1, 1, 0.00001)
#differences
hs = [0.00001*i for i in range(20)]
#error
errors_3 = [np.abs(np.mean(d - deriv_exact_3)/np.mean(deriv_exact_3)) for d in derivs_3]


plt.plot(hs, errors_3)
plt.xlabel("difference (h)")
plt.ylabel("Error")
plt.show()

#This is negligible


