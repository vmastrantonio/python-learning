# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

from random import randint

matriz = []

num_jogos = int(input("Quantos jogos você quer que eu sorteie? "))

for j in range(num_jogos):
    sorteador_temporario = []
    for n in range(6):
        while True:
            num_gerado = randint(1, 60)
            if num_gerado not in sorteador_temporario:
                sorteador_temporario.append(num_gerado)
                break
    matriz.append(sorteador_temporario)

for jogo in matriz:
    jogo.sort()
    print(f"Jogo: {jogo}")