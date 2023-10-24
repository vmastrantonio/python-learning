# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# OBS: use cores.

c = ('\033[m',         # 0 - fecha cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30m',     # 6 - branco
     )

def linhas(txt, cor=2):
    print(c[cor], end='')
    print(f'{"~" * (len(txt) + 2)}\n{txt:^{len(txt) + 2}}\n{"~" * (len(txt) + 2)}')
    print(c[0], end='')

def ajuda(a):
    print(c[6], end='')
    help(a)
    print(c[0], end='')

while True:
    linhas('SISTEMA DE AJUDA PyHELP')
    x = input('Função ou Bibioteca > ').lower().strip() #
    if x == 'fim':
        linhas('ATÉ LOGO!', 1)
        break
    else:
        linhas(f'Acessando o manual do comando {x}', 4)
        ajuda(x)