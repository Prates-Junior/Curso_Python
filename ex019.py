#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.


from random import choice

num1 = str(input('Primeiro aluno: '))
num2 = str(input('Segundo aluno: '))
num3 = str(input('Terceiro aluno: '))
num4 = str(input('Quarto aluno: '))
lista = [num1,num2 , num3, num4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))