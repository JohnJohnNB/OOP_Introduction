entrada = input().lower().split()
eh_tautograma = True
while entrada != ['*']:
    tamanho_frase = len(entrada)
    for i in range(tamanho_frase-1):
        if entrada[i][0]!=entrada[i+1][0]:
            eh_tautograma = False
            break
    if eh_tautograma == True:
        print("Y")
    else:
        print("N")       
    entrada = input().lower().split()