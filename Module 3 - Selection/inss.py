salario_bruto = float(input())


if salario_bruto<=720:
    inss_desconto=(7.65/100)
elif salario_bruto<=1200:
    inss_desconto=(9/100)
elif salario_bruto<=2400:
    inss_desconto=(11/100)
else:
    inss_desconto=((11/100)*2400)
    salario_bruto=1
    
    

print(salario_bruto*inss_desconto)