//Code released under GNU GPL.  Free to use for anything.
//Remove the following line if you are using the Arduino IDE
#include "Arduino.h"

int dec = 0;
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
if (dec==8)
{
	digitalWrite(2,0);
	digitalWrite(3,0);
	digitalWrite(4,0);
	digitalWrite(5,0);
	digitalWrite(6,0);
	digitalWrite(7,0);
	digitalWrite(8,0);
	
}
else if (dec==0)
{
	digitalWrite(2,0);
	digitalWrite(3,0);
	digitalWrite(2,0);
	digitalWrite(5,0);
	digitalWrite(6,0);
	digitalWrite(7,0);
	digitalWrite(8,1);
}

}
