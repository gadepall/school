#Setup seven segment display
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

GPIO.output(3,1)
GPIO.output(5,0)
GPIO.output(7,0)
GPIO.output(8,1)
GPIO.output(10,1)
GPIO.output(11,1)
GPIO.output(12,1)

