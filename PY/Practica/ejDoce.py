# Dada la lista [1, 2, 3, 4, 5], eliminar el primer y ultimo elemento de la lista. Posteriormente, mostrar por pantalla dos listas: aquella con los elementos eliminados y otra con los elementos que siguen en la misma

lista = [1, 2, 3, 4, 5]

primerElemento = lista.pop()
segundoElemento = lista.pop(0)

otraLista = []

otraLista.append(primerElemento)
otraLista.append(segundoElemento)
otraLista.sort()        # Ya que estamos, ordenemosla.

print(f"Lista original: {lista}\n")
print(f"Lista secundaria: {otraLista}\n")