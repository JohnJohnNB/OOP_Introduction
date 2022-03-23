frase = input().strip()
frase_limpa = ''
for letras in frase:
    if letras.isalpha() == True:
        frase_limpa += letras
inverso = frase_limpa[::-1]

if inverso == frase_limpa:
    print(True)
else:
    print(False)