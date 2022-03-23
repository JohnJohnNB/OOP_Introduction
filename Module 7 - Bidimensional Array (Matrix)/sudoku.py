num_matrizes = int(input())
matriz = []
linha_testada = []
coluna_testada = []
linha_base = [1,2,3,4,5,6,7,8,9]
eh_solucao = True
num_instancia = 1
for _ in range(num_matrizes):
    for i in range(9):
        linha = [int(x) for x in input().split()]
        matriz.append(linha)
    for j in range(9):
        linha_testada = sorted(matriz[j])
        if linha_testada != linha_base:
            eh_solucao = False
            break
        else:          
            coluna_testada = sorted([matriz[k][j] for k in range(9)])
            if coluna_testada != linha_base:
                eh_solucao = False
                break
    if eh_solucao == True:
        print(f"Instancia {num_instancia}")
        print("SIM")
    else:
        print(f"Instancia {num_instancia}")
        print("NAO")
    num_instancia+=1
    matriz = []
        
    
            
        