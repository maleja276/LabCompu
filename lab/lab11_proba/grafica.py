import numpy as np 
import matplotlib.pyplot as plt 

datos= np.genfromtxt('datos.txt')

t=datos[:,0]
N=datos[:,1]

plt.plot(t,N)
plt.show()
