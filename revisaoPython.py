class EndSimples (object):
    def __init__(self,rua, num, bairro):
        self.rua = rua
        self.num = num
        self.bairro = bairro

    def endereco(self):
        return self.rua, self.num, self.bairro

class EndCom(EndSimples):
    com: object

    def __init__(self, rua, num, bairro,com):
        EndSimples.__init__(self, rua, num, bairro)
        self.com = com

    def endereco(self):
        return EndSimples.endereco, self.com

#a = EndSimples( "x,28, Palmeiras")
#b= EndCom("y,28,Industrial, sl3")

#print(a.endereco())
#print(b.endereco())