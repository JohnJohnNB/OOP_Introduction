x = int(input())
binario = ''
if x == 0:
    binario = '0'
while x > 0:
    resto = x%2
    binario+=str(resto)
    x //=2
print(binario[::-1])
