#1)
#28 fichas
a="     "
b="     "
c="     "
def arriba():
        print("╒═══════╕")
        print("│ " + a +" │")
        print("│ " + b +" │")
        print("│ " + c +" │")
        print("│_______│")
def abajo():
        print("│       │")
        print("│ " + a +" │")
        print("│ " + b +" │")
        print("│ " + c +" │")
        print("╘═══════╛")
def numerito(z):
    if z == 0:
        a="     "
        b="     "
        c="     "
    elif z == 1:
        a="     "
        b="  0  "
        c="     "
    elif z == 2:
        a="    0"
        b="     "
        c="0    "
    elif z == 3:
        a="    0"
        b="  0  "
        c="0    "
    elif z == 4:
        a="0   0"
        b="     "
        c="0   0"
    elif z == 5:
        a="0   0"
        b="  0  "
        c="0   0"
    elif z == 6:
        a="0 0 0"
        b="     "
        c="0 0 0"
def domino():
    h = 0
    x = 0
    z = 0
    while z < 28:
        for x in range(0,6): 
            for i in range(0,(7-h)):
                numerito(x)
                arriba()
                numerito(i)
                abajo()
                h = h + 1
    z = z + 1
domino()

"""
palabra = str(input("Ingrese una palabra: "))
for i in range(1,1001):
    print(palabra, end=" ")
print()
print()

#2)

print("0  |  0")
for i in range(6):
    for x in range(7):
        print(x," | ",i + 1)

#3)

n = int(input("Ingrese un numero: "))
suma = 0
for i in range(1, n + 1):
    cont = i
    suma = suma + cont
print(suma)

#4)

c1 = []
c2 = []
c3 = []
for i in range(2):
    a = int(input("Ingrese una coordenada x y luego una y: "))
    c1.append(a)
    b = int(input("Ingrese una coordenada x y luego una y: "))
    c2.append(b)
    c = int(input("Ingrese una coordenada x y luego una y: "))
    c3.append(c)
"""
#5)



#7)

def dias():
    num = int(0)
    if num <= 366 or num >= 0:
        num = input("Ingrese un numero: ")
    else: 
        print("Numero incorrecto")
        num = input("Ingrese un numero: ") 
    cont = 1
    cont = (num / 7)
    sem = num - (7 * round(cont,0))
    if sem == 1:
        print("Lunes")
    elif sem == 2:
        print("Martes")
    elif sem == 3:
        print("Miercoles")
    elif sem == 4:
        print("Jueves")
    elif sem == 5:
        print("Viernes")
    elif sem == 6:
        print("Sabado")
    elif sem == 7:
        print("Domingo")
#dias()           

    

    

                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                

