import sqlite3 as conector
from criando_class_Bd import Marca, Veiculo
 
conexao = conector.connect("./veiculos_Banco.db")
conexao.execute("PRAGMA foreign_keys = on")
cursor = conexao.cursor()

# Inserção de dados na tabela Marca (usando execute com vars(), que é um dicionário)
comando1 = '''INSERT INTO Marca (id, nome, sigla) VALUES (:id, :nome, :sigla);'''

marca1 = Marca(1, "Marca A", "MA")
cursor.execute(comando1, vars(marca1))
marca1.id = cursor.lastrowid

marca2 = Marca(2, "Marca B", "MB")
cursor.execute(comando1, vars(marca2))
marca2.id = cursor.lastrowid

# Preparação dos dados de veículos
veiculo1 = Veiculo("AAA0001", 2001, "Prata", 10000000099, marca1.id, proprietario_id = 1)
veiculo2 = Veiculo("BAA0002", 2002, "Preto",  10000000099, marca1.id, proprietario_id = 2)
veiculo3 = Veiculo("CAA0003", 2003, "Branco", 20000000099, marca2.id, proprietario_id) = 3
veiculo4 = Veiculo("DAA0004", 2004, "Azul",  30000000099, marca2.id, proprietario_id = 4)

# Cria a lista de tuplas para uso com executemany()
lista_veiculos_dados = [
    (veiculo1.placa, veiculo1.ano, veiculo1.cor,  veiculo1.proprietario, veiculo1.marca),
    (veiculo2.placa, veiculo2.ano, veiculo2.cor,  veiculo2.proprietario, veiculo2.marca),
    (veiculo3.placa, veiculo3.ano, veiculo3.cor,  veiculo3.proprietario, veiculo3.marca),
    (veiculo4.placa, veiculo4.ano, veiculo4.cor,  veiculo4.proprietario, veiculo4.marca)
]

# Comando SQL para Veiculo, usando placeholders posicionais (?)
comando2 = '''INSERT INTO Veiculo
                VALUES (?, ?, ?, ?, ?, ?);''' # Adicionado o 6º placeholder (?)
 
try:
    # >>>>> CORRIGIDO: Usando executemany() para eficiência <<<<<
    cursor.executemany(comando2, lista_veiculos_dados)

    # Efetivação do comando
    conexao.commit()
    print("✅ Todos os dados inseridos e confirmados com sucesso!") # Corrigido o print vazio

except conector.IntegrityError as e:
    print(f"❌ Erro de integridade (duplicata ou chave estrangeira): {e}")
except Exception as e:
    print(f"❌ Ocorreu um erro: {e}")

finally:
    # 4. Fechamento seguro
    cursor.close()
    conexao.close()
    print("Conexão fechada.")
