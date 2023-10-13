# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint

chosen = randint(0,6)

choice = int(input("Qual o seu palpite? "))

if choice == chosen:
    print("Você acertou!")
else:
    print("Você errou")