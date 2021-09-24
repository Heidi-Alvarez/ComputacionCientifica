#!/home/heidi/Astronomy/Planetarias/Programas


import numpy as np
import pylab as p

i=3; n=5

Zm=[[0.0]*i]*n
Mm=[[0.0]*i]*n

#print Zm
#print Mm

for k in range(i):
   # print k
    Zm[k][0]=1.0
    Zm[k][1]=2.0
    Zm[k][2]=3.0
    for j in range(n):
        Zm[j][k]=j
        print j

print Zm

#for j in range(1,n):
#Zm[k][j]=Z
#Mm[k][j]=M
