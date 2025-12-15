from Classe.Conta import Conta
from Classe.Poupança import Poupanca



class ContaRemuneradaPoupanca(Conta, Poupanca):

    def __init__(self, clientes,numero, saldo,  taxa_remuneracao):
        Conta.__init__(self, clientes, numero, saldo)
        Poupanca.__init__(self, taxa_remuneracao)

    def remuneracao(self):
        self.saldo += self.saldo * (self.taxa_remuneracao/30)

