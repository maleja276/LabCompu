import numpy as np 
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fft2, ifft, ifft2
import matplotlib.cm as cm
import matplotlib.mlab as mlab

datos=plt.imread('moonlanding.png')

fft = np.fft.fft2(datos)

freq= np.fft.fftfreq(len(datos), 1)

#Quitar las frecuencias


for i in range(50,len(datos)-50):

	freq[i]=0


#Transformada inversa de las frecuencias para especto

inversa= np.fft.ifft(freq)



#Imagen original 


plt.imshow(datos, cmap=cm.Greys)
plt.savefig("imagenoriginal.png")
plt.close()


#Power spectrum image original

imagtf=abs(fft)**2

img=plt.imshow(imagtf,cmap=cm.Blues )

imagtf_cut = 95.0

clipped_imagtf = mlab.prctile(imagtf.flatten(), imagtf_cut)

img.set_clim(0, clipped_imagtf)


plt.savefig("powerspectrum_1.png")
plt.close()














