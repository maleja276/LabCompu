import numpy as np 
import matplotlib.pyplot as plt

c=1.0
n=80
x=np.linspace(0,2.0, 80)
dt=0.001
iteraciones=350

u_inicial=x
u_futuro=np.zeros(n)
u_presente=np.zeros(n)
u_pasado=np.zeros(n)

for i in range (n):

	if (u_inicial[i]>0.5 and u_inicial[i]<1.5):
		u_inicial[i]=2
	else:
		u_inicial[i]=0

for k in range(iteraciones):

	for i in range(n):
		
		u_futuro[i]=u_inicial[i]-dt*u_inicial[]

	u_presente= u_futuro.copy()
	u_pasado=
