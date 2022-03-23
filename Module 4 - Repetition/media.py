tamanho_sequencia = int(input())
media = 0

for i in range(tamanho_sequencia):
    numero = float(input())
    media += numero
    
print(media/tamanho_sequencia)
    