# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde todos esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint

jogos = {}

for n in range(4):
    dado = randint(1,6)
    jogos[f'jogador{[n]}'] = dado

for k,v in jogos.items():
    print(f"{k} tirou {v} no dado.")

resultado = sorted(jogos.items(), key=lambda item: item[1], reverse=True)

count = 1

for item in resultado:
    print(f"{count}º lugar {item[0]} = {item[1]}")
    count += 1