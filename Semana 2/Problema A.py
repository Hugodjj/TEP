import heapq

n = int(input())

operacoes_corrigidas = []

heap = []

for _ in range(n):
    entrada = input().split()
    operacao = entrada[0]
    
    if operacao == "insert":
        x = int(entrada[1])
        heapq.heappush(heap, x)
        operacoes_corrigidas.append(f"{operacao} {x}")
    
    elif operacao == "getMin":
        x = int(entrada[1])
        while heap and heap[0] < x:
            heapq.heappop(heap)
            operacoes_corrigidas.append("removeMin")
        
        if not heap or heap[0] != x:
            heapq.heappush(heap, x)
            operacoes_corrigidas.append(f"insert {x}")
        
        operacoes_corrigidas.append(f"{operacao} {x}")
    
    elif operacao == "removeMin":
        if not heap:
            heapq.heappush(heap, 0)
            operacoes_corrigidas.append("insert 0")
        heapq.heappop(heap)
        operacoes_corrigidas.append("removeMin")

print(len(operacoes_corrigidas))

for operacao in operacoes_corrigidas:
    print(operacao)