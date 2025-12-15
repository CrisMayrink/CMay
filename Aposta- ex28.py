from random import randint
num_computador = randint(0, 10) #jogo de advinhar o número q o pc pensou
print('''Sou seu computador.
Vamos fazer um desafio? 
Qual número estou pensando?''')
acertou = False
tentativa = 0
while not acertou:
    num_usuario = int(input('Entre com sua aposta: '))
    tentativa += 1
    if num_usuario == num_computador:
        acertou = True
    else:
        if num_usuario < num_computador:
            print('Mais...')
        elif num_usuario > num_computador:
            print('Menos...')
print('Você acertou com {} tentativas'.format(tentativa))