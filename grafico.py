#! /home/heidi/Astronomia/Laboratorios/II/Tercera


import matplotlib as pl
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

########Para leer los datos

datos=open('/home/heidi/Astronomia/Laboratorios /II/Tercera/datos.dat', 'r')
elementos=datos.readlines()
n=len(elementos)
X=[0.0]*n; Y=[0.0]*n; Z=[0.0]*n
l=0
for i in elementos:
    AR=float(i.split('\t\t')[0])
    DC=float(i.split('\t\t')[1])
    R=float(i.split('\t\t')[2])
    X[l]=R*np.sin(DC)*np.cos(AR)
    Y[l]=R*np.sin(DC)*np.sin(AR)
    Z[l]=R*np.cos(DC)
    l+=1
    #print AR, DC, R


#Para graficar los datos

fig=pl.figura()
Ax=fig.Gca(proyection='3d')
x=np.arange(0,360,0.01)
y=np.arange(-90,90,0.01)
x,y=np.meshgrid(x,y)
r=np.sqrt(x**2 + y**2)
#z=np.arange(0,30,0.01)
pl.show()
