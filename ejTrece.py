# Objetivo: crear una matriz desde teclado

filas = int(input("Indicar la cantidad de filas de su matriz: "))
columnas = int(input("Indicar la cantidad de columnas de su matriz: "))

matrix = []

for posicionDeFila in range(filas):
    fila = []
    for element in range(columnas):
        fila.append(int(input(f"Ingrese un elemento a la fila {posicionDeFila}: ")))
    matrix.append(fila)
    print("Fin de fila. \n")    

for row in matrix:
    print(row)