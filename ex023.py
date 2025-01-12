num = int(input('Digite um número de 0 a 9999: '))

# unidade
unidade = num % 10

# Eliminando a unidade do número
num = num // 10

# dezena
dezena = num % 10

# Eliminando a dezena do número
num = num // 10

# centena
centena = num % 10

# Eliminando a centena do número
num = num // 10

# milhar
milhar = num % 10

print('A unidade é:', unidade)
print('A dezena é:', dezena)
print('A centena é:', centena)
print('O milhar é:', milhar)
