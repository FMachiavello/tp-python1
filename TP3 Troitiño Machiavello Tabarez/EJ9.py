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
