import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm

datos= np.loadtxt("datos_CAMINATA.txt")

plt.hist(datos[0], bins=10, normed = True)
plt.savefig("binomial.png")
plt.close()

pasos=[]
i=0
while True:
	if i > (len(datos)-1):
		break 
	else:
		pasos.append(np.sum(np.array(datos[i])))
		i+=1


#loc=media scale=desviacion
loc, scale = norm.fit(pasos)

x=np.linspace(3300, 3700, 100)
y=norm.pdf(x, loc, scale)
plt.hist(pasos, bins=100, normed= True)
plt.plot(x,y, color = "r")
plt.savefig("normal.png")
plt.close()
#De acuerdo con el teorema central miu_o*M = miu miu_0= miu / M

N= 10
M=1000
miu0= loc/M

#m miu= N*p
p=miu0/(N)

print("La probabilidad de sacar una cara con esta moneda es: %s " % p)


