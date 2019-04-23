def numTriangular(n):
        """Calcula los numeros triangulares del numero ingresado"""
suma = 0
for i in range(1, n + 1):
        cont = i
        suma = suma + cont
        print(cont, " - ", suma)
