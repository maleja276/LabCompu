import numpy as np 
import matplotlib.pyplot as plt
import math

#Limites de la integral

a=0
b=2

#Funcion a integrar 

def funcion(x_1,x_2,x_3,x_4,x_5,x_6,x_7,x_8,x_9,x_10):

	y=(x_1+x_2+x_3+x_4+x_5+x_6+x_7+x_8+x_9+x_10)**3

	return(y)


#Numero de puntos entre el intervalo 

n=10000

#En este metodo de montecarlo se busca plantear una relacion entre la integra, el area y los puntos aleatorios que caen dentro y fuera del area del cuadrado 
#Cada variable de la integral esta compuesta de numeros aleatorios

def montecarlo(n):

	integ=[]
	puntos_debaj=0
	puntos_encima=0

	x_1= np.random.rand(int(n))*2
	x_2= np.random.rand(int(n))*2
	x_3= np.random.rand(int(n))*2
	x_4= np.random.rand(int(n))*2
	x_5= np.random.rand(int(n))*2
	x_6= np.random.rand(int(n))*2
	x_7= np.random.rand(int(n))*2
	x_8= np.random.rand(int(n))*2
	x_9= np.random.rand(int(n))*2
	x_10=np.random.rand(int(n))*2

	puntos= np.random.rand(int(n))*(20**3) #Rango de puntos

	for j in range(0,int(n)):

		fun_ev= funcion(x_1[j],x_2[j],x_3[j],x_4[j],x_5[j],x_6[j],x_7[j],x_8[j],x_9[j],x_10[j])

		if puntos[j] < fun_ev:

			puntos_debaj+=1

	integ= (puntos_debaj * ((2**10) *(20**3)))/len(puntos)

	return(integ)

#Repite 20 veces el metodo montecarlo y como resultado, toma el promedio 
def montecarlo20(n):

	integrales=[]

	for i in range (0,int(20)):

		montecarlo(n)
		integrales.append(montecarlo(n))

	return(int(np.mean(integrales)))
	



#Metodo para 13 N diferentes en potencias de 2 

z= np.linspace(1,13,13)	
N= 2 ** z
mont=[]



def montecarlo20_N(N):
	for i in N: 
		d=montecarlo20(i)
		mont.append(d)
	return(mont)	


#Grafica de la integral en funcion de los N utilizados

plt.plot(N, montecarlo20_N(N), color="green")
plt.semilogx()
plt.xlabel("N")
plt.ylabel("Integral")
plt.savefig("num_integral.pdf")
plt.close()

def error():

	x=montecarlo20_N(N)
	a=1126400.
	e=[]
	for i in range(0,13):
		e.append(abs(float(x[i])-a) / a)
	return(e)

#Grafica del error en funcion de 1/sqrt(N)
s=1./(N**0.5)
plt.plot(s,error(), color = "red")
plt.xlabel("1/(N**0.5)")
plt.ylabel("Error")
plt.savefig("err_integral.pdf")
plt.close()
	



	


	
		




	
