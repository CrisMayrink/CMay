import datetime
from classes.Extratos import Extratos

#codigo da classe
class Contas: # criando a classe conta

    def __init__(self,clientes, numero, saldo):
        self.Extratos = Extratos()
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()


    def depositar(self, valor): #criando o método depositar
        self.saldo = self.saldo + valor
        self.Extratos.transacoes.append(["DEPOSITO", valor, datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False # não tem saldo suficiente
        else:
            self.saldo = self.saldo - valor #saque realizado com sucesso
            self.Extratos.transacoes.append(["SAQUE", valor, datetime.datetime.today()])
            return True

    def transfere_valor(self, conta_destino, valor):
        if self.saldo < valor:
            return 'Saldo insuficiente.'
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            self.Extratos.transacoes.append(["TRANSFERÊNCIA", valor, datetime.datetime.today()])
            return 'Transferência realizada com sucesso.'

    def gerar_saldo(self):
        print(f"Número:{self.numero}\nSaldo:{self.saldo}\n")



