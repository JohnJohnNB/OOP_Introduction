def montante(capital, meses, taxa):
    montante1 = capital * ((1 + taxa/100)**meses)
    montante_limite = round(montante1, 2)
    return montante_limite

c = float(input())
m = int(input())
t = float(input())

print(montante(c, m, t))