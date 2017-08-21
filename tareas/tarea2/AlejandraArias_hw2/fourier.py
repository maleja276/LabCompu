import numpy as np 
import matplotlib.pyplot as plt
import math 
import scipy.io.wavfile as waves
from scipy.fftpack import fft, fftfreq, ifft

#Lectura de archivos con scipy.io 

freq_do=260.
freq_sol=391.

sr_do, do= waves.read('Do.wav')
sr_sol, sol= waves.read('Sol.wav')

#Transformada discreta de fourier

def transformada(y):
	
	N=len(y)

	trans=np.ones(N, dtype= complex )

	for n in range(0,N):

		t=0

		for k in range(0,N):

			t += y[k]*np.exp(-2*np.pi*(1j)*k*(float(n)/N))

		trans[n]=t
		

	return trans

def frecuencia(y,sr):

	N=len(y)
	
	dt=1./sr

	return np.fft.fftfreq(N,dt)

#Filtro para quitar la maxima amplitud.
 

def filtro(y,sr):
	
	#Datos de amplitud
	trs_flt=transformada(y).copy()
	
	#Datos de frecuencia
	freq=frecuencia(y,sr).copy()
	
	#Punto maxima amplitud 1 
	p1_max=trs_flt.argmax()
	
	#frecuencia de amplitud maxima
	f_1=freq[p1_max]
	
	#Buscar el segudo punto, frecuencia maxima valor negativo
	#Se toma unicamente el primer valor de la tupla

	p2_max= np.where(freq==-f_1)[0]

	#Quitar un rango de posiciones

	trs_flt[p1_max - 15 : p1_max + 15]=0

	trs_flt[p2_max - 15 : p2_max + 15]=0

	#Retorna nuevas amplitudes

	return trs_flt



#Filtro de bajos con frecuencia < 1000.

def f_bajos(y,sr):

	freq_bajos=frecuencia(y,sr)
	
	trans_fb=transformada(y).copy()

	a=np.where(abs(freq_bajos)>1000)

	trans_fb[a]=0

	return trans_fb


#Figura espacios de frecuencias Do.

fig, cuadros = plt.subplots(3,1, figsize=(10,10))
fig.suptitle("ESPACIO DE FRECUENCIAS DO", fontsize=16)

fig.text(0.5, 0.01, 'Frecuencia', ha='center')
fig.text(0.01, 0.5, '|Amplitud|', va='center', rotation='vertical')

cuadros[0].plot(frecuencia(do,sr_do), abs(transformada(do)), 
label="Datos originales", color="blue")

cuadros[1].plot(frecuencia(do,sr_do), abs(filtro(do,sr_do)), label="F. maxima amplitud", color="purple")

cuadros[2].plot(frecuencia(do,sr_do), abs(f_bajos(do,sr_do)), label="Filtro pasa bajos", color="magenta")

cuadros[0].legend()
cuadros[1].legend()
cuadros[2].legend()

plt.savefig("DoFiltros.pdf")
plt.close()

#Cambio de frecuencia artificialmente para DO 
#Sample rate para sacar artificialmente la frecuencia de do

sr_don= int(sr_do * 391./260.)

#Grafica Do-Sol con el cambio de frecuencia de 2 

plt.figure(figsize=(10,10))
plt.plot(frecuencia(do, sr_don), abs(transformada(do)), label="Do.", color="red")
plt.plot(frecuencia(sol, sr_sol), abs(transformada(sol)), label="Sol.")
plt.title("Espacio de frecuencias DO - SOL ")
plt.xlabel("Frecuencia")
plt.ylabel("|Amplitud|")
plt.legend()
plt.savefig("DoSol.pdf")
plt.close()


#Transformada de filtro,

it_filtro = np.fft.ifft(filtro(do, sr_do))
do_filtro = it_filtro.real #Parte real de la ifft
do_filtro.astype(np.float32) #Se necesita cambiar el tipo de dato para escribir el archivo de audio 

waves.write("Do_pico.wav", sr_do, do_filtro)

#Transformada de bajos y archivo de sonido 

it_bajos = np.fft.ifft(f_bajos(do, sr_do))
do_bajos = it_bajos.real
do_bajos.astype(np.float32)

waves.write("Do_pasabajos.wav", sr_do, do_bajos)

#Do modificado datos 

it_DoSol = np.fft.ifft(transformada(do))
do_sol = it_DoSol.real
do_sol.astype(np.float32)

waves.write("DoSol.wav", sr_don, do_sol)






