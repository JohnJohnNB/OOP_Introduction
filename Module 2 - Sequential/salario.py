normal = int(input())
extra = int(input())

bruto = normal*(25/2) + extra*15
bruto_limite = "{:.2f}".format(bruto)

IR = bruto*(13/100)
IR_limite = "{:.2f}".format(IR)

INSS = bruto*(9/100)
INSS_limite = "{:.2f}".format(INSS)

LIQ = bruto - (IR + INSS)
LIQ_limite = "{:.2f}".format(LIQ)



print("- Salário Bruto : R$", bruto_limite)
print("- IR (13%) : R$", IR_limite)
print("- INSS (9%) : R$", INSS_limite)
print("- Salário Líquido : R$", LIQ_limite)