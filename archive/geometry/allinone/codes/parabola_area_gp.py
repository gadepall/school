#Area under the parabola
import numpy as np
import matplotlib.pyplot as plt
 
n = 100
r = 0.98
k = np.linspace(1,n,n)
y = r**(3*k-3)
A = (1-r)*np.sum(y)
print(A)
