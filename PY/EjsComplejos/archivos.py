import os 

directorio = "C:/Users/jfran/OneDrive/Documentos/UTN"

# Listemos los archivos del directorio

try:
    archivos = os.listdir(directorio)
    print(f"Los archivos en {directorio} son: \n")
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        if os.path.isfile(ruta):
            tamaño = os.path.getsize(ruta)
            print(f"Archivo: {archivo} - Tamaño: {tamaño} bytes")
except Exception as e:
    print(f"Error: {e}")