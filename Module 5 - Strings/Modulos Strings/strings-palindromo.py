frase =  "Socorram-me, subi no onibus em marrocos."

frase_limpa = ''
for caracter in frase.lower():
    if caracter.isalpha():
        frase_limpa += caracter
print(frase_limpa == frase_limpa[::-1])