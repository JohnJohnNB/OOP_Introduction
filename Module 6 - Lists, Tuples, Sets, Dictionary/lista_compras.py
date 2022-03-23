num_listas = int(input())
for i in range(num_listas):
    compras = [str(x) for x in input().split()]
    compras_limpo = sorted(set(compras))
    print(*compras_limpo)