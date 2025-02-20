import forca
import advinhacao

def escolhe_jogo():
    print("*********************************")
    print("********Escolha seu jogo!*********")
    print("*********************************")

    print("(1)forca (2)advinhação")

    jogo = int(input('Qual o jogo?'))

    if (jogo == 1):
        print('jogando forca')
        forca.jogar()
    elif(jogo == 2):
        print('jogando dvinhação')
        advinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()


