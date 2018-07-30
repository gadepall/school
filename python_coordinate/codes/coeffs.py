import numpy as np
import matplotlib.pyplot as plt


A = np. matrix('-2;-2')
B = np. matrix('1;3')

p = np.zeros((3,1))
p[0] = A[1]-B[1]
p[1] = B[0]-A[0]
p[2] = A[0]*B[1]- A[1]*B[0]

print (p)


