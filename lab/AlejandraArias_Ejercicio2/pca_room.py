import numpy as np 
import matplotlib.pyplot as plt

datos= np.loadtxt('room-temperature.csv',dtype= float, delimiter= ",", skiprows= 1, usecols= (1,2,3,4,))

fig, esquinas = plt.subplots(4, 1, figsize = (10, 10))



esquinas[0].plot(datos[:,0], label="Front left")

esquinas[1].plot(datos[:,1], label="Front Right")

esquinas[2].plot(datos[:,2], label="Back Left")

esquinas[3].plot(datos[:,3], label="Back right")

esquinas[0].set_title("Temperaturas")
esquinas[0].legend()
esquinas[1].legend()
esquinas[2].legend()
esquinas[3].legend()


plt.savefig("temp.png")
plt.close()

dat_norm=np.ones((len(datos),4))
for j in range(0,4):
	media= np.mean(datos[:,j])
	varianza= np.std(datos[:,j])
	for i in range(0,len(datos)):
		dat_norm[i,j]= (datos[i,j]-media)/varianza
	
mat_cov=np.cov(dat_norm.T)
print(mat_cov)

valores, vectores = np.linalg.eig(mat_cov)


print("La primera componente principal es "+ str(vectores[0]) + " con un valor de %f " % valores[0])

print("La segunda componente principal es "+ str(vectores[1]) + " con un valor de %f " % valores[1])

pval=0
for i in range(0,len(valores)):
	pval+= valores[i]


print("La primera componente principal explica el " + str((valores[0]*100)/pval)+ "% de la varianza")

print("La segunda componente principal explica el " + str((valores[1]*100)/pval)+ "% de la varianza")

x_line= np.linspace(-3,3)

plt.scatter(dat_norm[:,0],dat_norm[:,1])
plt.plot(x_line, x_line* vectores[1,0]/vectores[0,0])
plt.plot(x_line, x_line* vectores[1,1]/vectores[0,1])
plt.xlabel("Front Left")
plt.ylabel("Front Right")
plt.title("Front Right vs Front Left")
plt.legend(('vector 1', 'vector 2'))
plt.savefig("pca_fr_fl.pdf")
plt.close()


plt.scatter(dat_norm[:,0],dat_norm[:,2])
plt.plot(x_line, x_line* vectores[2,0]/vectores[0,0])
plt.plot(x_line, x_line* vectores[2,1]/vectores[0,1])
plt.title("Back Left vs Front Left")
plt.legend(('vector 1', 'vector 2'))
plt.xlabel("Front Left")
plt.ylabel("Back Left")
plt.savefig("pca_bl_fl.pdf")
plt.close()



	
