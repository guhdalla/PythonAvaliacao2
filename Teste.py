#42321568879
CPF = int(input("Numero do CPF: "))
# Calcular digito verificador J
CPF = str(CPF)
indiceJ = (-11)
pesoJ = 10
CPFaJ = 0
CPFbJ = 0
while indiceJ < -2:
    somaJ = int(CPF[indiceJ]) * pesoJ
    CPFaJ = somaJ + CPFbJ
    CPFbJ += somaJ
    indiceJ += 1
    pesoJ -= 1
    print(CPFbJ)