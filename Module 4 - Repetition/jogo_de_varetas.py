num_comprimentos = int(input())
while num_comprimentos != 0:
    
    varetas_disponiveis = 0
    for _ in range(num_comprimentos):
        comprimento, num_varetas = [int(w) for w in input().split()]
        excedente = num_varetas%2
        varetas_disponiveis += num_varetas - excedente
    print(varetas_disponiveis//4)
    num_comprimentos = int(input())
