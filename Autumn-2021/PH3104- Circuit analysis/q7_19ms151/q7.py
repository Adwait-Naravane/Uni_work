import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

def amp(Q, w):
    wo = 2 * np.pi * 1800.
    return 1 / np.sqrt(1 + (Q ** 2) * ((w / wo) - (wo / w)) ** 2)


def phase(Q, w):
    wo = 2 * np.pi * 1800.
    return np.arctan(Q * ((wo / w) - (w / wo)))


def output(Q, N, w, time):  
    w = 2 * np.pi * w
    sig = np.zeros_like(time)
    for i in range(len(time)):
      k = 2* np.array(range(N)) + 1
      sig[i] = np.sum(amp(Q, k * w) * (4 / (k * np.pi)) * np.sin(w * k * time[i] + phase(Q, k * w)))
    return sig
#wish I could vectorise more

f = [2000, 1800, 1600, 900, 450, 200]
qf = [5, 1]
a, b = 0, 0
t = np.linspace(0, 8/f[b], 1000)  
output = output(qf[a], 1000, f[b], t)
plt.title(f"Q = {qf[a]} & $\omega$ = {f[b]} Hz")
plt.xlabel('time (s)')
plt.ylabel(r'$\frac{{V_0}}{{V_i}}$', fontsize = 15)

plt.plot(t, output)
plt.show()