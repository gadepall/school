//Code released under GNU GPL.  Free to use for anything.
//Remove the following line if you are using the Arduino IDE
#include "Arduino.h"


void sevenseg(int);
void setup()
{
  // initialize LED digital pin as an output.
  pinMode(2, OUTPUT);//p[0]=a
  pinMode(3, OUTPUT);//p[1]=b
  pinMode(4, OUTPUT);//p[2]=c
  pinMode(5, OUTPUT);//p[3]=d
  pinMode(6, OUTPUT);//p[4]=e
  pinMode(7, OUTPUT);//p[5]=f
  pinMode(8, OUTPUT);//p[6]=g
}

void loop()
{
		sevenseg(0);

}
void sevenseg(int dec)
{
	int p[7],i;
	
	for (i=0;i < 7; i++)
		p[i] = 0;

	switch(dec)
	{
		case 0:
			p[6]=1;
			break;
		case 1:
			p[0]=1,p[3]=1,p[4]=1,p[5]=1,p[6]=1;
			break;			
		case 2:
			p[2]=1,p[5]=1;
			break;			
		case 3:
			p[4]=1,p[5]=1;
			break;			
		case 4:
			p[0]=1,p[3]=1,p[4]=1;
			break;			
		case 5:
			p[1]=1,p[4]=1;
			break;			
		case 6:
			p[1]=1;
			break;			
		case 7:
			p[3]=1,p[4]=1,p[5]=1,p[6]=1;
			break;			
		case 8:
			break;			
		case 9:
			p[4]=1;
			break;			
		default:
			p[1]=1,p[2]=1;
			break;
	}

	for (i=0;i < 7; i++)
		digitalWrite(i+2,p[i]);

}
