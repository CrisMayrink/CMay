from abc import ABC, abstractmethod



class ContaCliente(ABC):

    def __init__(self, numero,  IOF, IR,  vlr_investido, taxa_rendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.vlr_investido = vlr_investido
        self.taxa_rendimento = taxa_rendimento

    @abstractmethod
    def calculo_rendimento(self):


     def extrato(self):
        print(f"O saldo atual da conta {self.numero} é {self.vlr_investido:10.2f}.")