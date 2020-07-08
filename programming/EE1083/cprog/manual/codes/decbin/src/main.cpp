//Code released under GNU GPL.  Free to use for anything.
//Remove the following line if you are using the Arduino IDE
#include "Arduino.h"



void binsevenseg(int,int,int,int);
void setup()
{
	int i;
  // initialize LED digital pin as an output.
	for (i=0;i < 7; i++)
		pinMode(i+2, OUTPUT);
}

void loop()
{
int dec = 5;
int E,F,G,H;

//decimal to binary conversion
E = dec%2;
dec = dec/2;
F = dec%2;
dec = dec/2;
G = dec%2;
dec = dec/2;
H = dec%2;

binsevenseg(E,F,G,H);

}
//function for binary to seven segment display
void binsevenseg(int A, int B, int C, int D)
{
	int p[7],i;
	
p[0] = A&&!B&&!C&&!D || !A&&!B&&C&&!D;
p[1] = A&&!B&&C&&!D || !A&&B&&C&&!D;
p[2] = !A&&B&&!C&&!D;
p[3] = A&&!B&&!C&&!D || !A&&!B&&C&&!D || A&&B&&C&&!D;
p[4] = A&&!B&&!C&&!D || A&&B&&!C&&!D || !A&&!B&&C&&!D || A&&!B&&C&&!D || A&&B&&C&&!D || A&&!B&&!C&&D;
p[5] = A&&!B&&!C&&!D || !A&&B&&!C&&!D || A&&B&&!C&&!D || A&&B&&C&&!D;
p[6] = !A&&!B&&!C&&!D || A&&!B&&!C&&!D || A&&B&&C&&!D;

	for (i=0;i < 7; i++)
		digitalWrite(i+2,p[i]);

}
