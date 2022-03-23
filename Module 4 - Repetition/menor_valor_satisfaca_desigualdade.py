def fatorial(entrada):
    fatorial = 1
    for i in range(1,entrada+1):
        fatorial = fatorial*i
    return fatorial

x=1

while fatorial(x)<=x**10:
    x+=1
print(x)