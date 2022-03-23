import math

num_valores = int(input())
lista = list()
for _ in range(num_valores):
    valores = float(input())
    lista.append(valores)

somatorio = 0
media_aritmetica = sum(lista)/num_valores

for valores in lista:
    somatorio+=(valores-media_aritmetica)**2

desvio_padrao = math.sqrt(somatorio/(num_valores-1))

print(desvio_padrao)
