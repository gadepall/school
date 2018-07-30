#This program computes the point of contact between a circle
#and its tangent 

import numpy as np
import matplotlib.pyplot as plt

def line_coeff(A,B):
	p = np.zeros((3,1))
	p[0] = A[1]-B[1]
	p[1] = B[0]-A[0]
	p[2] = A[0]*B[1]- A[1]*B[0]
	return p

A = np.matrix('-2;-2')
B = np.matrix('1;3')
p = line_coeff(A,B)
r=1.6
a=1.15
b=0.14

print((p[0]*(p[2]+b*p[1])-a*p[1]**2)**2)
print((p[0]**2+p[1]**2)*(p[1]**2*a**2+(p[2]+b*p[1])**2-p[1]**2*r**2))

X = np.zeros((2,1))
X[0] = -(p[0]*(p[2]+b*p[1])-a*p[1]**2)/(p[0]**2+p[1]**2)
X[1] = -(p[2]+p[0]*X[0])/p[1]
print(X)


