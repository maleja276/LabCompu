#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//r=dt/dx * dc
// * Punteros/arreglos


void initial_condition(double *u, int n_x, double delta_x);
void first_iteration(double *u_presente, double *u_inicial, int n_x, double r);
void iteration(double *u_futuro, double *u_presente, double *u_pasado, int n_x, double r);
void copy(double *u_nuevo, double *u_pasado, int n_x);
void print_u(double *u, int n_x, double delta_x);



int main(){

//Declara las variables

double x_f = 1.0;
int n_x = 1000;

double delta_x = 0.001;
double delta_t = 5E-4;
int n_t = 350; 

double c = 1.0;
double r= c * (delta_t/delta_x);


double *u_pasado = malloc(sizeof(double)*n_x);  
double *u_presente = malloc(sizeof(double)*n_x);  
double *u_futuro = malloc(sizeof(double)*n_x);

//utiliza las funciones

initial_condition(u_pasado, n_x, delta_x);
u_pasado[0]=0.0;
u_pasado[n_x-1]=0.0;

u_presente[0]=0.0;
u_presente[n_x-1]=0.0;

first_iteration(u_presente, u_pasado, n_x, r);

int i;
/*for (i=1;i<n_x;i++){

		printf("%f %f\n", i*delta_x, u_pasado[i]);
	}
*/

for (i=0;i<n_t;i++){
	iteration(u_futuro, u_presente, u_pasado, n_x, r);
	copy(u_presente, u_pasado, n_x);
	copy(u_futuro, u_presente, n_x);
}

print_u(u_presente, n_x, delta_x);
}

//Escribir que hace cada funcion 

void initial_condition(double *u, int n_x, double delta_x){

	int j;
	for(j=0;j<n_x;j++){

		double x = j*delta_x; 
		u[j]=exp(-pow((x-0.3),2.0)/0.01);		
	}
}

void first_iteration(double *u_presente, double *u_inicial, int n_x, double r){

	int i;
	for (i=1;i<n_x;i++){

	u_presente[i]=u_inicial[i] + pow(r,2.0)/2.0 *(u_inicial[i+1]-2.0*u_inicial[i]+u_inicial[i-1]);

	}
}

void iteration(double *u_futuro, double *u_presente, double *u_pasado, int n_x, double r){
	int i;

	for (i=1;i<n_x;i++){

		u_futuro[i]=(2.0*(1.0-pow(r,2.0)))*u_presente[i]-u_pasado[i]+(pow(r,2.0))*(u_presente[i+1]+u_presente[i-1]);
	}
}

void copy(double *u_nuevo, double *u_pasado, int n_x){
	int i;
	for (i=1;i<n_x;i++){
		u_pasado[i] = u_nuevo[i];
	}
}

void print_u(double *u, int n_x, double delta_x){
	int i;
	for (i=1;i<n_x;i++){
		printf("%f %f\n", i*delta_x, u[i]);
	}

}


