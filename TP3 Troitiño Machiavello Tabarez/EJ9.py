def evaluaciones():
    """Determina si un alumno esta aprobado o desaprobado
    dependiendo el porcentaje necesario para aprobar"""
    """Muestra el porcentaje de preguntas correctas"""
    aprobar = ""
    correctas = ""
    ejercicios = ""
    while correctas != "*" and ejercicios != "*" and aprobar != "*":
        ejercicios = input("¿Cuántos ejercicios tiene la evaluación?: ")
        aprobar = input("¿Cuál es el porcentaje necesario para aprobar?: ")
        correctas = input("¿Cuántas son correctas?: ")
        por = 100 * int(correctas) / ejercicios
        if por >= aprobar:
            print(round(por, 2), "%")
            print("Aprobado")
        elif por < aprobar:
            print(round(por, 2), "%")
            print("Desaprobado")
        correctas = input("""¿Cuántas son correctas?
        (Ingrese '*' para finalizar): """)
evaluaciones()
