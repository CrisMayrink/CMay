import sqlite3  as conector
 #Não precisamos importar as classes Veiculo, Marca, Proprietario para esta consulta, 
# pois estamos apenas lendo os dados diretamente do banco de dados e imprimindo.

conexao = conector.connect('./veiculos_BDados.db')
cursor = conexao.cursor()

try:
    
    comando_join = '''
    SELECT 
        V.placa AS Placa,
        M.nome AS NomeMarca,
        P.nome AS NomeProprietario
    FROM
        Veiculo AS V
    INNER JOIN
        Marca AS M on V.marca = M.id
    INNER JOIN
        Proprietario AS p ON V.proprietario_id = P.id '''
        
    cursor.execute(comando_join)
    #recupera todos os registros da tabela Veiculo com junção
    registros_combinados = cursor.fetchall()
    print(f"Registros encontrados: {len(registros_combinados)} registros.\n")#exibindo a quantidade de registros encontrados    
    print("Registros combinados (Veículo, Marca, Proprietário):")

    for registro in registros_combinados:
        #cada registro é uma tupla com os campos selecionados
        placa, nome_marca, nome_proprietario = registro
        print(f"{placa:8} | {nome_marca:15} | {nome_proprietario:20}")
        

except conector.OperationalError as e:
    print("Erro na operação com o banco de dados:", e)

finally:
    cursor.close()
    conexao.close() 
