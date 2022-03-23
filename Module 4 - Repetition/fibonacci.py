
n_esimo = int(input())
x = 1
y = 1
z = 1

for _ in range(3, n_esimo+1):
    z = x + y
    x = y
    y = z

print(z)


    
    
