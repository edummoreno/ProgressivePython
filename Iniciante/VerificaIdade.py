#Verifica se é maior ou menor de idade

idade = int(input("Digite sua idade:"))

if idade < 18:
    print("Você é menor de idade!")
elif idade >= 65:
    print("Você está na terceira idade!")
else:
    print("Você é maior de idade!")
