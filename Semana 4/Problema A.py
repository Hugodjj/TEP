def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    # Lê o número de casos de teste
    t = int(data[0])
    index = 1

    for _ in range(t):
        s = data[index]
        index += 1
        n = len(s)
        
        zero = 0
        even = 0
        total_sum = 0
        
        for char in s:
            temp = int(char)
            total_sum += temp
            if temp == 0:
                zero += 1
            if temp % 2 == 0:
                even += 1

        if (total_sum % 3 == 0 and zero > 0) and even >= 2:
            print("red")
        else:
            print("cyan")

if __name__ == "__main__":
    main()