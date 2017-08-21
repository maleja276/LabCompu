#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#define r 1.0

float pi(int n);

int main(void){

FILE *datos;
datos=fopen("resultados.txt","a");

double valor;
float x;
int n;

n=100000;

x=pi(n);
valor=4.0*x/(float)n;
fprintf(datos, "El valor de la constante pi es: %f\n", valor);	
fclose(datos);
}


float pi(int n){

int i;
double x;
double y;
int p_cir=0;
double valor;
srand(time(NULL));

	for (i=0; i<n; i++){

		x=drand48()*2.0-1.0;
		y=drand48()*2.0-1.0;
	
		if(pow(x,2)+pow(y,2)<1.0){
			p_cir+=1;		
		}

}

return p_cir;


}
