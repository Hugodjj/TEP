def encontrar_ananagrams(palavras):
    formas_normalizadas = {}
    
    for palavra in palavras:
        forma = ''.join(sorted(palavra.lower()))
        
        if forma in formas_normalizadas:
            formas_normalizadas[forma].append(palavra)
        else:
            formas_normalizadas[forma] = [palavra]
    
    ananagrams = []
    
    for lista_palavras in formas_normalizadas.values():
        if len(lista_palavras) == 1:
            ananagrams.append(lista_palavras[0])
    
    ananagrams.sort()
    
    return ananagrams

palavras = []
while True:
    linha = input().strip()
    if linha == "#":
        break
    palavras.extend(linha.split())

ananagrams = encontrar_ananagrams(palavras)
for palavra in ananagrams:
    print(palavra)