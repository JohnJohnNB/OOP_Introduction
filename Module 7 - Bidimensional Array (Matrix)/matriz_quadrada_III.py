ordem_matriz = int(input())
matriz = []
valor = 1
while ordem_matriz != 0:
    for j in range(ordem_matriz):
        matriz.append([0]*ordem_matriz)
        for i in range(ordem_matriz):
            if j>=1:
                matriz[j][i] = (matriz[j-1][i])*2
            else:
                matriz[j][i] = valor
                valor*=2
    branco = len(str(matriz[-1][-1]))
    
    print('\n'.join([' '.join([str(cell).rjust(branco) for cell in row]) for row in matriz]))
        
    print("")
    matriz = []
    valor = 1
    ordem_matriz = int(input())
    