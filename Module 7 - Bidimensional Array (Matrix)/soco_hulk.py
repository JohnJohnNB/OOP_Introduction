qtd_testes = int(input())

for _ in range(qtd_testes):
    blocos = []
    nl, nc, x, y = [int(x) for x in input().split()]
    for z in range(nl):
        blocos.append([int(x) for x in input().split()])

    for i in range(nl):
        for j in range(nc):
            distancia_x = 10-abs((x-1-i)) if 10-abs((x-1-i)) >= 1 else 1
            distancia_y = 10-abs((y-1-j)) if 10-abs((y-1-j)) >= 1 else 1
            blocos[i][j] += min(distancia_x,distancia_y)
    print(f"Parede {_+1}:")
    for z in range(nl): 
        print(*blocos[z])
