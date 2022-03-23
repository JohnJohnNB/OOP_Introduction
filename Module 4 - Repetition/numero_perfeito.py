tamanho_sequencia = int(input())

for _ in range(tamanho_sequencia):
    count_divisores = 0
    num_entrada = int(input())
    for i in range(1,num_entrada):
        if num_entrada%i == 0:
            count_divisores+=i
    if count_divisores == num_entrada:
        print(f"{num_entrada} eh perfeito")
    else:
        print(f"{num_entrada} nao eh perfeito")
    