import numpy as np

import matplotlib.pyplot as plt

#limites del cuadrado de 2 nm centrados en el origen.

n=int(50)
b= 1.
a= -1.

class Cuadrado:
	
	k = (8.987 * (10**9))*(10**9)**3 * ((1/(1.602176 * 10**(-19)))**-2)
	
	vx=np.linspace(a,b,n)
	vy=np.linspace(a,b,n)
	
	#Matriz que define todos los puntos del potencial 

	xp, yp = np.meshgrid(vx, vy)
	
	def __init__ (self, q0, x0, y0):
	
		self.x= x0
		self.y= y0
		self.q= q0

	def distancia(self):


		#Pitagoras para hallar todos los puntos 
		self.r = ((Cuadrado.xp - self.x )**2 + (Cuadrado.yp - self.y)**2)**0.5

		return(self.r)

	def constantes(self):

		self.C =(Cuadrado.k * self.q)
		return(self.C)


#Inicializacion de las cargas
	
q1=Cuadrado(1., 0.5, 0.5)

q2=Cuadrado(-1., -0.5, 0.5)

q3=Cuadrado(1., -0.5, -0.5)

q4=Cuadrado(-1., 0.5, -0.5)

#Operar simplemente las matrices para que me de la matriz de r y asi sacar el potencial el todos los puntos 

def potencial1():

	return (q1.constantes()*(1/q1.distancia()))

def potencial2():
	
	return(q2.constantes()*(1/q2.distancia()))

def potencial3():
	
	return(q3.constantes()*(1/q3.distancia()))

def potencial4():
	
	return(q4.constantes()*(1/q4.distancia()))

#Suma del potencial que generan todas las cargas
def potencialtot():

	return(potencial1()+potencial2()+potencial3()+potencial4())

#Grafica potecial 

plt.imshow(potencialtot(), extent=(q1.xp.min(), q1.xp.max(), q1.yp.min(), q1.yp.max()))
plt.colorbar()

#gradiente negativo del potencial es el campo electrico, central difference
# [y(t+h/2)-y(t-h/2)]/ h

def difx():

	h=(b-a)/(n-1.)
	campe=np.ones((n,n))

	for i in range(0,int(n)):

		for j in range (0,int(n)):

			d=0
			
			if j == 0:

				#Foward difference 

				d= ((potencialtot()[i+h][j])-(potencialtot()[i][j]))/ h

				campe[i][j]= d

			if j == n:
				#Back Differe
				d= ((potencialtot()[i][j])-(potencialtot()[i-h][j]))/ h
				campe[i][j]= d

			

			else:
			
				d= ((potencialtot()[i+(h/2)][j])-(potencialtot()[i-(h/2)][j]))/ h

				campe[i][j]= d

			#Central Dife
	return(-campe)



		
def dify():

	h=(b-a)/(n-1.)
	campey=np.ones((n,n))

	for j in range(0, int(n)):

		for i in range (0, int(n)):
			d=0
			
			if i == 0:

				d= ((potencialtot()[i][j+h])-(potencialtot()[i][j]))/h

				campey[i][j]= d

			#Foward difference 
			if i == n:

				d= ((potencialtot()[i][j])-(potencialtot()[i][j-h]))/h
				campey[i][j]= d

			#Back Differe

			else:
			
				d= ((potencialtot()[i][j+(h/2)])-(potencialtot()[i][j-(h/2)]))/h
			
				campey[i][j]= d

			#Central Dife
	return(-campey)

vx=np.linspace(a,b,n)

vy=np.linspace(a,b,n)

xp, yp = np.meshgrid(vx, vy)	

ex= difx()

ye= dify()


def dif():
	return((difx()+dify()))

#Grafica campo electrico
plt.streamplot(xp, yp, ex, ye)
plt.axis([-1,1,-1,1])
plt.title("Potencial y Campo electrico")
plt.savefig("cargas.pdf")
plt.close()
