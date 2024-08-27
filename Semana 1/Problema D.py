def main():
    t = int(input())
    
    for _ in range(t):
        a, b, c = map(int, input().split())
        
        # For candidate a
        A = max(0, max(b, c) - a + 1)
        # For candidate b
        B = max(0, max(a, c) - b + 1)
        # For candidate c
        C = max(0, max(a, b) - c + 1)
        
        print(A, B, C)

if __name__ == "__main__":
    main()