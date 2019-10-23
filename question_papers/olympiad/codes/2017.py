#Code by GVV Sharma
#May 19, 2019
#released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#from circumcentre import  ccircle

#if using termux
import subprocess
import shlex
#end if

#Generate line points


len = 100

#Generating Circle omega
r = 7
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)

#Generating points on circle
thetar = 0
thetas = 5*np.pi/6
thetaj = 5*np.pi/12
#thetaj = 10*np.pi/17
R = r*np.array([np.cos(thetar),np.sin(thetar)]) 
S = r*np.array([np.cos(thetas),np.sin(thetas)]) 
J = r*np.array([np.cos(thetaj),np.sin(thetaj)]) 
#R = r*np.array([1,0]) 
#S = r*np.array([np.cos(2*np.pi/3),np.sin(2*np.pi/3)]) 
#S = r*np.array([np.cos(5*np.pi/6),np.sin(5*np.pi/6)]) 
#J = r*np.array([np.cos(np.pi/3),np.sin(np.pi/3)]) 
T = 2*S-R

#Gnerating Circumcircle
O,r1 = ccircle(J,S,T)
theta = np.linspace(0,2*np.pi,len)
x_circg = np.zeros((2,len))
x_circg[0,:] = r1*np.cos(theta)
x_circg[1,:] = r1*np.sin(theta)
x_circg = (x_circg.T + O).T


#Generating all lines
x_RT = line_gen(R,T)
#x_l = line_gen(R,[0,-R.T@R])
#len =10
x_l = np.zeros((2,len))
lam_1 = np.linspace(0,1,len)
omat = np.array([[0,1],[-1,0]]) 

for i in range(len):
  temp1 = R - 7*lam_1[i]*(omat@R)
  x_l[:,i]= temp1.T

n1 = omat@R
c0 = np.linalg.norm(n1)**2
c1 = 2*n1.T@(R-O)
c2 = np.linalg.norm(R-O)**2-r1**2
polc = [c0,c1,c2]
[lam1,lam2] = np.roots(polc)
A = R + lam2*n1
B = R + lam1*n1

n1 = A-J
c0 = np.linalg.norm(n1)**2
#c1 = 2*n1.T@R
c1 = 2*n1.T@A
#c2 = np.linalg.norm(R)**2-r**2
c2 = np.linalg.norm(A)**2-r**2
polc = [c0,c1,c2]
[lam1,lam2] = np.roots(polc)
K = A + lam1*n1

#Generating more lines 
#x_KT = line_gen(K,T)
x_BT = line_gen(B,T)
x_KA = line_gen(K,A)
x_KR = line_gen(K,R)
x_KS = line_gen(K,S)
x_RA = line_gen(R,A)
x_JR = line_gen(R,J)

x_KT = np.zeros((2,len))
lam_1 = np.linspace(0,1,len)

for i in range(len):
  temp1 = K - 2*lam_1[i]*(K-T)
  x_KT[:,i]= temp1.T

#x_AB = line_gen(A,B) x_BC = line_gen(B,C) x_CA = line_gen(C,A) x_FG = 
#line_gen(F,G) x_DE = line_gen(D,E)

##Triangle sides
#a = 8
#b = 11
#c = 13
#p = (a**2 + c**2-b**2 )/(2*a)
#q = np.sqrt(c**2-p**2)
##x = 7
#x = 3
##Triangle vertices
#A = np.array([p,q]) 
#B = np.array([0,0]) 
#C = np.array([a,0]) 
#D = (x*B+(c-x)*A)/c
#E = (x*C+(b-x)*A)/b
#H = (D+B)/2
#I = (E+C)/2
#n1 = norm_vec(A,B)
#n2 = norm_vec(A,C)
#
##print((n1.T)@D)
#
#O,r = ccircle(A,B,C)
#c0 = n1.T@n1
#c1 = 2*n1.T@(H-O)
#c2 = ((H-O).T)@((H-O).T)-r**2
#polc = [c0,c1,c2]
#[lam1,lam2] = np.roots(polc)
#F = H + lam2*n1
#
##lam1 = (-c1 + np.sqrt(c1**2 - 4 * c0*c2))/(2*c0)
##print(lam1,lam2,n1,D)
#c0 = n2.T@n2
#c1 = 2*n2.T@(I-O)
#c2 = ((I-O).T)@((I-O).T)-r**2
#polc = [c0,c1,c2]
#[lam1,lam2] = np.roots(polc)
#G = I + lam2*n2
#
#
#
#
#
#Plotting all lines
#plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
#plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
#plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_circ[0,:],x_circ[1,:],label='$\Omega$')
plt.plot(x_circg[0,:],x_circg[1,:],label='$\Gamma$')
#plt.plot(x_FG[0,:],x_FG[1,:],label='$FG$')
#plt.plot(x_DE[0,:],x_DE[1,:],label='$DE$')
plt.plot(x_RT[0,:],x_RT[1,:],label='$RT$')
plt.plot(x_KT[0,:],x_KT[1,:],label='$KT$')
plt.plot(x_KR[0,:],x_KR[1,:],label='$KR$')
#plt.plot(x_BT[0,:],x_BT[1,:],label='$BT$')
plt.plot(x_KA[0,:],x_KA[1,:],label='$KA$')
plt.plot(x_KS[0,:],x_KS[1,:],label='$KS$')
plt.plot(x_RA[0,:],x_RA[1,:],label='$RA$')
plt.plot(x_JR[0,:],x_JR[1,:],label='$JR$')
#plt.plot(x_l[0,:],x_l[1,:],label='$l$')
#
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 + 0.1) , 'A')
#plt.plot(B[0], B[1], 'o')
#plt.text(B[0] * (1 + 0.1), B[1] * (1+0.1) , 'B')
#plt.text(B[0]  - 0.2, B[1] +0.3 , 'B')
#plt.plot(C[0], C[1], 'o')
#plt.text(C[0] * (1 + 0.1), C[1] * (1 - 0.2) , 'C')
#plt.plot(D[0], D[1], 'o')
#plt.text(D[0] * (1 - 0.1), D[1] * (1  ) , 'D')
#plt.plot(E[0], E[1], 'o')
#plt.text(E[0] * (1 + 0.05), E[1] * (1) , 'E')
#plt.plot(O[0], O[1], 'o')
#plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'O')
#plt.plot(F[0], F[1], 'o')
#plt.text(F[0] * (1 - 0.1), F[1] * (1 - 0.1) , 'F')
#plt.plot(G[0], G[1], 'o')
#plt.text(G[0] * (1 + 0.1), G[1] * (1 - 0.1) , 'G')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 + 0.1), R[1] * (1 + 0.1) , 'R')
plt.plot(S[0], S[1], 'o')
plt.text(S[0] * (1 + 0.1), S[1] * (1 + 0.1) , 'S')
plt.plot(T[0], T[1], 'o')
plt.text(T[0] * (1 + 0.1), T[1] * (1 + 0.1) , 'T')
plt.plot(J[0], J[1], 'o')
plt.text(J[0] * (1 + 0.1), J[1] * (1 + 0.1) , 'J')
plt.plot(K[0], K[1], 'o')
plt.text(K[0] * (1+0.5 ), K[1] * (1 - 0.1) , 'K')
#
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
#
#if using termux
plt.savefig('../figs/2017.pdf')
plt.savefig('../figs/2017.eps')
subprocess.run(shlex.split("termux-open ../figs/2017.pdf"))
#else
#plt.show()







