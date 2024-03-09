salário = float(input('Qual o salário do funcionário: '))

valor_desconto = salário +  (salário * 15/100)

print('Um funcionário que ganhava R${:.2f} com 15% de aumento, passa a ganhar R${:.2f}'.format(salário,valor_desconto))
