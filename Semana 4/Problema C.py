import sys

input = sys.stdin.read
data = input().split()
index = 0

# Ler o número de casos de teste
t = int(data[index])
index += 1

for tcase in range(1, t + 1):
    # Ler o valor de n
    n = int(data[index])
    index += 1
    
    # Ler a lista de a
    a = []
    yes = False
    cnt = 0
    for i in range(n):
        a_i = int(data[index])
        a.append(a_i)
        if a_i == 1:
            yes = True
            cnt += 1
        index += 1
    
    if not yes or cnt == n:
        print("YES")
    else:
        a.sort()
        diff = False
        for i in range(1, n):
            if a[i] - a[i - 1] == 1:
                diff = True
                break
        if diff:
            print("NO")
        else:
            print("YES")
