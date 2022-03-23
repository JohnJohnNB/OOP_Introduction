num_participantes = int(input())
num_teste = 1
while num_participantes != 0:
    ingressos = [int(x) for x in input().split()]
    for i in range(num_participantes):
        if ingressos[i] == i+1:
            print(f"Teste {num_teste}")
            print(ingressos[i])
            break
    num_participantes = int(input())
    num_teste += 1