alfabeto_original = input()
alfabeto_cifragem = input()
lista_alfabeto_cifragem = list(alfabeto_cifragem)
frase_cifrada = input()
tabela_cifragem = tuple(zip(alfabeto_original, alfabeto_cifragem))
frase_decifrada = ""

for i in range(len(frase_cifrada)):
    if frase_cifrada[i] == " ":
        frase_decifrada+=" "
    elif frase_cifrada[i] not in lista_alfabeto_cifragem:
        frase_decifrada+=frase_cifrada[i]   
    else:        
        for j in range(len(tabela_cifragem)):
            if frase_cifrada[i] in tabela_cifragem[j][1]:
                frase_decifrada += tabela_cifragem[j][0]
print(frase_decifrada)