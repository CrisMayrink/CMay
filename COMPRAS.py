print('='*80)
print('LOJÃO DO BARATÃO')
print('='*80)
total, menor, cont, quant = 0,0,0, 0
barato = ''
while True:
    nProduto = str(input('Digite o nome do produto: '))
    vlr = float(input('Digite o preço do produto: R$ '))
    total += vlr
    cont += 1
    if vlr >= 1000:
        quant += 1
    if cont == 1 or vlr < menor:
        menor = vlr
        barato = nProduto
    r = ' '
    while r not in 'SN':
        r = input('Quer continuar? [S/N] ').strip().upper()[0]
    if r == 'N':
        break
print('='*80)
print('FIM DO PROGRAMA')
print('='*80)
print(f'Você comprou R${total :.2f} de produtos.')
print(f'Foram comprados {quant} produtos acima de R$1000,00 reais!.')
print(f'O produto mais barato foi {barato} que custou R${menor:.2f} reais.')

