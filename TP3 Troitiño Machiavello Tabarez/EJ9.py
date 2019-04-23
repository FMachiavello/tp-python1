def evaluaciones():
    ejercicios = input("¿Cuántos ej. tiene la evaluación?('*' finalizar): ")
    while ejercicios != "*":
        aprobar = input("¿Con que porcentaje se apruebar?('*'): ")
        while aprobar != "*":
            correctas = input("¿Cuántas son correctas?('*'): ")
            while correctas != "*":
                por = 100 * int(correctas) / int(ejercicios)
                if por >= int(aprobar):
                    print(round(por, 2), "%")
                    print("Aprobado")
                elif por < int(aprobar):
                    print(round(por, 2), "%")
                    print("Desaprobado")
                correctas = input("¿Cuántas son correctas?('*' finalizar): ")
                if correctas == "*":
                    return
evaluaciones()
