#bcd-sevenseg
import RPi.GPIO as GPIO # RPi.GPIO can be referred as GPIO from now
import time

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

def bcd_sevenseg(dec):
	if dec == 0:
		sevenseg(0,0,0,0,0,0,1)
		return
	elif dec == 1:
		sevenseg(1,0,0,1,1,1,1)
		return
	elif dec == 2:
		sevenseg(0,0,1,0,0,1,0)
		return
	elif dec == 3:
		sevenseg(0,0,0,0,1,1,0)
		return
	elif dec == 4:
		sevenseg(1,0,0,1,1,0,0)
		return
	elif dec == 5:
		sevenseg(0,1,0,0,1,0,0)
		return
	elif dec == 6:
		sevenseg(0,1,0,0,0,0,0)
		return
	elif dec == 7:
		sevenseg(0,0,0,1,1,1,1)
		return
	elif dec == 8:
		sevenseg(0,0,0,0,0,0,0)
		return
	elif dec == 9:
		sevenseg(0,0,0,0,1,0,0)
		return				
	else:
		sevenseg(0,1,1,0,0,0,0)
		return

while True:
	for i in range(10):
		bcd_sevenseg(i)
		time.sleep(1.0)
	
