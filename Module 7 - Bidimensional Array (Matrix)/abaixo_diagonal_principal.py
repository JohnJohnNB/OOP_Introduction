operacao = input()
valor_operacao = 0
matriz = []
tamanho_linha = -1

for i in range(12):
    matriz.append([0]*12)
    for j in range(12):
        elementos = float(input())
        matriz[i][j] = elementos
    tamanho_linha += 1
    for k in range(tamanho_linha):
        valor_operacao+=matriz[i][k]
    
if operacao == 'S':
    print('{:.1f}'.format(valor_operacao))
else:
    print('{:.1f}'.format(valor_operacao/66))