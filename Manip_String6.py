frase1 = "Eu amo comer amoras no café da manhã!"

# resultado usando metodo count diretamente
print('Contagem direta: ', frase1.count('amo'))


#resultado usando a quebra da frase em palavras
contador = 0
lista_termos = frase1.split()
#percorre a lista procurando a palavra 'amo'
for termo in lista_termos:
    if termo == 'amo':
        contador += 1
print('Contagem correta: ', contador)