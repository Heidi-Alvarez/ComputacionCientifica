#!/home/heidi/Astronomy/Estelar/Parciales/III

import numpy as np
import math

#######Caracteristicas de la estrella
#### Densidad constante en toda la estrella, constituida por hidrogeno.

R=1000 ## Radio de la estrella en metros.
n=3.8e28 ## Densidad numerica de electrones por metro cubico.
sigma=7.0e-14 ## Seccion eficaz de un atomo de hidrogeno en metros cuadrados.
c=3.0e8 ## Velocidad de la luz en m/s
l=10.0 ## Camino libre medio del foton.


Npas=open("Pasos.dat", "w") ### Archivo de datos para el numero de pasos que da el foton antes de salir de la estrella

ftn1=open("Photon1.dat", "w")
ftn2=open("Photon2.dat", "w")
ftn3=open("Photon3.dat", "w")
ftn4=open("Photon4.dat", "w")
ftn5=open("Photon5.dat", "w")


N=1000  ### Numero de fotones

for j in range(N):
    r=0.0 ## Posicion inicial del foton.
    x=0.0 ## Posicion inicial del foton en el eje x.
    y=0.0 ## Posicion inicial del foton en el eje y.
    i=0
    while r<=R:
        if(j==0):
            mod=i/100.0
            entmod=int(mod)
            if((mod-entmod)==0):
                ftn1.write("%f \t %f \n"%(x,y))
        if(j==200):
            mod=i/100.0
            entmod=int(mod)
            if((mod-entmod)==0):
                ftn2.write("%f \t %f \n"%(x,y))
        if(j==400):
            mod=i/100.0
            entmod=int(mod)
            if((mod-entmod)==0):
                ftn3.write("%f \t %f \n"%(x,y))
        if(j==600):
            mod=i/100.0
            entmod=int(mod)
            if((mod-entmod)==0):
                ftn4.write("%f \t %f \n"%(x,y))
        if(j==800):
            mod=i/100.0
            entmod=int(mod)
            if((mod-entmod)==0):
                ftn5.write("%f \t %f \n"%(x,y))
        i+=1
        paso=l*np.random.rand()
        dir=int(4*np.random.rand())
        if(dir==0):
            y+=paso
        if(dir==1):
            y-=paso
        if(dir==2):
            x+=paso
        if(dir==3):
            x-=paso
        r=np.sqrt(x**2 +y**2)
    d=l*np.sqrt(i)
    ts=((n*sigma)/c)*d**2
    ty=ts/31557600.0
    Npas.write("%d \t %d \t %f \t %f \n"%(j,i,d,ty))


Npas.close()
ftn1.close()
ftn2.close()
ftn3.close()
ftn4.close()
ftn5.close()
