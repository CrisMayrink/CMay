arquivo = open('olaMundo.txt', 'r', encoding='utf-8')

conteudo = arquivo.readlines() #retorna todos os elementos, em forma de lista de strings

print("tipo de conteúdo:", type(conteudo))

print('Conteúdo retornado pelo readlines: ')

print(repr(conteudo))

arquivo.close()