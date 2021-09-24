#!/home/heidi/Astronomy/Astrophysics/Programas


import pylab as p
import numpy as np
import scipy as sp


c=1.0
X=[]
Y=[]
n=200
deltav=c/n

for i in range(n):
    v=deltav*i
    gamma=1.0/np.sqrt(1-v**2)
    X.append(v)
    Y.append(gamma)



p.figure()
p.grid(True)
axes=p.gca()
axes.set_xlim(0.0,1.0)
axes.set_ylim(0.0,10.0)
p.plot(X,Y)

p.show()
