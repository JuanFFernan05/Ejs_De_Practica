# A partir de una cadena elegida por usted, deberá retornar esa cadena quitando alguna subcadena que se encuentre en la misma

palabra = "Cuando menos te lo esperas sale el sol"

print(f"La palabra elegida fue: {palabra}\n")

subcadena = input("Ingrese su subcadena a eliminar: ")
indice = palabra.find(subcadena)

palabraModificada = palabra[:indice] + palabra[indice + len(subcadena) + 1 : ]
print(f"La palabra modificada es: {palabraModificada}")
