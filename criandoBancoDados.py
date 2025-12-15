import sqlite3 as conector
import os # Importar o módulo OS é necessário

def main():
    # 1. Definir o caminho completo do banco de dadosa
    
    diretorio_trabalho = r"C:\Users\cmaya\OneDrive\CMAYRINK\Documentos\FACULDADE SISTEMAS DE INT\SCRIPS PYTHON\manipulacaoDados\diretorio_trabalho"
    caminho_banco = os.path.join(diretorio_trabalho, 'veiculos_BDados.db')

    # 2. Garantir que o diretório exista
    if not os.path.exists(diretorio_trabalho):
        os.makedirs(diretorio_trabalho)
        print(f"Diretório '{diretorio_trabalho}' criado.")
    
    # Variáveis iniciais para garantir que existam no bloco finally
    conexao = None
    cursor = None

    try:
        conexao = conector.connect(caminho_banco)
        cursor = conexao.cursor()
        print(f"Conexão estabelecida. Banco de dados '{caminho_banco}' pronto.")
        
        
        comando_proprietario = '''CREATE TABLE  Proprietario(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            CPF INTEGER NOT NULL,           
            nome TEXT NOT NULL,
            nascimento TEXT NOT NULL,
            oculos INTEGER NOT NULL            
        );'''
        
        cursor.execute(comando_proprietario)   
        print("Tabela 'Proprietário' criada ou já existente.")
        
        comando_marca = '''CREATE TABLE IF NOT EXISTS Marca(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            sigla CHARACTER(4) NOT NULL
        );'''
        
        cursor.execute(comando_marca)
        print("Tabela 'Marca' criada ou já existente.")
           
        comando_veiculo = '''
        CREATE TABLE IF NOT EXISTS Veiculo(
            placa CHARACTER(7) NOT NULL PRIMARY KEY,
            ano INTEGER NOT NULL,
            cor TEXT NOT NULL,
            proprietario TEXT NOT NULL,
            marca INTEGER NOT NULL,
            proprietario_id INTEGER NOT NULL,
            
            FOREIGN KEY(proprietario_id) REFERENCES Proprietario(id)
                ON UPDATE CASCADE ON DELETE CASCADE         
        );'''
        cursor.execute(comando_veiculo)
        print("Tabela 'Veiculo' criada ou já existente com chaves estrangeiras.")
        
               
        conexao.commit()
        print("Todas as tabelas criadas com sucesso.")
        
    except conector.DatabaseError as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
    except Exception as e: # Adicionado tratamento para outros erros
        print(f"Ocorreu um erro geral: {e}")

    finally:
        # Verificações de segurança antes de fechar:
        if 'cursor' in locals() and cursor: # Verifica se 'cursor' existe localmente e não é None
            cursor.close()
        if 'conexao' in locals() and conexao: # Verifica se 'conexao' existe localmente e não é None
            conexao.close()
        print("Conexão com o banco de dados fechada.")

if __name__ == "__main__":
    main()
    
    #script funcionou perfeitamente, criando o banco de dados veiculos_Banco.db com as tabelas Marca, Proprietario e Veiculo