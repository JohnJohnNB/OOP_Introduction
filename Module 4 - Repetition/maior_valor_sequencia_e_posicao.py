tamanho_sequencia = int(input())
contagem = 0
posicao_maior = 0
maior_valor = -10000

for _ in range(tamanho_sequencia):
    x = int(input())
    contagem+=1
    if x > maior_valor:
        maior_valor = x
        posicao_maior = contagem
    
        
print(f"{maior_valor} {posicao_maior}")