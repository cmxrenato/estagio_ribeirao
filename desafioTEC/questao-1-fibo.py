def eh_fibonacci(a):
    fibo = [0, 1]

    # Gerando a sequência Fibonacci até ter pelo menos 300 números
    while len(fibo) < 300:
        prox_num = fibo[-1] + fibo[-2]
        fibo.append(prox_num)

    # Verificando se o número de entrada 'a' está na lista 'fibo'
    if a in fibo:
        return "O número pertence à sequência Fibonacci."
    else:
        return "O número não pertence à sequência Fibonacci."

# Entrada do usuário
entrada = int(input("Digite um número para verificar se pertence à sequência Fibonacci: "))

print(eh_fibonacci(entrada))


