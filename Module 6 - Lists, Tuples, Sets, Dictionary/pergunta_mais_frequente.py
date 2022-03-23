num_perguntas, qtd_frequente = [int(x) for x in input().split()]

while num_perguntas != 0 and qtd_frequente != 0:
    
    perguntas = [int(x) for x in input().split()]    
    contagem = [0]*num_perguntas
    for pergunta in perguntas:
        contagem[pergunta-1]+=1

    qtd_perguntas = 0
    for num in contagem:
        if num >= qtd_frequente:
            qtd_perguntas += 1
            
    print(qtd_perguntas)
    num_perguntas, qtd_frequente = [int(x) for x in input().split()]