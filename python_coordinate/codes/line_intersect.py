#This program calculates the
#intersection of two lines
#given their equations
import numpy as np
import matplotlib.pyplot as plt


def line_intersect(p,q):
	P = np.column_stack((p[0:2],q[0:2])).transpose()	
	c = -np.row_stack((p[2],q[2]))
	return np.matmul(np.linalg.inv(P),c)

p = np.matrix('2;-3;-2')
q = np.matrix('1;3;-1')
r = np.matrix('1;0;-1')

print(line_intersect(p,r))
