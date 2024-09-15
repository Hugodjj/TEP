import math

# Função para fatorar um número
def prime_factors(n):
    factors = {}
    # Conta o número de vezes que 2 divide n
    while n % 2 == 0:
        if 2 not in factors:
            factors[2] = 0
        factors[2] += 1
        n //= 2
    # Conta o número de vezes que números ímpares dividem n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            if i not in factors:
                factors[i] = 0
            factors[i] += 1
            n //= i
    # Se sobrar algum número primo maior que sqrt(n)
    if n > 2:
        factors[n] = 1
    return factors

# Função para verificar se m divide n!
def divides_factorial(n, m):
    if m == 0:
        return False  # Nenhum número divide 0

    # Fatora o número m
    m_factors = prime_factors(m)

    # Conta os fatores primos de m no fatorial de n
    for prime, exponent in m_factors.items():
        count = 0
        power = prime
        # Conta quantas vezes prime aparece nos fatores de n!
        while power <= n:
            count += n // power
            power *= prime
        if count < exponent:
            return False
    return True

# Função principal para processar a entrada e a saída
def process_input():
    while True:
        try:
            n, m = map(int, input().split())
            if divides_factorial(n, m):
                print(f"{m} divides {n}!")
            else:
                print(f"{m} does not divide {n}!")
        except EOFError:
            break

# Chamando a função principal
if __name__ == "__main__":
    process_input()
