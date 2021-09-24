#!/home/heidi/Planetarias


import pylab as p
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import os

############ Toma de datos

M=[]
L=[]
T=[]

pts=open("masas.dat", "r")
puntos=pts.readlines()

N=len(puntos)

for punto in puntos:
    m=float(punto.split(" ")[0])
    M.append(m)


pts2=open("luminosidad.dat", "r")
puntoslum=pts2.readlines()

N2=len(puntoslum)

for punto in puntoslum:
    l=float(punto.split(" ")[0])
    L.append(l)



pts3=open("temperaturas.dat", "r")
puntostem=pts3.readlines()

N3=len(puntostem)

for punto in puntostem:
    t=float(punto.split(" ")[0])
    T.append(t)



############## Calculo del brillo


X=[]
RV=np.zeros((N,2))
RaG=np.zeros((N,2))
MG=np.zeros((N,2))
MxG=np.zeros((N,2))
EM=np.zeros((N,2))
dmax=10.0 ####UA
dmin=0.001


##### Recent Venus

aRV=1.4316e-4 ; bRV=2.9875e-9;  cRV=-7.5702e-12 ;  dRV=-1.1635e-15    
SmRV=1.7753

##### Runaway Greenhouse

aRaG=1.0512 ;  bRaG=1.3242e-4 ;  cRaG=-7.9895e-12 ;  dRaG=-1.8328e-15
SmRaG=1.0512

##### Moist Greenhouse

aMG=1.0140  ;  bMG=8.1774e-5  ;  cMG=-4.3241e-12  ;  dMG=-6.6462e-16
SmMG=1.0140

#### Maximun Greenhouse

aMxG=0.3438 ;  bMxG=5.8942    ;  cMxG=-3.0045e-12 ;  dMxG=-5.2983e-16
SmMxG=0.3438

#### Early Mars

aEM=0.3179  ;  bEM=5.4513e-5  ;  cEM=-2.7786e-12  ;  dEM=-4.8997e-16
SmEM=0.3179

########## Creando el espaciamiento en X


dx=(dmax-dmin)/1000.0

for i in range(N):
    r=dmin+dx*i
    X.append(r)


################## Por secciones


for j in range(N):
    k1=0
    k2=0
    k3=0
    k4=0
    k5=0
    for i in range(N2):
        r=X[i]
        lum=L[j]
        A=np.pi*r**2
        brillo=lum/A
        masa=M[j]
        RV[j][1]=masa
        RaG[j][1]=masa
        MG[j][1]=masa
        MxG[j][1]=masa
        EM[j][1]=masa
        Teff=T[j]
        Tstar=Teff-5780  ##### En Kelvin
        SeffRV=brillo+aRV*Tstar+bRV*(Tstar**2)+cRV*(Tstar**3)+dRV*(Tstar**4)
        SeffRaG=brillo+aRaG*Tstar+bRaG*(Tstar**2)+cRaG*(Tstar**3)+dRaG*(Tstar**4)
        SeffMG=brillo+aMG*Tstar+bMG*(Tstar**2)+cMG*(Tstar**3)+dMG*(Tstar**4)
        SeffMxG=brillo+aMxG*Tstar+bMxG*(Tstar**2)+cMxG*(Tstar**3)+dMxG*(Tstar**4)
        SeffEM=brillo+aEM*Tstar+bEM*(Tstar**2)+cEM*(Tstar**3)+dEM*(Tstar**4)    
        if((np.abs(SeffRV)-SmRV)<=0.0):
            if(k1==0):
                RV[j][0]=r
                k1=1            
        if((np.abs(SeffRaG)-SmRaG)<=0.0):
            if(k2==0):
                RaG[j][0]=r
                k2=1
        if((np.abs(SeffMG)-SmMG)<=0.0):
            if(k3==0):
                MG[j][0]=r
                k3=1
        if((np.abs(SeffMxG)-SmMxG)<=0.0):
            if(k4==0):
                MxG[j][0]=r
                k4=1
        if((np.abs(SeffEM)-SmEM)<=0.0):
            if(k5==0):
                EM[j][0]=r
                k5=5
        K=k1+k2+k3+k4+k5
        if(K==5):
            i=N2


fig=plt.figure(figsize=(1,5))
ax=fig.gca()

ax.plot(RV[:,0],RV[:,1])
ax.plot(RaG[:,0],RaG[:,1])
ax.plot(MG[:,0],MG[:,1])
ax.plot(MxG[:,0],MxG[:,1])
ax.plot(EM[:,0],EM[:,1])

max=10
ax.set_xlim((0,max))
ax.set_ylim((0,1))
ax.grid()

plt.show()
