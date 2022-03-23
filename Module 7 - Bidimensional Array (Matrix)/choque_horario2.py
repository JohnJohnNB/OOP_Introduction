matriz = [[0 for coluna in range(5)] for linha in range(14)]
horarios = {'0730':0,'0820':1,'0910':2,'1010':3,'1100':4,'1330':5,'1420':6,'1510':7,'1620':8,'1710':9,'1830':10,'1920':11,'2020':12,'2110':13}

qtd_disciplinas = int(input())
em_choque = []

for i in range(qtd_disciplinas):
    disciplina = [str(x) for x in input().split()]
    tamanho = len(disciplina)
    if em_choque == []:     
        for j in range(tamanho-1):
            dia_semana = int(int(disciplina[j+1][0])-2)
            qtd_aulas = int(disciplina[j+1][-1])
            hora = disciplina[j+1][1:5]
            for k in range(qtd_aulas):
                if matriz[horarios[hora]+k][dia_semana] == 0:
                    matriz[horarios[hora]+k][dia_semana] = disciplina[0]
                else:
                    em_choque.append(matriz[horarios[hora]+k][dia_semana])
                    em_choque.append(disciplina[0])
                    break
            if em_choque != []:
                break   
print(*em_choque)
        
