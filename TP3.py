#1)

""" Complete """
palabra = str(input("Ingrese una palabra: "))
for i in range(1,1001):
    print(palabra, end=" ")
print()
print()

#2)

""" Macha """

#3)

""" En este faltan cosas """
n = int(input("Ingrese un numero: "))
suma = 0
for i in range(1, n + 1):
    cont = i
    suma = suma + cont
print(suma)

#4)

""" Macha """

#6)

""" Diego """

#7)

""" Complete """
def dias(num):
    cont = num / 7
    sem = num - (7 * round(cont))
    if num <= 366 and num > 0:
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
    else: 
        print("Numero incorrecto")

#8)   

