qtd_testes = int(input())
arvores = []
for _ in range(qtd_testes+1):
    arvore = input()
    while arvore != '':
        arvores.append(arvore)
        arvore = input()
    if arvore == '' and len(arvores)>0:       
        for especie in sorted(set(arvores)):
            porcentagem = (arvores.count(especie)/len(arvores))*100
            print(f"{especie} {porcentagem:.4f}")
        print("")
    arvores = []
