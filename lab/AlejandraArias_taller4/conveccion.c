#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define c 1.0 


void cond_inicial(double *u, double delta_x, int n_x);

void iteracion(double *u_presente, double delta_x, double delta_t, int n_x, double *u_futuro);

void copiar(double *u_futuro, double *u_presente, int n_x);

void print(double *u_presente, int n_x, double delta_x);


int main (){

int i;
double delta_x = 0.02;
int n_x= 100.0;
int n_t=300.0;
double delta_t= 0.3/n_t;


double *u_presente = malloc(sizeof(double)*n_x);
double *u_futuro = malloc(sizeof(double)*n_x);

cond_inicial(u_presente, delta_x, n_x);
print(u_presente, n_x, delta_x);

for (i=0;i<n_t;i++){

	iteracion(u_presente, delta_x, delta_t, n_x, u_futuro);
	copiar(u_futuro, u_presente, n_x);
	}

print(u_presente, n_x, delta_x);

}

void cond_inicial(double *u_inicial, double delta_x, int n_x){

	int j;

	for (j=0; j<n_x; j++){

		double x = j*delta_x;

		if(x>0.7 && x<1.2){

			u_inicial[j]=2.0;			
			}

		else{
			u_inicial[j]=0.0;			
			}		
		}
}


void iteracion(double *u_presente, double delta_x, double delta_t, int n_x, double *u_futuro){
	
	int i;
	for (i=1; i<n_x; i++){

	u_futuro[i]=(-c*(delta_t/delta_x)*(u_presente[i]-u_presente[i-1]))+u_presente[i];
			}
}

void copiar(double *u_futuro, double *u_presente, int n_x){

	int i;
	for (i=1;i<n_x;i++){
		u_presente[i] = u_futuro[i];
	}
	
}

void print(double *u_presente, int n_x, double delta_x){
	int i;
	for (i=1;i<n_x;i++){
		printf("%f %e\n", i*delta_x, u_presente[i]);
	}

}

