# OCHOA Briones Daniela melissa
from cuenta import Cuenta_finaciera

class cuenta_ahorro (Cuenta_finaciera):
    def __init__(self, interes: float =0, numero = None , nombre_propietario= None, saldo: float= 0):
        self._interes = interes
        super(cuenta_ahorro, self).__init__(numero=numero, nombrepropietario=nombre_propietario, saldo=saldo)
        
    @property
    def interes (self):
        return self._interes
        
    @interes.setter
    def interes(self, interes):
        self._interes=interes

    def pagar_interes (self):
        self._saldo =self._saldo + ((float(self._saldo)* int(self._interes))/10)
        return self._saldo
if __name__ == '__main__':
    cuenta_ahorro= cuenta_ahorro (8,'0907676768', 'Daniela', '320')

    cuenta_ahorro.mostrar_saldo()
    cuenta_ahorro.credito(1500)

    cuenta_ahorro.mostrar_saldo()
    cuenta_ahorro.debito(40)

    print(cuenta_ahorro)