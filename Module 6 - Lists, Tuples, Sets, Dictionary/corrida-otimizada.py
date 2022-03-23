import math

num_carros, num_voltas = [int(x) for x in input().split()]
lista_tempo = [0] * num_carros

for i in range(num_carros):
    lista_tempo[i] = sum([int(x) for x in input().split()])
    
for _ in range(3):
    indice = lista_tempo.index(min(lista_tempo))
    print(indice+1)
    lista_tempo[indice] = math.inf