import math
l1 = []
l2 = []
l3 = []
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
def pitagoras():
    h1 = math.sqrt(float(l1[0])*float(l1[0]) + float(l1[1])*float(l1[0]))
    h2 = math.sqrt(float(l2[0])*float(l2[0]) + float(l2[1])*float(l2[0]))
    h3 = math.sqrt(float(l3[0])*float(l3[0]) + float(l3[1])*float(l3[0]))
    if(h1 > h2 and h1 > h3):
        print("la cordenada mas lejana es (" ,float(l1[0]) ,";", float(l1[1]),")")
    elif(h2 > h1 and h2 > h3):
        print("la cordenada mas lejana es (" ,float(l2[0]) ,";", float(l2[1]),")")
    else:
        print("la cordenada mas lejana es (" ,float(l3[0]) ,";", float(l3[1]),")")
pitagoras()
