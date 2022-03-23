l, c = [int(x) for x in input().split()]
li, ci = [int(x)-1 for x in input().split()]

ladrilhos = [[int(x) for x in input().split()]for _ in range(l)]

deslocamentos = ((-1,0),(0,1),(1,0),(0,-1))

while True:
    for dl, dc in deslocamentos:
        if 0 <= li+dl < l and 0 <= ci+dc < c and ladrilhos[li+dl][ci+dc] == 1:
            break
    else:
        break
    ladrilhos[li][ci] = 0
    li += dl
    ci += dc
print(li+1,ci+1)
