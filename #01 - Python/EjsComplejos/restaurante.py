"""
Un restaurante tiene un sistema donde los clientes pueden hacer pedidos. Cada pedido tiene:

Un número de pedido (entero, único).
Una lista de platos (cada plato tiene un nombre y un precio).
Un estado (pendiente, en preparación, listo).
Objetivo:
Implementar una clase Pedido y una clase Restaurante con las siguientes funcionalidades:

Crear pedidos con un número único y una lista de platos.
Actualizar el estado de un pedido (pendiente → en preparación → listo).
Calcular el total de un pedido (suma de los precios de los platos).
Listar pedidos según su estado.

"""

class Pedido:
    estados = ["pendiente", "en realización", "listo"]

    def __init__ (self, numero, platos):            # ahora podemos instanciar pedidos
        self.numero = numero
        self.platos = platos
        self.estado = self.estados[0]

    def totalDePedido(self):
        return sum(precio for _, precio in self.platos)
    
    def avanzarEstado(self):
        indiceActual = self.estados.index[self.estado]
        if indiceActual < (len(self.estados) - 1):
            self.estado = self.estados[indiceActual + 1]


class Restaurante:
    def __init__(self):                             # ahora podemos instanciar restaurantes
        self.pedidos = []
        self.contadorDePedidos = 1

    def nuevoPedido(self, platos):                  # creación de pedidos
        pedido = Pedido(self.contadorDePedidos, platos)
        self.pedidos.append(pedido)
        self.contadorDePedidos += 1
        return pedido 
    
    def avanzarEstado(self, numeroPedido):
        for pedido in self.pedidos:
            if pedido.numero == numeroPedido:
                pedido.avanzarEstado()
                return f"Pedido {pedido.numero} ahora está en estado {pedido.estado}"
            else:
                return "Pedido no encontrado"
            
    def mostrarPedidos(self):
        return self.pedidos
    

hupaBurguers = Restaurante()

pedido1 = hupaBurguers.nuevoPedido([("Muzzarpada", 15000), ("La macanuda", 8000)])
pedido2 = hupaBurguers.nuevoPedido([("Maquina de guerra", 17000), ("La macanuda", 8000)])

hupaBurguers.avanzarEstado(1)
print(f"{hupaBurguers.avanzarEstado(1)}")