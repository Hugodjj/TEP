def encontrar_moeda_falsa(casos):
    for caso in casos:
        possiveis = set("ABCDEFGHIJKL")
        leve = set()
        pesada = set()
        
        for pesagem in caso:
            esquerda, direita, resultado = pesagem
            if resultado == "even":
                possiveis -= set(esquerda + direita)
            elif resultado == "up":
                leve.update(direita)
                pesada.update(esquerda)
                possiveis.intersection_update(set(esquerda + direita))
            elif resultado == "down":
                leve.update(esquerda)
                pesada.update(direita)
                possiveis.intersection_update(set(esquerda + direita))
        
        # Identificar a moeda falsa
        for moeda in possiveis:
            if moeda in leve and moeda not in pesada:
                print(f"{moeda} is the counterfeit coin and it is light.")
            elif moeda in pesada and moeda not in leve:
                print(f"{moeda} is the counterfeit coin and it is heavy.")

def main():
    n = int(input().strip())
    casos = []
    for _ in range(n):
        caso = []
        for _ in range(3):
            esquerda, direita, resultado = input().split()
            caso.append((esquerda, direita, resultado))
        casos.append(caso)
    
    encontrar_moeda_falsa(casos)

main()