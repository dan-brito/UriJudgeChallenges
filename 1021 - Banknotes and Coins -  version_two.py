valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    quantidade_de_notas = int(valor/nota)
    print("{} nota(s) de R$ {:.2f}".format(quantidade_de_notas,nota ))
    valor -= quantidade_de_notas * nota
print("MOEDAS:")
for moeda in moedas:
    quantidade_de_moedas = int(round(valor, 2)/moeda)
    print("{} moeda(s) de R$ {:.2f}".format(quantidade_de_moedas, moeda))
    valor -= quantidade_de_moedas * moeda
