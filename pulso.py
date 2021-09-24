#!/home/heidi/Astronomy/Astrophysics/Programas


import pylab as p
import numpy as np
import scipy as sp


PI=np.pi
dx=0.001
N1=[]
N2=[]
N3=[]
N4=[]
N1=[]
X=[]
N1.append(0.0)
N2.append(0.0)
N3.append(0.0)
N4.append(0.0)
X.append(0.0)

for k in range(4):
    x=0.0
    if (k==0):
        N=5
    if (k==1):
        N=11
    if (k==2):
        N=21
    if (k==3):
        N=41
    while(x<PI):
        sum=0.0
        cte=1.0/(N+1.0)
        for i in range(N+1):
            n=(2*i)+1
            sum+=((-1)**((n-1)/2))*np.sin(n*x)
        x+=dx
        sum=cte*sum
        if(k==0):
            N1.append(sum)
            X.append(x)
        if(k==1):
            N2.append(sum)
        if(k==2):
            N3.append(sum)
        if(k==3):
            N4.append(sum)


########### N=5
p.figure()
p.grid(True)
axes=p.gca()
axes.set_xlim(0.0,PI)
axes.set_ylim(-0.4,1.20)
p.xlabel("Radianes")
p.ylabel("Phi")
p.plot(X,N1, 'red')
p.legend(loc = 2)
p.title('N=5')
p.show()

############## N=11
p.figure()
p.grid(True)
axes=p.gca()
axes.set_xlim(0.0,PI)
axes.set_ylim(-0.4,1.20)
p.xlabel("Radianes")
p.ylabel("Phi")
p.plot(X,N2, 'green')
p.legend(loc = 2)
p.title('N=11')
p.show()

##################### N=21

p.figure()
p.grid(True)
axes=p.gca()
axes.set_xlim(0.0,PI)
axes.set_ylim(-0.4,1.20)
p.xlabel("Radianes")
p.ylabel("Phi")
p.plot(X,N3, 'blue')
p.legend(loc = 2)
p.title('N=21')
p.show()

################# N=41

p.figure()
p.grid(True)
axes=p.gca()
axes.set_xlim(0.0,PI)
axes.set_ylim(-0.4,1.20)
p.xlabel("Radianes")
p.ylabel("Phi")
p.plot(X,N4, 'violet')
p.legend(loc = 2)
p.title('N=41')
p.show()


#################################
p.figure()
p.grid(True)
axes=p.gca()
axes.set_xlim(0.0,PI)
axes.set_ylim(0.0,40.0)
p.subplot(2,2,1)
axes.set_xlim(0.0,PI)
p.plot(X,N1, 'r')
p.subplot(2,2,2)
p.plot(X,N2, 'g')
p.subplot(2,2,3)
p.plot(X,N3, 'b')
p.subplot(2,2,4)
p.plot(X,N4, 'y')
p.show()

            
     
