#!/home/heidi/Astronomy/Estelar/Parciales/III

import numpy as np
import pylab as p

#### Primera parte

### En el Sistema Internacional de unidades

Pe=20.0 ## Presion de electrones en N/m^2
me=9.1e-31 ## Masa del electron en kg
Kb=1.3806e-23 ## Constante de Boltzmann en J/K
h=6.62069e-34 ## Constante de Planck en Js
eV=1.602e-19 ## Equivalencia de eV en J
ZI=1 ## Funcion de particion para 1
ZII=2 ## Para 2
ZIII=1 ## Para 3
XI=24.6 ## Energia de ionizacion para el nivel base en eV
XII=54.4 ## Energia de ionizacion para el nivel II en eV
T1=5000 ## Temperatura en K
T2=15000 ## K
T3=25000 ## K

#####NII/NI
#### NII/NI=(ZII/PeZI)(pime/h^2)^3/2 (2KbT)^5/2  e^(-XI/KbT) 


X=XI*eV ## Conversion al SI
n=3
print "Variacion de NII/NI respecto a la temperatura, con T=5000K, 15000K y 25000K "
for i in range(n):
    a=(ZII/(Pe*ZI))*((me*np.pi)/(h**2))**(3/2.0)
    if (i==0):
        T=T1
        b=(2.0*Kb*T)**(5/2.0)
        e=np.exp(-X/(Kb*T))
        R=a*b*e ### NII/NI
        print R
    if (i==1):
        T=T2
        b=(2.0*Kb*T)**(5/2.0)
        e=np.exp(-X/(Kb*T))
        R=a*b*e
        print R
    if (i==2):
        T=T3
        b=(2.0*Kb*T)**(5/2.0)
        e=np.exp(-X/(Kb*T))
        R=a*b*e
        print R


#####NIII/NII
#### NIII/NII=(ZIII/PeZII)(pime/h^2)^3/2 (2KbT)^5/2  e^(-XII/KbT) 

X=XII*eV ## Conversion al SI
n=3
print "Variacion de NIII/NII respecto a la temperatura, con T=5000K, 15000K y 25000K "
for i in range(n):
    a=(ZIII/(Pe*ZII))*((me*np.pi)/(h**2))**(3/2.0)
    if (i==0):
        T=T1
        b=(2.0*Kb*T)**(5/2.0)
        e=np.exp(-X/(Kb*T))
        R=a*b*e
        print R
    if (i==1):
        T=T2
        b=(2.0*Kb*T)**(5/2.0)
        e=np.exp(-X/(Kb*T))
        R=a*b*e
        print R
    if (i==2):
        T=T3
        b=(2.0*Kb*T)**(5/2.0)
        e=np.exp(-X/(Kb*T))
        R=a*b*e
        print R


######## Segunda parte


####NII/NTot=alpha/(1+alpha(1+beta))
### Con alpha=NII/NI  y beta=NIII/NII


N=2000  ## Numero de intervalos para la variacion en la temperatura
dT=(T3-T1)/N ## Intervalo de temperatura
T=T1
XI=XI*eV
XII=XII*eV
a=(1/Pe)*((me*np.pi)/(h**2))**(3/2.0)
bI=ZII/ZI
bII=ZIII/ZII
TX=[]  ### Vector de temperatura
NY=[]  ### Vector de la relacion NII/NTot
error=1.0e-4

### I: Hace referencia a NII/NI
### II: Hace referencia a NIII/NII

for i in range(N+1):
    c=(2.0*Kb*T)**(5/2.0)
    dI=XI/(Kb*T)
    dII=XII/(Kb*T)
    eI=np.exp(-dI)
    eII=np.exp(-dII)
    alpha=a*bI*c*eI
    beta=a*bII*c*eII
    NN=alpha/(1+alpha*(1+beta)) ### NII/NTot
    TX.append(T)
    NY.append(NN)
    if (np.abs(NN-0.5)<error): ### Punto en el cual la ionizacion es parcial
        MX=T  ### Coordenada X
        MY=NN ### Coordenada Y
    T+=dT

print ("Temperatura parcial de ionizacion T=%d"%MX)


##########Grafica 

p.figure()
p.grid(True)
axes=p.gca()
p.title("$N_{II}/N_{Tot}$ vs $T$")
axes.set_xlim(5000,25000)
axes.set_ylim(0.0,1.0)
p.xlabel("T [K]")
p.ylabel("$N_{II}/N_{Tot}$")
p.plot(TX,NY)
p.plot(MX,MY, "*" )
p.annotate(r'$\frac{N_{II}}{N{Tot}}=0.5$',xy=(MX, MY), xycoords='data', xytext=(+8, +30), textcoords='offset points', fontsize=13, arrowprops=dict(arrowstyle="->"))
p.show()
