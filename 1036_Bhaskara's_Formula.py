# from math import sqrt -- Leva muito tempo pra importar

A, B, C = map(float,input().split())
delta = (B**2) - (4*A*C)

if A != 0 and delta > 0:
    R1 = ((-B) + (delta ** 0.5)) / (A * 2)
    R2 = ((-B) - (delta ** 0.5)) / (A * 2)
    print("R1 = %0.5f" % R1)
    print("R2 = %0.5f" % R2)
else:
    print("Impossivel calcular")


