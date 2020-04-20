
valorN = int(input())
cem = cinquenta = vinte = dez = cinco = dois = um = 0

n = valorN
print(n)
if n % 100 == 0:
    n = n / 100
    cem = n
elif n % 100 != 0:
    # in the next line, I should have used n//100 not int(n/100) -- double bar == integer division
    cem = int(n/100)
    n = n % 100
print('%.f nota(s) de R$ 100,00' % cem)

if n % 50 == 0:
    n = n / 50
    cinquenta = n
elif n % 50 != 0:
    cinquenta = int(n/50)
    n = n % 50
print('%.f nota(s) de R$ 50,00' % cinquenta)

if n % 20 == 0:
    n = n / 20
    vinte = n
elif n % 20 != 0:
    vinte = int(n/20)
    n = n % 20
print('%.f nota(s) de R$ 20,00' % vinte)

if n % 10 == 0:
    n = n / 10
    dez = n
elif n % 10 != 0:
    dez = int(n/10)
    n = n % 10
print('%.f nota(s) de R$ 10,00' % dez)

if n % 5 == 0:
    n = n / 5
    cinco = n
elif n % 5 != 0:
    cinco = int(n/5)
    n = n % 5
print('%.f nota(s) de R$ 5,00' % cinco)

if n % 2 == 0:
    n = n / 2
    dois = n
elif n % 5 != 0:
    dois = int(n/2)
    n = n % 2
print('%.f nota(s) de R$ 2,00' % dois)

if n % 1 == 0:
    n = n / 1
    um = n
elif n % 5 != 0:
    um = int(n/1)
    n = n % 1
print('%.f nota(s) de R$ 1,00' % um)


    # in the and, URI Fuck with me, so I Submitted this code: https://github.com/chgsilva/URI/blob/master/beginner/python/1018.py -- thanks bro