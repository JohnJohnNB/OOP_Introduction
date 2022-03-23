valor_compra = float(input())
valor_final = 0.8*valor_compra

if 500 <=valor_compra < 1000:
    valor_final -= 0.1*valor_compra
elif valor_compra >=1000:
    valor_final-= (0.1*valor_compra + 0.15*(valor_compra-1000))
    
print("{:.2f}".format(valor_final))
