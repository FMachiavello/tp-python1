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

