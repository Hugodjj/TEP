mapa_palavras = {
    'A': 'A', 'E': '3', 'H': 'H', 'I': 'I', 'J': 'L', 'L': 'J', 'M': 'M', 'O': 'O',
    'S': '2', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': '5',
    '1': '1', '2': 'S', '3': 'E', '5': 'Z', '8': '8'
}

def palindromo(s):
    return s == s[::-1]

def espelhado(s):
    palavra_espelhada = ''.join(mapa_palavras.get(c, '') for c in reversed(s))
    return palavra_espelhada == s

def checa_string(s):
    palavra_palindromo = palindromo(s)
    palavra_espelhada = espelhado(s)
    
    if palavra_palindromo and palavra_espelhada:
        return f"{s} -- is a mirrored palindrome."
    elif palavra_palindromo:
        return f"{s} -- is a regular palindrome."
    elif palavra_espelhada:
        return f"{s} -- is a mirrored string."
    else:
        return f"{s} -- is not a palindrome."

try:
    while True:
        s = input().strip()
        if s:
            print(checa_string(s))
            print("")
except EOFError:
    pass