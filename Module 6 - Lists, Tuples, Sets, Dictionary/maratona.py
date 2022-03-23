num_postos, dist_intermed = [int(x) for x in input().split()]

posicao_postos = [int(x) for x in input().split()]
consegue_completar = True
for i in range(len(posicao_postos)-1):
    if posicao_postos[i+1]-posicao_postos[i]>dist_intermed:
        consegue_completar = False
        break
if consegue_completar == True:
    print("S")
else:
    print("N")