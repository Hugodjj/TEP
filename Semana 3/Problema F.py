def eh_slump(s):
    # Um Slump deve começar com 'D' ou 'E'
    if not s or s[0] not in ['D', 'E']:
        return False

    i = 1
    # Após o 'D' ou 'E', deve haver um ou mais 'F's
    while i < len(s) and s[i] == 'F':
        i += 1

    # Depois dos 'F's, deve haver um 'G' ou outro Slump
    if i < len(s) and s[i] == 'G':
        return i == len(s) - 1 

    # Se não for 'G', deve ser outro Slump
    return i < len(s) and eh_slump(s[i:])

def eh_slimp(s):
    if not s or s[0] != 'A':
        return False
    
    if len(s) == 2 and s[1] == 'H':
        return True
    
    if len(s) > 2 and s[1] == 'B' and s[-1] == 'C':
        return eh_slimp(s[2:-1])
    
    if len(s) > 2 and s[-1] == 'C':
        return eh_slump(s[1:-1])
    
    return False

def eh_slurpy(s):
    for i in range(2, len(s)):
        if eh_slimp(s[:i]) and eh_slump(s[i:]):
            return True
    return False

def main():
    num_casos = int(input().strip())
    print("SLURPYS OUTPUT")
    
    for _ in range(num_casos):
        entrada = input().strip()
        if eh_slurpy(entrada):
            print("YES")
        else:
            print("NO")
    
    print("END OF OUTPUT")

main()