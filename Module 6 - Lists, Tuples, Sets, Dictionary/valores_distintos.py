lista=[]

for _ in range(4):
    entrada = input()
    lista.append(entrada)

valores_distintos = set(lista)
print(len(valores_distintos))
