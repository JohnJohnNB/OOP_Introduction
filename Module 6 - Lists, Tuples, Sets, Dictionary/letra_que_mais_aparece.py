entrada = input()
entrada = entrada.lower().replace(' ','')
lista = []

for letra in entrada:
    lista.append(letra)

contador = 0
letra_destaque = ''

for i in range(len(lista)):
    count = lista.count(lista[i])
    if count > contador:
        contador = count
        letra_destaque = lista[i]
print(letra_destaque)
    
