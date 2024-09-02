from collections import deque

grafo = [[] for _ in range(105)]
ordem_processamento = []
grau_entrada = [0] * 105

def ordenacao_topologica():

    fila = deque()

    for i in range(1, num_tarefas + 1):
        if grau_entrada[i] == 0:
            fila.append(i)

    while fila:
        tarefa_atual = fila.popleft()
        ordem_processamento.append(tarefa_atual)

        for vizinho in grafo[tarefa_atual]:
            grau_entrada[vizinho] -= 1

            if grau_entrada[vizinho] == 0:
                fila.append(vizinho)

def main():
    global num_tarefas, num_dependencias
    while True:
        num_tarefas, num_dependencias = map(int, input().split())
        if num_tarefas == 0 and num_dependencias == 0:
            break

        for i in range(1, num_tarefas + 1):
            grau_entrada[i] = 0
            grafo[i].clear()

        # Lê as dependências entre as tarefas
        for _ in range(num_dependencias):
            tarefa_antes, tarefa_depois = map(int, input().split())
            grau_entrada[tarefa_depois] += 1
            grafo[tarefa_antes].append(tarefa_depois)

        ordenacao_topologica()

        print(' '.join(map(str, ordem_processamento)))

        ordem_processamento.clear()

if __name__ == "__main__":
    main()
