"""
La compañia multinacional RAPPI nos solicita desarrollar un sistema que determine la cantidad de días de vacaciones para un trabajador.
Esta cantidad de días dependerá de 2 factores: la antiguedad y la jerarquía

- Departamento de 'Atención al Cliente' (clave 1):
    - Con 1 año de servicio, reciben 6 días de vacaiones
    - De 2 a 6 años de servicio, reciben 14 días de vacaciones
    - A partir de 7 años, reciben 20 días de vacaciones

- Departamento de 'Logística' (clave 2):
    - Con 1 año de servicio, reciben 7 días de vacaiones
    - De 2 a 6 años de servicio, reciben 15 días de vacaciones
    - A partir de 7 años, reciben 22 días de vacaciones

- Gerencia (clave 3):
    - Con 1 año de servicio, reciben 10 días de vacaiones
    - De 2 a 6 años de servicio, reciben 20 días de vacaciones
    - A partir de 7 años, reciben 30 días de vacaciones

El sistema debe solicitar: nombre del empleado, antiguedad y jerarquía (segun clave)
El sistema debe devovler: el nombre del empleado + sus dias de vacaciones

"""

print("======================")
print("SISTEMA DE DETERMINACIÓN DE DÍAS VACACIONALES")
print("======================\n")


nombre = input("Ingrese su nombre, por favor: ")
antiguedad = int(input("Excelente " + nombre + ", ahora ingrese su antiguedad (en años): "))

print("Por ultimo, debe ingresar su área de trabajo según el siguiente menú: ")
print("1: Departamento de 'Atención al Cliente'\n")
print("2: Departamento de 'Logística'\n")
print("3: Gerencia \n")

area = int(input("Ingrese su número de área: "))

if area == 1:
    if 2 > antiguedad > 1:
        diasVacacionales = 6
    elif 6 >= antiguedad >= 2:
        diasVacacionales = 14
    elif antiguedad >= 7:
        diasVacacionales = 20
    else:
        diasVacacionales = 0

elif area == 2:
    if 2 > antiguedad > 1:
        diasVacacionales = 7
    elif 6 >= antiguedad >= 2:
        diasVacacionales = 15
    elif antiguedad >= 7:
        diasVacacionales = 22
    else:
        diasVacacionales = 0

elif area == 3:
    if 2 > antiguedad > 1:
        diasVacacionales = 10
    elif 6 >= antiguedad >= 2:
        diasVacacionales = 20
    elif antiguedad >= 7:
        diasVacacionales = 30
    else:
        diasVacacionales = 0

else:
    print("Clave de área incorrecta")
    exit()

print("Nombre: " + nombre + " - Dias de vacaciones asignados: ", diasVacacionales)



"""
ACLARACION: hay una descarada repetición de lógica. A la fecha que hago este ejercicio (3/1/2025), no he visto el desarrollo de métodos en Python
"""