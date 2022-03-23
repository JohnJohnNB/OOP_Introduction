num_competidores, qtd_total_folhas, qtd_folhas_competidor = [int(w) for w in input().split()]

a = qtd_total_folhas/num_competidores

if a >= qtd_folhas_competidor:
    print("S")
else:
    print("N")
    
    