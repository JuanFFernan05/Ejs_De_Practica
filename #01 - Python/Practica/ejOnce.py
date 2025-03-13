# Objetivo: dada listaATrabajar, solicitar al usuario que ingrese un carácter por teclado. En caso de que ese elemento esté en la lista, eliminarlo.
# Aclaración: un caracter puede estar mas de 1 vez en una lista

listaATrabajar = ["A", "B", "b", "c", "E", "E", "f"]

print(f"La lista a trabajar es: {listaATrabajar}\n")
caracterAEliminar = input("Ingrese su caracter a eliminar: ")

for i in range(0, len(listaATrabajar) - 1):
    try:
        indice = listaATrabajar.index(caracterAEliminar)
        del listaATrabajar[indice]
    except:
        break           # En caso de no encontrar ninguna coincidencia, cortamos el ciclo

print(f"Listo. La lista ha quedado asi: {listaATrabajar}")    