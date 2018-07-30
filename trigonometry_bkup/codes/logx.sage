\begin{verbatim}


x=var('x')
f=log(x)#Objective function
g=Graphics()#Creates an empty Graphics Object
h=plot(f,(0,10))#plot of logx function
#Plotting line segment with x>0 and y=logx 
#Below are five random line segments
q1=line([(10^(-3),-3*log(10)),(8,log(8))],rgbcolor=(1,1,1))
#rgbcolor used to color each line with a different color
q2=line([(2,log(2)),(7,log(7))],rgbcolor=(3/7,1/4,2/5))
q3=line([(10^(-1),-1*log(10)),(3,log(3))],rgbcolor=(1/2,3/4,4/5))
q4=line([(1,0),(10,log(10))],rgbcolor=(1,0,0))
q5=line([(10^(-2),-2*log(10)),(6,log(6))],rgbcolor=(0,1,0))
g=g+h+q1+q2+q3+q4+q5 #adding all the plots into the Graphics window
g.show()#Reveals the plot

\end{verbatim}