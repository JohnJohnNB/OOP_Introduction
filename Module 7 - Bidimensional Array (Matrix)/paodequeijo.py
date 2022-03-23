contador = 0
while True:
    try:
        nl, nc = [int(x) for x in input().split()]
        mat = [[int(x) for x in input().split()] for _ in range(nl)]
        for i in range(nl):
            saida = []
            for j in range(nc):
                if mat[i][j] == 1:
                    saida.append(9)
                else:    
                    if i+1 < nl and mat[i+1][j] == 1:
                        contador+=1
                    if i>0 and mat[i-1][j] == 1:
                        contador+=1
                    if j+1 < nc and mat[i][j+1] == 1:
                        contador+=1
                    if j>0 and mat[i][j-1] == 1:
                        contador+=1
                    saida.append(contador)
                    contador = 0
            print(*saida, sep='')
    except EOFError:
        break
            
            
    
             
             