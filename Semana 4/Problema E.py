import sys

input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

for _ in range(t):
    n = int(data[index])
    index += 1
    a = []

    for p in range(n):
        x = int(data[index])
        a.append((x, p + 1))
        index += 1
    
    a.sort()

    cnt = 0
    for p in range(n):
        for q in range(p + 1, n):
            if a[p][0] * a[q][0] > 2 * n:
                break
            cnt += (a[p][0] * a[q][0] == a[p][1] + a[q][1])

    print(cnt)
