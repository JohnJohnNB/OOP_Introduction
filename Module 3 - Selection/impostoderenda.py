salario_bruto = float(input())
n_dependentes = int(input())
desconto_dependentes = 137.99*n_dependentes

if salario_bruto <= 1372.81:
    aliquota = 0
    dedução = 0
elif 1372.82<=salario_bruto<=2743.25:
    aliquota = 0.15
    dedução = 205.92
else:
    aliquota = 0.275
    dedução = 548.82

if salario_bruto <= 720:
    inss = 0.0765*salario_bruto
elif 720<salario_bruto<=1200:
    inss = 0.09*salario_bruto
elif 1200<salario_bruto<=2400:
    inss = 0.11*salario_bruto
else:
    inss = 0.11*2400

irrf = (salario_bruto-desconto_dependentes-inss)*aliquota - dedução
print("{:.2f}".format(irrf))

