consumo_energia = int(input())
ate_30kw = consumo_energia*0.09556
ate_100kw = 30*0.09556 + (consumo_energia-30)*0.16698
ate_200kw = 30*0.09556 + 70*0.16698 + (consumo_energia-100)*0.25052
maior_200kw = 30*0.09556 + 70*0.16698 + 100*0.25052 + (consumo_energia-200)*0.27836


if consumo_energia == 0:
    valor_energia = 0
elif 0<consumo_energia <= 30:
    valor_energia = ate_30kw
elif 30 < consumo_energia <= 100:
    valor_energia = ate_100kw
elif 100 < consumo_energia <= 200:
    valor_energia = ate_200kw
else:
    valor_energia = maior_200kw
    
print("{:.2f}".format(valor_energia))
