import sqlite3 as conector
import os # Importar o módulo OS é necessário

def main():
    # 1. Definir o nomedo banco de dadosa
    DB_FILE = 'Livraria.db'
   #pasta = './diretorio_trabalho'
   #caminho_banco = os.path.join(pasta, DB_FILE)
    caminho_banco = DB_FILE

    conexao = None
    cursor = None
    try:
       # AQUI O BANCO DE DADOS É CRIADO AUTOMATICAMENTE SE NÃO EXISTIR
       conexao = conector.connect(caminho_banco)
       cursor = conexao.cursor()

       print(f"Conexão estabelecida. Banco de dados Livraria '{caminho_banco}' criado ou pronto.")

       
       conexao.commit() 
       
    except conector.DatabaseError as e:
            print(f"❌ Erro ao operar no banco de dados: {e}")
       
    finally:
    # Fechamento seguro da conexão
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
            print("Conexão com o banco de dados fechada.")

if __name__ == "__main__":
    main()