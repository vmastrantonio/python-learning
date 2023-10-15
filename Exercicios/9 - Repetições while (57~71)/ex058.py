# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
pc = randint(1, 10)

tentativas = 0

chosen = -1

while chosen != pc:
    chosen = int(input("Qual o seu palpite? "))
    tentativas +=1
    if chosen != pc:
        print("Você errou, tente novamente!")
        sleep(0.5)
        
    
print(f"Você acertou na {tentativas}ª tentativa!")