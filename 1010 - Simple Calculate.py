# By line, the variables parameters are code of a product, number of units, price by unit
# My version
product_1 = (int(input()), int(input()), float(input()))
product_2 = (int(input()), int(input()), float(input()))

valor_of_product1 = (product_1[1]) * (product_1[2])
valor_of_product2 = (product_2[1]) * (product_2[2])
total_value = valor_of_product1 + valor_of_product2

print('VALOR A PAGAR: R$ %0.2f' % total_value)

# Online_JudUri_Solution
linha1 = input().split(" ")
linha2 = input().split(" ")

cod1, qtde1, valor1 = linha1
cod2, qtde2, valor2 = linha2

total = (int(qtde1) * float(valor1)) + (int(qtde2) * float(valor2))

print("VALOR A PAGAR: R$ %0.2f" % total)