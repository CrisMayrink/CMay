# Dados excedente em m³ 
# INPUT ARRAY Cada valor corresponde a um mês do ano, de Janeiro a Novembro, entre com os dados fornecidos.
excedente_m3 = [-56622.40,-5758.90,-23478.61] 
#-85273.70,-71733.40,-26996.90,12858.00,-252671.40,-77883.50,-38387.30,-55924.50,
#gerar UMA TABELA COM OS MESES PREENCHIMENTO PELO USUÁRIO -criada a partir dos dados fornecidos
meses = ["Set","Out","Nov"] #"Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago",
#ATRIBUIR NULL AOS MESES NÃO PREENCHIDOS PELO USUÁRIO - EXEMPLO: meses = ["Jan","Fev",null,"Abr",null,"Jun","Jul","Ago","Set","Out","Nov"]
 #INPUT PARA QUANTIDADE DE HORAS DE CAPTAÇÃO DIÁRIAS
 #INPUT PARA QUANTIDADE DE DIAS DE CAPTAÇÃO POR MÊS
#horas_captacao_diarias = 14
#INPUT PARA A VAZAO OUTORGADA NOS MESES PREENCHIDOS PELO USUÁRIO

# calculando o Tempo total em segundos por mês PREENCHIDOS PELO USUÁRIO

segundos_mes = 11 * 14 * 3600 
#RECEBE OS MESES PREENCHIDOS VEZES AS HORAS DE CAPTAÇÃO DIÁRIAS VEZES OS DIAS DO MÊS
 

# Lista para armazenar resultados EM FORMA DE TUPLAS (Mês, Excedente m³, Excedente L/s)

resultados = [] 

 # Cálculo do excedente em L/s para cada mês
 #obs onde for null não calcular e continuar para o próximo mês
for i, m3 in enumerate(excedente_m3): # Percorre cada mês e seu respectivo excedente em m³

    litros = m3 * 1000 

    lps = litros / segundos_mes 

    resultados.append((meses[i], round(m3,2), round(lps,2))) 

 

# Soma total em m³ e litros 

soma_m3 = sum(excedente_m3) 

soma_litros = soma_m3 * 1000 

 

# Soma total em L/s (não faz sentido somar L/s diretamente, mas podemos mostrar valores mensais) 

print("Mês | Excedente (m³) | Excedente (L/s)") 

for mes, m3, lps in resultados: 

    print(f"{mes} | {m3} | {lps}") 

 

print("\nTotal excedente:") 

print(f"Em m³: {round(soma_m3,2)}") 

print(f"Em litros: {round(soma_litros,2)}") 

print(f"Valor excedido em UFEMG nos termos do Código 231 do Decreto 47.838/2020, valor excedente em l/s vezes 1% do valor da multa base:  R${round(lps * 31,2)} reais")

print(f"Valor excedido em UFEMG nos termos do Código 231 do Decreto 47.838/2020, valor excedente em l/s vezes 1% do valor da multa base:  R${round(lps* 31,2)*5.79} reais")

# Nota: A soma total em L/s não é uma métrica válida, pois L/s é uma taxa instantânea.