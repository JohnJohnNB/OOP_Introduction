import math
tamanho_sequencia = int(input())

menor_valor = math.inf
segundo_menor_valor = math.inf


for i in range(tamanho_sequencia):
    x = int(input())
    if x < menor_valor:
        segundo_menor_valor = menor_valor
        menor_valor = x
    elif x < segundo_menor_valor:
        segundo_menor_valor = x
print(segundo_menor_valor)