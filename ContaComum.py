from Classes.ContaCliente import ContaCliente

class ContaComum(ContaCliente):

    def __ini__(self,  numero, IOF, IR, vlr_investido, taxa_rendimento):
        super().__init__(self, numero, IOF, IR, vlr_investido, taxa_rendimento)

    def calculo_rendimento(self):
        remuneracao = self.vlr_investido * self.taxa_rendimento
        valorIOF = remuneracao * self.IOF
        self.vlr_investido += remuneracao - valorIOF

    def extrato(self):
        print(f"O saldo atual da conta {self.numero} é {self.vlr_investido:10.2f}.")

