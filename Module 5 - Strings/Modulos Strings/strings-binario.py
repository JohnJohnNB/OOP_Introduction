numero = input()
eh_binario = True

for caracter in numero:
    if caracter != '1' and caracter != '0':
        eh_binario = False
        break
    
print(eh_binario)