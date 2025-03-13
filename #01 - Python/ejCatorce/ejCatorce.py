
# Rehacemos el ejTres.py, ahorrando logica.
# Importamos

from funcionesCatorce import vacacionesParaAsentados, vacacionesParaExperimentados, vacacionesParaIngresantes

print("======================")
print("SISTEMA DE DETERMINACIÓN DE DÍAS VACACIONALES")
print("======================\n")


aniosDeServicio = int(input("Ingrese sus años de servicio: "))
numeroDeArea = int(input("Ingrese su numero de area: "))



if(aniosDeServicio == 1):
    print(f"Dias de vacaciones asignados: {vacacionesParaIngresantes(numeroDeArea)}")
elif (6 > aniosDeServicio > 2):
    print(f"Dias de vacaciones asignados: {vacacionesParaAsentados(numeroDeArea)}")
else:
    print(f"Dias de vacaciones asignados: {vacacionesParaExperimentados(numeroDeArea)}")

