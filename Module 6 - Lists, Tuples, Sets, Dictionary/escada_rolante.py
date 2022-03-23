num_pessoas = int(input())
while num_pessoas != 0:
    
    entradas = [int(x) for x in input().split()]
    inicio = entradas[0]
    termino = inicio + 10

    tempo_total = 0
    for tempo in entradas[1:]:
        if tempo <= termino:
            termino = tempo + 10
        else:
            tempo_total += termino - inicio
            inicio = tempo
            termino = tempo + 10
    tempo_total += termino - inicio
    
    print(tempo_total)         
    num_pessoas = int(input())
            
            
