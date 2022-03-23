num_valores_cedulas = int(input())
cedulas = dict()

for i in range(num_valores_cedulas):
    valor_cedula = float(input())
    cedulas[valor_cedula] = int(input())
    
valor_saque = float(input())
cedulas_list = sorted(cedulas.keys(), reverse=True)
cedulas_necessarias = []


for j in range(len(cedulas_list)):
    if cedulas[cedulas_list[j]]> 0:
        quantia_cedula = int(valor_saque//cedulas_list[j])
        if quantia_cedula > cedulas[cedulas_list[j]]:
            valor_cedula = int(cedulas[cedulas_list[j]])
            cedulas_necessarias.append(valor_cedula)
            cedulas[cedulas_list[j]]-=int(valor_cedula)
            valor_saque = valor_saque-(cedulas_list[j]*valor_cedula)
        else:
            
            cedulas_necessarias.append(int(valor_saque//cedulas_list[j]))
            cedulas[cedulas_list[j]]-=int(valor_saque//cedulas_list[j])
            valor_saque = valor_saque%cedulas_list[j]
    else:
        cedulas_necessarias.append(0)  
                                                              
    
cedulas_necessarias.reverse()

print(*cedulas_necessarias)

