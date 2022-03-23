def equivalente(conceito):
    if conceito == 'A':
        nota = 4
    elif conceito == 'B':
        nota = 3
    elif conceito == 'C':
        nota = 2
    else:
        nota = 0
    return nota

conceito1 = input()
conceito2 = input()
conceito3 = input()
conceito4 = input()



eq1 = equivalente(conceito1)
eq2 = equivalente(conceito2)
eq3 = equivalente(conceito3)
eq4 = equivalente(conceito4)

ia = (eq1+eq2+eq3+eq4)/4
aprovacao = ia >= 3

print(aprovacao)