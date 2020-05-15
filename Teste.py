num = int(input("Opção desejada invalida, digite novamente: "))
if num == 1:
    CPF = int(input("Digite o numero do CPF sem os 2 ultimos digitos: "))
    while CPF > 999999999 or CPF < 100000000:
        CPF = int(input("Numero do CPF digitado invalido, digite novamente: "))
    # Calcular digito verificador J
    CPF = str(CPF)
    indice = 0
    peso = 2
    CPFb = 0
    while i != 9:
        CPF = int(CPF[indice]) * peso
        CPFa = CPF + CPFb
        CPFb = CPF
        indice +=
        peso +=
    divJ = somaJ % 11
    digJ = 0
    if divJ < 2:
        digJ = 0
    else:
        digJ = 11 - divJ
    CPF = int(CPF) * 10 + digJ
    # Calcular digito verificador K
    CPF = str(CPF)
    somaK = int(CPF[0]) * 11 + int(CPF[1]) * 10 + int(CPF[2]) * 9 + int(CPF[3]) * 8 + int(CPF[4]) * 7 + int(
        CPF[5]) * 6 + int(CPF[6]) * 5 + int(CPF[7]) * 4 + int(CPF[8]) * 3 + int(CPF[9]) * 2
    divK = somaK % 11
    digK = 0
    if divK < 2:
        digK = 0
    else:
        digK = 11 - divK
    CPF = int(CPF) * 10 + digK
    print("O numero do CPF: ", CPF)