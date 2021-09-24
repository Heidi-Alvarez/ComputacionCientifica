#!/home/heidi/Astronomy/Astrophysics/Programas


import pylab as p
import numpy as np
import scipy as sp

mo=1.0
c=1.0
X=[]    ####### velocity 
CSS=[]  ####### classic energy
RTV=[]  ####### relativist energy
n=500
dv=c/n
j=0
l=j
k=l

for i in range(n):
    v=dv*i
    gamma=1.0/np.sqrt(1-v**2)
    m=mo*gamma
    clasica=0.5*mo*v**2
    relativista=m-mo
    X.append(v)
    CSS.append(clasica)
    RTV.append(relativista)
    dif=relativista-clasica
    if((dif>0.01) and (dif<0.011)):
        j+=1
        if(j==1):
            print "La velocidad a la que el calculo clasico difiere en un 0.01 de la relativista es v=%f"%v
    if((dif>0.05) and (dif<0.051)):
        l+=1
        if(l==1):
            print "La velocidad a la que el calculo clasico difiere en un 0.05 de la relativista es v=%f"%v
    if((dif>0.5) and (dif<0.51)):
        k+=1
        if(k==1):
            print "La velocidad a la que el calculo clasico difiere en un 0.5 de la relativista es v=%f"%v
    


p.figure()
p.grid(True)
axes=p.gca()
axes.set_xlim(0.0,1.0)
axes.set_ylim(0.0,5.0)
p.plot(X,CSS,label = 'Clasica')
p.plot(X,RTV,label = 'Relativista')
p.legend(loc = 2)
p.show()
