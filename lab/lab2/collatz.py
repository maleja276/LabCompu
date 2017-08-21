#si es par : dividir entre 2
#si es impar: numero*3 + 1
import sys 

#Convertir un string a un entero
#Sys funciona como una lista de lo que se escribe en la terminal 
#Metodo 1 y 2, para que funcione hay que borrar 1 de los dos 

a = int(sys.argv[1])
numeros= [a]


while True:
	if a % 2 ==0:
		a=a/2
		numeros.append(a)

	elif a==1:
		 break 
	else: 
		a=(a*3)+1
		numeros.append(a)
	

print("La serie de Collatz es %s" % numeros)

a = input("Numero:")
numeros= [a]


while True:
	if a % 2 ==0:
		a=a/2
		numeros.append(a)

	elif a==1:
		 break 
	else: 
		a=(a*3)+1
		numeros.append(a)
	

print("La serie de Collatz es %s" % numeros)
