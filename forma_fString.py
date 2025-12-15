from datetime import datetime

#metodo FORMAT
hoje = datetime.now()
data_formatada= hoje.strftime("Data: %d/%m/%Y")
print(data_formatada)


#metodo F-string

hoje2 = datetime.now()
data_formatada2= f"Data: {hoje: %d/%m/%Y}"
print(data_formatada2)