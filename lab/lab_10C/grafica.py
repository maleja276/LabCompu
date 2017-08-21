import numpy as np 
import matplotlib.pyplot as plt

datos =np.genfromtxt('datos.txt')

plt.plot(datos[:,1])
plt.show()
