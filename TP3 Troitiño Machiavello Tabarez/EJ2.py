def domino():
    """ 28 fichas de domino """
    z = 0
    for i in range(0,28):
            if i <= 6:
                a = "     "
                b = "     "
                c = "     "
                h = 1
            elif i <= 12:
                a = "     "
                b = "  0  "
                c = "     "
                h = 2
            elif i <= 17:
                a = "    0"
                b = "     "
                c = "0    "
                h = 3
            elif i <= 21:
                a = "    0"
                b = "  0  "
                c = "0    "
                h = 4
            elif i <= 24:
                a = "0   0"
                b = "     "
                c = "0   0"
                h = 5    
            elif i <= 26:
                a = "0   0"
                b = "  0  "
                c = "0   0"
                h = 6
            elif i == 27:
                a = "0 0 0"
                b = "     "
                c = "0 0 0"
                h = 5
            print ("╒═════╕")
            print ("│"+ a +"│")
            print ("│"+ b +"│")
            print ("│"+ c +"│")   
            print ("╞═════╡")
            if z == 0:
                a = "     "
                b = "     "
                c = "     "
            elif z == 1:
                a = "     "
                b = "  0  "
                c = "     "
            elif z == 2:
                a = "    0"
                b = "     "
                c = "0    "
            elif z == 3:
                a = "    0"
                b = "  0  "
                c = "0    "
            elif z == 4:
                a = "0   0"
                b = "     "
                c = "0   0"    
            elif z == 5:
                a = "0   0"
                b = "  0  "
                c = "0   0"
            elif z == 6:
                a = "0 0 0"
                b = "     "
                c = "0 0 0"
            print ("│"+ a +"│")
            print ("│"+ b +"│")
            print ("│"+ c +"│")     
            print ("╘═════╛")
            z = z + 1
            if z == 7:
                z = 0 + h
domino()
        
