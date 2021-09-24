#!/home/heidi/Astronomy/Estelar/Parciales/III

import numpy as np
import pylab as p
from scipy.stats import norm


#######Caracteristicas de la estrella
#### Densidad constante en toda la estrella, constituida por hidrogeno.

R=1000 ## Radio de la estrella en metros.
n=3.8e28 ## Densidad numerica de electrones por metro cubico.
sigma=7.0e-14 ## Seccion eficaz de un atomo de hidrogeno en metros cuadrados.
c=3.0e8 ## Velocidad de la luz en m/s
l=10.0 ## Camino libre medio del foton.

Pasos=[]  ### Lista de numero total de pasos para cada foton
Tiempo=[] ### Lista para el tiempo en [a] que demora cada foton

X1=[]  ; Y1=[]     ### Listas de la posicion en el tiempo de un foton
X2=[]  ; Y2=[]     ### Para graficar
X3=[]  ; Y3=[]
X4=[]  ; Y4=[]
X5=[]  ; Y5=[]
X6=[]  ; Y6=[]

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
                X1.append(x)
                Y1.append(y)
        if(j==200):
            mod=i/100.0
            entmod=int(mod)
            if((mod-entmod)==0):
                X2.append(x)
                Y2.append(y)
        if(j==400):
            mod=i/100.0
            entmod=int(mod)
            if((mod-entmod)==0):
                X3.append(x)
                Y3.append(y)
        if(j==600):
            mod=i/100.0
            entmod=int(mod)
            if((mod-entmod)==0):
                X4.append(x)
                Y4.append(y)
        if(j==800):
            mod=i/100.0
            entmod=int(mod)
            if((mod-entmod)==0):
                X5.append(x)
                Y5.append(y)
        if(j==999):
            mod=i/100.0
            entmod=int(mod)
            if((mod-entmod)==0):
                X6.append(x)
                Y6.append(y)
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
    ts=((n*sigma)/c)*d**2  ## Tiempo que demora en salir un foton, en segundos
    ty=ts/31557600.0       ## Conversion a years
    Pasos.append(i)
    Tiempo.append(ty)



##########Grafica 

theta=np.linspace(0,2.0*np.pi,100)  ## Para graficar la estrella
x1=R*np.cos(theta)
y1=R*np.sin(theta)

### Graficas del camino de 6 fotones diferentes
p.figure(figsize=(10,10))
axes=p.gca()
p.subplot(2,3,1)
p.plot(x1,y1, color="red")
p.plot(X1,Y1, "o")
p.subplot(2,3,2)
p.plot(x1,y1, color="red")
p.plot(X2,Y2, "o")
p.subplot(2,3,3)
p.plot(x1,y1, color="red")
p.plot(X3,Y3, "o")
p.subplot(2,3,4)
p.plot(x1,y1, color="red")
p.plot(X4,Y4, "o")
p.subplot(2,3,5)
p.plot(x1,y1, color="red")
p.plot(X5,Y5, "o")
p.subplot(2,3,6)
p.plot(x1,y1, color="red")
p.plot(X6,Y6, "o")

p.figure(figsize=(10,10))
axes=p.gca()
p.subplot(2,3,1)
p.plot(x1,y1)
p.plot(X1,Y1)
p.subplot(2,3,2)
p.plot(x1,y1)
p.plot(X2,Y2)
p.subplot(2,3,3)
p.plot(x1,y1)
p.plot(X3,Y3)
p.subplot(2,3,4)
p.plot(x1,y1)
p.plot(X4,Y4)
p.subplot(2,3,5)
p.plot(x1,y1)
p.plot(X5,Y5)
p.subplot(2,3,6)
p.plot(x1,y1)
p.plot(X6,Y6)


###Histograma

p.figure("Histograma")
H=p.hist(Pasos,100, color="green")
p.title("Numero de Pasos")
p.xlabel("Valor")
p.ylabel("Frecuencia")
(mu,sigman)=norm.fit(Pasos)

print mu, sigman

p.figure("Histograma-Tiempo")
HT=p.hist(Tiempo,100, color="violet")
p.title("Tiempo [y]")
p.xlabel("Valor")
p.ylabel("Frecuencia")
(mut,sigmat)=norm.fit(Tiempo)

print mut, sigmat

p.show()
