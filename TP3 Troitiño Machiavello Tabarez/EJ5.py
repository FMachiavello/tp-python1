def MatrizIdentidad(dimension):
    g = []
    for i in range(0,dimension):
        g.append([0]*dimension)
        g[i][i] = 1
    for i in range(0,dimension):
        print (g[i])
