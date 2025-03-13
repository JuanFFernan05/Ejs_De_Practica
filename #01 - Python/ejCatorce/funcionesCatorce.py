def vacacionesParaIngresantes(area):
    if area == 1:
        return 6
    elif area == 2:
        return 7
    elif area == 3:
        return 10
    else:
        print("Numero de área ingresado: incorrecto\n")
        exit()

def vacacionesParaAsentados(area):
    if(area == 1):
        return 14
    elif (area == 2):
        return 15
    elif(area == 3):
        return 20
    else:
        print("Numero de área ingresado: incorrecto\n")
        exit()

def vacacionesParaExperimentados(area):
    if(area == 1):
        return 20
    elif (area == 2):
        return 22
    elif(area == 3):
        return 30
    else:
        print("Numero de área ingresado: incorrecto\n")
        exit()