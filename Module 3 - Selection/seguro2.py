valor = float(input())
sexo = str(input())
idade = int(input())

if sexo==('M') and idade<=24:
    desconto = (0/100)
elif sexo==('M') and 25<=idade<=33:
    desconto = (10/100)
elif sexo==('M') and idade>33:
    desconto = (20/100)
elif sexo==('F') and idade<=24:
    desconto = (5/100)
elif sexo==('F') and idade>33:
    desconto = (35/100)
elif sexo==('F') and 25<=idade<=33:
    desconto = (20/100)

resultado = ((valor*10/100)*((100/100)-desconto))

print(resultado)