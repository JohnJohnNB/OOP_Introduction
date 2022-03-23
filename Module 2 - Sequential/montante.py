capital = float(input())
meses = int(input())
taxa = float(input())

montante = capital * ((1 + taxa/100)**meses)
montante_limite = round(montante, 2)

print(montante_limite)
