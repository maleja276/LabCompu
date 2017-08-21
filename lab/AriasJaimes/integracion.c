#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

/*Escriba un script en C llamado integracion.c que calcule la integral de la funcion e−x en el intervalo [0,1]. Debe guardar el resultado en un archivo de texto llamado resultados.txt con el siguiente formato:
El valor de la integral es: valor encontrado*/


double funcion (double x);
double integral (int n);

int main(void){

FILE *datos;

datos= fopen("resultados.txt", "a");

double x= integral(180);

fprintf(datos, "El resultado de la integral es: %f\n", x);

fclose(datos);

}

double funcion(double x){
	
	return exp(-x);
}

double integral(int n){

	srand(time(NULL));
	int i;
	int p_debajo=0;
	double p;
	double x;
	double f_ev;

	for (i=0; i< n; i++){
	
		x = drand48(); //Numeros aleatorios de 0 a uno para la integral 
		f_ev=funcion(x);
		p = drand48(); //Rango de puntos hasta el maximo 

		if (p < f_ev)
		{
			p_debajo += 1;
			
		}

		
	}

	double integ= (double) p_debajo/n;
	return integ;

}
