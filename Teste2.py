divJ = CPFbJ % 11
if divJ < 2:
    digJ = 0
else:
    digJ = 11 - divJ

    if digJ == CPF[-1] and digK == CPF[-2]:
        print("CPF Valido")
    else:
        print("CPF Invalido")