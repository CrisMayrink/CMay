import os
import shutil
def criar_diretorios(diretorio_trabalho):
       for diretorio_novo in diretorio_trabalho:
           if not os.path.exists(diretorio_novo):
               try:
                   os.makedirs(diretorio_novo)
                   print(f"Diretório {diretorio_novo} criado.")
               except PermissionError:
                   print(f"Sem permissão para criar o diretório {diretorio_novo}.")
               except Exception as e:
                   print(f"Erro inesperado ao criar {diretorio_novo}: {e}")
                      
def mover_arquivos(diretorio_trabalho):
    for arquivo in os.listdir(diretorio_trabalho):
        caminho_arquivo = os.path.join(diretorio_trabalho, arquivo)
        if os.path.isfile(caminho_arquivo):
            extensao = arquivo.split('.')[-1].lower()
            if extensao in ['pdf', 'txt', 'jpg']:
                diretorio_novo = os.path.join(diretorio_trabalho, extensao)
                try:
                    shutil.move(caminho_arquivo, diretorio_novo)
                    print(f"{arquivo} movido para {diretorio_novo}.")
                except PermissionError:
                    print(f"Sem permissão para mover {arquivo}.")
                except Exception as e:
                    print(f"Erro inesperado ao mover {arquivo}: {e}")
            else:
                   print(f"Extensão {extensao} de {arquivo} não é suportada.")
                   
def main():
       diretorio_trabalho = "diretorio_trabalho"
       diretorio_novo = [os.path.join(diretorio_trabalho, 'pdf'),
                     os.path.join(diretorio_trabalho, 'txt'),
                     os.path.join(diretorio_trabalho, 'jpg')]
 
       # Criar diretórios se não existirem
       criar_diretorios(diretorio_novo)
 
       # Mover arquivos para os diretórios correspondentes
       mover_arquivos(diretorio_trabalho)
 
if __name__ == "__main__":
    main()