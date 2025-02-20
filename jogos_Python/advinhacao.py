
import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    print('Regras:Você deve advinhar um número de 1 a 10, escolhendo um dos 3 níveis sendo que')
    print('/nível(1)= 5 tentativas*/ /*nível(2)= 3 tentativas*/ /*nível(3) = 1 tentativas*/')

    numero_secreto = random.randrange(1, 11)
    total_de_tentativas = 0

    Nível = 0

    print('escolha um Nível: (1)Fácil (2)médio (3)Difícil')
    aNivel = input("Nível: ")
    bNível = ord(aNivel)

    if bNível == 49:
        Nível = 1
    elif bNível == 50:
        Nível = 2
    elif bNível == 51:
        Nível = 3

    elif(Nível <= 0 or Nível > 3):
        print('Ultima chance: Escolha um Nível Válido!!')
        print('(1)Fácil (2)médio (3)Difícil')

        aNivel = input("Nível: ")

        bNível = ord(aNivel)

        if bNível == 49:
            Nível = 1
        elif bNível == 50:
            Nível = 2
        elif bNível == 51:
            Nível = 3

    if(Nível <= 0 or Nível > 3):
        print('GAME OVER:VOCE NÃO RESPEITOU AS REGRAS !!')
    elif(Nível == 1):
        total_de_tentativas = 5
    elif(Nível == 2):
        total_de_tentativas = 3
    elif (Nível == 3):
        total_de_tentativas = 1
    elif (Nível <= 0 or Nível > 3):
        print('Gamer Over !!')
    for rodada in range(1, total_de_tentativas + 1):
        print('tentativa: {} de {} '.format(rodada, total_de_tentativas))
        chute = int(input("digite seu numero entre 1 e 10: "))
        print('você digitou', chute)

        acertou = chute == numero_secreto
        menor = chute > numero_secreto
        maior = chute < numero_secreto

        if(acertou):
            print('Parabéns você acertou!!!')
        elif(rodada == total_de_tentativas):
            print('Gamer Over: Acabaram as tentativas')
        elif(chute < 1 or chute > 10):
            print("o numero deve ser entre 1 e 10!! ")
            continue
        elif(acertou):
            print('Parabéns você acertou!!!')
            break
        elif (menor):
            print('você errou !')
            print('Dica: tente chutar para baixo')
        elif (maior):
            print('você errou !')
            print('Dica: tente chutar para cima')

if (__name__ == "__main__"):
    jogar()


