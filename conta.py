from cliente import Cliente

class Conta(Cliente):
    def __init__(self, nome, cpf, idade, saldo):
        Cliente.__init__(self, nome, cpf, idade, saldo)

    def deposito(self,dinheiro):
        self.saldo += dinheiro

    def saque(self, dinheiro):
        if self.saldo - dinheiro < 500:
            print('Erro: não existe limite disponíve')
        else:
            self.saldo -= dinheiro