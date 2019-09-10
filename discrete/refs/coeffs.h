//Function declaration
double **createMat(int m,int n);
void readMat(int m,int n,double **p);
void print(int m,int n,double **p);
//End function declaration


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


//Defining the function for reading matrix 
void readMat(int m,int n,double **p)
{
 int i,j;
 for(i=0;i<m;i++)
 {
  for(j=0;j<n;j++)
  {
   scanf("%lf",&p[i][j]);
  }
 }
}
//End function for reading matrix



//Defining the function for printing
void print(int m,int n,double **p)
{
 int i,j;

 for(i=0;i<m;i++)
 {
  for(j=0;j<n;j++)
  printf("%lf ",p[i][j]);
 printf("\n");
 }
}




//Defining linspace
//double linspace(double a, double b, int n)
//{
//double d;
//
//d = (b-1)/(n-1);
//
//
//}
