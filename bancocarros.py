import psycopg2

conn =  psycopg2.connect(
    host= 'localhost',
    port= 5433,
    database = 'postgres',
    user= 'postgres',
    password= '623198bc'
)
#criar um cursor
cursor = conn.cursor()
comando1 = '''DROP TABLE IF EXISTS public."CARROS" '''
cursor.execute(comando1)
conn.commit()

#criar uma tabela se ela ainda não existir "if not exists"
#public é o schema/pasta padrão
# collate-define a forma como o texto será ordenado/comparado (collation).colaçao padrão
#Define que a tabela será armazenada no tablespace padrão do PostgreSQL.Não precisa ser especificado
comando2 = ('''
    CREATE TABLE IF NOT EXISTS public."CARROS"( 
        id SERIAL PRIMARY KEY,
        nome TEXT COLLATE pg_catalog."default" NOT NULL,
        valor FLOAT NOT NULL
    )TABLESPACE pg_default;
    ''')

cursor.execute(comando2)
conn.commit()
print("Tabela 'Veículo' recriada com sucesso.")
# Alterar dono(OWNER) da tabela
#controle total sobre ela: pode alterar estrutura, permissões, apagar, etc.
#se uma tabela foi criada por um usuário temporário, mas você quer que o postgres (ou outro usuário principal) seja o responsável por ela.
comando3 = ('''
    ALTER TABLE public."CARROS"
    OWNER TO postgres;
''')
cursor.execute(comando3)
conn.commit()


# Inserir dados
cursor.execute('INSERT INTO public."CARROS"(nome, valor) VALUES (%s, %s);', ('Kicks1', 150000.00))
cursor.execute('INSERT INTO public."CARROS"(nome, valor) VALUES (%s, %s);', ('Toro', 200000.00))
cursor.execute('INSERT INTO public."CARROS"(nome, valor) VALUES (%s, %s);', ('March', 40000.00))

# salvando
conn.commit()
print("Dados inserirdos com sucesso.")

#ler os dados
cursor.execute('''
    SELECT id, nome, valor FROM public."CARROS";
    ''')
#apresenta os resultados da consulta em uma linha da tabela
rows = cursor.fetchall()
#percorre e imprime cada linha
for row in rows:
    print(f"id: {row[0]}, Nome: {row[1]}, valor: {row[2]:2f}")
    #:.2f → significa formato float com 2 casas decimais.
    
# Fechar conexão
cursor.close()
conn.close()