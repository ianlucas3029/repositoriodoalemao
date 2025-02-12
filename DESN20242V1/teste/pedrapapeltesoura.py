import random

def jogar():
    # Função que executa o jogo
    print("Escolha uma opção:")
    print("0 - Pedra")
    print("1 - Papel")
    print("2 - Tesoura")

    try:
        jogador = int(input("Digite sua opção (0, 1 ou 2): "))
    except ValueError:
        print("Opção inválida! Por favor, escolha entre os numeros 0, 1 ou 2.")
        return

    if jogador not in [0, 1, 2]:
        print("Opção inválida! Por favor, escolha entre os numeros 0, 1 ou 2.")
        return

    opcoes = ["Pedra", "Papel", "Tesoura"]
    computador = random.randint(0, 2)  # Computador escolhe aleatoriamente entre 0, 1 ou 2

    print(f"Você escolheu: {opcoes[jogador]}")
    print(f"O computador escolheu: {opcoes[computador]}")

    if jogador == computador:
        print("Empate!")
    elif (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

def main():
    # Função principal que controla o fluxo do jogo
    while True:
        jogar()

        resposta = input("Vamos jogar de novo? (Sim/Não): ").strip().lower()
        if resposta == "não" or resposta == "nao":
            print("Obrigado por jogar! Até a próxima!")
            break
        elif resposta != "sim":
            print("Resposta inválida. Encerrando o jogo.")
            break

# Chama a função principal para iniciar o jogo
main()