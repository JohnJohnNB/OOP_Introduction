import math

tamanho_sequencia = int(input())
menor_valor = math.inf


for i in range(tamanho_sequencia):
    a = int(input())
    if a < menor_valor:
        menor_valor = a
print(menor_valor)
