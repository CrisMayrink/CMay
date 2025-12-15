import sqlite3  as conector 
from criando_class_Bd import Veiculo

conexao = conector.connect('./veiculos_BDados.db')
cursor = conexao.cursor()

comando= '''SELECT placa, marca FROM Veiculo'''
cursor.execute(comando)

#recupera todos os registros da tabela Veiculo
reg_veiculos = cursor.fetchall()
print(f"Registros encontrados: {len(reg_veiculos)} registros.\n")#exibindo a quantidade de registros encontrados

for registro in reg_veiculos:
    placa = registro [0] #definindo o índice do campo placa e marca
    marca = registro [1]    
    print("Placa:", {placa},  "Marca:", {marca})        
    
cursor.close()
conexao.close()