# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato

nome_jogador = input("Digite o nome do jogador: ")

count = 1
campeonato = {'nome': nome_jogador, 'gols': [], 'total': 0}

for i in range(int(input("Digite o número de partidas do jogador: "))):
    numgols = int(input(f"Quantos gols o jogador {nome_jogador} fez na {count}ª partida? "))
    campeonato['gols'].append(numgols)
    campeonato['total'] += numgols
    count += 1

for k,v in campeonato.items():
    print(f"O campo {k} tem o valor {v}")

print(f"O jogador {nome_jogador} jogou {len(campeonato['gols'])} partidas")

count = 1

for gol in campeonato['gols']:
    print(f"Na {count}ª partida o jogador {nome_jogador} marcou {gol} vezes")
    count += 1

print(f"Total de {campeonato['total']} gols marcados.")