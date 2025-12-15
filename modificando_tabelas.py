import sqlite3 as conector
import os # Importar o módulo OS é necessário

caminho_banco = os.path.join(r"C:\Users\cmaya\OneDrive\CMAYRINK\Documentos\FACULDADE SISTEMAS DE INT\SCRIPS PYTHON\manipulacaoDados\diretorio_trabalho", 'veiculos_Banco.db')


try:
    conexao =  conector.connect(caminho_banco)
    cursor = conexao.cursor()
    
    print('Conexão ao banco de dados estabelecida com sucesso.')
    
    comando_adicionar_fk = '''
    ALTER TABLE Veiculo 
    ADD COLUMN proprietario_id INTEGER REFERENCES Proprietario(id) 
    '''
    
    cursor.execute(comando_adicionar_fk)
    conexao.commit()
    print("✅ Chave estrangeira 'proprietario_id' adicionada com sucesso.")

except conector.OperationalError as e:
    # Este erro ocorre se a coluna já existir ou se a tabela Proprietario não existir
    if "duplicate column name" in str(e):
        print("ℹ️ A coluna 'proprietario_id' já existe na tabela 'Veiculo'. Pulando.")
    else:
        print(f"❌ Erro operacional ao adicionar chave estrangeira: {e}")
except Exception as e:
    print(f"❌ Erro inesperado: {e}")

finally:
        # Verificações de segurança antes de fechar:
        if 'cursor' in locals() and cursor: # Verifica se 'cursor' existe localmente e não é None
            cursor.close()
        if 'conexao' in locals() and conexao: # Verifica se 'conexao' existe localmente e não é None
            conexao.close()
        print("Conexão com o banco de dados fechada.")

