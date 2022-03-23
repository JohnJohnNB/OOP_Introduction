num_bolas = int(input())
bolas = [int(x) for x in input().split()]

for j in range(num_bolas-1):
    for i in range(len(bolas)-1):
        if bolas[i]==bolas[i+1]:
            bolas[i] = 1
        else:
            bolas[i] = -1
    bolas.pop()
    
if bolas[0] == 1:
    print("preta")
else:
    print("branca")
