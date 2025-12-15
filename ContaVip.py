from Classes.ContaCliente import ContaCliente


class ContaVip(ContaCliente):

    def __init__(self, numero, IOF, IR, valor_investido, taxa_rendimento):
        super().__init__(numero, IOF, IR, valor_investido, taxa_rendimento)


    def calculo_rendimento(self):
        self.vlr_investido += self.vlr_investido * self.taxa_rendimento

    def extrato(self):
        print(f"O saldo atual da conta {self.numero} é {self.vlr_investido:10.2f}.")
