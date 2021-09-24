#!/home/heidi/Astronomy/Estelar/Tareas


import pylab as p
import numpy as np
import scipy as sp
import os

pts=open("datos.qti", "r")
puntos=pts.readlines()

N=len(puntos)

B=[]  #### Indice de color
M=[]  #### Magnitud absoluta

for punto in puntos:    
    bv=float(punto.split(" ")[3]) 
    ma=float(punto.split(" ")[4])
    B.append(bv)
    M.append(ma)
    print bv, ma


