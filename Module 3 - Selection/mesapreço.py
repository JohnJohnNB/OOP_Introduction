comprimento = float(input())
largura_mesa = float(input())
numero_gavetas = int(input())
tipo_madeira = input()

area_mesa = comprimento*largura_mesa
custo_area = 100*area_mesa
custo_gaveta = 30*numero_gavetas

if area_mesa > 2:
    acrescimo = 50
else:
    acrescimo = 0
    
if tipo_madeira == 'mogno':
    acrescimo += 150
elif tipo_madeira == 'carvalho'
    acrescimo += 125
else:
    acrescimo = 0

custo_mesa = max(200, (custo_area + custo_gaveta + acrescimo))
print("{:.2f}".format(custo_mesa))
