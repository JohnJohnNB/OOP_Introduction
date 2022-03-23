cpf = input()
cpf_limpo = ''
valido = True

for numero in cpf:
    if numero.isnumeric() == True:
        cpf_limpo+=numero  

if len(cpf_limpo) != 11 or cpf_limpo == cpf_limpo[::-1]:
    valido = False
    
else:
    #########################################
    soma = 0
    peso = len(cpf_limpo)-1
    for numero in range(len(cpf_limpo)-2):
        soma+=int(cpf_limpo[numero])*peso
        peso -= 1
    dv1 = 11 - soma%11
    if dv1 >= 10:
        dv1 = 0
    cpf_validado = cpf_limpo[0:9] + str(dv1)
    #########################################
    soma = 0
    peso = len(cpf_validado)+1
    for numero in range(len(cpf_validado)):
        soma+=int(cpf_validado[numero])*peso
        peso -= 1
    dv2 = 11 - soma%11
    if dv2 >= 10:
        dv2 = 0
    cpf_validado += str(dv2)
    #########################################
    if cpf_limpo != cpf_validado:
        valido = False

print(valido)


