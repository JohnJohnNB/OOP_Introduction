sequencia = input()
esta_ordenada = True

for i in range(1,len(sequencia)):
    if sequencia[i]<sequencia[i-1]:
        esta_ordenada = False
print(esta_ordenada)