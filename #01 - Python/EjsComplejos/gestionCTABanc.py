"""
Un banco quiere gestionar cuentas bancarias de clientes. Cada cuenta tiene:

Un número de cuenta (único).
Un titular (nombre del dueño).
Un saldo disponible.
🚀 Objetivo:
Implementar una clase CuentaBancaria y una clase Banco con las siguientes funcionalidades:

Crear cuentas con un número de cuenta, un titular y un saldo inicial.
Depositar dinero en una cuenta.
Retirar dinero, si el saldo lo permite.
Consultar el saldo de una cuenta.
Transferir dinero entre cuentas.
Listar todas las cuentas del banco.

"""


class CuentaBancaria:

    def __init__ (self, numero, titular, saldo):
        self.numero = numero 
        self.titular = titular 
        self.saldo = saldo

    def depositar(self,monto):
        self.saldo += monto

    def retirar(self,monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"${monto} retirado. Saldo actual: {self.saldo}")
        else:
            raise Exception("Monto no disponible para retirar")
        
    def saldoActual(self):
        return self.saldo 



class Banco:

    def __init__ (self, nombre):
        self.nombre = nombre
        self.cuentasActuales = []
        self.numeroDeCuenta = 1
        

    def crearCuenta(self,titular, saldo):
        cuenta = CuentaBancaria(self.numeroDeCuenta, titular, saldo)
        self.numeroDeCuenta += 1
        self.cuentasActuales.append(cuenta)

    def transferencia(self, monto, nroDeCuenta1, nroDeCuenta2):
        try: 
            cuenta1= self.buscarCuenta(nroDeCuenta1)
            cuenta2 = self.buscarCuenta(nroDeCuenta2)
            cuenta1.retirar(monto)
            cuenta2.depositar(monto)
            print("Transferencia completa!")
        except:
            print("Algo salió mal!")

    def listarCuentas(self):
        for cuenta in self.cuentasActuales:
            print(f"Cuenta N° {cuenta.numero}. Titular: {cuenta.titular}. Saldo: ${cuenta.saldo}")
        
    def buscarCuenta(self, numero):
        for cuenta in self.cuentasActuales:
            if (numero != cuenta.numero):
                continue
            else:
                return cuenta

    
santander = Banco("Santander")
santander.crearCuenta("Esteban", 15000)
santander.crearCuenta("Gimenez", 14000)
santander.listarCuentas()
santander.transferencia(5000, 1, 2)
santander.listarCuentas()







