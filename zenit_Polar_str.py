def zenit_polar_replace(text):
    #aplicar a codificação zenit polar utilizando o metodo replace
    # o replace substitui independente se ser uma unica palabra ou frase
    replacements= [('z', 'p'), ('e', 'o'), ('n', 'l'), ('i', 'a'), ('t', 'r'),
                   ('Z', 'P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R')]
    for old, new in replacements: #para cada letra anterior, troque pela nova
        text = text.replace(old, new)
    return text

def main():
    #entrada da frase e aplicação da codificação
    frase = "The quick brown fox jumps over the lazy dog."
    frase = frase.title() #primeira letra em maiúscula

    #dividir a frase em palavras
    words = frase.split()

    #processar cada palavra na lista usando ZENIT POLAR
    coded_words = [zenit_polar_replace(word) for word in words]

    #juntar todas as palavras codificadas em uma frase
    coded_frase = ' '.join(coded_words)

    print("Original: ", frase)
    print("Coded: ", coded_frase)

if __name__ == '__main__':
    main()

