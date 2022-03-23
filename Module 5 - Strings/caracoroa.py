qtd_jogos = int(input())
while qtd_jogos != 0:
    jogos = [int(x) for x in input().split()]
    marry = jogos.count(0)
    john = jogos.count(1)
    print(f"Mary won {marry} times and John won {john} times")
    qtd_jogos = int(input())