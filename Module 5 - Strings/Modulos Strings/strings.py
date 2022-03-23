nome = input("Insira o nome: ")

ind = nome.rindex(' ')
sobrenome = nome[ind+1:]
primeiro_nome = nome[:ind]
nome_lista_telefonica = sobrenome + ", " + primeiro_nome
print(nome_lista_telefonica)

