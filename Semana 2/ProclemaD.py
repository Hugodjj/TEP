def verificar_corretude(sequencia):
    pilha = []
    pares = {')': '(', ']': '['}

    for char in sequencia:
        if char in '([':
            pilha.append(char)
        elif char in ')]':
            if not pilha or pilha[-1] != pares[char]:
                return "No"
            pilha.pop()

    return "Yes" if not pilha else "No"

def main():
    n = int(input().strip())
    resultados = []
    for _ in range(n):
        sequencia = input().strip()
        resultado = verificar_corretude(sequencia)
        resultados.append(resultado)
    
    for resultado in resultados:
        print(resultado)


main()