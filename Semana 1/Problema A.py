def main(n):
    res = 4 if (n % 4 == 0) else 0
    return res


n = input().strip()
print(main(n))