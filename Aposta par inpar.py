from random import randint
print('''Sou seu computador.
Vamos jogar par ou impar?''')
v=0 #vitoria inicializada com 0

while True:
    jogador= int(input('Digite um número: '))
    num_computador = randint(0, 10) #jogo de adivinhar o par ou impar
    total = num_computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input(' Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou o número {jogador} e o computador {num_computador} o total foi {total}')
    print('Deu PAR' if total %2==0 else 'Deu ÍMPAR') #operador ternario
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!!!')
            v+=1
        else:
            print('Você perdeu!!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print(f'Você venceu!!!')
            v+=1
        else:
            print('Você perdeu!!!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes!!!')