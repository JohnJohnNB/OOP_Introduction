dias = int(input())
km_rodado = float(input())

custo_dias = 45*dias
km_rodado_cortesia = 60*dias
if km_rodado > km_rodado_cortesia:
    custo_dias += (km_rodado-km_rodado_cortesia)*0.5
    
print("{:.2f}".format(custo_dias))
    