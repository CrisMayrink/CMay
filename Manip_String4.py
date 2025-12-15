#contar as linhas

with open('olaMundo.txt', encoding='utf-8') as arquivo:
    contador =0
    print('Representação do arqquivo')
    for linha in arquivo:
        print(repr(linha))
        if linha:
            contador += 1
    print('Total de Linhas', contador)

#usar o stripe para limpar os espaços em branco
with open('olaMundo.txt', encoding='utf-8') as arquivo:
    contador = 0
    print('Representação do arqquivo após Strip')
    for linha in arquivo:
        linha_limpa = linha.strip()
        print(repr(linha_limpa))
        if linha_limpa:
            contador += 1
    print('Total de Linhas', contador)