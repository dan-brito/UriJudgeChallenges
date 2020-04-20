from fractions import Fraction
case_test = int(input())

operations = []
for i in range(case_test):
    operations.append(input())


for x in operations:
    v = x.split()
    if "+" in v:
        #result = Fraction((int(v[0]) * int(v[6]) + int(v[4]) * int(v[2])), (int(v[2])*int(v[6])))
        numerador = (int(v[0]) * int(v[6])) + (int(v[4]) * int(v[2]))
        denominador = int(v[2]) * int(v[6])
        parte1 = Fraction(int(v[0]), int(v[2]))
        parte2 = Fraction(int(v[4]), int(v[6]))
        result = parte1 + parte2
        print('{}/{} = {}'.format(numerador, denominador, result))

    elif "-" in v:
        numerador = (int(v[0]) * int(v[6])) - (int(v[4]) * int(v[2]))
        denominador = int(v[2]) * int(v[6])
        parte1 = Fraction(int(v[0]), int(v[2]))
        parte2 = Fraction(int(v[4]), int(v[6]))
        result = parte1 - parte2
        print('{}/{} = {}'.format(numerador, denominador, result))
    elif "*" in v:
        numerador = (int(v[0]) * int(v[4]))
        denominador = int(v[2]) * int(v[6])
        parte1 = Fraction(int(v[0]), int(v[2]))
        parte2 = Fraction(int(v[4]), int(v[6]))
        result = parte1 * parte2
        print('{}/{} = {}'.format(numerador, denominador, result))
    elif "/" in v:
        numerador = (int(v[0]) * int(v[6]))
        denominador = int(v[2]) * int(v[4])
        parte1 = Fraction(int(v[0]), int(v[2]))
        parte2 = Fraction(int(v[4]), int(v[6]))
        result = parte1 / parte2
        print('{}/{} = {}'.format(numerador, denominador, result))



