import math

a = int(input())
b = int(input())
c = int(input())

delta = b**2 - 4*a*c

x1 = (-b + math.sqrt(delta)) / (2*a)
x2 = (-b - math.sqrt(delta)) / (2*a)

print(x1, x2)