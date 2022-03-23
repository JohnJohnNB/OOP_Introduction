notas = [float(x) for x in input().split()]

notas_removidas = list()
notas_removidas.extend([(max(notas)), min(notas)])

for i in range(len(notas_removidas)):
    
    notas.remove(notas_removidas[i])

print(round(sum(notas), 2))