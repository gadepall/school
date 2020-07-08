//Code released under GNU GPL.  Free to use for anything.
//Remove the following two lines if you are using the Arduino IDE
//and include the sevenseg function definition after the loop function
#include "Arduino.h"
#include "sevenseg.h"

int i;
void sevenseg(int);
void setup()
{
  // initialize LED digital pin as an output.
  pinMode(2, OUTPUT);//a
  pinMode(3, OUTPUT);//b
  pinMode(4, OUTPUT);//c
  pinMode(5, OUTPUT);//d
  pinMode(6, OUTPUT);//e
  pinMode(7, OUTPUT);//f
  pinMode(8, OUTPUT);//g
}

void loop()
{
	for(i=0; i < 10; i++)
	{
		sevenseg(i);
		delay(1000);
	}
		

}
