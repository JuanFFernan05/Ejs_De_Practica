# MANEJO DE DICCIONARIOS

# Supongamos que estamos a cargo de registrar los datos de varios clientes en el banco. En funcion de una primary_key, tendremos que devolver el DNI de esa persona.

diccionarioDeIDS = {1: [24214904, "Federico Prete"], 2: [8092410, "Emanuel Garante"], 3: [31900001, "Juan Fernández"]}

print("------TUPLAS------\n")
print(f"{list(diccionarioDeIDS.items())}\n")

print("------KEYS------")
print(f"{list(diccionarioDeIDS.keys())}\n")

print("------ELEMENTOS------")
print(f"{list(diccionarioDeIDS.values())}\n")