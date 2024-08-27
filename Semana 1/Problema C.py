def solve():
    s = input().strip()

    n = len(s)

    dp = [0] * (n + 1)
    lastOccIdx = [-1] * 26  # Track last occurrence of each character

    lastOccIdx[ord(s[0]) - ord('a')] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1]

        current_char_idx = ord(s[i - 1]) - ord('a')
        if lastOccIdx[current_char_idx] != -1:
            dp[i] = max(dp[i], dp[lastOccIdx[current_char_idx] - 1] + 2)

        lastOccIdx[current_char_idx] = i

    print(n - dp[n])

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
