count_par = 0
count_impar = 0
count_positivo = 0
count_negativo = 0

for i in range(1, 6):
    valor = int(input())
    if abs(valor)%2 == 0:
        count_par += 1
    else:
        count_impar += 1
    if valor>0:
        count_positivo += 1
    elif valor<0:
        count_negativo += 1
        

print(f"{count_par} valor(es) par(es)")
print(f"{count_impar} valor(es) impar(es)")
print(f"{count_positivo} valor(es) positivo(s)")
print(f"{count_negativo} valor(es) negativo(s)")

