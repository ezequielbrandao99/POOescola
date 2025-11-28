class conta:

    def __init__(self, saldo):
        self.__saldo = saldo  # privado

    @property
    def saldo(self):
        return self.__saldo # getter
    
    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Saldo não pode ser negativo")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

conta2 = conta(500)
print('saldo inicial:', conta2.saldo)

conta2.saldo = -300 #tentativa invalida
print('saldo apos tentativa externa:', conta2.saldo)

conta2.depositar(300)
print('saldo apos deposito:', conta2.saldo)