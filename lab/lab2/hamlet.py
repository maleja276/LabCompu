import sys

infile = open('pg1524.txt', 'r')
lineas = infile.readlines()
#lineas es un arreglo 

palabras = []

for i in lineas:
	palabras.extend(i.split()) 

n=0
m=input("Inserte el numero de letras")
for b in palabras:

	if len(b)==m:
		n=n+1
	
print(n)
