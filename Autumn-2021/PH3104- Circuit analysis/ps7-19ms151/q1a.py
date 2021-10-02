import numpy as np
import matplotlib.pyplot as plt

a_R = 0.78
a_F = 0.97
I_ES = pow(10, -15)
I_CS = (a_F/a_R) * I_ES
V_T = 0.026
V_CB = [ 1,10, 20]
V_EB = np.linspace(0.1, 1, 100)

def I_E(V_eb, V_cb):
    return I_ES * (np.exp(V_eb / V_T) - 1) - a_R * I_CS * (np.exp(-V_cb / V_T) - 1)


x = V_EB
for i in V_CB:    
    plt.plot(x, I_E(x,i), '-', label=f'V_CB = {i} V')
plt.xlabel('$V_{EB}$ (V)')
plt.ylabel('$I_E$ (A)')
plt.title('Input characteristics of pnp transistor')
plt.legend()
plt.show()
plt.savefig('q1.png')