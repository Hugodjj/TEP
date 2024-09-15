import math

# Função para verificar se um número é primo
def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Função para encontrar o maior divisor primo
def largest_prime_divisor(n):
    if n <= 1:
        return -1

    original_n = n
    largest_prime = -1
    count_of_prime_divisors = 0

    # Verifica divisibilidade por 2
    while n % 2 == 0:
        largest_prime = 2
        n //= 2
        count_of_prime_divisors += 1

    # Verifica divisibilidade por outros números primos ímpares
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            largest_prime = i
            n //= i
            count_of_prime_divisors += 1

    # Se sobrou algum número primo maior que sqrt(n)
    if n > 2:
        largest_prime = n
        count_of_prime_divisors += 1

    # Se o número tem mais de um divisor primo
    if count_of_prime_divisors > 1:
        return largest_prime
    else:
        return -1

# Função principal para processar a entrada e a saída
def process_input():
    while True:
        n = int(input())
        if n == 0:
            break
        result = largest_prime_divisor(n)
        print(result)

# Chamando a função principal
process_input()
