def evaluaciones(aprobar, ejercicios, correctas):
    aprobar = ""
    correctas = ""
    ejercicios = ""
    while correctas != "*" and ejercicios != "*" and aprobar != "*":
        ejercicios = input("¿Cuántos ejercicios tiene la evaluación?: ")
        aprobar = input("¿Cuál es el porcentaje necesario para aprobar?: ")  
        while not(aprobar >= 1 and aprobar <= 100):
            aprobar = int(input("¿Cuál es el porcentaje necesario para aprobar?: "))
    	correctas = int(input("¿Cuántas son correctas?: "))
        por = 100 * int(correctas) / ejercicios
	""" Imprime por pantalla el porcentaje de respuestas correctas y si esta 
    	aprobado o no """
        if por >= aprobar:
            print(round(por, 2),"%")
            print("Aprobado")
        elif por < aprobar:
            print(round(por, 2),"%")
            print("Desaprobado")
        correctas = input("¿Cuántas son correctas?(Ingrese '*' para finalizar): ") 
