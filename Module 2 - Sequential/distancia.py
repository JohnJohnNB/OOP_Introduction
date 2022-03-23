import math

x, y = [float(w) for w in input().split()]
x2, y2 = [float(w) for w in input().split()]

distancia = math.sqrt((x2-x)**2+(y2-y)**2)
d_round = round(distancia, 4)

print(d_round)
