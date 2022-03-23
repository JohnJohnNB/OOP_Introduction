escala_origem = input()
valor_temp = float(input())
escala_destino = input()



if escala_origem==('c') and escala_destino==('k'):
    conversao = valor_temp+273.15
elif escala_origem==('c') and escala_destino==('f'):
    conversao = valor_temp*1.8 + 32
elif escala_origem==('c') and escala_destino==('r'):
    conversao = valor_temp*1.8 + 491.67
elif escala_origem==('k') and escala_destino==('c'):
    conversao = valor_temp-273.15
elif escala_origem==('k') and escala_destino==('f'):
    conversao = 1.8*(valor_temp-273.15)+32
elif escala_origem==('k') and escala_destino==('r'):
    conversao = valor_temp*1.8
elif escala_origem==('f') and escala_destino==('c'):
    conversao = (valor_temp-32)/1.8
elif escala_origem==('f') and escala_destino==('k'):
    conversao = (valor_temp+459.67)*5/9
elif escala_origem==('f') and escala_destino==('r'):
    conversao = valor_temp+459.67
elif escala_origem==('r') and escala_destino==('f'):
    conversao = valor_temp-459.67
elif escala_origem==('r') and escala_destino==('c'):
    conversao = (valor_temp-491.67)/1.8
elif escala_origem==('r') and escala_destino==('k'):
    conversao = valor_temp/1.8


print(conversao)