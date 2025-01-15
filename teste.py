def fib(n):
    # Inicializa as duas primeiras variáveis da sequência de Fibonacci
    a, b = 0, 1

    # Continua o loop enquanto 'a' for menor que 'n'
    while a < n:
        # Imprime o valor atual de 'a', seguido por um espaço
        print(a, end=' ')

        # Atualiza 'a' e 'b' para os próximos valores da sequência de Fibonacci
        a, b = b, a + b


# Chama a função 'fib' com o valor 2000 para imprimir a sequência de Fibonacci até o valor menor que 2000
fib(8000)



