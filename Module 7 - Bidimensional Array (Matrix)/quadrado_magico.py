ordem_matriz = int(input())
matriz = []

for i in range(ordem_matriz):
    valor = [int(x) for x in input().split()]
    matriz.append(valor)
    
valor_teste =  sum(matriz[0])
soma_geral = 0
soma_diag_secun = 0
indice_diag_secun = ordem_matriz-1

soma_diag_prin = sum(matriz[j][j] for j in range(ordem_matriz)) 
if soma_diag_prin != valor_teste:
    print(False)
else:
    for k in range(ordem_matriz):
        soma_linha = sum(matriz[k])
        soma_coluna = sum(matriz[j][k] for j in range(ordem_matriz))
        soma_geral += soma_linha + soma_coluna   
        soma_diag_secun += matriz[k][indice_diag_secun]
        if soma_linha != valor_teste or soma_coluna != valor_teste:
            print(False)
            break
        indice_diag_secun-=1
    if soma_diag_secun != valor_teste:
        print(False)
    else:
        print(True)