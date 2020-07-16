#Code by GVV Sharma
#July 15, 2020
#released under GNU GPL
#Drawing a parabola

import numpy as np
import matplotlib.pyplot as plt

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

#Standard parabola
x1= -1
x2 = 1
x = parab_gen(x1,x2,50)
x_D = directrix_gen(x1,x2)
#Parabola points
O = parab_vertex
F = parab_focus
D = -F

#Plotting the parabola
plt.plot(x[0,:],x[1,:],label='Standard Parabola')

#Plotting the directrix
plt.plot(x_D[0,:],x_D[1,:],label='Directrix')

#Labeling the coordinates
parab_coords = np.vstack((O,F, D)).T
plt.scatter(parab_coords[0,:], parab_coords[1,:])
vert_labels = ['O','F','D']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (parab_coords[0,i], parab_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
#
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('./figs/parabola.pdf')
plt.savefig('./figs/parabola.eps')
subprocess.run(shlex.split("termux-open ./figs/parabola.pdf"))
#else
#plt.show()
#
#
#
#
#
#
#
