import psycopg2

conn = psycopg2.connect(
    host = 'localhost', #acessar o banco local
    port = 5433, #porta padrão da versão 18
    database =  'postgres',#banco padrão postgres
    user = 'postgres', #usuario padrão
    password = '623198bc'
)
cursor = conn.cursor()
# Criar tabela corrigida
cursor.execute('''
    CREATE TABLE IF NOT EXISTS public."AGENDA" (
        id INTEGER NOT NULL,
        nome TEXT COLLATE pg_catalog."default" NOT NULL,
        telefone CHAR(12) COLLATE pg_catalog."default" NOT NULL
    )
    TABLESPACE pg_default;
''')

# Alterar dono da tabela
cursor.execute('''
    ALTER TABLE public."AGENDA"
    OWNER TO postgres;
''')

# Inserir dados
cursor.execute('''
    INSERT INTO public."AGENDA"(id, nome, telefone)
    VALUES (1, 'teste1', '0213333333');
''')

cursor.execute('''
    INSERT INTO public."AGENDA"(id, nome, telefone)
    VALUES (2, 'teste2', '0213330000');
''')

conn.commit()

# Ler os dados
cursor.execute('''
    SELECT id, nome, telefone FROM public."AGENDA";
''')

rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Nome: {row[1]}, Telefone: {row[2]}")

# Fechar conexão
cursor.close()
conn.close()