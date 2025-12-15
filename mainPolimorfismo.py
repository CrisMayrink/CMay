from Classes.ContaCliente import ContaCliente
from Classes.Banco import Banco
from Classes.ContaComum import ContaComum
from Classes.ContaRemunerada import ContaRemunerada


banco1 = Banco(999, "Teste")

conta_cliente1 = ContaCliente(1, 0.01, 0.1,2000, 0.01 )
conta_comum1 = ContaComum(2, 0.01, 0.1,2000, 0.02 )
conta_remunerada1 = ContaRemunerada(3, 0.01, 0.1,2000, 0.05 )

banco1.adiciona_conta(conta_cliente1)
banco1.adiciona_conta(conta_comum1)
banco1.adiciona_conta(conta_remunerada1)

banco1.calcular_rendimento_mensal()
banco1.imprime_saldo_contas()

