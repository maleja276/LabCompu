import numpy as np 
import matplotlib.pyplot as plt
#Ecuaciones diferenciales parciales

N=1000
x = np.linspace(0.0,1.0,N)
c=1.0
dt=0.0005
dx=x[1]-x[0]



#def funcion():

u= np.exp(-((x-0.3)**2/(0.01)))
#	return u 

u_inicial = u
u_inicial[0]=0.0
u_inicial[-1]=0.0

u_futuro=np.ones(N)
u_futuro[0]=0.0
u_futuro[-1]=0.0

		
alp=(dt/dx)**2


for i in range(N-1):

	u_futuro[i]=(alp/2*(u_inicial[i+1]-2*u_inicial[i]+u_inicial[i-1]))+u_inicial[i]

	

u_pas= u_inicial.copy()

u_pres= u_futuro.copy()

t=350

for i in range(t):

	for j in range(1,N-1):

		u_futuro[j]=(2*(1-(alp**2))*u_pres[j])-u_pas[j]+(((alp**2))*(u_pres[j+1]+u_pres[j-1]))
	
		
	
	u_pas=u_pres.copy()
	u_pres=u_futuro.copy()

plt.plot(x, u_inicial)
plt.plot(x, u_futuro)
plt.ylabel("U")
plt.xlabel("X")
plt.show()



	


