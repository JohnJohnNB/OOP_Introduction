
num_aeroportos, num_voos = [int(x) for x in input().split()]
while num_aeroportos != 0:
    
    num_teste = 1
    voos_aeroportos = []
    for _ in range(num_voos):
        voo = [int(x) for x in input().split()]
        voos_aeroportos.extend(voo)
        
    contagem = 0
    for i in range(num_aeroportos):
        num_voos_aero = voos_aeroportos.count(i)
        if num_voos_aero > contagem:
            contagem = num_voos_aero
            aero_mais_congest = voos_aeroportos[i]
    print(f'Teste {num_teste}')
    print(sortedaero_mais_congest)
    num_teste+=1
    
    
    num_aeroportos, num_voos = [int(x) for x in input().split()]
