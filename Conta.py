import datetime
from Classe.Extrato import Extrato

#codigo da classe
class Conta: # criando a classe conta

    def __init__(self,clientes, numero, saldo):
        self.Extrato = Extrato()
        self.clientes = clientes
        self.numero = numero
        self.__saldo = saldo
        self.data_abertura = datetime.datetime.today()

    def depositar(self, valor): #criando o método depositar
        self.__saldo = self.__saldo + valor
        self.Extrato.transacoes.append(["DEPOSITO", valor, datetime.datetime.today()])

    @property  # com esse decorador é possivel acessar o atributo pelo executavel mas não se pode modificar
    def saldo(self):
        return self.__saldo

    @saldo.setter  # com esse decorador é possivel modificar o saldo mas ele ainda fica protegido
    def saldo(self, valor):
        if valor < 0:
            print("Saldo inválido.")
        else:
            self.__saldo = valor

    def sacar(self, valor):
        if self.__saldo < valor:
            return False # não tem saldo suficiente
        else:
            self.__saldo = self.__saldo - valor #saque realizado com sucesso
            self.Extrato.transacoes.append(["SAQUE", valor, datetime.datetime.today()])
            return True

    def transfere_valor(self, conta_destino, valor):
        if self.__saldo < valor:
            return 'Saldo insuficiente.'
        else:
            conta_destino.depositar(valor)
            self.__saldo -= valor
            self.Extrato.transacoes.append(["TRANSFERÊNCIA", valor, datetime.datetime.today()])
            return 'Transferência realizada com sucesso.'

    def gerar_saldo(self):
        print(f"Número:{self.numero}\nSaldo:{self.__saldo}\n")

