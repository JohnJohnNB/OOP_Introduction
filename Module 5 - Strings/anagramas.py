palavra = input()
palavra2 = input()

anagrama = True

if palavra == palavra2 or len(palavra) != len(palavra2) or sorted(palavra) != sorted(palavra2):
    anagrama = False
print(anagrama)