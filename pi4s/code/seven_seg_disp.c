#include <wiringPi.h>

void sevenseg(int a,int b,int c,int d,int e,int f,int g)
{
  digitalWrite(0, a);
  digitalWrite(1, b);
  digitalWrite(2, c);
  digitalWrite(3, d);
  digitalWrite(4, e);
  digitalWrite(5, f);
  digitalWrite(6, g);
}

int main (void)
{
  wiringPiSetup () ;
  pinMode (0, OUTPUT) ;
  pinMode (1, OUTPUT) ;
  pinMode (2, OUTPUT) ;
  pinMode (3, OUTPUT) ;
  pinMode (4, OUTPUT) ;
  pinMode (5, OUTPUT) ;
  pinMode (6, OUTPUT) ;
 
  for (;;)
  {
  
sevenseg(1,0,0,1,1,1,1);  
}  
}	
//Command for raspberry pi
//gcc -Wall -o test seven_seg_disp.c -lwiringPi
//followed by 
// sudo ./test
