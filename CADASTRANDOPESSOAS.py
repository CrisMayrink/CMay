print('='*80)
print('CADASTRAMENTO')
print('='*80)
i = 0
s = ['M, F']
h = 0
r = ['S, N']
maiores =0
menores = 0

while True:
    i = int(input("IDADE:"))
    if i >= 18:
        maiores +=1
    s = str(input('SEXO [M/F]: ')).upper().strip()
    if s == 'M':
        h +=1
    if s == 'F' and i <=20:
        menores +=1
    print('='*80)
    r = str(input('Deseja fazer outro cadastro? [S/N]: ')).upper().strip()
    if r == 'N':
        break
print('='*80)
print(f'Foram cadastradas {maiores} maiores de idade.')
print(f'Foram cadastradas {menores} mulheres menores de idade.')
print(f"Foram cadastrados {h} homens.")
