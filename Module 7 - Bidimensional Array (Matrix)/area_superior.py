operacao = input()
valor_operacao = 0
matriz = []
inicio_linha = 1
tamanho_linha = 11

for i in range(12):
    matriz.append([0]*12)
    for j in range(12):
        elementos = float(input())
        matriz[i][j] = elementos
    for k in range(inicio_linha, tamanho_linha):
        valor_operacao+=matriz[i][k]
    tamanho_linha -= 1
    inicio_linha +=1
    
if operacao == 'S':
    print('{:.1f}'.format(valor_operacao))
else:
    print('{:.1f}'.format(valor_operacao/30))
