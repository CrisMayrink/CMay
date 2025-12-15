import sqlite3
import os

def criar_conectar_bd():
    
    conexao = None
        
    try:#criar o banco de dados e estabelecer a conexao
        conexao = sqlite3.connect('Eventos.db')
        print("Banco de dados 'Eventos.db' criado e conectado com sucesso.")
        return conexao
    except sqlite3.Error as e:
        print(f"Erro ao criar o banco de dados: {e}")
        return None
        
    
def criar_tabelas(conexao):
    if conexao is None:
        print("Conexão inválida. Não é possível criar tabelas.")
        return
    
    cursor = conexao.cursor()
    
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Locais (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    endereco TEXT NOT NULL )
                 ''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS  Eventos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    data DATE NOT NULL, 
                    local_id INTEGER NOT NULL,
                    FOREIGN KEY (local_id) REFERENCES Locais(id)
                    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS  Participantes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    evento_id INTEGER NOT NULL,
                    FOREIGN KEY (evento_id) REFERENCES Eventos(id))''')
                       
    conexao.commit()
    print("Tabelas criadas com sucesso.")

if __name__ == "__main__":
    conexao = criar_conectar_bd()

    if conexao:
        criar_tabelas(conexao)    
        conexao.close()
        print("Conexão com o banco de dados fechada  no final do script.")
    else:
        print("Não foi possível estabelecer a conexão com o banco de dados.")

