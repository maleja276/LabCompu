import numpy as np 
import matplotlib.pyplot as plt 


datos=np.loadtxt('/home/ubuntu/Downloads/food-texture.csv', dtype= float, delimiter= ",", skiprows= 1, usecols= (1,2,3,4,5))
datos_norm=np.ones((len(datos),5))

for j in range(0,5):

 	media=np.mean(datos[:,j])
	var=np.std(datos[:,j])

	for i in range(0,len(datos)):

		datos_norm[i][j]= (datos[i][j]-media)/var

#fig, medidas = plt.subplots(5, 1, figsize = (10, 10))

#medidas[0].hist(datos_norm[:,0])
#medidas[1].hist(datos_norm[:, 1])
#medidas[2].hist(datos_norm[:, 2])
#medidas[3].hist(datos_norm[:, 3])
#medidas[4].hist(datos_norm[:, 4])
#plt.show()

mat_cov=np.cov(datos_norm.T)

#sacar vectores y valores propios 


valores, vectores = np.linalg.eig(mat_cov)
ax = plt.axes()
x_line = np.linspace(-3,3)
#plt.scatter(datos_norm[:,0], datos_norm[:,1])

#plt.plot(x_line, x_line* (vectores[1,0]/vectores[0,0]), linewidth=5.0)
#plt.plot(x_line, x_line* (vectores[1,1]/vectores[0,1]), linewidth=5.0)



n_data=np.dot(vectores.T, datos_norm.T)
plt.scatter(n_data[0,:], n_data[1,:])
plt.show()



#Promedio varianza

h=[]

for i in range(0,len(mat_cov)):
	h.append(mat_cov[i,i])
	


#Porcentaje de valor propio

#p = (valores *100) / (np.mean(h))


