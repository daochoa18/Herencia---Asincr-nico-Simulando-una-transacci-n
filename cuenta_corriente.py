
from cuenta import Cuenta_finaciera 

class cuenta_corriente (Cuenta_finaciera):
    def __init__(self, numero= None, nombrepropietario= None, saldo:float= 0, tiene_cheque=bool):
        self._tiene_cheque= tiene_cheque
        super(cuenta_corriente, self).__init__(numero=numero, nombrepropietario=nombrepropietario, saldo=saldo)


    @property
    def tiene_cheque(self):
            return self._tiene_cheque
        
    @tiene_cheque.setter
    def tiene_cheque(self, tiene_cheque):
            self._tiene_cheque = tiene_cheque
            return self._saldo
        
    def pagar_cheque(self):
            self._saldo = self._saldo + ((float (self._saldo) - int (self._pagar_cheque)))
            return self._saldo
if __name__=='__main__':
    Cuentas_corriente = cuenta_corriente('096835874', 'Daniela', '150', bool)

    cuenta_corriente.mostrar_saldo()
    cuenta_corriente.credito(1500)

    cuenta_corriente.mostrar_saldo()
    cuenta_corriente.debito(40)

    print(cuenta_corriente)
            
        


  


     