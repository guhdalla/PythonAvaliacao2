num = int(input("Opção desejada invalida, digite novamente: "))
if num == 1:
    CPF = int(input("Digite o numero do CPF sem os 2 ultimos digitos: "))
    while CPF > 999999999 or CPF < 100000000:
        CPF = int(input("Numero do CPF digitado invalido, digite novamente: "))
    # Calcular digito verificador J
    CPF = str(CPF)
    indice = 0
    peso = int(10)
    CPFb = 0
    while indice < 10:
        CPF = CPF[indice] * peso
        CPFa = CPF + CPFb
        CPFb = CPF
        indice +=1
        peso -=1
    divJ = somaJ % 11
    digJ = 0
    if divJ < 2:
        digJ = 0
        print(digJ)
    else:
        digJ = 11 - divJ
        print(digJ)