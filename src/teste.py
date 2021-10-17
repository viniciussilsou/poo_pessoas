
arquivo = open("teste.txt","r")
for linha in arquivo:
    palavra = linha.split(" ")
    qtd_palavras = len(palavra)

    print(qtd_palavras)