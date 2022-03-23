L, D = [int(w) for w in input().split()]
K, P = [int(w) for w in input().split()]

preço = (L*K + (L//D)*P)

print(preço)