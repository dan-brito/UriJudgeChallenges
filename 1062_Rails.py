'''
Ordenação







'''

# A = input().split()
A = "5 4 3 2 1 ".split()
B = "7 5 2 3 4 1 6".split()
C = "1 3 2 5 4 6".split()
lista = [int(i)for i in C]
#print(lista)
#print(type(lista[0]))

matrix = list()

if sorted(lista) == lista or sorted(lista, reverse=True) == lista:
    print("Yes")
else:
    if max(lista) or min(lista) != lista[0]:
        print("No")
    else:
        for i in lista:
            if len(matrix) == 0:
                matrix.append(i)
                alpha = matrix[-1]
                print()
            elif alpha + 1 or alpha -1 or alpha +2 or alpha -2 != i:
                print("No")
            elif alpha + 1 or alpha -1 or alpha +2 or alpha -2 == i:
                matrix.append(i)

if len(matrix) == len(lista):
    print("Yes")

