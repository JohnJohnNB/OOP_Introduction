tabela = []
for _ in range(12):
    qtd_chuva = [int(x) for x in input().split()]
    tabela.append(qtd_chuva)
for mes in tabela:
    media = sum(mes)/len(mes)
    print(f"{media:.2f}",end=' ')