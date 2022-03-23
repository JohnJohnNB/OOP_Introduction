ordem = int(input())
P,Q,R,S,X,Y = [int(x) for x in input().split()]
posicao_matriz_c = [int(x) for x in input().split()]
matriz_a = []
matriz_b = []
elemento_a = 0
elemento_b = 0
for i in range(1,ordem+1):
    linha_a = []
    linha_b = []
    matriz_a.append(linha_a)
    matriz_b.append(linha_b)
    for j in range(1,ordem+1):
        elemento_a = (P*i+Q*j)%X
        elemento_b = (R*i+S*j)%Y
        matriz_a[i-1].append(elemento_a)
        matriz_b[i-1].append(elemento_b)     
elemento_c = 0
for i in range(ordem):
    elemento_c += matriz_a[posicao_matriz_c[0]-1][i] * matriz_b[i][posicao_matriz_c[1]-1]    
print(elemento_c)