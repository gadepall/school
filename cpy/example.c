#include <stdio.h>
#include <stdlib.h>
#include "coeffs.h"

int  main() //main function begins
{

//Defining the variables
int m,n, len ;//integers
double **a,**P,**Q,**mat,**c;

//Generate line points
len = 100;

//Given points
P = loadtxt(2,1,"P.dat");
Q = loadtxt(2,1,"Q.dat");

//Matrix equation
mat = loadtxt(2,2,"mat.dat");
c = loadtxt(2,1,"c.dat");

//Q = np.array([0,2]) 
//printf("Enter the size of the matrix m  n \n");
//scanf("%d %d", &m,&n);
//
//
//printf("Enter the values of the matrix\n");
//a = createMat(m,n);//creating the matrix a
//P =createMat(m,n);//creating the matrix a
// readMat(m,n,a);//reading values into the matrix a
//print(2,1,P);//printing the matrix P
//print(2,1,Q);//printing the matrix Q
print(2,2,mat);//printing the matrix Q
print(2,1,c);//printing the matrix Q

return 0;
}


