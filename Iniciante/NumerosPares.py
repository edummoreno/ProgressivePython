#Número Pares em um intervalo

num1 = int(input("Digite o primeiro numero:"))
num2 = int(input("Digite o segundo numero:"))

if num1 > num2:
    for num in range(num2,num1):
        if num % 2 == 0:
            print(num)
elif num2 > num1:
    for num in range(num1,num2):
        if num % 2 == 0:
            print(num)
else:
    print("Não tem nenhum número par, pois são o mesmo número")