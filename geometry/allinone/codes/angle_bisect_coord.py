#This program calculates point
#where the angle bisector meets the
#opposite side

import numpy as np
import matplotlib.pyplot as plt


def angle_bisect_coord(b,c,B,C):
	return np.multiply((np.multiply(b,B)+np.multiply(c,C)),1/(b+c))

A = np. matrix('-2;-2')
B = np. matrix('1;3')
C = np. matrix('4;-1')

a = side_length(B,C)
b = side_length(C,A)
c = side_length(A,B)

U = angle_bisect_coord(b,c,B,C)
V = angle_bisect_coord(c,a,C,A)
W = angle_bisect_coord(a,b,A,B)

print (U)
print (V)
print (W)

