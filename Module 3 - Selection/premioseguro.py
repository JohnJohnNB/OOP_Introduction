
valor_veiculo = float(input())
classe = str(input())
procedencia = str(input())
idade = int(input())



if classe==('a') or classe==('A'):
    valor_classe = (30/100)
elif classe==('b') or classe==('B'):
    valor_classe = (20/100)
elif classe==('c') or classe==('C'):
    valor_classe = (20/100)
elif classe==('d') or classe==('D'):
    valor_classe = (5/100)
elif classe==('e') or classe==('E'):
    valor_classe = (0/100)
    
if procedencia == ('nacional'):
    valor_procedencia = (10/100)
elif procedencia == ('estrangeira'):
    valor_procedencia = (15/100)
    
if 24<idade:
    desconto_idade = (10/100)
else:
    desconto_idade = 0

resultado_final = (valor_veiculo*valor_procedencia)*((1)-(valor_classe + desconto_idade))

print("{0:.2f}".format(resultado_final))