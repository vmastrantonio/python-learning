# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint

cont = 0

while True:
    print("(1) IMPAR | (2) PAR")
    escolha = int(input("Escolha: "))
    
    if escolha == 1:
        pc_escolha = 2
    elif escolha == 2:
        pc_escolha = 1
    
    num = int(input("Escollha um número de 1 a 10: "))
    pc_numero = randint(1, 10)
    
    print(f"O computador jogou {pc_numero}!")
    
    resultado = num + pc_numero
    
    if resultado % 2 == 0:
        if escolha == 2:
            cont += 1
            ganhou = True
        else:
            ganhou = False
    else:
        if escolha == 1:
            cont += 1
            ganhou = True
        else:
            ganhou = False
    
    if ganhou:
        print(f"Você acertou! Agora você está com {cont} vitória(s) consecutiva(s)!")
    else:
        print(f"Que pena, você perdeu com {cont} vitória(s) consecutiva(s).")
        break
        
        
        
    