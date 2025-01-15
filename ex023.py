# num = int(input('Digite um número de 0 a 9999: '))
#
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
#
# print('A unidade é:', u)
# print('A dezena é:', d)
# print('A centena é:', c)
# print('O milhar é:', m)


# jeito de se fazer usando String
num = int(input('Digite um número de 0 a 9999: '))

n = str(num)
print("Analisando o numero {}".format(num))
print("unidade: {}".format(n[3]))
print("dezena: {}".format(n[2]))
print("centena: {}".format(n[1]))
print("milhar: {}".format(n[0]))