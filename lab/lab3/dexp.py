import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import expon
from scipy.stats import norm

#funcion expon.fit
#funcion numpy.random.exponential: numero aleatorios para la funcion exponencial escala = 1/lamda, size es el numero de datos o numeros aleatorios

lista= np.random.exponential(scale= 0.1, size=1000)
#plt.hist(lista, bins= 100, normed=True)
#plt.show()

# m es la media y debe ser igual a la escala
#fit= tendencia de numeros (Linea), mirar a que distribucion pertenece

sig, m = expon.fit(lista)

x=np.linspace(0,1,100)
y= expon.pdf(x, scale=m)
#plt.plot(x,y, color = "r")
#plt.show()

lg=[]
i=1

#lista con suma de los datos de una lista de 1000 datos 
while True:
	if i > 1000:
		break 
	else:
 
		lista= np.random.exponential(scale= 0.1, size=1000)
		lg.append(np.sum(np.array(lista)))
		i+=1

plt.hist(lg, bins=100, normed = True)
#fit de una funcion normal s = desviacion m = media 
s, m = norm.fit(lg)

#Variable aleatoria de numeros 
x= np.linspace(80,130,100)

#funcion de probabilidad (pdf)
y= norm.pdf(x, s, m)
plt.plot(x,y, color="r")
plt.show()

