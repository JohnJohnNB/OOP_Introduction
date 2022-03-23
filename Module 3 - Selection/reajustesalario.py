salario_atual = float(input())
salario_minimo = float(input())


if salario_atual<=3*salario_minimo:
    reajuste_perc = 0.2
elif 3*salario_minimo<salario_atual<=5*salario_minimo:
    reajuste_perc = 0.15
else:
    reajuste_perc = 0.1

salario_reajustado = salario_atual*(1+reajuste_perc)

if salario_reajustado<3/2*salario_minimo:
    salario_reajustado = 3/2*salario_minimo
elif salario_reajustado>20*salario_minimo:
    salario_reajustado = 20*salario_minimo
else:
    salario_reajustado = salario_atual*(1+reajuste_perc)

print("{:.2f}".format(salario_reajustado))
