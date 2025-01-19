
# Dada una clase simple, mostrar algun atributo de la misma

personas = []

class Persona:
    especie = "Humano"

    def __init__(self, edad, nombre, nacionalidad):
        self.edad = edad
        self.nombre = nombre 
        self.nacionalidad = nacionalidad

juan = Persona(edad = 19, nombre = "Juan", nacionalidad = "Argentina")
fernando = Persona(edad = 40, nombre = "Fernando", nacionalidad = "Uruguay")
martina = Persona(edad = 23, nombre = "Martina", nacionalidad = "Canada")

personas.append(juan)
personas.append(fernando)
personas.append(martina)

print("---EDADES---\n")
for i in range(len(personas)):
    print(f"{personas[i].edad}", end="-")


print("\n---ESPECIES---\n")
for i in range(len(personas)):
    print(f"{personas[i].especie}", end = "-")

