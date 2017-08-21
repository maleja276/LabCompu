import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 

s=10.0 
p=28.0
b=8.0/3.0
t=40.
dt=0.01
N=4000

x=np.ones(N)
y=np.ones(N)
z=np.ones(N)
x[0]=1
y[0]=1
z[0]=1

def funcion_1(x, y, z):

	return s*(y-x)

def funcion_2(x, y, z):
	
	return x*(p-z)-y

def funcion_3(x, y, z):
	
	return (x*y)-(b*z)

def euler():
	
	for i in range(1,N):

		x[i]=x[i-1]+(dt*funcion_1(x[i-1], y[i-1], z[i-1]))
		y[i]=y[i-1]+(dt*funcion_2(x[i-1], y[i-1], z[i-1]))
		z[i]=z[i-1]+(dt*funcion_3(x[i-1], y[i-1], z[i-1]))
	
	return x,y,z

plt.plot(euler()[0],euler()[1])
plt.savefig("Euler x-y ")
plt.close()

plt.plot(euler()[0],euler()[2])
plt.savefig("Euler x-z ")
plt.close()

plt.plot(euler()[1],euler()[2])
plt.savefig("Euler y-z ")
plt.close()

