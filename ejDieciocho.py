# JUEGO
# Usted, usuario, deberá pensar un numero (no deberá ser ingresado)
# El programa intentará adivinarlo
# Usted definirá el rango de números (enteros). Tambien le dirá al programa si el numero es mayor, menor, o igual al mostrado.

import random

def numAleatEnRango(num1: int, num2: int):
    numAleat = random.randint(num1, num2)
    return numAleat


minimo = int(input("Ingrese el entero mínimo de su rango (debe ser mayor o igual que 0): "))

if(minimo < 0):
    print("Numero de rango inválido.\n")
    exit()


maximo = int(input("Ingrese el entero máximo de su rango: "))


intentos = int(input("Indique la cantidad de intentos del programa: "))

while intentos <= 0:
    intentos = int(input("Cantidad invalida de intentos. Ingrese nuevamente la cantidad de intentos: "))


for i in range(1, intentos + 1):
    intento = numAleatEnRango(minimo, maximo)
    print(f"Intento {i}: ")
    rtaUsuario = input(f"Numero: {intento}. Es este numero mayor, menor o igual al que pensaste? ")
    rtaUsuario = rtaUsuario.lower()

    if rtaUsuario == "igual":
        print(f"Perfecto. Entonces el numero si era {intento}. \n")
        exit()
    elif rtaUsuario == "menor":
        maximo = intento - 1
        print(f"De acuerdo. Entonces el numero está entre el rango: [{minimo}, {maximo}]")
    elif rtaUsuario == "mayor":
        minimo = intento + 1 
        print(f"De acuerdo. Entonces el numero está entre el rango: [{minimo}, {maximo}]")
    else:
        raise Exception("Reglas no seguidas.")
    
print(f"Intentos terminados. No pude adivinar el numero :(. Quedaban estas opciones: {list(range(minimo, maximo + 1))}")