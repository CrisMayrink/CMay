arquivo = open('olaMundo.txt', 'r', encoding='utf-8')

conteudo = arquivo.readline() #retorna o conteudo da primeira linha

print("tipo de conteúdo:", type(conteudo))

print('Proximo conteúdo retornado pelo readline: ')
print(repr(conteudo))

arquivo.close()