massa = float(input())
count = 0
    
while True:
    if massa < 0.5:
        count = 0
        break
    massa_restante = massa/2
    massa = massa_restante
    count+=1
    if massa_restante < 0.5:
        break
tempo = count*50
print(tempo)