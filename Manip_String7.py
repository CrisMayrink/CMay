minha_lista =['arroz', 'feijão', 'batata', 'macarrão']

texto1 = ','.join(minha_lista)
with open("meu_arquivo.txt", "w") as arquivo:
    arquivo.write(texto1)
    arquivo.write("\n")

texto2 = '\n'.join(minha_lista)
with open("olaMundo.txt", "w") as arquivo:
    arquivo.write(texto2)
    arquivo.write("\n")

print(texto2, texto1)


