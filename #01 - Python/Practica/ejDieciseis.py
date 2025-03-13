# Definir el maximo de tres numeros, en una funcion. Sin usar max()


def custom_max_tresNum(primerNum: int, segundoNum: int, tercerNum: int):
    if(primerNum > segundoNum and primerNum > tercerNum):
        return primerNum
    elif (segundoNum > tercerNum):
        return segundoNum
    elif (tercerNum > segundoNum):
        return tercerNum
    else:
        raise Exception("Los numeros no pueden ser iguales")
    

numeroUno = int(input("Ingrese el primer numero: "))
numeroDos = int(input("Ingrese el segundo numero: "))
numeroTres = int(input("Ingrese el tercer numero: "))

print(f"De los ingresados, el mayor numero fue el {custom_max_tresNum(numeroUno, numeroDos, numeroTres)}\n")
