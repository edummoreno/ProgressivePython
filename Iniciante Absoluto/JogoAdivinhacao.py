#Jogo de Adivinhação de um número
import random

numero_secreto = random.randint(1,10)
tentativa = int(input("Adivinhe o número de 1 a 10: "))
if tentativa == numero_secreto:
    print("Parabéns! Você Acertou.")
else:
    print("Que pena, o número era:", numero_secreto)