import numpy as np 

N=10000.
h=0.
a=0.
b=np.pi

#Numeros en un intervalo a y b con N numeros
x=np.linspace(a, b, num=N)

def mifuncion(x):

	y = (np.cos(x)**2) + (np.sin(x)**2)

	return (y)

#intervalos
intervalo= []
def integrar():

	h = (b-a)/(N-1)
	intervalo= h * mifuncion(x)

	integ= np.sum(intervalo[1:-1]) + h/2*  mifuncion(x[0])+ h/2 * mifuncion (x[-1])
	

	return (integ)

print integrar()

