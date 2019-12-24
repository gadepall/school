#Code by GVV Sharma
#December 24, 2019
#released under GNU GPL
#Line Inequality

import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex
#end if

affine1 = np.array(([2,1],[-1,-1]))
affine2 = np.array(([-1,-1],[-2,3]))
affine3 = np.array(([2,1],[-2,3]))
c1 =  np.array([4,-3])
c2 =  np.array([-3,-6])
c3 =  np.array([4,-6])

#Original axes
points = np.array([[0, 0], [0,2],[2, 0]])

#Transformed axes
affine_points1 = np.linalg.inv(affine1)@(c1+points).T
affine_points2 = np.linalg.inv(affine2)@(c2+points).T
affine_points3 = np.linalg.inv(affine3)@(c3+points).T
affine_points1 = affine_points1.T
affine_points2 = affine_points2.T
affine_points3 = affine_points3.T

#Filling up the desired region
plt.fill(affine_points1[:,0], affine_points1[:,1], 'k', alpha=0.3)
plt.fill(affine_points2[:,0], affine_points2[:,1], 'k', alpha=0.1)
plt.fill(affine_points3[:,0], affine_points3[:,1], 'k', alpha=0.2)

#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
plt.axis('equal')
#if using termux
plt.savefig('./line/figs/line_ineq_mult.pdf')
plt.savefig('./line/figs/line_ineq_mult.eps')
subprocess.run(shlex.split("termux-open ./line/figs/line_ineq_mult.pdf"))
#else
#plt.show()

	

