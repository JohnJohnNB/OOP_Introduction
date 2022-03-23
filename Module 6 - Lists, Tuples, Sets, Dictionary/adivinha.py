num_casos_teste = int(input())

for _ in range(num_casos_teste):
    num_alunos, num_secreto = [int(x) for x in input().split()]
    valor_adivinha = [int(x) for x in input().split()]
    lista = []
    for i in range(num_alunos):
        diferenca_valores = lista.append(abs(valor_adivinha[i]-num_secreto))
    diferenca_vencedor = min(lista)
    posicao_vencedor = lista.index(diferenca_vencedor)+1
    
    print(posicao_vencedor)