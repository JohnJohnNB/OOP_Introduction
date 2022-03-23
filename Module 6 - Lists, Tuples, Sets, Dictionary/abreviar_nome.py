nome = input().split()

nomes_centrais = nome[1:-2]

for i in range(len(nomes_centrais)):
    nome[i+1] = nomes_centrais[i][0] + '.'

nome_limpo = ' '.join(nome)
print(nome_limpo)