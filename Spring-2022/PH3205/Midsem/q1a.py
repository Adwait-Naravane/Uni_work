import numpy as np
import matplotlib.pyplot as plt

def w(x):
  return (1 - 1/4)*(x**(-1/4))

def inv(N):
  x = np.random.uniform(0,1,N)
  return x**(4/3)

hists, bins, ignore = plt.hist(inv(1000000), bins = 500, density = True)
bins = (bins[1:] + bins[:1])
plt.plot(bins, w(bins))
plt.xlabel('val')
plt.ylabel('freq')
#plt.xscale('log')
#plt.yscale('log')
plt.show()