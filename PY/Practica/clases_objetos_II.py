# Introducción a métodos en py.


class Auto:
    def __init__(self, marca, año, nombre):
        self.nombre = nombre
        self.marca = marca 
        self.año = año 

    def valor(self):        # Suponemos, de forma muy práctica, que el valor de un automóvil es 1.5 de su año 
        return self.año * 1.5
    
    def presentacion(self):
        return f"Presentamos al nuevo {self.nombre}. El mismo, de la marca {self.marca}, está cotizado en U$S {self.valor()}"


golCountry = Auto(marca = "Volkswagen", año = 2005, nombre = "Gol Country")
print(golCountry.presentacion())