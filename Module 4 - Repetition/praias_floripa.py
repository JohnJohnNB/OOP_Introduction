num_praia = int(input())

maior_distancia = 0
praia_mais_distante = ''
count_entre15e20km = 0
distancia_media = 0

for _ in range(num_praia):
    praia, distancia = input().split(';')
    distancia = int(distancia)
    if distancia > maior_distancia:
        maior_distancia = distancia
        praia_mais_distante = praia
    if 15<=distancia<=20:
        count_entre15e20km += 1
    distancia_media += distancia
    
distancia_media = round(distancia_media/num_praia,1)

print(f"{praia_mais_distante};{count_entre15e20km};{distancia_media}")