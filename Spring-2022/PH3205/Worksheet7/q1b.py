from q1a import *

Ns = np.arange(10, 1000, 1)
dts = (T-t_0)/Ns

rmss = []
for N in Ns:
  t, SX, SY = BlackScholes(N, num_sims, T)
  rmss.append(np.sqrt(np.mean((SX - SY)**2)))
  #Rms error above

plt.scatter(dts, rmss, s= 1)
#plt.plot(dts, rmss, linewidth = 0.5)
plt.xlabel('dt')
plt.ylabel('RMS error')
plt.xscale('log')
plt.show()