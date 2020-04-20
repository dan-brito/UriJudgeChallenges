# My first solution - The result it is correct, except by the runtime error

a = float(input())
b = float(input())
c = float(input())

pi = 3.14159

triangulo = (a * c)/2
circulo = pi * c ** 2
trapezio = ((a + b) * c)/2
quadrado = b ** 2
retangulo = a * b

print('TRIANGULO: %0.3f' % triangulo )
print('CIRCULO: %0.3f' % circulo)
print('TRAPEZIO: %0.3f' % trapezio)
print('QUADRADO: %0.3f '% quadrado)
print('RETANGULO: %0.3f' % retangulo)

# Uri Solution -  this code if a lot of floats - seems really bad
valor = input().split(" ")

a, b, c = valor
pi = 3.14159

triangulo = (float(a) * float(c))/2
circulo = pi * (float(c)* float(c))
trapezio = float(c) *(float(a) + float(b)) / 2
quadrado = float(b) * float(b)
retangulo = float(a) * float(b)


print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" % (triangulo, circulo, trapezio, quadrado, retangulo))



