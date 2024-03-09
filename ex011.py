largura = float(input('Digite a largura em metros: '))
altura = float(input('Digite a altura em metros: '))

area = largura * altura
tinta_necessaria = area / 2
print('Sua parede tem a dimensão de {} X {}, e sua area é de {}m\u00B2.'.format(largura, altura, (largura * altura)))
print('Para pintar uma parede de {} largura, e {} altura, são necessãrios {}l litros de tinta.'.format(largura, altura, tinta_necessaria))