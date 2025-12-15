import psycopg2

# 1. Conectar ao banco
conn = psycopg2.connect(
    host='localhost',
    port=5433,
    database='postgres',
    user='postgres',
    password='623198bc'
)

# 2. Criar cursor
cursor = conn.cursor()

try:
    # 3. Executar comandos SQL
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS public."CARROS"(
            id SERIAL PRIMARY KEY,
            nome TEXT NOT NULL,
            valor FLOAT NOT NULL
        );
    ''')

    # Inserir dados (exemplo com executemany)
    dados = [
        ('Kicks1', 150000.00),
        ('Toro', 200000.00),
        ('March', 40000.00)
    ]
    cursor.executemany('''
        INSERT INTO public."CARROS"(nome, valor)
        VALUES (%s, %s);
    ''', dados)

    # 4. Confirmar alterações
    conn.commit()

    # 5. Ler dados
    cursor.execute('SELECT id, nome, valor FROM public."CARROS";')
    rows = cursor.fetchall()
    for row in rows:
        print(f"id: {row[0]}, Nome: {row[1]}, valor: {row[2]}")

except Exception as e:
    print("Erro:", e)
    conn.rollback()  # desfaz alterações em caso de erro

finally:
    # 6. Fechar cursor e conexão
    cursor.close()
    conn.close()
