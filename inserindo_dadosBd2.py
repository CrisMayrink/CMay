import sqlite3 as conector
from criando_class_Bd import  Marca, Veiculo

# Query dinâmica de inserção de dados no banco de dados

conexao = conector.connect('./veiculos_BDados.db')
cursor = conexao.cursor()

# --- (Restante do código de criação e inserção de Marcas) ---
comando_criar_tabela_marca = '''CREATE TABLE IF NOT EXISTS Marca(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            sigla CHARACTER(4) NOT NULL
        );'''

# Comando omitido para brevidade
cursor.execute(comando_criar_tabela_marca)
conexao.commit()
print("Tabela 'Marca' verificada/criada.")

comando_marca = '''INSERT INTO Marca (nome, sigla) VALUES (:nome, :sigla);'''
marca1 = Marca(1, 'Fiat', 'FI')
cursor.execute(comando_marca, {'nome': marca1.nome, 'sigla': marca1.sigla})
marca1.id = cursor.lastrowid
marca2 = Marca(2, 'Chevrolet', 'CH')
cursor.execute(comando_marca, {'nome': marca2.nome, 'sigla': marca2.sigla})
marca2.id = cursor.lastrowid
conexao.commit()
print("Tabela 'Marca' Dados inseridos com sucesso.")
# --- Fim do código de criação e inserção de Marcas ---

comando_criar_tabela_veiculo = '''
        CREATE TABLE IF NOT EXISTS Veiculo(
            placa CHARACTER(7) NOT NULL PRIMARY KEY,
            ano INTEGER NOT NULL,
            cor TEXT NOT NULL,
            marca INTEGER NOT NULL,
            proprietario_id INTEGER NOT NULL,
            
            FOREIGN KEY(proprietario_id) REFERENCES Proprietario(id)
                ON UPDATE CASCADE ON DELETE CASCADE         
        );'''
cursor.execute(comando_criar_tabela_veiculo)
print("Tabela 'Veiculo' criada ou já existente com chaves estrangeiras.")

# 2. Preparar os dados de veículos em uma lista de tuplas
veiculo1 = Veiculo("AAA0001", 2001, "Prata", marca1.id, 7) # Assumindo ID Proprietario 7
veiculo2 = Veiculo("BAA0002", 2002, "Preto", marca1.id, 8) # Assumindo ID Proprietario 8
veiculo3 = Veiculo("CAA0003", 2003, "Branco", marca2.id, 9) # Assumindo ID Proprietario 9
veiculo4 = Veiculo("DAA0004", 2004, "Azul", marca2.id, 10) # Assumindo ID Proprietario 10

# Extrair atributos dos objetos em ordem: placa, ano, cor, marca, proprietario_id
lista_veiculos_dados = [
    (veiculo1.placa, veiculo1.ano, veiculo1.cor,  veiculo1.marca, veiculo1.proprietario_id),
    (veiculo2.placa, veiculo2.ano, veiculo2.cor,  veiculo2.marca, veiculo2.proprietario_id),
    (veiculo3.placa, veiculo3.ano, veiculo3.cor,  veiculo3.marca, veiculo3.proprietario_id),
    (veiculo4.placa, veiculo4.ano, veiculo4.cor,  veiculo4.marca, veiculo4.proprietario_id)
]

# Usando placeholders posicionais (?) no comando SQL
comando_veiculo = '''INSERT INTO Veiculo (placa, ano, cor, marca, proprietario_id) 
                     VALUES (?, ?, ?, ?, ?);'''

# 3. Usar executemany() para inserir múltiplos registros de uma vez
try:
    cursor.executemany(comando_veiculo, lista_veiculos_dados)
    conexao.commit()
    print('✅ Dados inseridos com sucesso!')
    print(f'   - {cursor.rowcount} registros de veículos foram adicionados.')

except conector.IntegrityError as e:
    conexao.rollback()
    print(f"❌ Erro de integridade (duplicata ou chave estrangeira): {e}")

except Exception as e:
    conexao.rollback()
    print(f"❌ Ocorreu um erro inesperado: {e}")

finally:
    # 4. Fechamento seguro
    cursor.close()
    conexao.close()
    print("Conexão fechada.")