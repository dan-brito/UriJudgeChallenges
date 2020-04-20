'''
this is a multiple comment
'''

print(5/2)
print(5//2.0)
value = int(input())
val = value
cem = cinquenta = vinte = dez = cinco = dois = um = 0

if value // 100 >= 1:
    cem = value // 100
    value -= cem * 100

if int(value / 50) >= 1:
    cinquenta = int(value / 50)
    value -= cinquenta * 50

print("%d" % val)
print("%d nota(s) de R$ 100,00" % cem)
print("%d nota(s) de R$ 50,00" % cinquenta)

a = 0.73/0.50
b = a * 0.50
print(b)
