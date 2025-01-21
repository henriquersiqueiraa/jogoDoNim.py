def partida():
    while True:
        try:
            n = int(input("Defina o número de peças: "))
            m = int(input("Limite a quantidade de peças retiradas: "))

            if n <= 0 or m <= 0:
                print("Os valores devem ser maiores que 0.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite números inteiros maiores que 0.")

    # Determina quem começa
    jogador = n % (m + 1) != 0
    print("Computador começa!" if jogador else "Você começa!")

    # Loop das jogadas
    while n > 0:
        if jogador:
            jogada = computador_escolhe_jogada(n, m)
            print(f"Computador retirou {jogada} peça(s).")
        else:
            jogada = usuario_escolhe_jogada(n, m)

        n -= jogada

        if n > 0:
            print(f"Restam {n} peça(s).")
        else:
            print("Computador ganhou!" if jogador else "Você ganhou!")
            break

        # Alterna o jogador
        jogador = not jogador

    return "Computador" if jogador else "Você"

def computador_escolhe_jogada(n, m):
    # Computador escolhe a jogada que deixa múltiplo de (m+1)
    for jogada in range(1, m + 1):
        if (n - jogada) % (m + 1) == 0:
            return jogada
    return min(m, n)

def usuario_escolhe_jogada(n, m):
    # Loop para validar a jogada do usuário
    while True:
        try:
            jogada = int(input("Quantas peças você vai retirar? "))
            if 1 <= jogada <= min(m, n):
                return jogada
            print(f"Valor inválido. Você pode retirar entre 1 e {min(m, n)} peça(s).")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def campeonato():
    placar = {"Você": 0, "Computador": 0}
    for i in range(1, 4):
        print(f"\n**** Partida {i} ****")
        vencedor = partida()
        print(f"{vencedor} venceu a partida {i}!")
        placar[vencedor] += 1

    print("\n**** Final do campeonato! ****")
    print(f"Placar final: Você {placar['Você']} X {placar['Computador']} Computador")

# Menu principal
def main():
    print("Bem-vindo ao jogo NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    while True:
        try:
            escolha = int(input("Sua escolha: "))
            if escolha == 1:
                print("\nVocê escolheu uma partida isolada!")
                partida()
                break
            elif escolha == 2:
                print("\nVocê escolheu um campeonato!")
                campeonato()
                break
            else:
                print("Escolha inválida. Digite 1 ou 2.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

if __name__ == "__main__":
    main()