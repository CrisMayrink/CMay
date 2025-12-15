from Classe.Conta import Conta
from Classe.Cliente import Cliente
import datetime


class ContaEspecial(Conta): # a herança traz os atributos da superclasse.

    def __init__(self, clientes, numero, saldo, limite): #atributos da superclasse
        super().__init__(clientes, numero, saldo) # super é a classe conta, classe mãe.
        self.limite = limite
        self.numero = numero
        self.saldo = saldo

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print(f"Não existe saldo suficiente na conta número {self.numero}, CPF:  {self.clientes.cpf}")
            return False
        else:
            self.saldo -= valor #saque realizado com sucesso
            if self.saldo < 0:
                self.limite = self.saldo
            self.Extrato.transacoes.append(["SAQUE", valor, datetime.datetime.today()])
            return True

        #essa conta recebe por herança os metodos, gerar_saldo, transfere_valor, depositar.
        #apenas os metodos que seráo modificados precisam ser sobrescritos na nova classe
