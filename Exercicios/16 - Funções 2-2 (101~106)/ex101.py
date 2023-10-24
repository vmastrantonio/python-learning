# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições

from datetime import datetime

def voto(idade):
    if idade < 16:
        return 'VOTO NEGADO'
    elif idade < 18 or idade >= 70:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'

ano = int(input("Em que ano você nasceu? "))
idade = datetime.now().year - ano

print(f"Com {idade} anos: {voto(idade)}.")