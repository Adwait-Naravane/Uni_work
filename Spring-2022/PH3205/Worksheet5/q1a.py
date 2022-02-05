
import numpy as np
import matplotlib.pyplot as plt 
'''
#1A 
'''

def normal(mean = 0, std = 1, N = 100000):
  t = np.random.uniform(0,1,(N))
  p = np.random.uniform(0,1,(N))
  X = np.sqrt(-2*np.log(p))*np.cos(2*np.pi*t)
  Y = np.sqrt(-2*np.log(p))*np.sin(2*np.pi*t)
  new = np.concatenate((X,Y), axis = 0)

  new_gen = mean + new*(np.sqrt(std))
  return new_gen

if __name__ == "__main__":  
    y = normal()
    x = np.arange(-4,4,0.01)
    f = (1/(2*np.pi)**0.5)*np.exp(-(x**2)/2)
    plt.hist(y, bins = 200, density = True)
    plt.plot(x,f)
    plt.xlabel('value')
    plt.ylabel('density')
    plt.title('WKST 5 | 1.A')
    plt.grid()
    plt.show()