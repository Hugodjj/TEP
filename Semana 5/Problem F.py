import sys

# Cria uma lista de números primos até um limite usando o algoritmo de crivo de Eratóstenes
def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    primes = [i for i in range(2, limit + 1) if is_prime[i]]
    return primes, is_prime

# Função para tentar encontrar a decomposição de N em quatro primos
def find_four_primes(n, primes, is_prime):
    # Verifica se o número pode ser decomposto em dois primos de forma trivial
    if n < 8:
        return "Impossible."

    # Tratamento para garantir que a soma de quatro primos seja possível
    # Reduzimos o problema para a soma de dois primos
    if n % 2 == 0:
        p1, p2 = 2, 2
        n -= 4
    else:
        p1, p2 = 2, 3
        n -= 5

    # Agora tentamos encontrar dois primos que somem a n
    for prime in primes:
        if prime > n:
            break
        if is_prime[n - prime]:
            return f"{p1} {p2} {prime} {n - prime}"

    return "Impossible."

# Função principal para processar a entrada e calcular as decomposições
def process_input():
    limit = 10000000
    primes, is_prime = sieve(limit)

    for line in sys.stdin:
        n = int(line.strip())
        if not n:
            break
        result = find_four_primes(n, primes, is_prime)
        print(result)

if __name__ == "__main__":
    process_input()
