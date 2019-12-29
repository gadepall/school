#Area under the parabola
import numpy as np
import matplotlib.pyplot as plt
 
n = 100
h = 1/n
x = np.linspace(1,n,n)
y = (h*x)**2
A_1 = h*np.sum(y)
print(A_1)
