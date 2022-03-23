nota = float(input())
parte_inteira = int(nota)
parte_decimal = nota-parte_inteira


if 0<=parte_decimal<0.25:
    parte_decimal = 0
elif 0.25<=parte_decimal<0.75:
    parte_decimal = 0.5
elif 0.75<=parte_decimal<1:
    parte_decimal = 1

nota_final = parte_inteira+parte_decimal

print(nota_final)
