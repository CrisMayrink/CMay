import sqlite3 as conector


try:
    conexao = conector.connect('./veiculos_BDados.db')
    cursor = conexao.cursor()

    print("Tentando excluir linhas 2 a 10 da tabela 'Marca'...")
        
    # Definir o intervalo de IDs
    id_inicio = 2
    id_fim = 16

    # Comando SQL DELETE usando BETWEEN com placeholders (?)
    comando_delete = '''
    DELETE FROM Marca WHERE id BETWEEN ? AND ?;
    '''
    
    # Executa o comando, passando o intervalo de IDs como uma tupla
    cursor.execute(comando_delete, (id_inicio, id_fim))
    conexao.commit()

    print(f"✅ Registros de ID {id_inicio} a {id_fim} excluídos com sucesso.")
    print(f"   Total de linhas excluídas: {cursor.rowcount}")

except conector.OperationalError as e:
    print(f"❌ Erro operacional ao excluir: {e}")
except Exception as e:
    print(f"❌ Ocorreu um erro inesperado: {e}")

finally:
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()

