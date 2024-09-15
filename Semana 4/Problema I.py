def precompute_golomb_sequence(limit):

    f = [0] * (limit + 1)
    f[1] = 1
    length = 1
    
    for i in range(2, limit + 1):
        f[i] = 1 + f[i - f[f[i - 1]]]
        
        length += 1
        

    cumulative_count = [0] * (limit + 1)
    for i in range(1, limit + 1):
        cumulative_count[i] = cumulative_count[i - 1] + f[i]
    
    return f, cumulative_count

def find_f_n(n, cumulative_count):

    lo, hi = 1, len(cumulative_count) - 1
    
    while lo < hi:
        mid = (lo + hi) // 2
        if cumulative_count[mid] < n:
            lo = mid + 1
        else:
            hi = mid
    
    return lo

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    

    limit = 2000000
    f, cumulative_count = precompute_golomb_sequence(limit)
    
    for line in data:
        n = int(line)
        if n == 0:
            break

        result = find_f_n(n, cumulative_count)
        print(result)

if __name__ == "__main__":
    main()
