import numpy as np 
import matplotlib.pyplot as plt

#lectura de datos y de dos filas que estan corridas

datos= np.genfromtxt('DatosBancoMundial5.csv', dtype= float, delimiter=",", skip_header=1, usecols= range(4,227))

datos_2 =np.genfromtxt('DatosBancoMundial5.csv', dtype= float, delimiter=",", skip_header=3, skip_footer=1, usecols= range(5,228))


datos[2,:]=datos_2[0,:]
datos[3,:]=datos_2[1,:]

#Transpuesta de los datos para aplicar la covarianza segun mi metodo

paises = datos.T


#Variables

N=223

variables=5

normalizados= np.ones((len(paises),variables))


#Normalizacion de los datos


for j in range(0,variables):
	
	media= np.mean(paises[:,j])
	var= np.std(paises[:,j])

	for i in range(0,len(paises)):

		normalizados[i][j]= (paises[i][j]-media) / var


#Grafica Exploracion datos


fig, cuadros = plt.subplots(5,1, figsize= (10,10))

cuadros[0].plot(normalizados[:,0], label = "Tax rate")
cuadros[1].plot(normalizados[:,1], label = "Cost of business")
cuadros[2].plot(normalizados[:,2], label = "Unemployment Female")
cuadros[3].plot(normalizados[:,3], label = "Unemployment Male")
cuadros[4].plot(normalizados[:,4], label = "Ratio of female to male")

fig.text(0.5, 0.07, 'PAISES', ha='center',fontsize=16)

fig.text(0.07, 0.5, 'VARIABLES', va='center', rotation='vertical',fontsize=16)

fig.suptitle("EXPLORACION DE DATOS", fontsize=16)

cuadros[0].legend()
cuadros[1].legend()
cuadros[2].legend()
cuadros[3].legend()
cuadros[4].legend()


plt.savefig("ExploracionDatos.pdf")
plt.close()

#Matriz de covarianza, Formula = (dato_i_k - media_i)*(dato_j_k - media_j) / N-1

cova= np.ones((5,5))

for i in range(0,5):

	for j in range(0,5):

		data=[]

		for k in range(0,len(normalizados)):
			
			data.append((normalizados[k][i]-np.mean(normalizados[:,i]))*(normalizados[k][j]-np.mean(normalizados[:,j])) / (len(normalizados)-1))
	
		cova[i][j] = np.sum(data)


#Valores y vectores propios 

valores, vectores = np.linalg.eig(cova)


print "El primer componente principal es:\n " + str(vectores[:,0]) +"\n"
print "La segunda componente principal es:\n " + str(vectores[:,1]) + "\n"


#Graficar en el nuevo sistema de coordenadas

datos_n= np.dot(vectores.T, normalizados.T)
plt.scatter(datos_n[0,:],datos_n[1,:], color="purple")
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title("PCA DATOS")
plt.savefig("PCAdatos.pdf")
plt.close()


#PCA variables 

plt.scatter(vectores[0,0], vectores[0,1], color="red")

plt.scatter(vectores[1,0], vectores[1,1], color="green")

plt.scatter(vectores[2,0], vectores[2,1], color="blue")

plt.scatter(vectores[3,0], vectores[3,1], color="purple")

plt.scatter(vectores[4,0], vectores[4,1], color="brown")

plt.legend(labels= ("Total tax rate (%)","Cost of business (%)","Unemployment Female(%)","Unemployment Male(%)","Ratio(%)"), loc= 1 , title= "Componentes", fontsize=12)

plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCA AGRUPACION DE VARIABLES')

plt.savefig("PCAvariables.pdf")
plt.close()

#Variables correlacionadas


print "Las variables que estan correlacionadas son: \n " + "Grupo 1: "+ "Total tax rate (%) - Cost of business (%)\n" + "Grupo 2: "+ "Unemployment Female(%) - Employment Female(%)\n" 			
 
