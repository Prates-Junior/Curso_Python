frase = "Curso em Video Python"
dividido = frase.split()
print(dividido[2][3])

print(frase[3:13])


# # Comando find procura um caractere dentro de uma string
# print(frase.find('P'))
#
#
# # upper Função que transforma a palavra em maiuscula
# print(frase.upper())


# Deixa a primeira letra em maiuscula
print(frase.capitalize())

# Deixa as inicias de todas as palavras em maiusculas
print(frase.title())

# Split, é usado para separar cadeias de caracteres
print(frase.split())

# uso da função Join, usada para unir caracteres novamente
junção = "-".join(frase)
print(junção)