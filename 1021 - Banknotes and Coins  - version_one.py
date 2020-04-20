value = float(input())
#Notas
cem = cinquenta = vinte = dez = cinco = dois = 0
#Moedas
um = cinquentinha = vinti_e_cinco = dezinho = cinquinho = unzinho = 0

# Notas

if int(value / 100) >= 1:
    cem = int(value / 100)
    value -= cem * 100

if int(value / 50) >= 1:
    cinquenta = int(value / 50)
    value -= cinquenta * 50

if int(value / 20) >= 1:
    vinte = int(value / 20)
    value -= vinte * 20

if int(value / 10) >= 1:
    dez = int(value / 10)
    value -= dez * 10

if int(value / 5) >= 1:
    cinco = int(value / 5)
    value -= cinco * 5

if int(value / 2) >= 1:
    dois = int(value / 2)
    value -= dois * 2

# Moedas

if int(value / 1) >= 1:
    um = int(value / 1)
    value -= um * 1
    value = float('%0.2f'%value)

if value // 0.50 >= 1:
    cinquentinha = value // 0.50
    value -= cinquentinha * 0.50

if value // 0.25 >= 1:
    vinti_e_cinco = value // 0.25
    value -= vinti_e_cinco * 0.25

if value // 0.10 >= 1:
    dezinho = value // 0.10
    value -= dezinho * 0.10

if value / 0.05 >= 1:
    cinquinho = value / 0.05
    value -= cinquinho * 0.05

if value / 0.01 >= 1:
    unzinho = value / 0.01
    value -= unzinho * 0.01


print("NOTAS:")
print("%d nota(s) de R$ 100.00" % cem)
print("%d nota(s) de R$ 50.00" % cinquenta)
print("%d nota(s) de R$ 20.00" % vinte)
print("%d nota(s) de R$ 10.00" % dez)
print("%d nota(s) de R$ 5.00" % cinco)
print("%d nota(s) de R$ 2.00" % dois)

print("MOEDAS:")
print("%d moedas(s) de R$ 1.00" % um)
print("%d moedas(s) de R$ 0.50" % cinquentinha)
print("%d moedas(s) de R$ 0.25" % vinti_e_cinco)
print("%d moedas(s) de R$ 0.10" % dezinho)
print("%d moedas(s) de R$ 0.05" % cinquinho)
print("%d moedas(s) de R$ 0.01" % unzinho)

