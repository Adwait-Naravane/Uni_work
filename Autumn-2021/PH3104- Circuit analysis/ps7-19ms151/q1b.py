
import numpy as np
import matplotlib.pyplot as plt


a_R = 0.78
a_F = 0.97
I_ES = pow(10, -15)  
I_CS = (a_F/a_R) * I_ES
V_T = 0.026  
I_E = np.arange(0, 0.008, 0.001)  
V_BC = np.linspace(-1.2, 5, 1000)

def I_C(V_bc, I_e):
    return (1 - a_R * a_F) * I_CS * (np.exp(-V_bc / V_T) - 1) - a_F * I_e


x = V_BC
for i in I_E:
    y = I_C(x, i)
    plt.plot(x, -y, '-', label=f'I_E = {i * 1000} mA')
    plt.text(x[-1]-1.5, -0.00035-y[-1], '$I_E$ = ' + f'{i * pow(10, 3)} mA')
plt.ylim(-0.003, 0.007)
plt.xlabel('$V_{BC}$ (V)')
plt.ylabel('$I_C$ (A)')
plt.title('OUTPUT CHARACTERISTICS OF A PNP TRANSISTOR')
plt.savefig('q1b.png')
plt.show()