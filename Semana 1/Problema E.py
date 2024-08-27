def totcount(s, t):
    count = 0
    l = len(s)
    
    while s and t:
        if s[-1] == t[-1]:
            t = t[:-1]
        else:
            count += 1
        s = s[:-1]
    
    if not t:
        return count
    return l

def main():
    t = int(input())
    
    for _ in range(t):
        s = input().strip()
        
        if len(s) < 2:
            print(len(s))
        else:
            # Check all possibilities: "00", "25", "50", "75"
            result = min(totcount(s, "00"), totcount(s, "25"), totcount(s, "50"), totcount(s, "75"))
            print(result)

if __name__ == "__main__":
    main()