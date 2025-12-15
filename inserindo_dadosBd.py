import sqlite3 as conector
from criando_class_Bd import Proprietario

conexao = conector.connect('./veiculos_BDados.db')
cursor = conexao.cursor()

# >>>>> ADICIONADO AQUI: Cria a tabela se ela não existir <<<<<
comando_criar_tabela = '''
CREATE TABLE IF NOT EXISTS Proprietario (
    id TEXT NOT NULL PRIMARY KEY,
    cpf INTEGER NOT NULL UNIQUE,
    nome TEXT NOT NULL,
    nascimento TEXT,
    oculos INTEGER
);'''
cursor.execute(comando_criar_tabela)
conexao.commit()
print("Tabela 'Proprietario' verificada/criada.")
# <<<<< FIM DO CÓDIGO ADICIONADO <<<<<

proprietario1 = Proprietario('007', 25814736458, 'Luzia Mayrink', '10-04-1945', True)
proprietario2 = Proprietario('008', 25814738900,  'Anita Souza', '10-04-1975', False)
proprietario3 = Proprietario('009', 25814738901, 'Carlos Silva', '15-08-1980', False)
proprietario4 = Proprietario('010', 25814738902,  'Mariana Lima', '22-11-1990', True)
proprietario5 = Proprietario('011', 25814738903, 'Fernando Costa', '05-05-1985', False) 

# ... (restante do código de inserção permanece o mesmo) ...

lista_de_proprietarios_dados = [
    ( proprietario1.id, proprietario1.cpf, proprietario1.nome, proprietario1.nascimento, proprietario1.oculos),
    ( proprietario2.id, proprietario2.cpf, proprietario2.nome, proprietario2.nascimento, proprietario2.oculos),
    ( proprietario3.id, proprietario3.cpf, proprietario3.nome, proprietario3.nascimento, proprietario3.oculos),
    ( proprietario4.id, proprietario4.cpf, proprietario4.nome, proprietario4.nascimento, proprietario4.oculos),
    ( proprietario5.id, proprietario5.cpf, proprietario5.nome, proprietario5.nascimento, proprietario5.oculos)
]
   
comando = ''' 
    INSERT INTO Proprietario (id, cpf, nome, nascimento, oculos) 
    VALUES (?, ?, ?, ?, ?);
'''
try:
    cursor.executemany(comando, lista_de_proprietarios_dados)
    conexao.commit()    
    print('✅ Dados inseridos com sucesso!')

except conector.IntegrityError as e:
    print(f"❌ Erro de integridade (duplicata ou chave estrangeira): {e}")
except Exception as e:
    print(f"❌ Ocorreu um erro: {e}")

finally:
    cursor.close()
    conexao.close()
    print("Conexão fechada.")
