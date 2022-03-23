import math

x = int(input())
primo = True

if x == 1:
    primo = False
elif x == 2:
    primo = True
    
if x >= 6:
    
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            primo = False
            break
else:
    
    for i in range(2,x):
        if x%i==0:
            primo = False
            break
        
print(primo)
    
