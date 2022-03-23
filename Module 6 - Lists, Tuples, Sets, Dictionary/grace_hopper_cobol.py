base = ['c','o','b','o','l']
resultado = []
while True:
    try:
        resultado = []
        tem_cobol = True
        entrada = input().lower().split("-")
        if entrada[0][0] == 'c' or entrada[0][-1] == 'c':
            resultado.append('c')
            for i in range(1,len(entrada)):
                if entrada[i][0] == base[i] or entrada[i][-1] == base[i]:
                    resultado.append(base[i])
                else:
                    tem_cobol = False
                    break
        else:
            tem_cobol = False
        if tem_cobol == False:
            print("BUG")
        else:
            print("GRACE HOPPER") 
    except EOFError:
        break