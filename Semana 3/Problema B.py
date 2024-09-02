from collections import deque
import sys
input = sys.stdin.read

def inicializar():
    for i in range(n_num):
        flag_equipe[i] = False
        filas_equipes[i].clear()
    fila_principal.clear()

def entrada():
    global m
    m = {}
    for i in range(n_num):
        tamanho_equipe = int(dados[indice])
        indice += 1
        for _ in range(tamanho_equipe):
            elemento = int(dados[indice])
            indice += 1
            m[elemento] = i

def resolver():
    global indice
    print(f"Cenário #{numero_cenario}")
    while indice < len(dados) and dados[indice] != "STOP":
        comando = dados[indice]
        indice += 1
        if comando == "ENQUEUE":
            elemento = int(dados[indice])
            indice += 1
            equipe = m[elemento]
            if not flag_equipe[equipe]:
                fila_principal.append(equipe)
                flag_equipe[equipe] = True
            filas_equipes[equipe].append(elemento)
        elif comando == "DEQUEUE":
            equipe = fila_principal[0]
            print(filas_equipes[equipe].popleft())
            if not filas_equipes[equipe]:
                fila_principal.popleft()
                flag_equipe[equipe] = False
    print()

if __name__ == "__main__":
    dados = input().strip().split()
    indice = 0
    numero_cenario = 1
    
    while True:
        n_num = int(dados[indice])
        indice += 1
        if n_num == 0:
            break
        
        # Inicializar estruturas de dados
        filas_equipes = [deque() for _ in range(1001)]
        fila_principal = deque()
        flag_equipe = [False] * 1001
        
        entrada()
        resolver()
        
        numero_cenario += 1
