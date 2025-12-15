import sqlite3 as conector
from criando_class_Bd import Marca 

try:
    conexao = conector.connect('./veiculos_BDados.db')
    cursor = conexao.cursor()

    comando = '''INSERT INTO Marca (nome, sigla) VALUES (:nome, :sigla);'''
   
    marca3 =  Marca(3, 'Hyundai', 'HY')   
    cursor.execute(comando, {'nome': marca3.nome, 'sigla': marca3.sigla})
    marca3.id = cursor.lastrowid
    
    marca4 =  Marca(4, 'Volkswagen', 'VW')   
    cursor.execute(comando, {'nome': marca4.nome, 'sigla': marca4.sigla})
    marca4.id = cursor.lastrowid    
    
    Marca5 =  Marca(5, 'Renault', 'RE')   
    cursor.execute(comando, {'nome': Marca5.nome, 'sigla': Marca5.sigla})
    Marca5.id = cursor.lastrowid
    
    conexao.commit()
    print("Tabela 'Marca' Dados inseridos com sucesso.")

except conector.IntegrityError as e:
    print(f"❌ Erro de integridade (duplicata ou chave estrangeira): {e}")  
except Exception as e:
    print(f"❌ Ocorreu um erro: {e}")   
finally:
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()