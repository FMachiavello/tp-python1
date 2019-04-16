

import math
a = float(input("Ingrese a "))
b = float(input("Ingrese b "))
c = float(input("Ingrese c "))

def MaxMin(a,b,c):
    if a < 0:
        xv = (-b/2*a)
        yv = a * xv + b * xv + c * xv
        print("El maximo esta en (",xv,",",yv,")") 
    elif a > 0:
        xv = (-b/2*a)
        yv = a * xv + b * xv + c * xv
        print("El minimo esta en (",xv,",",yv,")") 
    else:
        print("a no puede valer 0 ")
#MaxMin(a,b,c)

def Raices(a,b,c):
    if a==0:
        print("a no puede valer 0")
    else:
        raizmas = ((-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a))
        raizmenos = ((-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a))
        print("Las raices son {",raizmas,",",raizmenos,"}")
Raices(a,b,c)

pendiente = float(input("Ingrese la pendiente de la recta 1 "))
origen = float(input("Ingrese la ordenada origen de la recta 1 "))
pendiente2 = float(input("Ingrese la pendiente de la recta 2 "))
origen2 = float(input("Ingrese la ordenada origen de la recta 2 "))

def Interseccion(pendiente,origen,pendiente2,origen2)
    if pendiente == pendiente2:
        print("son rectas paralelas ")
    else:
        
