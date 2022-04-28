import numpy as np
import matplotlib.pyplot as plt

L = 1

f = lambda x,y,z: y**2 + np.cos(2*np.pi*x) - np.sin(np.pi*x)**4 + z - z


def rk4(initial, dx, a, b):
  t = np.arange(a,b, dx)
  x = []
  x.append(initial)
  for i in range(len(t)-1):
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
  return t, x

y0 = 0
yL = 0

def func(guess):
  initial = np.array([y0, guess])
  t, stuff = rk4(initial, 0.001, 0, L)
  position = [stuff[i][0] for i in range(len(stuff))]
  return position[-1]

def bisection(a,b):
 
    if (func(a) * func(b) >= 0):
        print("You have not assumed right a and b\n")
        return
  
    c = a
    while (abs(b-a) >= 0.001):
 
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
#print('There are actually 2 solutions , 0.18 and -33.57. This is one of them')
best_guess = bisection(-40,-30)
print(best_guess)

initial = np.array([y0, best_guess])
t, stuff = rk4(initial, 0.001, 0, L)
position = [stuff[i][0] for i in range(len(stuff))]

#t = np.arange(0,L+0.001, 0.001)
plt.plot(t, position)
plt.xlabel('x')
plt.title("best guess plot")
plt.ylabel('y')
plt.savefig('non_linear.png')
plt.show()

'''
#To display those two solutions, you can see the curve crosses 0 two times. 
guesses = np.arange(-100, 10, 1)
poslast = [func(guess) for guess in guesses]
plt.plot(guesses, poslast)
plt.xlabel('derivative at x = 0')
plt.ylabel('y(1)')
plt.grid()
plt.show()
'''