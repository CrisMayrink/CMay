import sqlite3 as conector
import os

DB_FILE = 'Livraria.db'# caminho do arquivo do banco de dados

def exibir_pedidos(conexao):
    cursor = conexao.cursor()#criar um cursor para executar comandos SQL
    #consulta SQL com JOIN para obter informações dos pedidos, clientes e livros
    query =  '''
    SELECT Pedidos.id, Clientes.nome, Livros.titulo, Pedidos.quantidade, Pedidos.data_pedido
    FROM Pedidos
   
    JOIN Clientes ON Pedidos.cliente_id = Clientes.id
    
    JOIN Livros ON Pedidos.livro_id = Livros.id
    '''
    
    cursor.execute(query) #executar a consulta SQL
    pedidos = cursor.fetchall()#buscar todos os resultados da consulta
    
    print("Pedidos realizados:")
    for pedido in pedidos:#iterar sobre os resultados e exibir as informações
        print(pedido)
    
if __name__ == '__main__':
    conexao = None
        
try:
    #criar a conexao com o banco de dados
    conexao = conector.connect(DB_FILE)
    print("Conexão com o banco de dados estabelecida.")
    
    #chamar a função para exibir os pedidos
    exibir_pedidos(conexao) 

except conector.DatabaseError as e:
    print(f"Erro ao operar o banco de dados: {e}")
    
    if conexao:
        conexao.rollback() #desfazer alterações em caso de erro
finally:#fechamento seguro
    if conexao:
        conexao.close()
        print("Conexão com o banco de dados encerrada.")

