num_jogadores, num_partidas = [int(x) for x in input().split()]
gols = []
jogadores_goleadores = 0
for _ in range(num_jogadores):
    gols.append([])
    gols[_] = [str(x) for x in input().split()]
    if '0' not in gols[_]:
        jogadores_goleadores+=1
print(jogadores_goleadores)