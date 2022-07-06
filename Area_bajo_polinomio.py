import numpy as np
import matplotlib.pyplot as plt
print("Este programa obtiene el area bajo un polinimo")
Coeff=str(input("Ingrese los coeficienets del polinomio -incluidos los elementos cero-: an,an-1,...,a2,a1: "))
Coeff=np.array(Coeff.split(","), dtype=float)
#limites
print("Ingrese los limites de integracion, recuerde que A<B")
B=float(input("Ingrese el limite B: "))
A=float(input("Ingrese el limite A: "))
#Transformacion lineal
MAT=np.zeros((len(Coeff),len(Coeff)), dtype=float)
INV=np.arange(len(Coeff),0,-1)
for i in range(len(Coeff)):
    for j in range(len(Coeff)):
        MAT[i][i]=1/INV[i]
Row=np.zeros(len(INV), dtype=float)
MAT=np.append(MAT, [Row], axis=0)
#Producto
Coeff_n=np.matmul(MAT, Coeff, dtype=float)
#Evaluacion
def Horner(VAL):
    K=Coeff_n[0]
    for i in range(1, len(Coeff_n)):
        K=(K*VAL)+Coeff_n[i] 
    return K
Area=Horner(B)-Horner(A)
print("El area bajo el polinomio delimitada por {B} y {A} es: {Area}u".format(B=B, A=A, Area=Area))




#Plot
#PLOT_START=A-(A*0.1)
#PLOT_END=B+(B*0.1)
#X=np.arange(A, B+1)
#Y=[]
#for x in X:
 #   y=Horner

"""
Por ahora horner corre solo con una lista de coeficientes, que es la del polinomio interal, sin embargo si quieor graficar la funcion
debo de usar horer con el polinomio poriginal, agregar esto como parametro

"""    









    

