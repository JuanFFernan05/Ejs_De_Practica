# Dado un numero aleatorio elegido por el programa, el usuario tendrá 5 intentos para adivinar aquel numero. 
# Se podrá elegir un nivel de dificultad. Cuanto mayor sea el nivel, mayor será el rango

import random


print("1: Fácil.\n")
print("2: Medio. \n")
print("3. Díficil. \n")
dificultad = int(input("Elija su nivel de dificultad: "))

if(dificultad == 1):
    print("Dificultad: Fácil. - Su rango será entre el 1 y el 7")
    numero = random.randint(1,7)
elif(dificultad == 2):
    print("Dificultad: Medio. - Su rango será entre el 1 y el 12")
    numero = random.randint(1,12)
elif (dificultad == 3):
    print("Dificultad: Díficil. - Su rango será entre el 1 y el 25")
    numero = random.randint(1,25)
else:
    raise Exception("Opcion incorrecta")

print("HORA DE ADIVINAR!\n")

for i in range (1,6):
    eleccion = int(input(f"Intento {i}/5: "))

    if(eleccion == numero):
        print(f"Has ganado. El numero era {numero}")
        exit()

    print("Incorrecto\n")
    print("\n")
    
print(f"Lo siento. Has perdido. El numero era {numero}\n")        
