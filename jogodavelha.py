import os
import random

jogarNovamente = "s"
jogadas = 0
quemjoga = 2
maxjogadas = 9
vit = "n"
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def tela():
    global tela
    global jogadas
    os.system("cls")
    print("    0    1    2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas: ", jogadas)

def jogadorjoga():
    global jogadas
    global quemjoga
    global vit
    global maxjogadas
    if quemjoga == 2 and jogadas<maxjogadas:
        try:
            l = int(input("Linha..: "))
            c = int(input("Coluna.: "))
            while velha[l][c] != " ":
                l = int(input("Linha..: "))
                c = int(input("Coluna.: "))
            velha[l][c]="X"
            quemjoga=1
            jogadas+= 1
        except:
            print("Linha e/ou coluna inválida")

def cpujoga():
    global jogadas
    global quemjoga
    global vit
    global maxjogadas
    if quemjoga == 1 and jogadas<maxjogadas:
        l=random.randrange(0,3)
        c=random.randrange(0,3)
        while velha[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        velha[l][c]="O"
        jogadas += 1
        quemjoga = 2

def verificarvitoria():
    global velha
    vitoria="n"
    simbolos=["X","O"]
    for s in simbolos:
        vitoria="n"
        #verificar linhas
        il=ic=0
        while il<3:
            soma=0
            ic=0
            while ic<3:
                if(velha[il][ic]==s):
                    soma+=1
                ic+=1
            il+=1
            if(soma==3):
                vitoria = s
                break
        if(vitoria!="n"):
            break
        #verificar diagonal
        soma = 0
        idiag = 0
        while idiag<3:
            if (velha[idiag][idiag] == s):
                soma += 1
            idiag +=1
        if (soma == 3):
            vitoria = s
            break
        #verificar diagonal 2
        soma = 0
        idiagl = 0
        idiagc = 0
        while idiagc>=0:
            if (velha[idiagl][idiagc] == s):
                soma += 1
            idiagl +=1
            idiagc -=1
        if (soma == 3):
            vitoria = s
            break
    return vitoria

def redefinir():
    global velha
    global jogadas
    global quemjoga
    global maxjogadas
    global vit
    jogadas = 0
    quemjoga = 2
    maxjogadas = 9
    vit = "n"
    velha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    
    
while (jogarNovamente =="s"):   
    while True:
        tela()
        jogadorjoga()
        cpujoga()
        tela()
        vit=verificarvitoria()
        if(vit!="n")or(jogadas>=maxjogadas):
            break
    print("FIM DE JOGO")
    if(vit == "X" or vit == "O"):
        print("Resultado: Jogador ", vit, "venceu")
    else:
        print("Resultado: Empate")
    jogarNovamente = input("Jogar novamente? [s/n]: ")
    redefinir()