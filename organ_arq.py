import os
from pathlib import Path
import shutil

# Função para criar um subdiretório

def criar_diretorio (diretorio_trabalho):
    for novo_diretorio in diretorio_trabalho:
        try:
            os.makedirs(novo_diretorio, exist_ok=True) # Cria o diretório, se não existir
            print(f"O novo diretorio {novo_diretorio} foi criado com sucesso ou ja existia.")
        except PermissionError:
            print(f"Sem permissão para criar diretórios em {diretorio_trabalho}.")
        except Exception as e:
            print(f"Erro Inesperado ao criar dirtetório.{e}")
                   
def mover_arquivos(diretorio_trabalho): # Função para mover arquivos para os subdiretórios correspondentes
    pastas_necessarias = ['pdf', 'txt', 'jpg', 'py']
    caminho_destino_completo = [os.path.join(diretorio_trabalho, pasta) for pasta in pastas_necessarias]
    
    criar_diretorio(caminho_destino_completo)
    print(f"Organizando arquivos em {diretorio_trabalho}...")
    
    for item_no_diretorio in os.listdir(diretorio_trabalho):
        caminho_completo_item = os.path.join(diretorio_trabalho, item_no_diretorio)
        
        if os.path.isfile(caminho_completo_item): #verifica se é um arquivo
            extensao = os.path.splitext(caminho_completo_item)[-1].replace('.', '').lower() #pega a extensão do arquivo
            
            if extensao in ['pdf', 'txt', 'jpg', 'py']:
                novo_diretorio = extensao
                novo_diretorio = os.path.join(diretorio_trabalho, novo_diretorio)
                    
                try:#exceções para mover arquivos
                    shutil.move(caminho_completo_item, novo_diretorio)
                    print(f"Arquivo movido de {caminho_completo_item} para {novo_diretorio} com sucesso.")
                except FileNotFoundError:
                    print(f"O arquivo {item_no_diretorio} não foi encontrado.")
                except PermissionError:
                    print(f"Sem permissão para mover o arquivo {item_no_diretorio}.")
                except Exception as e:
                    print(f"Erro inesperado ao mover o arquivo.{e}")       
            else:
                print(f"Extensão {extensao} de {item_no_diretorio} não é suportada.")
def main():
    novo_diretorio = r"C:\Users\cmaya\OneDrive\CMAYRINK\Documentos\FACULDADE SISTEMAS DE INT\SCRIPS PYTHON\manipulacaoDados\diretorio_trabalho"
    if not os.path.exists(novo_diretorio):
        print(f"O diretório de trabalho {novo_diretorio} não existe. Por favor, verifique o caminho.")
        return
    # Nota: O 'r' antes da string (r"...") é para garantir que o Python trate as contrabarras (\) 
    # como parte do caminho e não como caracteres de escape.
    
    # Chama a função que organiza os arquivos neste diretório específico
    
 
    mover_arquivos(diretorio_trabalho=novo_diretorio) 
       
   
if __name__ == "__main__":
    main()
            