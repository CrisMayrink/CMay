vlr_imovel= float(input('Bem vindo ao site de financiamentos do Banco Novo! Para prosseguir digite o valor do imóvel pretendido: R$'))
sal = float(input("Digite o seu salário: R$"))
anos = int(input("Digite em quanto tempo pretende pagar o imóvel: "))
nr_prest = anos * 12
vlr_prestacao= vlr_imovel/nr_prest
if vlr_prestacao > sal*0.30:
    print('Infelizmente você não possui margem para financiamento.')
elif vlr_prestacao < sal*0.30:
    print('Parabens, seu financiamento foi aprovado. Sua prestação será de R${:.2f} pelo prazo de {} anos.'.format(vlr_prestacao, anos))
