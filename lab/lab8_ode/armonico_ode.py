import numpy as np 
import matplotlib.pyplot as plt 

k=42.
g=9.8
m=0.25
mu=0.15

N=5000

tt=4.

dt=4./N

x=np.zeros(N) #y1 posicion 
v=np.ones(N) #y2 funcion prima 1 velocidad
a=np.ones(N) #funcion prima 2 aceleracion 

t=np.linspace(0,4.,5000)

x[0]=0.2
v[0]=0.0



def funcion_prime(t,x,v):
	return v

def funcion_prime2(x,v):

	if v>0:

	 	a=-k/m*x - (mu * m * g)

	elif v==0:

		a=-k/m*x

	else:	

		a=-k/m*x + (mu * m * g)

	return a

for i in range(1,N):

	#y1_prima= funcion_prime(t[i-1],x[i-1],v[i-1])
	#y2_prima= funcion_prime2(t[i-1],x[i-1],v[i-1])

	
	x[i]=x[i-1]+dt*v[i-1]
	v[i]=v[i-1]+dt*funcion_prime2(x[i-1],v[i-1])
	
	

plt.plot(v)
plt.show()
