a = int(input())
b = int(input())

if a>b:
    intervalo = range(b,a)
else:
    intervalo = range(a,b)
    
num_elementos = len(list(intervalo))
resultado = (num_elementos+1)

    
print(resultado)
