import sqlite3 as conector
from criando_class_Bd import Proprietario

# --- CONEXÃO E REGISTRO DE CONVERSORES ---

# O SQLite usa INTEGER (1 ou 0) para booleanos. 
# Podemos simplificar a conversão.
def conv_bool(dado):
    return dado == 1

conector.register_converter("oculos", conv_bool) # Registra o conversor para a coluna 'oculos'

# Detecta tipos e usa conversores registrados
conexao = conector.connect('./veiculos_BDados.db', detect_types=conector.PARSE_DECLTYPES)
cursor = conexao.cursor()

#consulta para buscar todos os proprietários que usam óculos
comando = '''SELECT * FROM Proprietario WHERE oculos= :valor_oculos;'''
cursor.execute(comando, {'valor_oculos': True})  # 1 representa True

registros = cursor.fetchall()

for registro in registros:
    
    id_prop, cpf_prop, nome_prop, nasc_prop, oculos_prop = registro
    proprietario = Proprietario(id_prop, cpf_prop, nome_prop, nasc_prop, oculos_prop)
    
    print(f"ID: {proprietario.id}, Nome: {proprietario.nome}, Usa Óculos: {proprietario.oculos}")
    
cursor.close()
conexao.close()