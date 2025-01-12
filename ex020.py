#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.


from random import shuffle
num1 = str(input('Primeiro aluno: '))
num2 = str(input('segundo aluno: '))
num3 = str(input('terceiro aluno: '))
num4 = str(input('quarto aluno: '))
lista = [num1 , num2 , num3, num4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)