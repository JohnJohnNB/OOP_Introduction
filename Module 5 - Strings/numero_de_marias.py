num_nomes = int(input())
contagem = 0

for i in range(num_nomes):
    nome = input()
    substrings = nome.split(' ')
    for _ in range(len(substrings)):
        if substrings[_] == 'Maria':
            contagem+=1
    

print(contagem)

