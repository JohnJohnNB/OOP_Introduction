num_carros, num_voltas = [int(x) for x in input().split()]
lista_tempo = []

contador_primeiro = 100
contador_segundo = 100
lista_carros = []

for i in range(num_carros):
    tempo_gasto = sum([int(x) for x in input().split()])
    lista_tempo.append(tempo_gasto)
    if i == 0:
        lista_carros.append(lista_tempo.index(lista_tempo[i])+1)
        contador_primeiro = tempo_gasto
    else:
        if tempo_gasto < contador_primeiro:
            lista_carros.insert(0, lista_tempo.index(lista_tempo[i])+1)
            contador_segundo = contador_primeiro
            contador_primeiro = tempo_gasto
        elif tempo_gasto < contador_segundo:
            lista_carros.insert(1, lista_tempo.index(lista_tempo[i])+1)
            contador_segundo = tempo_gasto
        else:
            lista_carros.insert(2, lista_tempo.index(lista_tempo[i])+1)

print(lista_carros[0])
print(lista_carros[1])
print(lista_carros[2])
