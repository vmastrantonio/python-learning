# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# OBS: use cores.

def mini_sistema():
    while True:
        print("\033[97;42m'", end="")
        print(f"SISTEMA DE AJUDA PyHELP")
        print("\033[m'", end="")
        comando = input("Função ou biblioteca > ")
        if comando.upper() == 'FIM':
            print("\033[41;97m", end="")
            print("Até logo!")
            print("\033[m'", end="")
            break
        else:
            print("\033[30;107m", end="")
            print(f"Acessando o manual do comando '{comando}'")
            print("\033[m'", end="")
            help(comando)

mini_sistema()