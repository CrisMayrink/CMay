
class Proprietario:
    def __init__(self, id, cpf, nome, nascimento, oculos):
        self.id = id
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.oculos = oculos
       
    
class Marca:
    def __init__(self, id, nome, sigla):
        self.id = id
        self.nome = nome
        self.sigla = sigla
        
class Veiculo:
    def __init__(self, placa, ano, cor, proprietario,  marca, proprietario_id):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.proprietario = proprietario
        self.marca = marca
        self.proprietario_id = proprietario_id