valor_reais = float(input('Quanto dinheiro você na carteira: R$ '))
valor_dolar = valor_reais / 3.27
valor_euro = valor_reais / 5.43
print("Com R${:.2f} você consegue comprar U$${:.2f}".format(valor_reais, valor_dolar))
print("Com R${:.2f} você consegue comprar €{:.2f}".format(valor_reais, valor_euro))

