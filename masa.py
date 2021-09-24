#!/home/heidi/Astronomy/Galaxias/Parcial/Primero


import pylab as p
import numpy as np
import scipy as sp

## Perfil de Hernquist ###

def Perfil(M,a,r):
    Rho=M/(2.0*np.pi*a**2*r(1.0+r/a)**3)
    return Rho

def MasaH(M,a,r):
    masa=(M(r/a)**2)/(1+r/a)**2
    return masa

def sigmaR(M,a,r,rho):
    G=6.67e-11
    num=(25a**3 +52.0*a**2 *r + 42.0*a*r**2 +12.0*r**3)
    den=12.0*(a+r)**4
    sigma=(-G*M**2 /(2*np.pi*rho+a**3))*((num/den)+np.log(1+a/r)) 
    return sigma

def Beta(vphi,vtheta,vr):
    beta=1-(vphi+vtheta)/(2.0*vr)
    return beta

rmin=0.1
rmax=10.0
N=2
dR=(ramx-rmin)/N
M=1.0
a=0.1


for i in range(N):
    


    
