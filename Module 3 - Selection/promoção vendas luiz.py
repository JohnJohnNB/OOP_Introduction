valor = float(input())
custo = valor*0.8

if valor >=500 and valor<1000:
    custo -=valor*0.1
if valor>=1000:
    valor-=1000
    valor-=valor*0.15
    custo=1000*0.7 + valor
print(round(custo, 2))
