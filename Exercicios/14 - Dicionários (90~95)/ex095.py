# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

campeonato = []
adicionar_jogador = True
count_1 = 1

while adicionar_jogador:
    count_2 = 1

    print("-" * 30)
    nome_jogador = input(f"Insira o nome do {count_1}º jogador: ")
    qtd_partidas = int(input(f"Quantas partidas {nome_jogador} jogou? "))

    dicionario_temporario = {'nome_jogador': nome_jogador, 'qtd_partidas': qtd_partidas, 'historico_gols': [], 'total_gols': 0}

    for i in range(qtd_partidas):
        num_gols = int(input(f"Quantos gols {nome_jogador} fez na {count_2}ª partida? "))
        dicionario_temporario['historico_gols'].append(num_gols)
        dicionario_temporario['total_gols'] += num_gols
        count_2 += 1

    campeonato.append(dicionario_temporario)

    while True:
        print("-" * 30)
        resposta = input("Deseja continuar? [S/N] ").lower()

        if resposta == 's':
            break
        elif resposta == 'n':
            adicionar_jogador = False
            break
        else:
            print("Resposta inválida, tente novamente!")

    count_1 += 1
    

print(f"{"cod":<2} {"nome":<10} {"gols":<10} {"total":<5}")
print("-" * 30)
for k,v in enumerate(campeonato):
    print(f"{k} {v['nome_jogador']} {v['historico_gols']} {v['total_gols']}")

detalhar_jogador = True

while detalhar_jogador:
    escolha = int(input("Deseja mostrar os dados de qual jogador? ou [999 para sair]: "))

    if escolha == 999:
        break
    elif escolha <= len(campeonato) and escolha >= 0:
        print(f"Levantamento do jogador {campeonato[escolha]['nome_jogador']}: ")
        for jogo, gols_partida in enumerate(campeonato[escolha]['historico_gols']):
            print(f"No jogo {jogo + 1}, o jogador marcou {gols_partida} vezes")
    else:
        print("Opção inválida, tente novamente!")