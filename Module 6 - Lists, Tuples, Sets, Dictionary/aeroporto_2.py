num_aeroportos, num_voos = [int(x) for x in input().split()]
numero_teste = 1
while num_aeroportos != 0:
    
    
    lista_num_aero = []
    dict_aeroporto = dict()

    for i in range(num_aeroportos):
        lista_num_aero.append(i+1)
        dict_aeroporto[lista_num_aero[i]] = 0
        
    lista_voos = []

    for _ in range(num_voos):
        voos = [int(x) for x in input().split()]
        lista_voos.extend(voos)
    for i in lista_voos:
        dict_aeroporto[i] += 1
        
    aeroporto_congestionado = max(dict_aeroporto, key= lambda x: dict_aeroporto[x])
    lista_congestionados = []
    lista_congestionados.append(aeroporto_congestionado)
    voos_aero_congestionado = dict_aeroporto[aeroporto_congestionado]
    dict_aeroporto.pop(aeroporto_congestionado)
    
    for keys in dict_aeroporto.keys():
        if dict_aeroporto[keys] == voos_aero_congestionado:
            lista_congestionados.append(keys)
    

    
    
    print(f'Teste {numero_teste}')
    print(*sorted(lista_congestionados))
    print(" ")
    
    numero_teste += 1
    num_aeroportos, num_voos = [int(x) for x in input().split()]

