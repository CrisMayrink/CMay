class Conta:

    __total_contas =  0 #atributo de classe, conta o num de contas (0bjetos) abertas no executavel

    @classmethod #decorador para dar acesso ao __total_contas
    def get_total_contas(cls):
        return cls.__total_contas


    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo
        type(self).__total_contas += 1

    @staticmethod #podem ser acessados dentro da classe sem ter objeto pra ele
    def nome_banco( ):
        return "Banco Guanabara"


    @property #com esse decorador é possivel acessar o atributo pelo executavel mas não se pode modificar
    def saldo(self):
        return self.__saldo

    @saldo.setter  #com esse decorador é possivel modificar o saldo mas ele ainda fica protegido
    def saldo(self, valor):
        if valor < 0:
            print("Saldo inválido.")
        else:
            self.__saldo = valor

    def sacar(self,valor):
        if self.__saldo < valor:
            return False
        else:
            self.__saldo -= valor
            return True

    def gerar_saldo(self):
        print(f"Conta: {self.__numero}")
        print(f"Saldo: R${self.__saldo:10.2f}")

