#teste
num = 1
while num == 1 or num == 2 or num==3:
    print("|___Menu de Opções___|")
    print("1. Gerar digitos verificadores")
    print("2. Verificar digitos verificadores")
    print("3. Estado de Origem")
    print("4. Sair")
    num = int(input("Digite a opção desejada: "))
    while num > 4 or num < 1:
        num = int(input("Opção desejada invalida, digite novamente: "))
    if num == 1:
        CPF = int(input("Digite o numero do CPF sem os 2 ultimos digitos: "))
        while CPF > 999999999 or CPF < 100000000:
            CPF = int(input("Numero do CPF digitado invalido, digite novamente: "))
        # Calcular digito verificador J
        CPF = str(CPF)
        somaJ = int(CPF[0])*10 + int(CPF[1])*9 + int(CPF[2])*8 + int(CPF[3])*7 + int(CPF[4])*6 + int(CPF[5])*5 + int(CPF[6])*4 + int(CPF[7])*3 + int(CPF[8])*2
        divJ = somaJ % 11
        if divJ < 2:
            digJ = 0
        else:
            digJ = 11 - divJ
        CPF = int(CPF) * 10 + digJ
        #Calcular digito verificador K
        CPF = str(CPF)
        somaK = int(CPF[0])*11 + int(CPF[1])*10 + int(CPF[2])*9 + int(CPF[3])*8 + int(CPF[4])*7 + int(CPF[5])*6 + int(CPF[6])*5 + int(CPF[7])*4 + int(CPF[8])*3 + int(CPF[9])*2
        divK = somaK % 11
        if divK < 2:
            digK = 0
        else:
            digK = 11 - divK
        CPF = int(CPF) * 10 + digK
        print("O numero do CPF: ", CPF)