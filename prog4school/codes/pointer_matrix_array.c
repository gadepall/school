#include <stdio.h>
#include <stdlib.h>

//This program shows how to use pointers as 2-D arrays

//Function declaration
double **createMat(int m,int n);
//End function declaration

int  main() //main function begins
{

//Defining the variables
int m,n;//integers
double **a,det;

printf("Enter the size of the matrix m  n \n");
scanf("%d %d", &m,&n);


A = createMat(m,n);//creating the matrix a
A[0][0] = 1;
A[0][1] = 1;
A[1][0] = 3;
A[1][1] = -1;

det = A[0][0]*A[1][1]-A[0][1]*A[1][0];
printf("%f\n",det);

return 0;
}


//Defining the function for matrix creation
double **createMat(int m,int n)
{
 int i;
 double **a;
 
 //Allocate memory to the pointer
a = (double **)malloc(m * sizeof( *a));
    for (i=0; i<m; i++)
         a[i] = (double *)malloc(n * sizeof( *a[i]));

 return a;
}
//End function for matrix creation


