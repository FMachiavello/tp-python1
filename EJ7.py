def dias(n):
    """ Variable count devuelve las semanas en numeros enteros """
    cont = n // 7
    sem = n - (7 * cont)
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
