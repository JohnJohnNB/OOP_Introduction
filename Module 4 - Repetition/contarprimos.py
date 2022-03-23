def contarprimo(x):
    primo = True

    if x == 1:
        primo = False
    elif x == 2:
        primo = True
        
    for i in range(2,x):
        if x%i==0:
            primo = False
            break
    return primo
    
x = int(input())
y = int(input())
numero_primos = 0

for i in range(x,y+1):
    if contarprimo(i):
        numero_primos+=1
print(numero_primos)