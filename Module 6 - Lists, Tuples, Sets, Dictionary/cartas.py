cartas = [int(x) for x in input().split()]

for i in range(len(cartas)-1):
    if cartas[i+1]<cartas[i]:
        if cartas[i+1]>cartas[i+2]:
            print("D")
            break
        else:
            print("N")
            break
    else:
        print("C")
        break
       