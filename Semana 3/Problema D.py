from collections import defaultdict, deque

def determinar_ordem_alfabetica(palavras_ordenadas):
    grau_entrada = defaultdict(int)
    grafo = defaultdict(list)

    for palavra in palavras_ordenadas:
        for letra in palavra:
            grau_entrada[letra] = 0

    for i in range(len(palavras_ordenadas) - 1):
        palavra_atual = palavras_ordenadas[i]
        proxima_palavra = palavras_ordenadas[i + 1]
        tamanho_minimo = min(len(palavra_atual), len(proxima_palavra))

        for j in range(tamanho_minimo):
            if palavra_atual[j] != proxima_palavra[j]:
                letra_u = palavra_atual[j]
                letra_v = proxima_palavra[j]

                if letra_v not in grafo[letra_u]:
                    grafo[letra_u].append(letra_v)
                    grau_entrada[letra_v] += 1
                break

    fila = deque([letra for letra in grau_entrada if grau_entrada[letra] == 0])

    ordem_alfabetica = []

    while fila:
        caractere = fila.popleft()
        ordem_alfabetica.append(caractere)

        for vizinho in grafo[caractere]:
            grau_entrada[vizinho] -= 1
            if grau_entrada[vizinho] == 0:
                fila.append(vizinho)

    return ''.join(ordem_alfabetica)

def main():
    palavras_ordenadas = []
    while True:
        entrada = input().strip()
        if entrada == '#':
            break
        palavras_ordenadas.append(entrada)

    ordem = determinar_ordem_alfabetica(palavras_ordenadas)
    print(ordem)

main()