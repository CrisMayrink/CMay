import os

#Crie uma função para ler o conteúdo de um arquivo e escrever em um novo arquivo com uma linha de cabeçalho:
def processar_arquivo(arq_origem, arq_destino):
    try:
        with open( arq_origem, 'r', encoding= 'utf-8') as f_origem:
            conteudo = f_origem.read()
    except FileNotFoundError:
        print(f"o arquivo de origem'{arq_origem}' não foi encontrado")
        print("Certifique-se que o arquivo 'arq_origem.txt' existe dentro da pasta de destino.")
        return
    except PermissionError:
        print(f"Sem permissão para ler '{arq_origem}'.")
        return
    except Exception as e:
        print(f"Erro inesperado ao ler '{arq_origem}' : {e}")
        return
    
    try:
        with open( arq_destino, 'w', encoding= 'utf-8') as f_destino:
            f_destino.write('Cabeçalho: contéudo do arquivo\n')
            f_destino.write(conteudo)
    except PermissionError:
        print(f"Sem permissão para escrever em '{arq_destino}'.") 
        return
    except Exception as e:
        print(f"Erro inesperao ao escrever em '{arq_destino}': {e}")   
    
def main():
    # Define o caminho base desejado, usando os.path.join para compatibilidade (Windows/Linux)
    diretorio_base  = os.path.join("manipulacaoDados", "diretorio_trabalho")
    
    #1. GARANTE QUE O CAMINHO COMPLETO EXISTA
    if not os.path.exists(diretorio_base):
        print(f"Criando a estrutura de diretórios: {diretorio_base}")
        # os.makedirs cria todas as pastas intermediárias necessárias (manipulacaoDados E diretorio_trabalho)
        os.makedirs(diretorio_base)
    
        # !!! CORREÇÃO AQUI: Use os.path.join() !!!
    # os.path não é uma função, é um módulo. os.path.join é a função que você precisa.
    #3 CONSTRUÇÃO CORRETA DOS NOMES DOS ARQUIVOS DENTRO DESSE CAMINHO
    arq_origem = os.path.join(diretorio_base,  "arq_origem.txt")
    arq_destino = os.path.join(diretorio_base, "arq_destino.txt")
    
    # 3. (Opcional) Cria um arquivo de origem básico se ele não existir, para testar o programa
    if not os.path.exists(arq_origem):
        print(f"Criando arquivo de origem básico para teste: {arq_origem}")
        with open(arq_origem, 'w', encoding='utf-8') as f:
            f.write("Primeira linha de teste.\nSegunda linha de teste.")
    
    processar_arquivo(arq_origem, arq_destino)
        
if __name__ == "__main__":
    main()