#Area under the parabola
import numpy as np
import matplotlib.pyplot as plt
 
n = 100
h = 1/n
x = np.linspace(1,n,n)
y = np.sqrt(h*x)
A = h*np.sum(y)
print(A)
