#Conta vogais em um palavra ou frase
conta_vogais = 0
palavra = str(input("Digite algo:")).lower()

palavra_alltrim = palavra.replace(" ","")

for letra in palavra_alltrim:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        conta_vogais = conta_vogais + 1

print(f"O que você escreveu tem {conta_vogais} vogais!")