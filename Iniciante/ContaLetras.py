#conta o numero de letras de uma palavra

palavra = str(input("Digite uma Palavra ou Frase:"))

palavra_sem_espaco = palavra.replace(" ","")

quantidade_de_letras = len(palavra_sem_espaco)

print(f"O que você escreveu tem {quantidade_de_letras} de letras")