entrada = input()
soma = 0
peso = len(entrada)

for numero in range(len(entrada)-1):
    soma+=int(entrada[numero])*peso
    peso -= 1
dv1 = 11 - soma%11
if dv1 >= 10:
    dv1 = 0
        
print(dv1==int(entrada[-1]))