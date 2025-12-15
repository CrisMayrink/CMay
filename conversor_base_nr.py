nr = int(input('Digite um numero inteiro: '))
escolha = int(input(''' Escolha uma das bases para conversão: 
[ 1 ] para conversão para a base binária
[ 2 ] para conversão para a base octal
[ 3 ] para conversão para a base hexadecimal
Sua opção é: ''')) #3 aspas simples para mudar de linha sem sair do input
if escolha == 1:
    binario = bin(nr)[2:] #o [:2] é para suprimir o caracter 0oxxx da saída. Ex oct(10) = 0o12, com[:2] = '12'
    print('O número {} na base binária é {}.'.format(nr, binario))
elif escolha == 2:
    octal = oct(nr)[2:]
    print('O numero {} na base octal é {}.'.format(nr, octal))
elif escolha == 3:
    hexadecimal = hex(nr)[2:]
    print('O número {} na base hexadecimal é {}. '.format(nr, hexadecimal))
else:
    print('Opção inválida. Tente novamente.')
print('FIM')