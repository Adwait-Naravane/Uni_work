import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st 



N=100000  
mu=2    
std=2    

def A(x1,x):

    p_x1 = st.norm.pdf(x1,loc = mu,scale = std) 
    p_x = st.norm.pdf(x,loc = mu,scale = std)
    cc = np.amin([1, p_x1/p_x])

    return cc


def metro(N):
  x=[0]   
  for i in range(N):
      epsilon = np.random.uniform(-3,3) 
      x1=x[i-1] + epsilon    
      u=np.random.uniform(0,1)
      if u <= A(x1,x[i-1]): 
          x.append(x1)    
      else: 
          x.append(x[i-1])
  return np.array(x)


plt.hist(metro(N), bins='auto', density=True)



xk = np.linspace(mu - 4*std, mu + 4*std, 100)
plt.plot(xk, st.norm.pdf(xk, mu, std), color='green')



plt.ylabel('frequency')
plt.xlabel('X')
plt.show()