valor = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    quantidadeDeNotas = int(valor/nota)
    print("{} notas(s) de R$ {:.2f}".format(quantidadeDeNotas, nota))
    valor = valor-quantidadeDeNotas*nota

print("MOEDAS:")
for moeda in moedas:
    quantidadeDeMoedas = int(round(valor,2)/moeda)
    print("{} moeda(s) de R$ {:.2f}".format(quantidadeDeMoedas, moeda))
    valor = valor-quantidadeDeMoedas*moeda
