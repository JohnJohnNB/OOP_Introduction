n_bandejas = int(input())
copos_quebrados = 0
for _ in range(n_bandejas):
    n_latas, n_copos = [int(w) for w in input().split()]
    if n_latas > n_copos:
        copos_quebrados+=n_copos
print(copos_quebrados)