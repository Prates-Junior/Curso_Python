metros = float(input('Digite os metros aqui: '))

cm = metros*100
mm = metros*1000
dm = metros*10
hm = metros/100
km = metros/1000
print('a quantidade  de metros em centimetros equivale a: {:.2f} , '
'\ne quantidade de metros em milimetros equivale a: {:.2f}'.format(cm , mm))

print('hectometro', hm)
print('decimetro {:.0f}cm'.format(dm))
print('kilometro {}km'.format(km))

