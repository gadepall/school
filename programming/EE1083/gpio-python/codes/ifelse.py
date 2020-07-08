#if-else
import RPi.GPIO as GPIO # RPi.GPIO can be referred as GPIO from now

GPIO.setmode(GPIO.BOARD)       # GPIO Numbering of Pins

#Matching pins to segments
GPIO.setup(3, GPIO.OUT)#a
GPIO.setup(5, GPIO.OUT)#b
GPIO.setup(7, GPIO.OUT)#c
GPIO.setup(8, GPIO.OUT)#d
GPIO.setup(10, GPIO.OUT)#e
GPIO.setup(11, GPIO.OUT)#f
GPIO.setup(12, GPIO.OUT)#g

def sevenseg(a,b,c,d,e,f,g):
	GPIO.output(3,a)
	GPIO.output(5,b)
	GPIO.output(7,c)
	GPIO.output(8,d)
	GPIO.output(10,e)
	GPIO.output(11,f)
	GPIO.output(12,g)
	return

dec = 8

if dec == 8:
	sevenseg(0,0,0,0,0,0,0)
	
elif dec == 0:
	sevenseg(0,0,0,0,0,0,1)
