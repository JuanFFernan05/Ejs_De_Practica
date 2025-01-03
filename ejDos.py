# SENTENCIAS CONDICIONALES ANIDADAS

print("========================")
print("CONVERSOR")
print("========================\n")

print("Opcion 1: Conversor de letras a numeros")
print("Opcion 2: Conversor de numeros a letras")

eleccion = int(input("¿Que opción desea?"))

if (eleccion == 1):
    palabra = input("¿Que numero desea conocer?\n")

    if palabra == "Uno":
            print("El numero es 1")
    elif palabra == "Dos":
            print ("El numero es 2")
    else:
            print("Numero desconocido")
elif (eleccion == 2):
    entero = int(input("¿Que palabra desea conocer"))

    if entero == 1:
        print("La palabra es 'Uno' ")
    elif entero == 2:
        print ("La palabra es 'Dos' ")
    else:
        print("Entero desconocido")
else:
      print("Elija una opción viable")

print ("Fin del programa.")






