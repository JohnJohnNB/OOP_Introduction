import math

quantidade_valores = int(input())
lista = list()

for _ in range(quantidade_valores):
    valores = float(input())
    lista.append(valores)

soma = 1
for valores in lista:
    soma *= valores

media_geometrica = soma **(1/quantidade_valores)

print(media_geometrica)


    