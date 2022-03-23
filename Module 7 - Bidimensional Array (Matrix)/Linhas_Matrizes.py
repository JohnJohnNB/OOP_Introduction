linha = int(input())
operacao = input()
matriz = []

for i in range(12):
    matriz.append([0]*12)
    for j in range(12):
        elementos = float(input())
        matriz[i][j] = elementos
if operacao == 'S':
    print('{:.1f}'.format(sum(matriz[linha])))
else:
    print('{:.1f}'.format(sum(matriz[linha])/12))