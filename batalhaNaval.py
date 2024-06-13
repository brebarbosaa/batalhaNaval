import random

def criarTabuleiro():
    return [['0' for _ in range(10)] for _ in range(10)]

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))

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

def ataqueJogador():
    while True:
        try:
            ataqueX = int(input("Qual linha quer atacar? digite um número (0-9): "))
            ataqueY = int(input("Qual coluna quer atacar? digite um número (0-9): "))
            if 0 <= ataqueX < 10 and 0 <= ataqueY < 10:
                return ataqueX, ataqueY
            else:
                print("Os valores devem estar entre 0 e 9, por favor tente novamente.")
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

# Função para criar tabuleiro 10x10 com embarcações em posições aleatórias
def tabuleiroEscondido():
    tabuleiro = [[0 for _ in range(10)] for _ in range(10)]
    for _ in range(10):
        linha = random.randint(0, 9)  # gera um número aleatório de 0 a 9 para a coordenada x
        coluna = random.randint(0, 9)  # gera um número aleatório de 0 a 9 para a coordenada y
        if tabuleiro[linha][coluna] == 0:
            tabuleiro[linha][coluna] = 'X'
            break
    # for linha in tabuleiro:
    #         print(linha)


def main():
    embarcacoes = 5
    tabuleiroJogador = criarTabuleiro()
    tabuleiroComputador = criarTabuleiro()

    print("Seja bem vindo ao Batalha Naval!")

    for _ in range(embarcacoes):
        imprimir_tabuleiro(tabuleiroJogador) ## mudar pra tabuleiro escondido
        while True:
            x, y = coordenadasUsuario()
            if embarcacoesPosicionadas(tabuleiroJogador, x, y):
                break

    tabuleiroEscondido()

    ## mudar pra tabuleiro escondido
    ## modo ataque jogador
    print("agora é a vez de atacar o tabuleiro do computador, boa sorte!")

    while True:
        x, y = ataqueJogador()
        if tabuleiroComputador[x][y] == 'X':
            print("parabéns! você acertou uma embarcação do computador!")
            ## mudar a coordenada do tabuleiro do computador para 'A' quando a embarcação for afundada
            tabuleiroComputador[x][y] = 'A'
            break
        else:
            print("você não acertou nenhuma embarcação do computador :( tente novamente!")

## fazer uma variavel para poder printar no final quem ganhou
## ex: se o computador ganhou = computadorGanhou
    print("fim de jogo! ")
if __name__ == "__main__":
    main()
