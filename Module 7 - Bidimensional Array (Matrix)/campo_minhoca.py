linha, coluna = [int(x) for x in input().split()]
matriz = []
maior_celula = 0
for i in range(linha):
    matriz.append([int(x) for x in input().split()])
    valor_celula = sum(matriz[i])
    if valor_celula > maior_celula:
        maior_celula = valor_celula
for j in range(coluna):
    valor_celula = sum(matriz[k][j] for k in range(linha))
    if valor_celula > maior_celula:
        maior_celula = valor_celula
print(maior_celula)