import math

numero = 0.5

if numero<0:
    sinal_expoente = '-'
else:
    sinal_expoente = '+'
    
expoente = int(math.log(n, 10))   

if numero<1:
    expoente-=1

numero_notacao = numero/10**expoente

print(f'{numero_notacao:.4f}E{expoente:02}')

