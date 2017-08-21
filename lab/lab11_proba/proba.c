#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void grafica(double *Nt){
	int i;
	float t;
	for (i=0; i<1000; i++){
		t = i*0.01;
		Nt[i]=10*exp(-t/2);}
}

void print(double *Nt){
	int i;
	float t;
	for (i=0; i<1000; i++){
		printf("%f %f\n", i*0.01, Nt[i]);}
}

float delta_n_step(float n, float l, float dt)
{	float rand_num=drand48();
	if (rand_num < l*n*dt)
	{
		return -1.0;
	}
	else
	{
		return 0.0;	
	}

}
void single_decay(float N0, float l, float dt){

	float t_total = 5.0 / l;
	int n_points = (int)t_total/dt;
	int i;
	
	float t =0.0;
	float n = N0;
	
	FILE *out= fopen("data_rand.txt", "w");
	
	
	
	for(i=0; i<n_points; i++){

		t+=dt;
		float delta_n=delta_n_step(n,l,dt);
		n+=delta_n;
		fprintf(out,"%f %f\n",t, n);	
	}	
	fclose(out);

}
int main(void){ 

int n=1000;
double *Nt = malloc(n*sizeof(double));

grafica(Nt);
print(Nt);

}

		
	


