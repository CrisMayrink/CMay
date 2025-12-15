import sqlite3 as conector

conexao = conector.connect('./meu_Banco.db')
cursor = conexao.cursor()
comando1 = '''DROP TABLE IF EXISTS veiculo'''
cursor.execute(comando1)

comando2 = '''CREATE TABLE Veiculo(
        placa CHARACTER(7) NOT NULL PRIMARY KEY,
        ano INTEGER NOT NULL,
        cor TEXT NOT NULL,
        motor REAL NOT NULL,
        proprietario_id INTEGER NOT NULL,
        marca INTEGER NOT NULL,
        FOREIGN KEY (proprietario_id) REFERENCES proprietario (id),
        FOREIGN KEY (Marca) REFERENCES Marca (id)
        )'''

cursor.execute(comando2)
conexao.commit()
print("Tabela 'Veículo' recriada com sucesso.")
cursor.close()
conexao.close()