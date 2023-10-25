def cabecalho(msg, cor_escolhida):
    print(f"{cor(cor_escolhida)}{'-' * 30}{cor(0)}")
    print(f"{cor(cor_escolhida)}{msg:^30}{cor(0)}")
    print(f"{cor(cor_escolhida)}{'-' * 30}{cor(0)}")

def cor(cor):
    c = (
    '\033[m',    # 0 - fecha cores
    '\033[31m',  # 1 - vermelho
    '\033[32m',  # 2 - verde
    '\033[33m',  # 3 - amarelo
    '\033[34m',  # 4 - azul
    '\033[35m',  # 5 - roxo
    '\033[97m',  # 6 - branco
     )
    return c[int(cor)]