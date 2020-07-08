#include <stdio.h>

float mul(float,float);

int main(void)
{
printf("%f\n",mul(4,5));
return 0;
}
//gcc main.c mul.so -Wl,-rpath=$(pwd)
