import numpy as np
import matplotlib.pyplot as plt
E = 200* (10**(9))
I = 30000 * ((1/100)**4)
w = 1500000
L = 3

f = lambda t,x,z: ((w*L)/(2*E*I)) * t - ((w)/(2*E*I)) * (t**2)


def rk4(initial, dx, a, b):
  t = np.arange(a,b, dx)
  x = []
  x.append(initial)
  for i in range(len(t)):
    k1 = x[i][1]
    l1 = f(t[i], x[i][0], x[i][1])   
    k2 = k1 + l1*dx/2
    l2 = f(t[i], x[i][0] + k1*dx/2, x[i][1] + l1*dx/2)
    k3 = k1 + l2*dx/2
    l3 = f(t[i], x[i][0] + k2*dx/2, x[i][1] + l2*dx/2)
    k4 = k1 + l3*dx
    l4 = f(t[i], x[i][0] + k3*dx, x[i][1] + l3*dx)
    y = x[i][0] + (1/6)*dx*(k1 + 2*(k2 + k3) + k4)
    z = x[i][1] + (1/6)*dx*(l1 + 2*(l2 + l3) + l4)
    x.append(np.array([y,z]))
  return x

y0 = 0
yL = 0

def func(guess):
  initial = np.array([y0, guess])
  stuff = rk4(initial, 0.0001, 0, L)
  position = [stuff[i][0] for i in range(len(stuff))]
  return position[-1]

def bisection(a,b):
 
    if (func(a) * func(b) >= 0):
        print("You have not assumed right a and b\n")
        return
  
    c = a
    while (abs(b-a) >= 0.00001):
 
        # Find middle point
        c = (a+b)/2
  
        # Check if middle point is root
        if (func(c) == 0.0):
            break
  
        # Decide the side to repeat the steps
        if (func(c)*func(a) < 0):
            b = c
        else:
            a = c
             
    return c

best_guess = bisection(0,-0.1)
print(best_guess)

initial = np.array([y0, best_guess])
stuff = rk4(initial, 0.0001, 0, L)
position = [stuff[i][0] for i in range(len(stuff))]

t = np.arange(0,L+0.0001, 0.0001)
plt.plot(t, position)
plt.xlabel('x')
plt.title("best guess plot")
plt.ylabel('y')
plt.show()
