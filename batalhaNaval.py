import random

def criarTabuleiro():
    return [['0' for _ in range(10)] for _ in range(10)]

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))

def criarTabuleiroEscondido():
    return [['0' for _ in range(10)] for _ in range(10)]

def coordenadasUsuario():
    while True:
        try:
            x = int(input("Digite a linha da embarcação (0-9): "))
            y = int(input("Digite a coluna da embarcação (0-9): "))
            if 0 <= x < 10 and 0 <= y < 10:
                return x, y
            else:
                print("Coordenadas devem estar entre 0 e 9. Tente novamente.")
        except ValueError:
            print("Por favor, digite números inteiros. Tente novamente.")

def embarcacoesPosicionadas(tabuleiro, x, y):
    if tabuleiro[x][y] == '0':
        tabuleiro[x][y] = 'X'
        return True
    else:
        print("Essa posição já está ocupada por uma embarcação. Tente novamente.")
        return False
    
def tabuleiroAmostra():
    print("Tabuleiro do Computador")
    tabuleiro = [[0 for _ in range(10)] for _ in range(10)]
    for linha in tabuleiro:
        print(linha)

tabuleiroAmostra()

print("embarcações restantes:", embarcacoes)

# Função para criar tabuleiro 10x10 com embarcações em posições aleatórias
def tabuleiroEscondido():
    print("tabu")
    tabuleiro = [[0 for _ in range(10)] for _ in range(10)]
    for _ in range(10):
        linha = random.randint(0, 9)  # gera um número aleatório de 0 a 9 para a coordenada x
        coluna = random.randint(0, 9)  # gera um número aleatório de 0 a 9 para a coordenada y
        if tabuleiro[linha][coluna] == 0:
            tabuleiro[linha][coluna] = 1
    for linha in tabuleiro:
            print(linha)

        
def main():
    embarcacoes = 5
    tabuleiro = criarTabuleiro()

    print("Posicione suas embarcações no tabuleiro.")

    for _ in range(embarcacoes):
        imprimir_tabuleiro(tabuleiro)
        while True:
            x, y = coordenadasUsuario()
            if embarcacoesPosicionadas(tabuleiro, x, y):
                break

    print("Todas as embarcações foram posicionadas.")
    imprimir_tabuleiro(tabuleiro)

if __name__ == "__main__":
    main()
