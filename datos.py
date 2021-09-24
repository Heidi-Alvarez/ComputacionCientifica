#!/home/heidi/Astronomy/Estelar/Parciales/I


import pylab as p
import numpy as np
import scipy as sp
import os

pts=open("V-I.txt","r")
puntos=pts.readlines()

N=len(puntos)
print N

V=[]  #### Magnitud en el visible
I=[]  #### Magnitud en el infrarojo
M=[]  #### Masa en masas solares
VI=[] #### Indice de color, V-I


for punto in puntos:    
    v=float(punto.split(" ")[2])
#   i=float(punto.split(" ")[19])
#   masa=float(punto.split(" ")[21])
#   print v, i, masa
#   vi=v-i
    print v
#   V.append(v)
#   I.append(i)
#   M.append(masa)
#   VI.append(vi)

