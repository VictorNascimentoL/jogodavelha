op = 0
while op != 2:
    print("""    [ 1 ] Jogar Jogo da velha
    [ 2 ] Sair
    [ 3 ] Créditos""")
    print("=-=" * 10)
    op = int(input(">>>>Qual opção vc deseja?: "))
    if op == 1:
        import os  # comando usado para a limpeza da tela

        import random  # comando usado para que o computador faça jogadas aleatórias

        # variavéis
        vitoria_jogador = 0
        vitoria_cpu = 0
        continuarJogando = "s"
        numDeJogadas = 0
        jogador = 1
        vit = "n"
        maxJogadas = 9
        hashtag = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]


        # regenciamento de tela - função
        def tela():  # o comando cls é só para windows
            os.system("cls")  # limpando a tela com o comando "os"
            print("    0    1    2")  # colunas
            print("0:  " + hashtag[0][0] + " | " + hashtag[0][1] + " | " + hashtag[0][2])  # linha vertical
            print("   -----------")  # linha horizontal
            print("1:  " + hashtag[1][0] + " | " + hashtag[1][1] + " | " + hashtag[1][2])
            print("   -----------")
            print("2:  " + hashtag[2][0] + " | " + hashtag[2][1] + " | " + hashtag[2][2])
            print("Jogadas: ", numDeJogadas)  # variável convertida para uma string


        # regenciamento de jogadas do player - função
        def vezDoJogador():
            print("Sua vez de jogar:")
            global jogador
            global numDeJogadas
            global maxJogadas
            if jogador == 1 and numDeJogadas < maxJogadas:  # verificar quem vai jogar

                try:  # tratamento de erro
                    l = int(input("Linha: "))
                    c = int(input("Coluna: "))
                    while hashtag[l][c] != " ":  # verificando se ali existe uma posição vazia
                        l = int(input("Linha: "))
                        c = int(input("Coluna: "))
                    hashtag[l][c] = "X"  # se a posição estiver vazia
                    numDeJogadas += 1
                    jogador = 2  # passando a vez do jogador
                except:  # caso encontre um erro
                    print("Linha e ou coluna inválida tente novamente!")


        # regenciamento de jogadas da máquina - função
        def vezDaCPU():
            print("Vez do computador:")
            global jogador
            global numDeJogadas
            global maxJogadas
            if jogador == 2 and numDeJogadas < maxJogadas:  # verificando quem vai jogar
                l = random.randrange(0, 3)  # seleção de uma linha aleatória
                c = random.randrange(0, 3)  # seleção de uma coluna aleatória
                while hashtag[l][c] != " ":  # verificando se ali existe uma posição vazia
                    l = random.randrange(0, 3)
                    c = random.randrange(0, 3)
                hashtag[l][c] = "O"  # se a posição estiver vazia
                numDeJogadas += 1
                jogador = 1  # passando a vez do jogador


        # gerenciamento de vitórias - função
        def verificaResultado():
            global vitoria_jogador
            global vitoria_cpu
            global hashtag
            simbolos = ["X", "O"]  # símbolos que precisam ser verificados
            resultado = "n"  # considerando que ainda não houve vitória ou empate
            continuarJogando = "s"

            # Verifica empate
            if numDeJogadas >= maxJogadas:
                resultado = "E"

            # verificação de linhas
            for i in simbolos:  # interação com o "X" e "O"
                il = ic = 0
                while il < 3:  # loop linha
                    soma = 0
                    ic = 0
                    while ic < 3:  # loop coluna
                        if hashtag[il][ic] == i:  # se hashtag índice de linha e índice de coluna for igual a "s"
                            soma += 1
                        ic += 1
                    if soma == 3:  # verificando a soma/vitória das linhas
                        resultado = i
                        break
                    il += 1

                if resultado != "n":
                    break

                # verificação de colunas
                il = ic = 0
                while ic < 3:  # loop coluna
                    soma = 0
                    il = 0
                    while il < 3:  # loop linha
                        if (hashtag[il][ic] == i):  # se hashtag índice de linha e índice de coluna for igual a "s"
                            soma += 1
                        il += 1
                    if soma == 3:  # verificando a soma/vitória das colunas
                        resultado = i
                        break
                    ic += 1

                if resultado != "n":
                    break

                # verificação da diagonal 1
                soma = 0
                idiag = 0

                while idiag >= 0 and idiag < 3:  # basta ter apenas um índice já que são os mesmos valores
                    if hashtag[idiag][idiag] == i:  # verificando as diagonais
                        soma += 1
                    idiag += 1
                if soma == 3:  # verificando a soma das diagonais 1
                    resultado = i
                    break

                # verificação da diagonal 2
                soma = 0  # duas variáveis por ser processo inverso e ter valores diferentes
                idiagl = 0  # índice de linha começa em zero e o de coluna em dois
                idiagc = 2

                while (idiagc >= 0 and idiagl >= 0) and (idiagc < 3 and idiagl < 3):
                    if hashtag[idiagl][idiagc] == i:
                        soma += 1
                    idiagl += 1
                    idiagc -= 1
                if soma == 3:  # verificando a soma das diagonais 2
                    resultado = i  # se tiver vitória ele para
                    break

            if resultado != "n":
                print("Partida encerrada")
                if resultado == "X" or resultado == "O":
                    print("Resultado: Jogador " + resultado + " venceu")
                    if resultado == "X":
                        vitoria_jogador += 1
                    if resultado == "O":
                        vitoria_cpu += 1
                #o código a seguir é usado para computar os pontos em um arquivo txt para fazer o ranking
                    arquivo = open("arquivo do ranking.txt", "w")
                    arquivo.write("Vitorias do jogador: ")
                    arquivo.write(str(vitoria_jogador))
                    arquivo.write("Vitortias do computador: ")
                    arquivo.write(str(vitoria_cpu))
                    arquivo.close()

                else:
                    print("Resultado empatado")
                    redefinir()
                continuarJogando = input("Deseja começar uma nova partida? [s/n]:")
                if continuarJogando == "n":
                    print("""                    [ 4 ] Deseja sair do jogo?: 
                    [ 5 ] deseja ver o ranking? :
                    """)
                    opf = 0
                    opf = int(input("Oque vc deseja ?: "))
                    if opf == 4:
                        print("voce saiu do jogo")
                        exit()
                    if opf == 5 :
                    #código usado para mostrar na tela o ranking
                        arquivo = open("arquivo do ranking.txt", "r")
                        print(arquivo.read())
                        arquivo.close()
                        exit()


                else:
                    redefinir()

                return continuarJogando


        # redefinir todas as variáveis - função
        def redefinir():
            global hashtag  # global serve para uma variável que está fora da função funcionar
            global numDeJogadas
            global maxJogadas
            global vit
            global continuarJogando
            global jogador

            continuarJogando = "s"
            numDeJogadas = 0
            jogador = 1
            vit = "n"
            maxJogadas = 9
            hashtag = [
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]
            ]


        while (continuarJogando != "n"):  # loop para jogar novamente

            tela()
            vezDoJogador()
            tela()
            continuarJogando = verificaResultado()
            vezDaCPU()
            tela()
            continuarJogando = verificaResultado()
        exit()

    if op == 3:
        print("Jogo criado por Laura Lavínia e Victor Eduardo!")