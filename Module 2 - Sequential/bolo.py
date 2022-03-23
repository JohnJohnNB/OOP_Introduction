xicaras, ovos, colheres = [int(w) for w in input().split()]

xi = (xicaras//2)
ov = (ovos//3)
co = (colheres//5)

print(min(xi,ov,co))