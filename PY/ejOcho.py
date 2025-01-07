# Objetivo: imprimir una lista a la inversa sin usar el método reverse(). La lista será pasada por parametro por el usuario.


lista = input("Ingrese una cadena: ")

tamanioLista = len(lista)

for i in range(1, tamanioLista + 1):
    if i == 1:
        print(f"[{lista[-i]}", end=", ")
        continue
    if i == tamanioLista:
        print(f"{lista[-i]}]")
        continue
    print(f"{lista[-i]},", end=" ")
    


print("Listo. Ahora tu lista está al reves\n")




