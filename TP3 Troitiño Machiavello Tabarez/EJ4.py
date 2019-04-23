import math
l1 = []
l2 = []
l3 = []


def pitagoras(l1, l2, l3):
    """Dada 3 coordenadas devuelve la mas lejana al eje de coordenadas"""
    h1 = math.sqrt(float(l1[0])**2 + float(l1[1])**2)
    h2 = math.sqrt(float(l2[0])**2 + float(l2[1])**2)
    h3 = math.sqrt(float(l3[0])**2 + float(l3[1])**2)
    if(h1 > h2 and h1 > h3):  # Compara si las hipotenusa1 es la mas lejana.
        print("la cordenada mas lejana es (", l1[0], ";", l1[1], ")")
    elif(h2 > h1 and h2 > h3):  # Compara si las hipotenusa2 es la mas lejana.
        print("la cordenada mas lejana es (", l2[0], ";", l2[1], ")")
    else:  # Por descarte la hipotenusa3 es la mas lejana.
        print("la cordenada mas lejana es >>> (", l3[0], ";", l3[1], ")")
for i in range(2):
    if i == 0:
        letra = "x"
    else:
        letra = "y"
    a = input("Ingrese una coordenada " + letra + "1 >>> ")
    l1.append(a)
    b = input("Ingrese una coordenada " + letra + "2 >>> ")
    l2.append(b)
    c = input("Ingrese una coordenada " + letra + "3 >>> ")
    l3.append(c)
pitagoras(l1, l2, l3)
