#!/home/heidi/Astronomy/Estelar/Parciales/II

import pylab as p
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
from math import fabs
import os

SEC=[1.16,1.45,1.83,2.1,2.49,2.75,3.1]
I=[0.25,0.21,0.17,0.15,0.13,0.1,0.07]

dt=open("datos.dat", "w")

n=len(SEC)

for j in range(n):
    sec=SEC[j]
    idad=I[j]
    dt.write("%f\t%f\n"%(sec, idad))

def grafica():
    sct=open("script_ajuste.txt", "w")
    sct.write("set terminal postscript eps enhanced \n")
    sct.write("set terminal pdf \n")
    sct.write("set title '$sec(\theta) vs Ln(I_{\lambda 0}$' \n")
    sct.write("set output 'Ajuste' \n")
    sct.write("set xrange [1.0:3.2] \n")
    sct.write("set yrange [0.065:0.26] \n")
    sct.write("set xlabel 'sec(theta)' \n")
    sct.write("set ylabel 'I_{lambda0}' \n")
    sct.write("plot './datos.dat' w p ls 7 \n")
    sct.write("f(x)=A*x+B \n")
    sct.write("fit f(x) './datos.dat' via A,B \n")
    sct.write("replot f(x) \n")
    sct.close()
    os.system("gnuplot script_ajuste.txt")

dt.close()

grafica=grafica()
#p.figure()   #### Crea la figura
#p.grid(True)
#p.grid(color = '0.5', linestyle = '--', linewidth = 1) 
#axes=p.gca()
#plt.xlabel(r"$sec (\theta)$", fontsize = 20, color= "red") ### Etiqueta eje X
#plt.ylabel(r"$Ln (I_{\lambda})$", fontsize = 20, color= "red") #Etiqueta eje Y
#p.plot(SEC,I, '*') ## Grafica las funciones


#def funcion(x,A,B):
#    return (A*x+B)
#### Ajuste
#popt,pcov = curve_fit(funcion,SEC,I)
#grafica=funcion(SEC, popt[0], popt[1])
#print popt, pcov
#p.plot(SEC,grafica)

#cop, cze = curve_fit(funcion, SEC, I) ## coeficientes optimizados y covarianza estimada
#print cop
#print cze
#grafica=funcion(SEC, cop[0], cop[1])
#p.plot(SEC,grafica)


#(A,B)=curve_fit(funcion,SEC,I)
#grafica=funcion(A,SEC,B)
#print A,B
#p.plot(SEC,grafica)


#p.show()

