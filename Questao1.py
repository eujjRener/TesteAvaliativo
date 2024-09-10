def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return n == a or n == b

numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
if is_fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")
