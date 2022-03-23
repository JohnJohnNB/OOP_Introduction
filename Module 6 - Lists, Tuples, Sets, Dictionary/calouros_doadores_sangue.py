calouros = []
num_calouros = int(input())
for _ in range(num_calouros):
    calouros.append(input())
num_doadores = int(input())
doadores = []
for i in range(num_doadores):
    doadores.append(input())
calouros_doadores = 0
for j in range(len(calouros)):
    if calouros[j] in doadores:
        calouros_doadores+=1
print(calouros_doadores/num_calouros)

        