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
