import random

def inicializar_tabuleiro():
    return [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]

def exibir_tabuleiro(tabuleiro):
    print("+-------" * 3 + "+")
    for linha in tabuleiro:
        print("|       " * 3 + "|")
        print("|   " + "   |   ".join(linha) + "   |")
        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

def tabuleiro_cheio(tabuleiro):
    return all(cell in ['X', 'O'] for row in tabuleiro for cell in row)

def numero_para_coordenadas(numero):
    numero -= 1
    return numero // 3, numero % 3

def movimento_computador(tabuleiro):
    opcoes = [(i, j) for i in range(3) for j in range(3) if tabuleiro[i][j] not in ['X', 'O']]
    if opcoes:
        i, j = random.choice(opcoes)
        tabuleiro[i][j] = 'X'

def movimento_usuario(tabuleiro):
    while True:
        try:
            escolha = int(input("Digite o número da célula (1-9) para sua jogada: "))
            if escolha < 1 or escolha > 9:
                print("Número inválido. Escolha um número entre 1 e 9.")
                continue
            i, j = numero_para_coordenadas(escolha)
            if tabuleiro[i][j] in ['X', 'O']:
                print("Célula já ocupada. Escolha outra.")
                continue
            tabuleiro[i][j] = 'O'
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def jogar():
    tabuleiro = inicializar_tabuleiro()
    tabuleiro[1][1] = 'X'
    while True:
        exibir_tabuleiro(tabuleiro)
        if verificar_vitoria(tabuleiro, 'X'):
            print("O computador venceu!")
            break
        if tabuleiro_cheio(tabuleiro):
            print("Empate!")
            break
        movimento_usuario(tabuleiro)
        exibir_tabuleiro(tabuleiro)
        if verificar_vitoria(tabuleiro, 'O'):
            print("Você venceu!")
            break
        if tabuleiro_cheio(tabuleiro):
            print("Empate!")
            break
        movimento_computador(tabuleiro)

jogar()