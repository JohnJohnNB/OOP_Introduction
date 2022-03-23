lista=list()

for _ in range(4):
    entrada = input()
    lista.append(entrada)
    
lista_limpa = list()

for item in lista:
    if item not in lista_limpa:
        lista_limpa.append(item)

    
print(len(lista_limpa))
