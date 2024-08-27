def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    if n == 1:
        if arr[0] <= 1:
            print("YES")
        else:
            print("NO")
        return

    arr.sort(reverse=True)

    if arr[0] - arr[1] > 1:
        print("NO")
    else:
        print("YES")

def main():
    tc = int(input())
    for _ in range(tc):
        solve()

main()