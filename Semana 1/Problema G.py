def solve():
    s = input().strip()

    if len(s) < 3:
        print(0)
        return

    cnt_zero = s.count('0')
    cnt_one = s.count('1')

    if cnt_zero != cnt_one:
        print(min(cnt_zero, cnt_one))
    else:
        print(cnt_zero - 1)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()