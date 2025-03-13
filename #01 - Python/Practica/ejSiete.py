# Aprendizaje de for, in range() 

# Objetivo N°1: dados un numero a y un numero b: mostrar la secuencia de exponenciación a^b

print("PROGRAMA DE POTENCIAS\n".center(50))

base = int(input("Ingrese su base: "))
exponente = int(input("Ingrese su potencia: "))

print(f"Perfecto. Entonces, usted quiere obtener la secuencia de {base} elevado al exponente {exponente}")


for variable in range (1, exponente + 1, 1):

    print(f"{base ** variable}\n")

print("Fin del programa.\n")


"""
# Objetivo N°2: tabla de multiplicar


print("TABLAS DE MULTIPLICAR\n".center(100))

numero = int(input("¿De que numero desea conocer su tabla?: "))
extension = int(input("¿Que tan extensa quiere su tabla?: "))

for i in range(extension):
    print(f"{numero}x{i} = {numero*i}\n")

print("Fin del programa\n")
"""
