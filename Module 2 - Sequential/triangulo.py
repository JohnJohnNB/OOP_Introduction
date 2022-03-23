lado1 = float(input())
lado2 = float(input())
lado3 = float(input())

triangulo = (abs(lado1) + abs(lado2)) > abs(lado3) and (abs(lado2) + abs(lado3)) > abs(lado1) and (abs(lado3) + abs(lado1)) > abs(lado2)
print(triangulo)