qtd_disciplinas = int(input())
dias = {'2':[],'3':[],'4':[],'5':[],'6':[]}
horarios = ['0730','0820','0910','1010','1100','1330','1420','1510','1620','1710','1830','1920','2020','2110']
disciplinas = dict()

for _ in range(qtd_disciplinas):
    infos = [str(x) for x in input().split()]
    disciplinas[infos[0]] = infos[1:]
    if len(infos)>=3:
        for i in range(len(infos)-1):
            dias[infos[i+1][0]].append(infos[0])
    else:
        dias[infos[1][0]].append(infos[0])
        
dias_keys = dias.keys()
disciplina_um = []
disciplina_dois = []
disciplinas_choque = []
indice = 0

for chaves in dias_keys:
    if len(dias[chaves])>=2:
        for k in range(len(dias[chaves])-1):
            disciplinas_choque.append(dias[chaves][k])
            disciplinas_choque.append(dias[chaves][k+1])
            
            vtnc = horarios.index(disciplinas[dias[chaves][k]][0][1:5])
            vtnc2 = int(disciplinas[dias[chaves][k]][0][-1])
            fodase = [disciplina_um.append(horarios[j]) for j in range(vtnc,(vtnc+vtnc2))]
                
    
    
        
        