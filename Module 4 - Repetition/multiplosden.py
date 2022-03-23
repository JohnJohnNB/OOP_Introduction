n_valor = int(input())
m_valor = int(input())

for i in range(1, (m_valor+1)):
    if i%n_valor == 0:
        print(i, end=' ')
