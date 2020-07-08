#Calling C function in Python
from ctypes import *

#load the shared object file
multip = CDLL('./mul.so')

a=2.0
b=8.0

#Find multiplication of floats

mul = multip.mul
mul.restype = c_float

print (a,"x",b,"=", mul(c_float(a), c_float(b)))
