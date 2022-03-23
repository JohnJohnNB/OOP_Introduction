valores_romanos = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1, 'IV':4, 'IX': 9, 'XL':40,
                   'XC':90, 'CD':400, 'CM':900}

entrada = input()
numero_decimal = 0
i = 0

while i<len(entrada):
    grupo = entrada[i:i+2]
    if grupo in valores_romanos:
        numero_decimal += valores_romanos[grupo]
        i+=2
    else:
        digito_romano = entrada[i]
        numero_decimal+= valores_romanos[digito_romano]
        i+=1

print(numero_decimal)