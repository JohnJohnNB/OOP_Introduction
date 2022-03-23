salario = float(input())

if salario <= 720:
    inss = salario * 0.0765
else:
    if salario <= 1200:
        inss = salario * 0.09
    else:
        if salario <=2400:
            inss = salario * 0.11
        else:
            inss = salario * 2400
print(f'vntc seu arrombado {inss}')
        
    