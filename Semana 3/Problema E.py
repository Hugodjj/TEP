def encontrar_senha(tamanho_senha, mensagem_codificada):
    frequencia_substrings = {}
    
    for i in range(len(mensagem_codificada) - tamanho_senha + 1):
        substring = mensagem_codificada[i:i+tamanho_senha]
        if substring in frequencia_substrings:
            frequencia_substrings[substring] += 1
        else:
            frequencia_substrings[substring] = 1
    
    senha = max(frequencia_substrings, key=frequencia_substrings.get)
    
    return senha

def main():
    import sys
    input = sys.stdin.read
    entradas = input().splitlines()

    for entrada in entradas:
        if entrada.strip() == "#":
            break
        
        try:
            tamanho_senha, mensagem_codificada = entrada.split(maxsplit=1)
            tamanho_senha = int(tamanho_senha)
        except ValueError:
            continue
        
        print(encontrar_senha(tamanho_senha, mensagem_codificada))

main()