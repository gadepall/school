#Code by Amey Waghmare, 
#Jan 16, 2020
#Revised by GVV Sharma
#Jan 17, 2020
#Released under GNU GPL
#Quadratic program example
#Minimum distance from a point to a parabola
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5,5,100)
y = (x**2)/2
P = np.array([[0],[5]])


ax=plt.plot(x,y)
plt.grid()
plt.axis('equal')


C1 = np.array([[8**(1/2)],[4]])
C2 = np.array([[-8**(1/2)],[4]])
bx=plt.scatter(C1[0],C1[1])
plt.text(C1[0]+0.1,C1[1]+0.1,"C")
print("Point at minimum distance is ",C1)
plt.scatter(P[0],P[1])
plt.text(P[0]+0.1,P[1]+0.1,"P")


plt.legend(['$x^2=4y$','$C$'])


#if using termux
plt.savefig('./figs/quadprog_parab.pdf')
plt.savefig('./figs/quadprog_parab.eps')
subprocess.run(shlex.split("termux-open ./figs/quadprog_parab.pdf"))
#else
#plt.show()






