from PIL import Image
import numpy as np

def main(): #definindo a função principal
    #carregar a imagem que deve estar na pasta do script

    img = Image.open("candle.png")
    img.show() #abre com o visualizador padrão

    #converter a imagem em binario puros- bytes
    img_data = np.array(img) #Converte o objeto imagem em um array NumPy.
    # Este array contém os valores numéricos de cada pixel (por exemplo, valores RGB).
    binary_data = img_data.tobytes() #Converte o array NumPy em uma sequência pura de bytes (dados binários crus).

    #salvar os dados binarios em um arquivo .bin
    with open('original_img.bin', 'wb') as file: file.write(binary_data)

    #copiar o arquivo binário
    with open('original_img.bin', 'rb') as original_file:
        data = original_file.read()

    with open('copy_img.bin', 'wb') as copy_file: #ler arquivo bin
        copy_file.write(data) #copia de arquivo

    #manipulação dos dados do arq binario cópia
    #exemplo: Inverter o bytes
    with (open('copy_img.bin', 'rb')) as file:
        data =  bytearray(file.read()) #lê o conteudo do arq bin e converte em um obj array- lista

    #inverte todos os bytes
    data = data[::-1] #usa um slice python para =reverter a ordem de todos os bytes na lista

    with open('copy_img.bin', 'wb') as file:
        file.write(data) # o arquivo é sobrescdrito com os bytes invertidos

    #carregar e mostrar a imagem manipulada
    #np.frombuffer converte os bytes de volta para um array NumPy
    #trata cada byte com uminteio de 8bits -> uint8
    # reshape reorganiza o array de volta ao formato original
    modified_data = np.frombuffer(data, dtype=np.uint8).reshape(img_data.shape)

    #cria um novo obj imagem a partir do array modificado
    modified_img = Image.fromarray(modified_data)

    #mostra a imagem que pode estar distorcida
    modified_img.show()

# garante que execução da função principal
if __name__ == '__main__':
    main()

