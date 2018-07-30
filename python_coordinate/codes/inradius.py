#This program calculates the inradius

import numpy as np
import matplotlib.pyplot as plt

def line_dist(I,p):
	return np.abs((I[0]*p[0]+I[1]*p[1]+p[2])/(np.sqrt(p[0]**2+p[1]**2)))

I = np. matrix('1.15;0.14')
A = np. matrix('-2;-2')
B = np. matrix('1;3')
C = np. matrix('4;-1')
AB = line_coeff(A,B)
BC = line_coeff(B,C)
CA = line_coeff(C,A)

print(line_dist(I,AB))



