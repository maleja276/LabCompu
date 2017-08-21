import numpy as np 
import matplotlib.pyplot as plt 

datos = np.genfromtxt('plots.txt')

x=datos[range(0,100),0]
y=datos[range(0,100),1]

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('U(x,0)')
plt.ylim(0.0, 2.1)
plt.title("CONDICION INICIAL")
plt.savefig("inicial.pdf")
plt.close()

a=datos[range(100,198),0]
b=datos[range(100,198),1]

plt.plot(a,b)
plt.xlabel('x')
plt.ylabel('U(x)')
plt.ylim(0.0, 2.1)
plt.title("ECUACION DE DIFUSION")
plt.savefig("difusion.pdf")
plt.close()
