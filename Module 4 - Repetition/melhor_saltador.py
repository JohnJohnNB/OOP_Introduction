num_saltadores = int(input())
melhor_salto = 0
melhor_saltador = ''

        
for _ in range(num_saltadores):
    a, b, c, d = [str(w) for w in input().split()]
    a = float(a)
    b = float(b)
    c = float(c)
    if a > melhor_salto:
        melhor_salto = a
        melhor_saltador = d
    if b > melhor_salto:
        melhor_salto = b
        melhor_saltador = d
    if c > melhor_salto:
        melhor_salto = c
        melhor_saltador = d
print(melhor_saltador)
