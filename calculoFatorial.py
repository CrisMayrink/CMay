from math import factorial #modulo math para importar a função fatorial

n = int(input('Entre com um número inteiro para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {},'.format(n, f))