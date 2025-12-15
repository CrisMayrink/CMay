import psycopg2

conn= psycopg2.connect(database= "postgres", user= "postgres", password= "623198bc", host= 'localhost', port= 5433)

print("Conexão aberta com sucesso!")
cursor =  conn.cursor()

cursor.execute('''SELECT * from public."AGENDA" where "id"=1 ''')
registro= cursor.fetchone()
print(registro)

cursor.execute('UPDATE public."AGENDA" set "telefone"=%s where "id"=1', ('21888891111',))
conn.commit()
print("Registro atualizado com sucesso!")

print("Consulta depois da atualização:")
cursor.execute('SELECT * from public."AGENDA" where "id"=1 ')
registro = cursor.fetchone()
print(registro)

print("Seleção realizada com sucesso!")
cursor.close()
conn.close()
print("Conexão fechada com o bando de dados.")