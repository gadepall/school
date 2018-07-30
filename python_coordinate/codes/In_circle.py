#This program plots the incircle
import numpy as np 
import matplotlib.pyplot as plt 

r=1.6
a=1.15
b=0.14
x=np.linspace(a-r,a+r,1000)
y1=b+np.sqrt((r)**2-((x-a)**2))
y2=b-np.sqrt((r)**2-((x-a)**2))
plt.plot(x,y1)
plt.plot(x,y2)
plt.grid()
plt.axis("equal")
#plt.savefig('../figs/incircle.eps')
plt.show()

	
	
	
