arquivo = open('olaMundo.txt', 'r', encoding='utf-8')

conteudo = arquivo.read() #retorna o conteudo do arquivo

print("tipo de conteúdo:", type(conteudo))

print('Conteúdo retornado pelo read: ')
print(repr(conteudo))
arquivo.close()
