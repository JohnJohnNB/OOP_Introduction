lista = list()
for _ in range(2):
    tamanho_lista = int(input())
    for i in range(tamanho_lista):
        lista.append(input())
lista.sort()

for nomes in lista:
    print(nomes)