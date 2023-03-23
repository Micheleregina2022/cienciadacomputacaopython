#######################################Explicação do jogo NIM:###################################################
#Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada. 
# Para garantir que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o
# início do jogo:
#
#Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida 
# com a frase "Você começa!"

#Caso contrário, o computador toma a inciativa de começar o jogo, declarando "Computador começa!"

#Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número 
# de peças que seja múltiplo de (m+1) ao jogador. Caso isso não seja possível, deverá tirar o número 
# máximo de peças possíveis.

################################################################################################################

#Uma função computador_escolhe_jogada que recebe, como parâmetros, os números n e m descritos acima e devolve um 
# inteiro correspondente à próxima jogada do computador (ou seja, quantas peças o computador deve retirar do 
# tabuleiro) de acordo com a estratégia vencedora.

def computador_escolhe_jogada(n, m):
    computadorRemove = 1

    while computadorRemove != m:
        if (n - computadorRemove) % (m+1) == 0:
            return computadorRemove

        else:
            computadorRemove += 1

    return computadorRemove

#Uma função usuario_escolhe_jogada que recebe os mesmos parâmetros, solicita que o jogador informe sua jogada e 
# verifica se o valor informado é válido. Se o valor informado for válido, a função deve devolvê-lo; caso 
# contrário, deve solicitar novamente ao usuário que informe uma jogada válida.

def usuario_escolhe_jogada(n, m):
    jogadaValida = False

    while not jogadaValida:
        jogadorRemove = int(input('Quantas peças você vai tirar? '))
        if jogadorRemove > m or jogadorRemove < 1:
            print()
            print('Oops! Jogada inválida! Tente de novo.')
            print()

        else:
            jogadaValida = True

    return jogadorRemove

#Uma função partida que não recebe nenhum parâmetro, solicita ao usuário que informe os valores de n e m e inicia o 
# jogo, alternando entre jogadas do computador e do usuário (ou seja, chamadas às duas funções anteriores). 
# A escolha da jogada inicial deve ser feita em função da estratégia vencedora, como dito anteriormente. A cada 
# jogada, deve ser impresso na tela o estado atual do jogo, ou seja, quantas peças foram removidas na última 
# jogada e quantas restam na mesa. Quando a última peça é removida, essa função imprime na tela a mensagem 
# "O computador ganhou!" ou "Você ganhou!" conforme o caso.

def campeonato():
    numeroRodada = 1
    while numeroRodada <= 3:
        print()
        print('**** Rodada', numeroRodada, '****')
        print()
        partida()
        numeroRodada += 1
    print()
    print('Placar: Você 0 X 3 Computador')

#Como todos sabemos, uma única rodada de um jogo não é suficiente para definir quem é o
# melhor jogador. Assim, uma vez que a função partida esteja funcionando, você deverá
# criar uma outra função chamada campeonato. Essa nova função deve realizar três partidas
# seguidas do jogo e, ao final, mostrar o placar dessas três partidas e indicar o vencedor
# do campeonato. O placar deve ser impresso na forma:
#Placar: Você ??? X ??? Computador#

def partida():
    n = int(input('Quantas peças? '))

    m = int(input('Limite de peças por jogada? '))

    vezDoPC = False

    if n % (m+1) == 0:
        print()
        print('Voce começa!')

    else:
        print()
        print('Computador começa!')
        vezDoPC = True

    while n > 0:
        if vezDoPC:
            computadorRemove = computador_escolhe_jogada(n, m)
            n = n - computadorRemove
            if computadorRemove == 1:
                print()
                print('O computador tirou uma peça')
            else:
                print()
                print('O computador tirou', computadorRemove, 'peças')

            vezDoPC = False
        else:
            jogadorRemove = usuario_escolhe_jogada(n, m)
            n = n - jogadorRemove
            if jogadorRemove == 1:
                print()
                print('Você tirou uma peça')
            else:
                print()
                print('Você tirou', jogadorRemove, 'peças')
            vezDoPC = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')
                print()

    print('Fim do jogo! O computador ganhou!')

print('Bem-vindo ao jogo do NIM! Escolha:')
print()

print('1 - para jogar uma partida isolada')

tipoDePartida = int(input('2 - para jogar um campeonato '))

if tipoDePartida == 2:
    print()
    print('Voce escolheu um campeonato!')
    print()
    campeonato()
else:
    if tipoDePartida == 1:
        print()
        partida()





