#!/home/heidi/Astronomy/Planetarias/Programas


import numpy as np
import pylab as p

rho=3.0; rhog=1e-9; vhh=1e5; Omega=(2e-7)**2; h=3e11; Z0=5.0*h; f=1e-2; 
tfinal=8.6e12; n=10; deltat=tfinal/n; i=3
Zcte=(-rho/rhog)*(Omega/vhh); Mcte=(3.0/4.0)*(Omega/vhh)*f
Zm=[[0.0]*i]*n
Mm=[[0.0]*i]*n
Rm=[[0.0]*i]*n
t=[0.0]*n


def ZFUN(r,Z):
    fun=Zcte*r*Z
    return fun

def MFUN(Z,M):
    fun=Mcte*Z*M
    return fun

for k in range(i):
    if(k==0):
        r=0.01e-4
        Rm=[k][0]=r
    if(k==1):
        r=0.1e-4
        Rm=[k][0]=r
    if(k==2):
        r=1e-4 
        Rm=[k][0]=r
    M=(4.0*rho*np.pi*r**3)/3.0
    Z=Z0
    Zm[k][0]=Z
    Mm[k][0]=M
    for j in range(1,n-1):
        ZK1=ZFUN(r,Z)
        ZK2=ZFUN(r,Z+0.5*deltat*(j)*ZK1)
        ZK3=ZFUN(r,Z+0.5*deltat*(j)*ZK2)
        ZK4=ZFUN(r,Z+deltat*(j)*ZK3)
        Z=Z+(1/6.0)*deltat*(j)*(ZK1+2.0*ZK2+2.0*ZK3+ZK4)
        MK1=MFUN(Z,M)
        MK2=MFUN(Z,M+0.5*deltat*(j)*MK1)
        MK3=MFUN(Z,M+0.5*deltat*(j)*MK2)
        MK4=MFUN(Z,M+deltat*(j)*MK3)
        M=M+(1/6)*deltat*(j)*(MK1+(2.0*MK2)+(2.0*MK3)+MK4)
        Zm[j][k]=Z
        Mm[j][k]=M
        r=((3.0*M)/(4.0*np.pi*rho))**(1/3)
 #       Rm[j][k]=r

for j in range(n):
    t[j]=deltat*j

print Zm, Mm, t

p.plot(t,Zm)
p.plot(t,Mm)

p.show()
