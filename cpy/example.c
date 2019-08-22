#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main() //main function begins
{

//Defining the variables
int m,n, len ;//integers
double **a,**P,**Q,**mat,**c,**temp, r;

//Generate line points
len = 100;

//Given points
P = loadtxt("P.dat",2,1);
Q = loadtxt("Q.dat",2,1);

//Matrix equation
mat = loadtxt("mat.dat",2,2);
c = loadtxt("c.dat",2,1);

//Circle centre and radius
//O = linalg_inv(mat)@c
//linalg_norm(O-P)

// readMat(m,n,a);//reading values into the matrix a
temp = linalg_sub(P,c,2,1);
r = linalg_norm(temp,2);
printf("\n %lf\n",r);
//print(2,1,temp);//printing the matrix Q
//print(2,1,Q);//printing the matrix Q

free(P);
free(Q);
free(mat);
free(c);
free(temp);
return 0;
}


