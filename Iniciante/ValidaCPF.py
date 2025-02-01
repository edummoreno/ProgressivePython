#Valida Se é um CPF

CPF = (input("Digite seu CPF:")).lower()

CPF = CPF.replace(".","")
CPF = CPF.replace("-","")

if len(CPF) == 11:
    print("É um CPF!")