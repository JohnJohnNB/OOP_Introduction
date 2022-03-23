lado1 = int(input())
lado2 = int(input())
lado3 = int(input())

if lado1==lado2==lado3:
    print("equilátero")
elif lado1==lado2 or lado2==lado3 or lado1==lado3:
    print("isósceles")
else:
    print("escaleno")

