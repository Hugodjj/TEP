def max_knights(m, n):
    if m == 0 or n == 0:
        return 0
    elif m == 1 or n == 1:
        return max(m, n)
    elif m == 2 or n == 2:
        max_side = max(m, n)
        return (max_side // 4) * 4 + min(2, max_side % 4) * 2
    else:
        return (m * n + 1) // 2

def main():
    while True:
        m, n = map(int, input().split())
        if m == 0 and n == 0:
            break
        result = max_knights(m, n)
        print(f"{result} knights may be placed on a {m} row {n} column board.")

main()