import sqlite3 as conector
import os # Importar o módulo OS é necessário

def main():
    # 1. Definir o caminho completo do banco de dadosa
    
    diretorio_trabalho = r"C:\Users\cmaya\OneDrive\CMAYRINK\Documentos\FACULDADE SISTEMAS DE INT\SCRIPS PYTHON\manipulacaoDados\diretorio_trabalho"
    caminho_banco = os.path.join(diretorio_trabalho, 'meu_Banco.db')

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

        comando = '''CREATE TABLE Veiculo(
            placa CHARACTER(7) NOT NULL PRIMARY KEY,
            ano INTEGER NOT NULL,
            cor TEXT NOT NULL,
            motor REAL NOT NULL,
            proprietario_id INTEGER NOT NULL,
            marca INTEGER NOT NULL,
            FOREIGN KEY (proprietario_id) REFERENCES Proprietario (id),
            FOREIGN KEY (Marca) REFERENCES Marca (id)
            )'''
            
        cursor.execute(comando)
        conexao.commit()
        print("Tabela 'Veículo' criada com sucesso.")  
        
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