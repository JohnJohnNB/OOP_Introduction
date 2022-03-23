conector1 = [int(x) for x in input().split()]
conector2 = [int(x) for x in input().split()]
eh_compativel = True
for i in range(len(conector1)):
    if conector1[i] == conector2[i]:
        eh_compativel = False
print("Y") if eh_compativel == True else print("N")    