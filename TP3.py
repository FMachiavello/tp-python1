#1)

def milPalabras(palabra):
    for i in range(1,1001):
        """ Uso el parametro end para que deje un espacio cuando imprima las 
        palabras en la misma linea """
        print(palabra, end=" ")   

#2)

""" Macha """

#3)

def numTriangular(n):
    suma = 0
    for i in range(1, n + 1):
        cont = i
        suma = suma + cont
        print(cont," - ",suma)

#4)

""" Macha """
#5)

""" Diego """

#6)

""" Diego """

#7)

def dias(n):
    """ Variable count devuelve las semanas en numeros enteros """
    cont = n // 7
    """ La variable sem multiplica count por 7 para determinar los dias que hay
    en esa/s semana/s y luego lo resta por la cantidad de dias que 
    se ingreso en num para que de un numero entre 1 y 7 """
    sem = n - (7 * cont)
    """ Dependiendo el numero que da sem determina que dia es """
    if n <= 366 and n > 0:
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

def numRomanos(n):
    """ Variable n es la cantidad de numeros ingresados """
    """ Declaro listas para asignar un numero romano dependiendo la longitud del numero """
    unidad = ["", "I", "II", "III", "IV", "V", "VI", "VII","VIII","IX"]
    dec = ["", "X","XX","XXX","XL", "L", "LX", "LXX", "LXXX", "XC"]
    cent = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    mil = ["", "M", "MM", "MMM", "IV/", "V/", "VI/", "VII/", "VIII/", "IX/"]
    dmil = ["", "X/", "XX/", "XXX/", "XL/", "L/", "LX/", "LXX/", "LXXX/", "XC/"]
    cmil = ["", "C/", "CC/", "CCC/", "CD/", "D/", "DC/", "DCC/", "DCCC/", "CM/"]
    """ Uso el modulo de 10 de n para que recorra los index de las listas """
    u = n % 10
    d = int(n // 10) % 10
    c = int(n // 100) % 10
    m = int(n // 1000) % 10
    dm = int(n // 10000) % 10
    cm = int(n // 100000) 
    if n > 1000000:
        print("Limite 1000000")
    elif n == 1000000:
        print("M//")
    elif n >= 100000:
        print(cmil[cm] + dmil[dm] + mil[m] + cent[c] + dec[d] + unidad[u])
    elif n >= 10000:
        print(dmil[dm] + mil[m] + cent[c] + dec[d] + unidad[u])
    elif n >= 1000:
        print(mil[m] + cent[c] + dec[d] + unidad[u])
    elif n >= 100:
        print(cent[c] + dec[c] + unidad[u])
    elif n >= 10:
        print(dec[d] + unidad[u])
    else:
        print(unidad[n])

n = int(input("Numeros  "))
numRomanos(n)

#9)   

def evaluaciones(aprobar, ejercicios, correctas):
    aprobar = 0
    ejercicios = int(input("¿Cuántos ejercicios tiene la evaluación?: "))  
    while not(aprobar >= 1 and aprobar <= 100):
        aprobar = int(input("¿Cuál es el porcentaje necesario para aprobar?: "))
    correctas = int(input("¿Cuántas son correctas?: "))
    while correctas != "*":
        por = 100 * int(correctas) / ejercicios
        if por >= aprobar:
            print(round(por, 2),"%")
            print("Aprobado")
        elif por < aprobar:
            print(round(por, 2),"%")
            print("Desaprobado")
        correctas = input("¿Cuántas son correctas?(Ingrese '*' para finalizar): ")       
