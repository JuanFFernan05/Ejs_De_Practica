# Objetivo: bastante sencillo - contaremos hasta un numero particular

numero = int(input("¿Hasta qué numero quiere contar?:"))

for i in range(1, numero + 1):
    print(f"{i}")

print("Fin. Terminamos de contar.\n")