dia1 = int(input())
dia2 = int(input())
dia3 = int(input())

if dia1==dia2==dia3:
    festas = 1
elif dia1==dia2 or dia1==dia3 or dia2==dia3:
    festas = 2
else:
    festas = 3
print(festas)