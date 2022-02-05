from q1a import *


'''
#1.B
'''
mu = 0
sigma = 1
for i in range(4):
    plt.figure(i+1)
    mu = i
    sigma = sigma + i

    y = normal(mean = mu, std = sigma)
    x = np.arange(-10,10,0.01)
    f = (1/((sigma*2*np.pi)**0.5))*np.exp(-(((x-mu))**2)/(2*sigma))
    plt.hist(y, bins = 200, density = True)
    plt.plot(x,f)
    plt.xlabel('value')
    plt.ylabel('density')
    plt.title('WKST5 | 1b |')
    plt.grid()
    plt.show()