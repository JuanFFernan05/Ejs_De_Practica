# Gestión simple de un curso de alumnos
# Objetivo: manejar de forma simple funciones, listas y ciclos


listaDeAlumnos = []
listaDeInformacion = []

def aniadirAlumno(alumno):
    listaDeAlumnos.append(alumno)

def aniadirInformacion (infoGeneral):       # una tupla
    listaDeInformacion.append(infoGeneral)

cantidad = int(input("Cuantos alumnos tiene en su clase? : "))
print("Perfecto. Ahora, mencione el apellido de cada uno de ellos. \n")

for i in range(1, cantidad + 1):
    alumno = input(f"Alumno N° {i}: ")
    aniadirAlumno(alumno)

print(f"Lista de alumnos: {listaDeAlumnos}\n")

print("Ahora. A calificar :) \n")

for i in range(0, len(listaDeAlumnos)):
    nota = int(input(f"Nota de {listaDeAlumnos[i]}: "))
    infoGeneral = (listaDeAlumnos[i], nota)
    aniadirInformacion(infoGeneral)

print(f"Listo. Aqui tienes la información general de tu curso: {listaDeInformacion}")


