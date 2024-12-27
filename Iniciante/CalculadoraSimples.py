#Calculadora simples

num1 = int(input("Digite o Primeiro Número:"))
num2 = int(input("Difite o Segundo Número:"))

operacao = str(input("Digite a operação, SOMA, SUBTRAÇÂO, MULTIPLICAÇÃO OU DIVISÃO:")).lower()

if operacao == "soma":
    resultado = num1 + num2
elif operacao == "subtração":
    resultado = num1 - num2
elif operacao == "multiplicação":
    resultado = num1 * num2
elif operacao == "divisão":
    resultado = num1 / num2

print(f"O Resultado da Conta é {resultado}")
