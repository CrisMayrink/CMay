
class Livro:
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor   
        self.preco = preco
        
        
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        
class Pedido:
    def __init__ (self, cliente_id, livro_id, quantidade, data_pedido):
        self.cliente_id = cliente_id
        self.livro_id = livro_id
        self.quantidade = quantidade
        self.data_pedido = data_pedido  
        