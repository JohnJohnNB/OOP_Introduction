numero_entrada= int(input())
if numero_entrada == 1:
    numero_entrada =+ 6

while numero_entrada % 2 == 0:
    numero_entrada //= 2
while numero_entrada % 3 == 0:
    numero_entrada //= 3
while numero_entrada % 5 == 0:
    numero_entrada //= 5

print(numero_entrada==1)
