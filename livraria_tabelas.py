import sqlite3  as conector
import os #importar o módulo os para manipulação de caminhos de arquivos

DB_FILE = 'Livraria.db' 
  
def criar_tabelas(conexao):  
    cursor = conexao.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                preco REAL NOT NULL)''')

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Clientes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL)''')
                
    cursor.execute('''    
                CREATE TABLE IF NOT EXISTS Pedidos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER NOT NULL,
                livro_id INTEGER NOT NULL,
                quantidade INTEGER NOT NULL,
                data_pedido TEXT NOT NULL, 
                FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
                FOREIGN KEY (livro_id) REFERENCES Livros(id))'''
                    )
        
    conexao.commit()
    print("Tabelas criadas com sucesso.")
    
    #logica principal
if __name__ == '__main__':
    conexao= None
    cursor= None
    try:
        #criar a conexao com o banco de dados
        conexao = conector.connect(DB_FILE)
        print("Conexão com o banco de dados estabelecida.")
        
        #chamar a função para criar as tabelas
        criar_tabelas(conexao)
        
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
        
    

        