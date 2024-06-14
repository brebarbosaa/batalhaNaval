import random

## criar o tabuleiro
def criarTabuleiro():
    return [['🌊' for _ in range(10)] for _ in range(10)]

def imprimir_tabuleiro(tabuleiro, titulo):
    print(titulo)
    for linha in tabuleiro:
        print(" ".join(linha))
    print()

## pegar as coordenadas do user para posicionar as embarcações
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

## colocar os emojis
def embarcacoesPosicionadas(tabuleiro, x, y):
    if tabuleiro[x][y] == '🌊':
        tabuleiro[x][y] = '🚢'
        return True
    else:
        print("Essa posição já está ocupada por uma embarcação. Tente novamente.")
        return False

## logica de ataque do jogador
def ataqueJogador():
    while True:
        try:
            ataqueX = int(input("Qual linha quer atacar? Digite um número (0-9): "))
            ataqueY = int(input("Qual coluna quer atacar? Digite um número (0-9): "))
            if 0 <= ataqueX < 10 and 0 <= ataqueY < 10:
                return ataqueX, ataqueY
            else:
                print("Os valores devem estar entre 0 e 9. Por favor, tente novamente.")
        except ValueError:
            print("Por favor, digite números inteiros. Tente novamente.")

## logica de ataque do computador
def ataqueComputador(tabuleiro, ataques_feitos):
    while True:
        ataqueX = random.randint(0, 9)
        ataqueY = random.randint(0, 9)
        if (ataqueX, ataqueY) not in ataques_feitos:
            ataques_feitos.append((ataqueX, ataqueY))
            break

    if tabuleiro[ataqueX][ataqueY] == '🚢':
        print(f"O computador atacou a posição ({ataqueX}, {ataqueY}) e acertou uma embarcação sua!")
        tabuleiro[ataqueX][ataqueY] = '🎯'  # marca como 'A' para indicar que acertou
        return True
    else:
        print(f"O computador atacou a posição ({ataqueX}, {ataqueY}) e não acertou nenhuma embarcação sua.")
        tabuleiro[ataqueX][ataqueY] = '👎'  # marca como 'M' para indicar que errou
        return False
        
## Função para criar o tabuleiro do computador com as embarcações escondidas
def tabuleiroEscondido():
    tabuleiro = [['🌊' for _ in range(10)] for _ in range(10)]
    for _ in range(5):
        linha = random.randint(0, 9)  # gera um número aleatório de 0 a 9 para a coordenada x
        coluna = random.randint(0, 9)  # gera um número aleatório de 0 a 9 para a coordenada y
        if tabuleiro[linha][coluna] == '🌊':
            tabuleiro[linha][coluna] = '🚢'
    return tabuleiro

## Função para mostrar o tabuleiro do computador com os resultados dos ataques
def tabuleiroAmostra(tabuleiro):
    print("Tabuleiro do Computador")
    tabuleiro_visivel = [[c if c in ['🎯', '👎'] else '🌊' for c in linha] for linha in tabuleiro]
    for linha in tabuleiro_visivel:
        print(" ".join(linha))
    print()

## logica principal do jogo
def main():
    embarcacoes = 5 # número de embarcações
    acertos_jogador = 0 # contador de acertos do jogador
    acertos_computador = 0 # contador de acertos do computador


    tabuleiroJogador = criarTabuleiro() # cria o tabuleiro do jogador
    tabuleiroComputador = tabuleiroEscondido() # cria o tabuleiro do computador com embarcações escondidas


    print("​(っ◔◡◔)っ ♥ 𝔹̲𝔼̲𝕄̲  𝕍̲𝕀̲ℕ̲𝔻̲𝕆̲  𝔸̲𝕆̲  𝔹̲𝔸̲𝕋̲𝔸̲𝕃̲ℍ̲𝔸̲ ℕ̲𝔸̲𝕍̲𝔸̲𝕃̲ ♥")
    print("Posicione suas embarcações:")
    
   ## Posiciona as embarcações do jogador
    for _ in range(embarcacoes):
        imprimir_tabuleiro(tabuleiroJogador, "Tabuleiro do Jogador")
        while True:
            x, y = coordenadasUsuario()
            if embarcacoesPosicionadas(tabuleiroJogador, x, y):
                break

    print("Agora é a vez de atacar o tabuleiro do computador. Boa sorte!")

    ataques_feitos = [] # lista para armazenar os ataques feitos

    embarcacoes_restantes_jogador = embarcacoes # contador de embarcações restantes do jogador
    embarcacoes_restantes_computador = embarcacoes # contador de embarcações restantes do jogador

    ## Loop principal do jogo, continua enquanto houver embarcações para serem acertadas por ambos os lados
    while acertos_jogador < embarcacoes and acertos_computador < embarcacoes:
        tabuleiroAmostra(tabuleiroComputador) # mostra o tabuleiro do computador com os resultados dos ataques
        x, y = ataqueJogador() # jogador realiza um ataque
        ## Verifica se acertou uma embarcação do computador
        if tabuleiroComputador[x][y] == '🚢':
            print(f"Parabéns! Você atacou a linha {x} e a coluna {y} e acertou uma embarcação do computador!")
            tabuleiroComputador[x][y] = '🎯' 
            acertos_jogador += 1
            embarcacoes_restantes_computador -= 1 ## Verifica se acertou uma embarcação do computador
        else:
            print(f"Você atacou a linha {x} e a coluna {y} e não acertou nenhuma embarcação do computador. Tente novamente!")
            tabuleiroComputador[x][y] = '👎' 
    

        imprimir_tabuleiro(tabuleiroJogador, "Seu Tabuleiro") # imprime o tabuleiro atualizado do jogador

        ## Verifica se o jogador já destruiu todas as embarcações do computador    
        if acertos_jogador >= embarcacoes:
            break

        # Ataque do computador
        print("Agora é a vez do computador atacar o seu tabuleiro...")
        if ataqueComputador(tabuleiroJogador, ataques_feitos):
            acertos_computador += 1
            embarcacoes_restantes_jogador -= 1 # reduz o número de embarcações restantes do jogador

        imprimir_tabuleiro(tabuleiroJogador, "Seu Tabuleiro") # imprime o tabuleiro atualizado do jogador
        print(f"Embarcações restantes do jogador: {embarcacoes_restantes_jogador}")
        print(f"Embarcações restantes do computador: {embarcacoes_restantes_computador}")
        print()
        print(".・。.・゜✭・.・✫・゜・。.")

    ## Verifica o resultado do jogo (se o jogador ou o computador destruíram todas as embarcações do adversário)
    if acertos_jogador >= embarcacoes:
        print("Parabéns! Você venceu o jogo!")
    else:
        print("O computador venceu o jogo. Melhor sorte da próxima vez!")

    print("Fim de jogo!")
    print("Obrigada por jogar nosso jogo! 💫")
    print("Desenvolvido por: Alana Queiroz ♡ e Brenda Barbosa ♡")
    print(".・。.・゜✭・.・✫・゜・。.")

if __name__ == "__main__":
    main()
