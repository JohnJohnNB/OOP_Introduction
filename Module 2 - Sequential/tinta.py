area = int(input())
minimo = 1

galoes = (area/64.8)
galoes_round = round(galoes)
galoes_final = max(minimo, galoes_round)
valor = (galoes_final*25)
valor_round = "{:.2f}".format(valor)


print("- área de cobertura:", area)
print("- número de galões:", galoes_final)
print("- valor a ser pago: R$", valor_round)