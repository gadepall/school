x1,x2=var('x1,x2')
f=4*x1^2+2*x2^2#Objective function
g1=3*x1+x2-8#Constraint 1
g2=15-2*x1-4*x2#Constraint 2
h=Graphics()#Creates an empty Objective function
#Region plot of constraint 1
h1=region_plot(g2>=0,(x1,0,15),(x2,0,15),incol='grey')
#Region plot of constraint 2
h2=region_plot(g1==0,(x1,0,15),(x2,0,15))
for c in range(0,25):
#Creates a series of level sets of f
    h=h+implicit_plot(f-(c^2)/8,(x1,0,15),(x2,0,15))
h=h+h1+h2#Adding all the plots into Graphics window
h.show()