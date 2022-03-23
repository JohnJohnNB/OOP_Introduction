idade =  int(input())

anos = idade//365
meses = (idade%365)//30
dias = (idade%365)%30

print(anos,"ano(s)")
print(meses,"mes(es)")
print(dias,"dia(s)")