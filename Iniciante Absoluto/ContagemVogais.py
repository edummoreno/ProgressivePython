#

frase = input("Digite uma frase: ").lower()

vogais = "aeiou"

contador = sum(1 for letra in frase if letra in vogais)
print("A frase tem", contador, "vogais.")

#De forma tradicional
# contador = 0
# for letra in frase:
#   if letra in vogais:
#       contador += 1