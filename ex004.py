a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('só tem espaços?',a.isspace())
print('É um numero?',a.isnumeric())
print('É alfabético?',a.isalpha())
print('É alfanumerico?',a.isalnum())
print('Está em maísculas?',a.isupper())
print('Está em minisculas?',a.islower())
print('Está captalizada? {}'.format(a.istitle()))



