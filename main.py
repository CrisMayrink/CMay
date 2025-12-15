from Classe.Cliente import  Cliente
from Classe.Conta import Conta
from Classe.ContaEspecial import ContaEspecial
from Classe.ContaRemuneradaPoupanca import ContaRemuneradaPoupanca



cliente1 = Cliente(cpf='123', nome='Maria', endereco = "rua a")
cliente2 = Cliente(cpf='234', nome='Joao1', endereco = "rua x")
cliente3 = Cliente(cpf='345', nome='Joao2', endereco = "rua y")
cliente4 = Cliente(cpf='789', nome='Joao', endereco = "rua Z")

conta1 = Conta([cliente1, cliente2], 111, 0)
conta2 = ContaRemuneradaPoupanca([cliente3], 121, 500, 0.5)
conta3 = ContaEspecial([cliente4], 456, 1000, 1000)


conta2.remuneracao()
conta2.sacar(100)
conta2.transfere_valor(conta3, 200)
conta2.depositar(1000)
conta2.Extrato.gerar_extrato(conta2)
conta2.gerar_saldo()
