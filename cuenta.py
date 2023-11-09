#cuenta
class Cuenta_finaciera:
    def __init__(self, numero, nombre_propietario, saldo):
        self.numero = numero
        self.nombre_propietario = nombre_propietario
        self.saldo = saldo
    def __str__(self):
        return f' Cuentas Bancarias: {self.__dict__.__str__() }'

    def credito(self, valor):
        self.saldo += valor

    def debito(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("No se puede realizar la operación. El saldo es insuficiente.")

    def mostrar_saldo(self):
        print(f"Saldo de la cuenta {self.numero} de {self.nombre_propietario}: {self.saldo}")