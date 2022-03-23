altura_pulo, num_canos = [int(x) for x in input().split()]
altura_canos = [int(x) for x in input().split()]

for i in range(num_canos-1):
    if abs(altura_canos[i] - altura_canos[i+1]) > altura_pulo:
        print("GAME OVER")
        break
    else:
        print("YOU WIN")
        break