import os#comando usado para a limpeza da tela


import random #comando usado para que o computador faça jogadas aleatórias

jogarnovamente = "s"
numdejogadas = 0
jogador = 1
vit = "n"
maxjogadas = 9
hashtag = [
    [" ", " ",  ""],
    [" ", " ", " "],
    [" ", " ", " "]
]

def tela():
    os.system("cls") #comando usado para limpar a tela
    print("    0    1    2")
    print("0:  " + hashtag[0][0] + " | " + hashtag[0][1] + " | " + hashtag[0][2])
    print("   -----------")
    print("1:  " + hashtag[1][0] + " | " + hashtag[1][1] + " | " + hashtag[0][2])
    print("   -----------")
    print("2:  " + hashtag[2][0] + " | " + hashtag[2][1] + " | " + hashtag[2][2])

def vezdojogador():
    global jogador
    global numdejogadas
    global maxjogadas
    if jogador == 1 and numdejogadas < maxjogadas:

        try: #tratamento de erro
            l = int(input("Linha: "))
            c = int(input("Coluna: "))
            while hashtag[l][c] != " ":
                l = int(input("Linha: "))
                c = int(input("Coluna: "))
            hashtag[l][c] = "X"
            numdejogadas += 1
            jogador = 2
        except:
            print("Linha e ou coluna invalida tente novamente!")

def vezdacpu():
    global jogador
    global numdejogadas
    global maxjogadas
    if jogador == 2 and numdejogadas < maxjogadas:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)
        while hashtag[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        hashtag[l][c] = "O"
        numdejogadas += 1
        jogador = 1
while True:
    tela()
    vezdojogador()
    vezdacpu()
