import sqlite3  as conector
import os
from classes_livraria import Livro, Cliente, Pedido

DB_FILE = 'Livraria.db' 

def inserir_dados(conexao):
    cursor = conexao.cursor()
    
    livros = [Livro('Python para Iniciantes', 'John Doe', 39.99),
            Livro('Algoritmos e Estruturas de Dados', 'Jane Smith', 49.99),
            Livro('Inteligência Artificial', 'Alan Turing', 59.99)]    

    clientes = [Cliente('Alice', 'alice@example.com'),
            Cliente('Bob', 'bob@example.com'),
            Cliente('Charlie', 'charlie@example.com')]    

    pedidos = [Pedido(1, 1, 2, '2023-06-15'),
            Pedido(2, 2, 1, '2023-06-16'),
            Pedido(3, 3, 3, '2023-06-17')]    
    
    for livro in livros:
        cursor.execute('INSERT INTO Livros (titulo, autor, preco) VALUES (:titulo, :autor, :preco)', vars(livro))
    
    for cliente in clientes:
        cursor.execute('INSERT INTO Clientes(nome, email) VALUES (:nome, :email)', vars(cliente))
        
    for pedido in pedidos:
        cursor.execute('INSERT INTO Pedidos (cliente_id, livro_id, quantidade, data_pedido) VALUES (:cliente_id, :livro_id, :quantidade, :data_pedido)', vars (pedido))
    conexao.commit()
    print('Dados inseridos com sucesso')
    
    #logica principal
if __name__ == '__main__':
    conexao= None
    cursor= None
    
    try:
        #criar a conexao com o banco de dados
        conexao = conector.connect(DB_FILE)
        print("Conexão com o banco de dados estabelecida.")
        
        #chamar a função para criar as tabelas
        inserir_dados(conexao)
        
    except conector.DatabaseError as e:
        print(f"Erro ao operar o banco de dados: {e}")
        
        if conexao:
            conexao.rollback() #desfazer alterações em caso de erro
    finally:#fechamento seguro
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
            print("Conexão com o banco de dados encerrada.")       
        