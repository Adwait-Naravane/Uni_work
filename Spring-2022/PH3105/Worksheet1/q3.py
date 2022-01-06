import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.exp(x)
X = np.arange(0, 11, 1)

def second_der(f, h):
  g = lambda x, m: (m(x+h)+m(x-h)-2*m(x))/(h**2)
  return np.array([g(x,f) for x in X])

derivssecond = [second_der(f, 10**(-1-i)) for i in range(6)]
hs = ["h = 10^({})".format(-i-1) for i in range(6)]
table = {}
for i in range(6):
  table[hs[i]] = derivssecond[i]

second_der_exact = np.exp(X)

table["exact"] = second_der_exact 

df = pd.DataFrame(table)

#List

print(df)

errors_her = [np.abs(np.sum((second_der_exact - m)/second_der_exact)) for m in derivssecond]
#print("errors for second der: ")
#print(errors_her)
#This gives h = 10^(-4) as least error

errors_her = [np.log(np.abs(np.sum((second_der_exact - m)/second_der_exact))) for m in derivssecond]
plt.plot(range(1,7), errors_her)
plt.xlabel("exponent of h")
plt.ylabel("log error")
plt.show()
