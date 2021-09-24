#!/home/heidi/Astronomy/Astrophysics/Programas


import pylab as p
import numpy as np
import scipy as sp



c=1.0
T0=0.0  ######## Tiempo inicial del gemelo en Tierra
Tf=10.0  ########## Tiempo final en years del gemelo en Tierra
n=40
dT=(Tf-T0)/n
vmin=0.0
vmax=c
N=50
deltav=(vmax-vmin)/N
X=[]
dif=[]


for j in range(N):
    v=deltav*j
    beta=v/c
    gamma=np.sqrt(1-beta**2)
    for i in range(n):
        if(i<(n/2)):
            t=dT*i
            x=v*dT
            tprima=(t-v*x/c**2)/gamma
        else:
            t=dT*i
            vr=-v  ### regreso
            x=vr*dT
            tprima=(t-v*x/c**2)/gamma
    T=tprima-t
    X.append(v)
    dif.append(T)
        


p.figure()
p.grid(True)
axes=p.gca()
axes.set_xlim(0.0,1.0)
axes.set_ylim(0.0,40.0)
p.xlabel("Velocidad")
p.ylabel("Diferencia de edades nave-Tierra")
p.plot(X,dif)
p.show()

            
            
        

