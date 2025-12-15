from classes.Clientes import Clientes
from classes.Contas import Contas


cliente1 = Clientes(cpf='123', nome='Maria', endereco = "rua a")
cliente2 = Clientes(cpf='234', nome='Joao', endereco = "rua x")
cliente3 = Clientes(cpf='345', nome='Joao', endereco = "rua y")
cliente4 = Clientes(cpf='456', nome='Joao', endereco = "rua Z")

conta1 = Contas([cliente1, cliente2], 111, 0)
conta2 = Contas([cliente3, cliente3], 121, 500)

conta1.depositar(1000)
conta1.sacar(100)
conta1.transfere_valor(conta2, 150)
conta1.Extratos.gerar_extrato(conta1.numero)
conta2.Extratos.gerar_extrato(conta2.numero)
conta2.gerar_saldo()

